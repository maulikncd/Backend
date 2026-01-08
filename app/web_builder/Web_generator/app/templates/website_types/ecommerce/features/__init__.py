from typing import Dict, Any
import random

from .variant_aura_features import render as render_aura
from .variant_badges import render as render_badges
from .variant_bento_grid import render as render_bento
from .variant_icon_row import render as render_icon
from .variant_cards import render as render_cards
from .variant_strip import render as render_strip
from .variant_split import render as render_split
from .variant_stats import render as render_stats
from .variant_trust import render as render_trust
from .variant_marquee import render as render_marquee

class EcommerceFeaturesTemplates:
    VARIANTS = [
        "aura-features", "badges", "bento-grid", "icon-row", "cards",
        "strip", "split", "stats", "trust", "marquee"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "aura-features": render_aura,
            "badges": render_badges,
            "bento-grid": render_bento,
            "icon-row": render_icon,
            "cards": render_cards,
            "strip": render_strip,
            "split": render_split,
            "stats": render_stats,
            "trust": render_trust,
            "marquee": render_marquee
        }
        return dispatch.get(variant, render_aura)(props, colors)
