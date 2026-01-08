from typing import Dict, Any
import random

from .variant_mission_cyber import render as render_mission
from .variant_team_roster import render as render_team
from .variant_studio_timeline import render as render_timeline
from .variant_stats_counter import render as render_stats
from .variant_cinematic_split import render as render_cinematic
from .variant_glass_cards import render as render_glass
from .variant_neon_grid import render as render_neon
from .variant_parallax_story import render as render_parallax
from .variant_holo_cards import render as render_holo
from .variant_bento_premium import render as render_bento

class GamingAboutTemplates:
    VARIANTS = [
        "mission-cyber", "team-roster", "studio-timeline", "stats-counter",
        "cinematic-split", "glass-cards", "neon-grid", "parallax-story",
        "holo-cards", "bento-premium"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "mission-cyber": render_mission,
            "team-roster": render_team,
            "studio-timeline": render_timeline,
            "stats-counter": render_stats,
            "cinematic-split": render_cinematic,
            "glass-cards": render_glass,
            "neon-grid": render_neon,
            "parallax-story": render_parallax,
            "holo-cards": render_holo,
            "bento-premium": render_bento
        }
        return dispatch.get(variant, render_mission)(props, colors)
