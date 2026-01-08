from typing import Dict, Any
import random

from .variant_shop import render as render_shop
from .variant_mega_menu import render as render_mega
from .variant_minimal import render as render_minimal
from .variant_search_focus import render as render_search
from .variant_two_row import render as render_tworow
from .variant_centered import render as render_centered
from .variant_glass import render as render_glass
from .variant_dark import render as render_dark
from .variant_sidebar import render as render_sidebar
from .variant_catbar import render as render_catbar

class EcommerceNavbarTemplates:
    VARIANTS = [
        "shop", "mega-menu", "minimal", "search-focus", "two-row",
        "centered", "glass", "dark", "sidebar", "catbar"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "shop": render_shop,
            "mega-menu": render_mega,
            "minimal": render_minimal,
            "search-focus": render_search,
            "two-row": render_tworow,
            "centered": render_centered,
            "glass": render_glass,
            "dark": render_dark,
            "sidebar": render_sidebar,
            "catbar": render_catbar
        }
        return dispatch.get(variant, render_shop)(props, colors)
