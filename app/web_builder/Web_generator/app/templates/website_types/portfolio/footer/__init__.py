from typing import Dict, Any
import random

from .variant_minimal import render as render_minimal
from .variant_social_only import render as render_social
from .variant_newsletter import render as render_newsletter
from .variant_columns import render as render_columns
from .variant_big_name import render as render_bigname
from .variant_cta import render as render_cta
from .variant_split import render as render_split
from .variant_centered import render as render_centered
from .variant_gradient import render as render_gradient
from .variant_bento import render as render_bento

class PortfolioFooterTemplates:
    VARIANTS = [
        "minimal", "social-only", "newsletter", "columns", "big-name",
        "cta", "split", "centered", "gradient", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "minimal": render_minimal,
            "social-only": render_social,
            "newsletter": render_newsletter,
            "columns": render_columns,
            "big-name": render_bigname,
            "cta": render_cta,
            "split": render_split,
            "centered": render_centered,
            "gradient": render_gradient,
            "bento": render_bento
        }
        return dispatch.get(variant, render_minimal)(props, colors)
