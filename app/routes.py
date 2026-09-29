from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

load_dotenv(BASE_DIR / ".env")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        outline = generate_outline(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style
        )

        story = generate_story(
            outline=outline,
            character_name=character_name,
            tone=tone,
            art_style=art_style
        )

        image_paths = []

        for panel in outline:
            image_path = generate_image(
                image_prompt=panel["image_prompt"],
                panel_number=panel["panel_number"]
            )
            image_paths.append(image_path)

        layout = build_comic_layout(
            outline=outline,
            story=story,
            image_paths=image_paths
        )

        pdf_path = save_pdf(
            layout=layout,
            title="ComicCraft"
        )

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "request": request,
                "layout": layout,
                "pdf_path": pdf_path,
                "story_prompt": story_prompt,
                "character_name": character_name,
                "setting": setting,
                "tone": tone,
                "art_style": art_style
            }
        )

    except Exception as error:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "request": request,
                "error": str(error),
                "story_prompt": story_prompt,
                "character_name": character_name,
                "setting": setting,
                "tone": tone,
                "art_style": art_style
            },
            status_code=500
        )


@router.get("/export-success", response_class=HTMLResponse)
async def export_success(
    request: Request,
    file: Optional[str] = None
):
    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={
            "request": request,
            "file": file
        }
    )
