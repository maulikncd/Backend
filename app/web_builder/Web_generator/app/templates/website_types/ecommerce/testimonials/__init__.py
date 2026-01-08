from typing import Dict, Any
import random

from .variant_cards import render as render_cards
from .variant_carousel import render as render_carousel
from .variant_stats import render as render_stats
from .variant_marquee import render as render_marquee
from .variant_video import render as render_video
from .variant_list import render as render_list
from .variant_photos import render as render_photos
from .variant_quote import render as render_quote
from .variant_masonry import render as render_masonry
from .variant_bento import render as render_bento

class EcommerceTestimonialsTemplates:
    VARIANTS = [
        "cards", "carousel", "stats", "marquee", "video",
        "list", "photos", "quote", "masonry", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cards": render_cards,
            "carousel": render_carousel,
            "stats": render_stats,
            "marquee": render_marquee,
            "video": render_video,
            "list": render_list,
            "photos": render_photos,
            "quote": render_quote,
            "masonry": render_masonry,
            "bento": render_bento
        }
        return dispatch.get(variant, render_cards)(props, colors)
