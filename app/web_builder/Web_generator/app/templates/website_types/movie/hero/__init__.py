from typing import Dict, Any
import random

from .variant_cinematic import render as render_cinematic


class MovieHeroTemplates:
    """Movie theater hero section"""
    
    VARIANTS = ["cinematic"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "cinematic": render_cinematic
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_cinematic(props, colors)
