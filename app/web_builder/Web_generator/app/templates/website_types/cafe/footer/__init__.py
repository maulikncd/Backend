from typing import Dict, Any
import random

from .variant_elegant_dark import render as render_elegant_dark
from .variant_aura_newsletter import render as render_aura_newsletter
from .variant_minimal_center import render as render_minimal_center
from .variant_split_image import render as render_split_image
from .variant_mega_footer import render as render_mega_footer
from .variant_gradient_cta import render as render_gradient_cta
from .variant_with_map import render as render_with_map
from .variant_stacked_elegant import render as render_stacked_elegant
from .variant_social_focus import render as render_social_focus
from .variant_wave_shape import render as render_wave_shape

class CafeFooterTemplates:
    """Modular Footer Templates for Cafe - 10 Premium Variants"""
    
    VARIANTS = [
        "elegant-dark",
        "aura-newsletter",
        "minimal-center",
        "split-image",
        "mega-footer",
        "gradient-cta",
        "with-map",
        "stacked-elegant",
        "social-focus",
        "wave-shape"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-dark": render_elegant_dark,
            "aura-newsletter": render_aura_newsletter,
            "minimal-center": render_minimal_center,
            "split-image": render_split_image,
            "mega-footer": render_mega_footer,
            "gradient-cta": render_gradient_cta,
            "with-map": render_with_map,
            "stacked-elegant": render_stacked_elegant,
            "social-focus": render_social_focus,
            "wave-shape": render_wave_shape
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_elegant_dark(props, colors)
