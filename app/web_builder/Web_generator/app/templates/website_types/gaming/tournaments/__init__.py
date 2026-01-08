from typing import Dict, Any
import random

from .variant_bracket_view import render as render_bracket
from .variant_featured import render as render_featured
from .variant_card_grid import render as render_cards
from .variant_timeline import render as render_timeline
from .variant_leaderboard import render as render_leader
from .variant_live_match import render as render_live
from .variant_prizes import render as render_prizes
from .variant_teams import render as render_teams
from .variant_registration import render as render_register
from .variant_bento import render as render_bento

class GamingTournamentsTemplates:
    VARIANTS = [
        "bracket-view", "featured", "card-grid", "timeline", "leaderboard",
        "live-match", "prizes", "teams", "registration", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "bracket-view": render_bracket,
            "featured": render_featured,
            "card-grid": render_cards,
            "timeline": render_timeline,
            "leaderboard": render_leader,
            "live-match": render_live,
            "prizes": render_prizes,
            "teams": render_teams,
            "registration": render_register,
            "bento": render_bento
        }
        return dispatch.get(variant, render_bracket)(props, colors)
