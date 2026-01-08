from typing import Dict, Any
import random

from .variant_minimal_elegance import render as render_minimal
from .variant_gradient_mesh import render as render_gradient
from .variant_3d_perspective import render as render_3d
from .variant_split_showcase import render as render_split
from .variant_developer_spotlight import render as render_developer
from .variant_creative_agency import render as render_agency
from .variant_floating_cards import render as render_floating
from .variant_terminal import render as render_terminal
from .variant_bento import render as render_bento
from .variant_scroll_reveal import render as render_scroll

class PortfolioHeroTemplates:
    VARIANTS = [
        "minimal-elegance", "gradient-mesh", "3d-perspective", "split-showcase",
        "developer-spotlight", "creative-agency", "floating-cards", "terminal",
        "bento", "scroll-reveal"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "minimal-elegance": render_minimal,
            "gradient-mesh": render_gradient,
            "3d-perspective": render_3d,
            "split-showcase": render_split,
            "developer-spotlight": render_developer,
            "creative-agency": render_agency,
            "floating-cards": render_floating,
            "terminal": render_terminal,
            "bento": render_bento,
            "scroll-reveal": render_scroll
        }
        return dispatch.get(variant, render_minimal)(props, colors)
