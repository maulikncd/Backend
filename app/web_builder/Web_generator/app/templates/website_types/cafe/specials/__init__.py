from typing import Dict, Any, List
import random

from .variant_highlight_card import render as render_highlight

class CafeSpecialsTemplates:
    """Modular Specials Templates for Cafe"""
    
    VARIANTS = [
        "highlight-card"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
            
        dispatch = {
            "highlight-card": render_highlight
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        return render_highlight(props, colors)
