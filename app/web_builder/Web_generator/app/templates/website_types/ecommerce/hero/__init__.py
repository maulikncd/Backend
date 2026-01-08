from typing import Dict, Any
import random

from .variant_aura_premium import render as render_aura
from .variant_cinematic_video import render as render_video
from .variant_glitch_art import render as render_glitch
from .variant_luxury_brand import render as render_luxury
from .variant_modern_shop import render as render_modern
from .variant_split_scroll import render as render_split
from .variant_flash_sale import render as render_flash
from .variant_minimal_product import render as render_minimal
from .variant_categories import render as render_cats
from .variant_bento import render as render_bento

class EcommerceHeroTemplates:
    VARIANTS = [
        "aura-premium", "cinematic-video", "glitch-art", "luxury-brand",
        "modern-shop", "split-scroll", "flash-sale", "minimal-product",
        "categories", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "aura-premium": render_aura,
            "cinematic-video": render_video,
            "glitch-art": render_glitch,
            "luxury-brand": render_luxury,
            "modern-shop": render_modern,
            "split-scroll": render_split,
            "flash-sale": render_flash,
            "minimal-product": render_minimal,
            "categories": render_cats,
            "bento": render_bento
        }
        return dispatch.get(variant, render_aura)(props, colors)
