from typing import Dict, Any
import random

from .variant_minimal import render as render_minimal


class PortfolioFooterTemplates:
    """Portfolio footer section"""
    
    VARIANTS = ["minimal"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "minimal": render_minimal
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_minimal(props, colors)
