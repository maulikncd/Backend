from typing import Dict, Any
import random

from .variant_story_timeline import render as render_story_timeline


class PortfolioAboutTemplates:
    """Portfolio about section"""
    
    VARIANTS = ["story-timeline"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "story-timeline": render_story_timeline
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_story_timeline(props, colors)
