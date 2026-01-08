from typing import Dict, Any
import random

from .variant_cyber_neon import render as render_cyber
from .variant_glass_float import render as render_glass
from .variant_minimal_dark import render as render_minimal
from .variant_topbar_split import render as render_topbar
from .variant_sticky_transparent import render as render_sticky
from .variant_mega_menu import render as render_mega
from .variant_centered_logo import render as render_centered
from .variant_sidebar_toggle import render as render_sidebar
from .variant_animated_pills import render as render_pills
from .variant_bottom_bar import render as render_bottom

class GamingNavbarTemplates:
    VARIANTS = [
        "cyber-neon", "glass-float", "minimal-dark", "topbar-split",
        "sticky-transparent", "mega-menu", "centered-logo", "sidebar-toggle",
        "animated-pills", "bottom-bar"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cyber-neon": render_cyber,
            "glass-float": render_glass,
            "minimal-dark": render_minimal,
            "topbar-split": render_topbar,
            "sticky-transparent": render_sticky,
            "mega-menu": render_mega,
            "centered-logo": render_centered,
            "sidebar-toggle": render_sidebar,
            "animated-pills": render_pills,
            "bottom-bar": render_bottom
        }
        return dispatch.get(variant, render_cyber)(props, colors)
