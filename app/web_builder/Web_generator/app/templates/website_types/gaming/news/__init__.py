from typing import Dict, Any
import random

from .variant_cards_grid import render as render_cards
from .variant_featured_hero import render as render_featured
from .variant_timeline import render as render_timeline
from .variant_magazine import render as render_magazine
from .variant_list_view import render as render_list
from .variant_horizontal_scroll import render as render_scroll
from .variant_masonry import render as render_masonry
from .variant_video_news import render as render_video
from .variant_breaking import render as render_breaking
from .variant_bento import render as render_bento

class GamingNewsTemplates:
    VARIANTS = [
        "cards-grid", "featured-hero", "timeline", "magazine",
        "list-view", "horizontal-scroll", "masonry", "video-news",
        "breaking", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cards-grid": render_cards,
            "featured-hero": render_featured,
            "timeline": render_timeline,
            "magazine": render_magazine,
            "list-view": render_list,
            "horizontal-scroll": render_scroll,
            "masonry": render_masonry,
            "video-news": render_video,
            "breaking": render_breaking,
            "bento": render_bento
        }
        return dispatch.get(variant, render_cards)(props, colors)
