from typing import Dict, Any
import random

from .variant_elegant_grid import render as render_elegant_grid
from .variant_visual_feast import render as render_visual_feast
from .variant_aura_cards import render as render_aura_cards
from .variant_tabbed_filter import render as render_tabbed_filter
from .variant_magazine_style import render as render_magazine_style
from .variant_horizontal_scroll import render as render_horizontal_scroll
from .variant_dark_luxury import render as render_dark_luxury
from .variant_zen_minimal import render as render_zen_minimal
from .variant_split_showcase import render as render_split_showcase
from .variant_floating_cards import render as render_floating_cards

class CafeMenuTemplates:
    """Modular Menu Templates for Cafe - 10 Premium Variants"""
    
    VARIANTS = [
        "elegant-grid",
        "visual-feast",
        "aura-cards",
        "tabbed-filter",
        "magazine-style",
        "horizontal-scroll",
        "dark-luxury",
        "zen-minimal",
        "split-showcase",
        "floating-cards"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-grid": render_elegant_grid,
            "visual-feast": render_visual_feast,
            "aura-cards": render_aura_cards,
            "tabbed-filter": render_tabbed_filter,
            "magazine-style": render_magazine_style,
            "horizontal-scroll": render_horizontal_scroll,
            "dark-luxury": render_dark_luxury,
            "zen-minimal": render_zen_minimal,
            "split-showcase": render_split_showcase,
            "floating-cards": render_floating_cards
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_elegant_grid(props, colors)
