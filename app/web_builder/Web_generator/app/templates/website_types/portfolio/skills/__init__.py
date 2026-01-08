from typing import Dict, Any
import random

from .variant_tech_stack import render as render_tech_stack
from .variant_categories import render as render_categories


class PortfolioSkillsTemplates:
    """Portfolio skills section with 2 variants"""
    
    VARIANTS = ["tech-stack", "categories"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "tech-stack": render_tech_stack,
            "categories": render_categories
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_tech_stack(props, colors)
