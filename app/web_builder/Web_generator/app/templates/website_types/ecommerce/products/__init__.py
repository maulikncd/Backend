from typing import Dict, Any
import random

from .variant_grid import render as render_grid
from .variant_aura_products import render as render_aura
from .variant_carousel_3d import render as render_carousel
from .variant_masonry_wall import render as render_masonry
from .variant_minimal_list import render as render_minimal
from .variant_featured_row import render as render_featured
from .variant_horizontal import render as render_horizontal
from .variant_bento import render as render_bento
from .variant_quick_view import render as render_quick
from .variant_sale import render as render_sale

class EcommerceProductsTemplates:
    VARIANTS = [
        "grid", "aura-products", "carousel-3d", "masonry-wall", "minimal-list",
        "featured-row", "horizontal", "bento", "quick-view", "sale"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "grid": render_grid,
            "aura-products": render_aura,
            "carousel-3d": render_carousel,
            "masonry-wall": render_masonry,
            "minimal-list": render_minimal,
            "featured-row": render_featured,
            "horizontal": render_horizontal,
            "bento": render_bento,
            "quick-view": render_quick,
            "sale": render_sale
        }
        return dispatch.get(variant, render_grid)(props, colors)
