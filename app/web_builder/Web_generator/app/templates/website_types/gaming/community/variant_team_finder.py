from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Team Finder - Find teams or players"""
    title = props.get("title", "Find Your Team")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    listings = [
        {"type": "Team", "name": "Alpha Squad", "looking": "2 Players Needed", "rank": "Diamond", "region": "NA"},
        {"type": "Player", "name": "ShadowKing", "looking": "Looking for Team", "rank": "Master", "region": "EU"},
        {"type": "Team", "name": "Pro Gaming", "looking": "Support Player Needed", "rank": "Platinum", "region": "ASIA"},
    ]
    
    listings_html = ""
    for l in listings:
        listings_html += f'''
        <div class="listing-card">
            <span class="listing-type">{l['type']}</span>
            <h3>{l['name']}</h3>
            <p>{l['looking']}</p>
            <div class="listing-tags">
                <span class="rank">{l['rank']}</span>
                <span class="region">{l['region']}</span>
            </div>
            <button class="contact-btn">Contact</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-teams" id="community">
        <div class="teams-container">
            <div class="teams-header">
                <h2>{title}</h2>
                <a href="#" class="post-btn">+ Post Listing</a>
            </div>
            <div class="listings-grid">{listings_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-teams {{ padding: 120px 24px; background: {background}; }}
    .teams-container {{ max-width: 1000px; margin: 0 auto; }}
    .teams-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; flex-wrap: wrap; gap: 20px; }}
    .teams-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .post-btn {{ padding: 12px 28px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; }}
    .listings-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .listing-card {{ background: {text}05; border-radius: 20px; padding: 28px; transition: all 0.4s ease; }}
    .listing-card:hover {{ transform: translateY(-8px); box-shadow: 0 20px 50px {primary}15; }}
    .listing-type {{ display: inline-block; padding: 4px 12px; background: {primary}20; color: {primary}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 12px; }}
    .listing-card h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .listing-card p {{ color: {secondary}; margin-bottom: 16px; }}
    .listing-tags {{ display: flex; gap: 8px; margin-bottom: 20px; }}
    .rank, .region {{ padding: 5px 12px; background: {text}10; color: {text}; font-size: 0.75rem; font-weight: 600; border-radius: 100px; }}
    .contact-btn {{ width: 100%; padding: 12px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; transition: all 0.3s ease; }}
    .contact-btn:hover {{ transform: scale(1.02); }}
    @media (max-width: 900px) {{ .listings-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
