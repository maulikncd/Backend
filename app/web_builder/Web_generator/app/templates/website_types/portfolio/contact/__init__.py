from typing import Dict, Any
import random

from .variant_modern_split import render as render_split
from .variant_simple_form import render as render_simple
from .variant_cards import render as render_cards
from .variant_cta import render as render_cta
from .variant_bento import render as render_bento
from .variant_minimal_email import render as render_minimal
from .variant_booking import render as render_booking
from .variant_social_links import render as render_social
from .variant_faq import render as render_faq
from .variant_location import render as render_location

class PortfolioContactTemplates:
    VARIANTS = [
        "modern-split", "simple-form", "cards", "cta", "bento",
        "minimal-email", "booking", "social-links", "faq", "location"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "modern-split": render_split,
            "simple-form": render_simple,
            "cards": render_cards,
            "cta": render_cta,
            "bento": render_bento,
            "minimal-email": render_minimal,
            "booking": render_booking,
            "social-links": render_social,
            "faq": render_faq,
            "location": render_location
        }
        return dispatch.get(variant, render_split)(props, colors)
