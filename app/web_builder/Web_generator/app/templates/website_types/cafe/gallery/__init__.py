from typing import Dict, Any
import random

from .variant_masonry_food import render as render_masonry_food
from .variant_interlocking_grid import render as render_interlocking_grid
from .variant_aura_masonry import render as render_aura_masonry
from .variant_lightbox_grid import render as render_lightbox_grid
from .variant_polaroid_scatter import render as render_polaroid_scatter
from .variant_carousel_slider import render as render_carousel_slider
from .variant_filmstrip import render as render_filmstrip
from .variant_staggered_pins import render as render_staggered_pins
from .variant_split_showcase import render as render_split_showcase
from .variant_fullscreen_immersive import render as render_fullscreen_immersive

class CafeGalleryTemplates:
    """Modular Gallery Templates for Cafe - 10 Premium Variants"""
    
    VARIANTS = [
        "masonry-food",
        "interlocking-grid",
        "aura-masonry",
        "lightbox-grid",
        "polaroid-scatter",
        "carousel-slider",
        "filmstrip",
        "staggered-pins",
        "split-showcase",
        "fullscreen-immersive"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "masonry-food": render_masonry_food,
            "interlocking-grid": render_interlocking_grid,
            "aura-masonry": render_aura_masonry,
            "lightbox-grid": render_lightbox_grid,
            "polaroid-scatter": render_polaroid_scatter,
            "carousel-slider": render_carousel_slider,
            "filmstrip": render_filmstrip,
            "staggered-pins": render_staggered_pins,
            "split-showcase": render_split_showcase,
            "fullscreen-immersive": render_fullscreen_immersive
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_masonry_food(props, colors)
