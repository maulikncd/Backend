from typing import Dict, Any
import random

from .variant_simple import render as render_simple
from .variant_benefits import render as render_benefits
from .variant_discount import render as render_discount
from .variant_inline import render as render_inline
from .variant_bento import render as render_bento
from .variant_minimal import render as render_minimal
from .variant_glass import render as render_glass
from .variant_image import render as render_image
from .variant_dark import render as render_dark
from .variant_social import render as render_social

class EcommerceNewsletterTemplates:
    VARIANTS = [
        "simple", "benefits", "discount", "inline", "bento",
        "minimal", "glass", "image", "dark", "social"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "simple": render_simple,
            "benefits": render_benefits,
            "discount": render_discount,
            "inline": render_inline,
            "bento": render_bento,
            "minimal": render_minimal,
            "glass": render_glass,
            "image": render_image,
            "dark": render_dark,
            "social": render_social
        }
        return dispatch.get(variant, render_simple)(props, colors)
