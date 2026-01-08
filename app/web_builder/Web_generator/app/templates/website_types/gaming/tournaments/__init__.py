from typing import Dict, Any
import random

from .variant_bracket_view import render as render_bracket

class GamingTournamentsTemplates:
    VARIANTS = ["bracket-view"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        return render_bracket(props, colors)
