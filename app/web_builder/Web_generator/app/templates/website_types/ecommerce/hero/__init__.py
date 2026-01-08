from typing import Dict, Any
import random

from .variant_modern_shop import render as render_modern_shop
from .variant_luxury_brand import render as render_luxury_brand
from .variant_aura_premium import render as render_aura_premium
from .variant_cinematic_video import render as render_cinematic_video
from .variant_split_scroll import render as render_split_scroll
from .variant_glitch_art import render as render_glitch_art


class EcommerceHeroTemplates:
    """E-commerce hero sections"""
    
    VARIANTS = [
        "modern-shop", 
        "luxury-brand", 
        "aura-premium",
        "cinematic-video",
        "split-scroll",
        "glitch-art"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "modern-shop": render_modern_shop,
            "luxury-brand": render_luxury_brand,
            "aura-premium": render_aura_premium,
            "cinematic-video": render_cinematic_video,
            "split-scroll": render_split_scroll,
            "glitch-art": render_glitch_art
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_modern_shop(props, colors)
