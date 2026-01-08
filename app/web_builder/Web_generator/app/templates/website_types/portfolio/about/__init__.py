from typing import Dict, Any
import random

from .variant_story_timeline import render as render_timeline
from .variant_split_layout import render as render_split
from .variant_cards_grid import render as render_cards
from .variant_bento import render as render_bento
from .variant_minimal_text import render as render_minimal
from .variant_experience import render as render_exp
from .variant_tech_stack import render as render_tech
from .variant_fun_facts import render as render_facts
from .variant_process import render as render_process
from .variant_quote import render as render_quote

class PortfolioAboutTemplates:
    VARIANTS = [
        "story-timeline", "split-layout", "cards-grid", "bento", "minimal-text",
        "experience", "tech-stack", "fun-facts", "process", "quote"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "story-timeline": render_timeline,
            "split-layout": render_split,
            "cards-grid": render_cards,
            "bento": render_bento,
            "minimal-text": render_minimal,
            "experience": render_exp,
            "tech-stack": render_tech,
            "fun-facts": render_facts,
            "process": render_process,
            "quote": render_quote
        }
        return dispatch.get(variant, render_timeline)(props, colors)
