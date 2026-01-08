from typing import Dict, Any
import random

from .variant_discord_hub import render as render_discord
from .variant_forums import render as render_forums
from .variant_social_feed import render as render_social
from .variant_stats import render as render_stats
from .variant_team_finder import render as render_teams
from .variant_events import render as render_events
from .variant_creators import render as render_creators
from .variant_fan_art import render as render_art
from .variant_clips import render as render_clips
from .variant_bento import render as render_bento

class GamingCommunityTemplates:
    VARIANTS = [
        "discord-hub", "forums", "social-feed", "stats", "team-finder",
        "events", "creators", "fan-art", "clips", "bento"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "discord-hub": render_discord,
            "forums": render_forums,
            "social-feed": render_social,
            "stats": render_stats,
            "team-finder": render_teams,
            "events": render_events,
            "creators": render_creators,
            "fan-art": render_art,
            "clips": render_clips,
            "bento": render_bento
        }
        return dispatch.get(variant, render_discord)(props, colors)
