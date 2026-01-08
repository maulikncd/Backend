from typing import Dict, Any, List
import random

from .variant_minimal_list import render as render_list

class CafeHoursTemplates:
    """Modular Hours Templates for Cafe"""
    
    VARIANTS = [
        "minimal-list"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
            
        dispatch = {
            "minimal-list": render_list
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_list(props, colors)
