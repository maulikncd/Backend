from typing import Dict, Any
import random

from .variant_tech_grid import render as render_tech
from .variant_stats_showcase import render as render_stats
from .variant_bento_grid import render as render_bento
from .variant_hcards import render as render_hcards
from .variant_split_image import render as render_split
from .variant_interactive_cards import render as render_interactive
from .variant_floating_icons import render as render_floating
from .variant_neon_showcase import render as render_neon
from .variant_scroll_reveal import render as render_scroll
from .variant_compare_table import render as render_compare

class GamingFeaturesTemplates:
    VARIANTS = [
        "tech-grid", "stats-showcase", "bento-grid", "hcards", "split-image",
        "interactive-cards", "floating-icons", "neon-showcase", "scroll-reveal", "compare-table"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "tech-grid": render_tech,
            "stats-showcase": render_stats,
            "bento-grid": render_bento,
            "hcards": render_hcards,
            "split-image": render_split,
            "interactive-cards": render_interactive,
            "floating-icons": render_floating,
            "neon-showcase": render_neon,
            "scroll-reveal": render_scroll,
            "compare-table": render_compare
        }
        return dispatch.get(variant, render_tech)(props, colors)
