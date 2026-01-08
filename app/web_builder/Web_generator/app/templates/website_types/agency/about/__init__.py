from typing import Dict, Any
import random

from .variant_story import render as render_story


class AgencyAboutTemplates:
    """Agency about section"""
    
    VARIANTS = ["story"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "story": render_story
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_story(props, colors)
