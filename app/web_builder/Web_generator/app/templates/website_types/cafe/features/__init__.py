from typing import Dict, Any
import random

from .variant_grid_minimal import render as render_grid_minimal
from .variant_aura_cards import render as render_aura_cards
from .variant_icon_boxes import render as render_icon_boxes
from .variant_timeline_vertical import render as render_timeline_vertical
from .variant_split_image import render as render_split_image
from .variant_floating_numbers import render as render_floating_numbers
from .variant_bento_grid import render as render_bento_grid
from .variant_hscroll_cards import render as render_hscroll_cards
from .variant_glassmorphism import render as render_glassmorphism
from .variant_minimal_list import render as render_minimal_list

class CafeFeaturesTemplates:
    """Modular Features Templates for Cafe - 10 Premium Variants"""
    
    VARIANTS = [
        "grid-minimal",
        "aura-cards",
        "icon-boxes",
        "timeline-vertical",
        "split-image",
        "floating-numbers",
        "bento-grid",
        "hscroll-cards",
        "glassmorphism",
        "minimal-list"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "grid-minimal": render_grid_minimal,
            "aura-cards": render_aura_cards,
            "icon-boxes": render_icon_boxes,
            "timeline-vertical": render_timeline_vertical,
            "split-image": render_split_image,
            "floating-numbers": render_floating_numbers,
            "bento-grid": render_bento_grid,
            "hscroll-cards": render_hscroll_cards,
            "glassmorphism": render_glassmorphism,
            "minimal-list": render_minimal_list
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_grid_minimal(props, colors)
