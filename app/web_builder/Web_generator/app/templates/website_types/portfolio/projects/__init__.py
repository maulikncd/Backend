from typing import Dict, Any
import random

from .variant_bento_grid import render as render_bento_grid
from .variant_case_studies import render as render_case_studies
from .variant_minimal_cards import render as render_minimal_cards


class PortfolioProjectsTemplates:
    """Portfolio projects/work section with 3 premium variants"""
    
    VARIANTS = [
        "bento-grid",
        "case-studies",
        "minimal-cards"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "bento-grid": render_bento_grid,
            "case-studies": render_case_studies,
            "minimal-cards": render_minimal_cards
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_bento_grid(props, colors)
