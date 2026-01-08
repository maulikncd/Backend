from typing import Dict, Any
import random

from .variant_full import render as render_full
from .variant_minimal import render as render_minimal
from .variant_columns import render as render_columns
from .variant_newsletter import render as render_newsletter
from .variant_dark import render as render_dark
from .variant_app import render as render_app
from .variant_bento import render as render_bento
from .variant_cta import render as render_cta
from .variant_split import render as render_split
from .variant_trust import render as render_trust

class EcommerceFooterTemplates:
    VARIANTS = [
        "full", "minimal", "columns", "newsletter", "dark",
        "app", "bento", "cta", "split", "trust"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "full": render_full,
            "minimal": render_minimal,
            "columns": render_columns,
            "newsletter": render_newsletter,
            "dark": render_dark,
            "app": render_app,
            "bento": render_bento,
            "cta": render_cta,
            "split": render_split,
            "trust": render_trust
        }
        return dispatch.get(variant, render_full)(props, colors)
