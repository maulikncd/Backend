from typing import Dict, Any
import random

from .variant_elegant_dining import render as render_elegant_dining
from .variant_rustic_bistro import render as render_rustic_bistro
from .variant_modern_split import render as render_modern_split
from .variant_dark_luxe import render as render_dark_luxe
from .variant_fullscreen_food import render as render_fullscreen_food
from .variant_minimal_zen import render as render_minimal_zen
from .variant_warm_welcome import render as render_warm_welcome
from .variant_parallax_story import render as render_parallax_story
from .variant_chef_spotlight import render as render_chef_spotlight
from .variant_gradient_glass import render as render_gradient_glass


class RestaurantHeroTemplates:
    """Restaurant-specific hero sections - 10 premium variants"""
    
    VARIANTS = [
        "elegant-dining",
        "rustic-bistro", 
        "modern-split",
        "dark-luxe",
        "fullscreen-food",
        "minimal-zen",
        "warm-welcome",
        "parallax-story",
        "chef-spotlight",
        "gradient-glass"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-dining": render_elegant_dining,
            "rustic-bistro": render_rustic_bistro,
            "modern-split": render_modern_split,
            "dark-luxe": render_dark_luxe,
            "fullscreen-food": render_fullscreen_food,
            "minimal-zen": render_minimal_zen,
            "warm-welcome": render_warm_welcome,
            "parallax-story": render_parallax_story,
            "chef-spotlight": render_chef_spotlight,
            "gradient-glass": render_gradient_glass
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant_dining(props, colors)
