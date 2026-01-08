from typing import Dict, Any
import random

from .variant_corporate_modern import render as render_corporate_modern


class AgencyHeroTemplates:
    """Agency-specific hero sections"""
    
    VARIANTS = ["corporate-modern"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "corporate-modern": render_corporate_modern
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_corporate_modern(props, colors)
