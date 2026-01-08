from typing import Dict, Any
import random

from .variant_elegant import render as render_elegant
from .variant_story_split import render as render_story_split
from .variant_timeline import render as render_timeline
from .variant_team_cards import render as render_team_cards
from .variant_video_bg import render as render_video_bg
from .variant_stats_counter import render as render_stats_counter
from .variant_minimal_clean import render as render_minimal_clean
from .variant_gallery_mosaic import render as render_gallery_mosaic
from .variant_quote_centered import render as render_quote_centered
from .variant_parallax_scroll import render as render_parallax_scroll
from .variant_cards_grid import render as render_cards_grid


class RestaurantAboutTemplates:
    """Restaurant about section - 10 premium variants"""
    
    VARIANTS = [
        "elegant",
        "story-split",
        "timeline",
        "team-cards",
        "video-bg",
        "stats-counter",
        "minimal-clean",
        "gallery-mosaic",
        "quote-centered",
        "parallax-scroll"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant": render_elegant,
            "story-split": render_story_split,
            "timeline": render_timeline,
            "team-cards": render_team_cards,
            "video-bg": render_video_bg,
            "stats-counter": render_stats_counter,
            "minimal-clean": render_minimal_clean,
            "gallery-mosaic": render_gallery_mosaic,
            "quote-centered": render_quote_centered,
            "parallax-scroll": render_parallax_scroll,
            "cards-grid": render_cards_grid
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant(props, colors)
