from typing import Dict, Any
import random

from .variant_elegant_cards import render as render_elegant_cards
from .variant_modern_grid import render as render_modern_grid
from .variant_image_cards import render as render_image_cards
from .variant_tabbed import render as render_tabbed
from .variant_minimal_lines import render as render_minimal_lines
from .variant_horizontal_scroll import render as render_horizontal_scroll
from .variant_split_showcase import render as render_split_showcase
from .variant_dark_luxury import render as render_dark_luxury
from .variant_magazine_style import render as render_magazine_style
from .variant_bento_grid import render as render_bento_grid


class RestaurantMenuTemplates:
    """Restaurant menu section - 10 premium variants"""
    
    VARIANTS = [
        "elegant-cards",
        "modern-grid",
        "image-cards",
        "tabbed",
        "minimal-lines",
        "horizontal-scroll",
        "split-showcase",
        "dark-luxury",
        "magazine-style",
        "bento-grid"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-cards": render_elegant_cards,
            "modern-grid": render_modern_grid,
            "image-cards": render_image_cards,
            "tabbed": render_tabbed,
            "minimal-lines": render_minimal_lines,
            "horizontal-scroll": render_horizontal_scroll,
            "split-showcase": render_split_showcase,
            "dark-luxury": render_dark_luxury,
            "magazine-style": render_magazine_style,
            "bento-grid": render_bento_grid
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant_cards(props, colors)
