from typing import Dict, Any
import random

from .variant_cards_grid import render as render_cards

class GamingNewsTemplates:
    VARIANTS = ["cards-grid"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        return render_cards(props, colors)
