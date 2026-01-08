from typing import Dict, Any
import random

from .variant_grid import render as render_grid
from .variant_circle_scroll import render as render_circle
from .variant_parallax_cards import render as render_parallax
from .variant_featured import render as render_featured
from .variant_horizontal import render as render_horizontal
from .variant_bento import render as render_bento
from .variant_icons import render as render_icons
from .variant_list import render as render_list
from .variant_mega import render as render_mega
from .variant_pills import render as render_pills

class EcommerceCategoriesTemplates:
    VARIANTS = [
        "grid", "circle-scroll", "parallax-cards", "featured", "horizontal",
        "bento", "icons", "list", "mega", "pills"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "grid": render_grid,
            "circle-scroll": render_circle,
            "parallax-cards": render_parallax,
            "featured": render_featured,
            "horizontal": render_horizontal,
            "bento": render_bento,
            "icons": render_icons,
            "list": render_list,
            "mega": render_mega,
            "pills": render_pills
        }
        return dispatch.get(variant, render_grid)(props, colors)
