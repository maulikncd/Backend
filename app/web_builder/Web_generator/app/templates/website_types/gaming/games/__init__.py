from typing import Dict, Any
import random

from .variant_grid_showcase import render as render_grid
from .variant_carousel import render as render_carousel

class GamingGamesTemplates:
    VARIANTS = ["grid-showcase", "carousel"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {"grid-showcase": render_grid, "carousel": render_carousel}
        return dispatch.get(variant, render_grid)(props, colors)
