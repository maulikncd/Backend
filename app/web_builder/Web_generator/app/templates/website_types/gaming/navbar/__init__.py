from typing import Dict, Any
import random

from .variant_cyber_neon import render as render_cyber
from .variant_minimal_dark import render as render_minimal
from .variant_glass_float import render as render_glass
from .variant_topbar_split import render as render_topbar

class GamingNavbarTemplates:
    VARIANTS = ["cyber-neon", "minimal-dark", "glass-float", "topbar-split"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cyber-neon": render_cyber,
            "minimal-dark": render_minimal,
            "glass-float": render_glass,
            "topbar-split": render_topbar
        }
        return dispatch.get(variant, render_cyber)(props, colors)
