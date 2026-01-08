from typing import Dict, Any
import random

from .variant_categories import render as render_categories
from .variant_tech_stack import render as render_tech
from .variant_progress_bars import render as render_progress
from .variant_icon_cards import render as render_icons
from .variant_bento import render as render_bento
from .variant_circular import render as render_circular
from .variant_tag_cloud import render as render_cloud
from .variant_timeline import render as render_timeline
from .variant_logos_grid import render as render_logos
from .variant_marquee import render as render_marquee

class PortfolioSkillsTemplates:
    VARIANTS = [
        "categories", "tech-stack", "progress-bars", "icon-cards", "bento",
        "circular", "tag-cloud", "timeline", "logos-grid", "marquee"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "categories": render_categories,
            "tech-stack": render_tech,
            "progress-bars": render_progress,
            "icon-cards": render_icons,
            "bento": render_bento,
            "circular": render_circular,
            "tag-cloud": render_cloud,
            "timeline": render_timeline,
            "logos-grid": render_logos,
            "marquee": render_marquee
        }
        return dispatch.get(variant, render_categories)(props, colors)
