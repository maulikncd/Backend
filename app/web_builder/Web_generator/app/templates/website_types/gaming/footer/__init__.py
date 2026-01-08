from typing import Dict, Any
import random

from .variant_cyber_link import render as render_cyber
from .variant_mega_links import render as render_mega
from .variant_newsletter import render as render_newsletter

class GamingFooterTemplates:
    VARIANTS = ["cyber-link", "mega-links", "newsletter"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cyber-link": render_cyber,
            "mega-links": render_mega,
            "newsletter": render_newsletter
        }
        return dispatch.get(variant, render_cyber)(props, colors)
