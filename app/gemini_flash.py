from typing import Any, Dict, List


def generate_outline(
    story_prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
) -> List[Dict[str, Any]]:

    return [
        {
            "panel_number": 1,
            "title": "The Beginning",
            "scene_description": (
                f"{character_name} begins an unexpected adventure "
                f"in {setting}."
            ),
            "image_prompt": (
                f"{character_name} in {setting}, beginning an adventure, "
                f"{art_style} comic illustration"
            )
        },
        {
            "panel_number": 2,
            "title": "A Discovery",
            "scene_description": (
                f"{character_name} discovers something unusual "
                f"connected to the story: {story_prompt}."
            ),
            "image_prompt": (
                f"{character_name} making a mysterious discovery in "
                f"{setting}, {art_style} comic illustration"
            )
        },
        {
            "panel_number": 3,
            "title": "The Turning Point",
            "scene_description": (
                f"A difficult situation appears and {character_name} "
                f"must find a way forward."
            ),
            "image_prompt": (
                f"{character_name} facing a dramatic challenge in "
                f"{setting}, {tone} mood, {art_style} comic illustration"
            )
        },
        {
            "panel_number": 4,
            "title": "The Climax",
            "scene_description": (
                f"{character_name} faces the biggest challenge of "
                f"the adventure and takes action."
            ),
            "image_prompt": (
                f"{character_name} in an exciting dramatic climax, "
                f"{setting}, {tone} mood, {art_style} comic illustration"
            )
        },
        {
            "panel_number": 5,
            "title": "The Ending",
            "scene_description": (
                f"The adventure comes to an end as {character_name} "
                f"learns something important."
            ),
            "image_prompt": (
                f"{character_name} celebrating the conclusion of the "
                f"adventure in {setting}, {art_style} comic illustration"
            )
        }
    ]