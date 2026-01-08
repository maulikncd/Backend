from typing import Dict, Any
import random

from .variant_story_split import render as render_story_split
from .variant_minimal_creative import render as render_minimal_creative
from .variant_aura_timeline import render as render_aura_timeline
from .variant_fullscreen_parallax import render as render_fullscreen_parallax
from .variant_magazine_editorial import render as render_magazine_editorial
from .variant_video_background import render as render_video_background
from .variant_cards_stack import render as render_cards_stack
from .variant_horizontal_story import render as render_horizontal_story
from .variant_team_focus import render as render_team_focus
from .variant_numbers_showcase import render as render_numbers_showcase

class CafeAboutTemplates:
    """Modular About Templates for Cafe - 10 Premium Variants"""
    
    VARIANTS = [
        "story-split",
        "minimal-creative",
        "aura-timeline",
        "fullscreen-parallax",
        "magazine-editorial",
        "video-background",
        "cards-stack",
        "horizontal-story",
        "team-focus",
        "numbers-showcase"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "story-split": render_story_split,
            "minimal-creative": render_minimal_creative,
            "aura-timeline": render_aura_timeline,
            "fullscreen-parallax": render_fullscreen_parallax,
            "magazine-editorial": render_magazine_editorial,
            "video-background": render_video_background,
            "cards-stack": render_cards_stack,
            "horizontal-story": render_horizontal_story,
            "team-focus": render_team_focus,
            "numbers-showcase": render_numbers_showcase
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_story_split(props, colors)
