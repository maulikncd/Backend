"""
HTML Generator Service
Generates complete multi-page websites from blueprint using Tailwind CSS and GSAP
"""

import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

# Import Template Registry for type-specific templates
try:
    from ..templates.registry import TemplateRegistry
    from ..templates.combination_tracker import CombinationTracker
    HAS_TEMPLATE_REGISTRY = True
except ImportError:
    HAS_TEMPLATE_REGISTRY = False
    CombinationTracker = None
    print("[HTMLGenerator] Warning: TemplateRegistry not available, using generic templates")

# Import ColorUtils for smart text color selection
try:
    from ..prompts.color_library import ColorUtils, ColorPaletteLibrary
    HAS_COLOR_UTILS = True
except ImportError:
    HAS_COLOR_UTILS = False
    print("[HTMLGenerator] Warning: ColorUtils not available")

# Import Compliance Validator for blueprint-website verification
try:
    from .compliance_validator import BlueprintComplianceValidator, BlueprintWebsiteTracker
    HAS_COMPLIANCE_VALIDATOR = True
except ImportError:
    HAS_COMPLIANCE_VALIDATOR = False
    BlueprintComplianceValidator = None
    BlueprintWebsiteTracker = None
    print("[HTMLGenerator] Warning: ComplianceValidator not available")


class HTMLGeneratorService:
    """
    Generates complete HTML websites from blueprint.
    
    Features:
    - Multi-page generation (separate HTML files per page)
    - Website type-specific templates (cafe, gaming, portfolio, etc.)
    - Tailwind CSS for styling
    - GSAP for animations
    - Responsive design
    - Google Fonts integration
    """
    
    # CDN Links
    TAILWIND_CDN = "https://cdn.tailwindcss.com"
    GSAP_CDN = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"
    GSAP_SCROLL_CDN = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"
    
    def __init__(self):
        self.pages_generated = []
        self._website_type = None  # Will be detected from blueprint
        self._used_variants_in_current_gen = {}  # Track variants used in this run
    
    def generate(self, blueprint: Dict[str, Any], output_dir: str = None) -> Dict[str, str]:
        """
        Generate standalone HTML pages for each component in blueprint.
        
        Creates separate pages based on componentOrder:
        - index.html (Hero/Home)
        - about.html (About section)
        - menu.html (Menu section)
        - etc.
        
        Also tracks template history to avoid repetition.
        """
        print(f"[HTMLGenerator] 🚀 Starting multi-page HTML generation...")
        
        # Extract key data from blueprint
        project_name = blueprint.get("projectName", "Website")
        seo = blueprint.get("seo", {})
        theme = blueprint.get("theme", {})
        global_styles = blueprint.get("globalStyles", {})
        navigation = blueprint.get("navigation", {})
        
        # Detect website type from blueprint or project description
        website_type = blueprint.get("websiteType", blueprint.get("projectType", ""))
        if not website_type:
            # Try to detect from project name or SEO keywords
            keywords = " ".join(seo.get("keywords", []) + [project_name, seo.get("description", "")])
            if HAS_TEMPLATE_REGISTRY:
                website_type = TemplateRegistry.detect_website_type(keywords)
            else:
                website_type = "agency"  # default
        
        self._website_type = website_type
        print(f"[HTMLGenerator] 🏷️ Website Type: {website_type}")
        
        # Handle both component formats
        components_raw = blueprint.get("components", {})
        
        # If components is a list (simple format), convert to dict
        if isinstance(components_raw, list):
            components = {}
            component_order = []
            for i, comp_name in enumerate(components_raw):
                comp_id = f"comp-{comp_name}"
                components[comp_id] = {
                    "id": comp_name,
                    "type": comp_name.capitalize(),
                    "name": comp_name.capitalize(),
                    "props": {}
                }
                component_order.append(comp_id)
        else:
            # Full blueprint format (dict)
            components = components_raw
            component_order = blueprint.get("componentOrder", list(components.keys()) if components else [])
        
        # Extract colors and fonts
        colors = self._extract_colors(theme)
        fonts = self._extract_fonts(global_styles)
        
        # Reset current generation variant tracking
        self._used_variants_in_current_gen = {}
        if HAS_TEMPLATE_REGISTRY and CombinationTracker:
            CombinationTracker.start_session()
        
        # Load template history to avoid repetition
        template_history = self._load_template_history()
        used_variants = {}
        
        # ============================================================
        # PRE-CHECK: Warn if we're running low on unique combinations
        # ============================================================
        if HAS_TEMPLATE_REGISTRY and CombinationTracker:
            try:
                stats = CombinationTracker.get_generation_stats(website_type)
                if stats.get("duplicate_rate", 0) > 0.3:
                    print(f"[HTMLGenerator] ⚠️ High duplication rate ({stats['duplicate_rate']*100:.0f}%) for {website_type}")
                    print(f"[HTMLGenerator] 💡 Consider clearing history or adding more template variants")
            except Exception as e:
                pass  # Stats check is optional
        
        print(f"[HTMLGenerator] 📊 Project: {project_name}")
        print(f"[HTMLGenerator] 🎨 Primary Color: {colors.get('primary')}")
        print(f"[HTMLGenerator] 📝 Components: {len(component_order)}")
        
        # Build Tailwind config
        tailwind_config = self._build_tailwind_config(colors, fonts)
        
        # Select header style ONCE for all pages (consistent navbar across website)
        import random
        header_variants = ["minimal", "centered", "floating", "dark", "gradient"]
        recently_used_headers = template_history.get("Header", [])
        fresh_header_variants = [v for v in header_variants if v not in recently_used_headers]
        if not fresh_header_variants:
            fresh_header_variants = header_variants
        selected_header_style = random.choice(fresh_header_variants)
        print(f"[HTMLGenerator] 🎨 Header Style: {selected_header_style} (same for all pages)")
        
        # Select animation style ONCE for all pages (consistent feel)
        animation_styles = ["fade_up", "fade_scale", "slide_left", "stagger_reveal", "bounce"]
        selected_animation = random.choice(animation_styles)
        print(f"[HTMLGenerator] ✨ Animation Style: {selected_animation} (same for all pages)")
        
        # Store for use in page generation
        self._current_header_style = selected_header_style
        self._current_animation_style = selected_animation
        
        # Generate standalone page for EACH component in blueprint
        # Each page: Header + Single Component Content + Footer
        pages = {}
        
        for idx, comp_id in enumerate(component_order):
            comp = components.get(comp_id, {})
            comp_type = comp.get("type", "Unknown")
            comp_type_lower = comp_type.lower()
            
            # Get the actual component ID (e.g., "games", "tournaments", "community")
            actual_id = comp.get("id", comp_type_lower)
            
            # First component or Hero → index.html
            # All other components → {id}.html (using ID, not type!)
            if idx == 0 or actual_id.lower() == "hero":
                page_name = "index.html"
            else:
                # Use the actual component ID for page name, not the generic type
                page_name = f"{actual_id.lower()}.html"
            
            # Skip if already generated (duplicate component)
            if page_name in pages:
                print(f"[HTMLGenerator] ⚠️ Skipping duplicate page: {page_name}")
                continue
            
            # Select variant avoiding recent history
            variant = self._select_variant(comp_type, template_history)
            used_variants[comp_type] = variant
            
            print(f"[HTMLGenerator] 📄 Generating {page_name} (variant: {variant})")
            
            # Generate standalone page with header, SINGLE component content, footer
            page_html = self._generate_standalone_page(
                page_name=page_name,
                project_name=project_name,
                seo=seo,
                colors=colors,
                fonts=fonts,
                navigation=navigation,
                component=comp,
                component_type=comp_type,
                variant=variant,
                tailwind_config=tailwind_config,
                all_components=components,
                component_order=component_order
            )
            pages[page_name] = page_html
        
        # Save template history (including header style for future generations)
        used_variants["Header"] = selected_header_style
        self._save_template_history(used_variants)
        
        # Record generation in CombinationTracker for better unique combinations
        if HAS_TEMPLATE_REGISTRY and CombinationTracker:
            try:
                # Get variants picked by TemplateRegistry during this session
                session_variants = CombinationTracker.get_session_variants()
                # Combine with ones selected in HTMLGenerator itself (generic fallbacks etc)
                final_combination = {**used_variants, **self._used_variants_in_current_gen, **session_variants}
                
                CombinationTracker.record_generation(
                    website_type=self._website_type,
                    used_variants=final_combination
                )
            except Exception as e:
                print(f"[HTMLGenerator] Failed to record in CombinationTracker: {e}")
        
        # Save to files if output_dir provided
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            for page_name, html_content in pages.items():
                file_path = os.path.join(output_dir, page_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"[HTMLGenerator] 💾 Saved: {file_path}")
        
        # ============================================================
        # COMPLIANCE VALIDATION: Check website matches blueprint
        # ============================================================
        if HAS_COMPLIANCE_VALIDATOR and BlueprintComplianceValidator:
            try:
                session_id = blueprint.get("session_id", blueprint.get("blueprint_id", "unknown"))
                compliance_report = BlueprintComplianceValidator.generate_compliance_report(
                    blueprint=blueprint,
                    generated_html=pages,
                    session_id=session_id
                )
                
                # Track generation for debugging
                if BlueprintWebsiteTracker:
                    BlueprintWebsiteTracker.record_generation(
                        session_id=session_id,
                        blueprint=blueprint,
                        generated_html=pages,
                        used_variants=final_combination if 'final_combination' in dir() else used_variants
                    )
                
                # Warn if compliance is low
                if compliance_report["compliance_score"] < 70:
                    print(f"[HTMLGenerator] ⚠️ LOW COMPLIANCE SCORE: {compliance_report['compliance_score']}/100")
                    print(f"[HTMLGenerator] ⚠️ Failed checks: {compliance_report['checks_failed']}")
            except Exception as e:
                print(f"[HTMLGenerator] Compliance validation error: {e}")
        
        print(f"[HTMLGenerator] ✅ Generated {len(pages)} standalone pages!")
        return pages
    
    def generate_single_page(self, blueprint: Dict[str, Any], output_dir: str = None) -> Dict[str, str]:
        """
        Generate a SINGLE HTML page with ALL sections combined.
        
        Creates one index.html file with:
        - Header (fixed navigation with anchor links)
        - All sections stacked vertically (Hero, About, Features, Menu, etc.)
        - Footer
        
        Navigation uses anchor links (#about, #menu, etc.) for smooth scrolling.
        This is the classic "Single Page Website" approach.
        """
        print(f"[HTMLGenerator] 🚀 Starting SINGLE PAGE HTML generation...")
        
        # Extract key data from blueprint
        project_name = blueprint.get("projectName", "Website")
        seo = blueprint.get("seo", {})
        theme = blueprint.get("theme", {})
        global_styles = blueprint.get("globalStyles", {})
        navigation = blueprint.get("navigation", {})
        
        # Detect website type from blueprint or project description
        website_type = blueprint.get("websiteType", blueprint.get("projectType", ""))
        if not website_type:
            keywords = " ".join(seo.get("keywords", []) + [project_name, seo.get("description", "")])
            if HAS_TEMPLATE_REGISTRY:
                website_type = TemplateRegistry.detect_website_type(keywords)
            else:
                website_type = "agency"
        
        self._website_type = website_type
        print(f"[HTMLGenerator] 🏷️ Website Type: {website_type}")
        
        # Handle both component formats
        components_raw = blueprint.get("components", {})
        
        if isinstance(components_raw, list):
            components = {}
            component_order = []
            for i, comp_name in enumerate(components_raw):
                comp_id = f"comp-{comp_name}"
                components[comp_id] = {
                    "id": comp_name,
                    "type": comp_name.capitalize(),
                    "name": comp_name.capitalize(),
                    "props": {}
                }
                component_order.append(comp_id)
        else:
            components = components_raw
            component_order = blueprint.get("componentOrder", list(components.keys()) if components else [])
        
        # Extract colors and fonts
        colors = self._extract_colors(theme)
        fonts = self._extract_fonts(global_styles)
        
        # Reset variant tracking
        self._used_variants_in_current_gen = {}
        if HAS_TEMPLATE_REGISTRY and CombinationTracker:
            CombinationTracker.start_session()
        
        template_history = self._load_template_history()
        used_variants = {}
        
        print(f"[HTMLGenerator] 📊 Project: {project_name}")
        print(f"[HTMLGenerator] 🎨 Primary Color: {colors.get('primary')}")
        print(f"[HTMLGenerator] 📝 Components: {len(component_order)}")
        
        # Build Tailwind config
        tailwind_config = self._build_tailwind_config(colors, fonts)
        
        # Select header style
        import random
        header_variants = ["minimal", "centered", "floating", "dark", "gradient"]
        recently_used_headers = template_history.get("Header", [])
        fresh_header_variants = [v for v in header_variants if v not in recently_used_headers]
        if not fresh_header_variants:
            fresh_header_variants = header_variants
        selected_header_style = random.choice(fresh_header_variants)
        self._current_header_style = selected_header_style
        print(f"[HTMLGenerator] 🎨 Header Style: {selected_header_style}")
        
        # Select animation style
        animation_styles = ["fade_up", "fade_scale", "slide_left", "stagger_reveal", "bounce"]
        selected_animation = random.choice(animation_styles)
        self._current_animation_style = selected_animation
        print(f"[HTMLGenerator] ✨ Animation Style: {selected_animation}")
        
        # Build header with ANCHOR navigation (single page mode)
        header_html = self._render_header_single_page(
            navigation.get("header", {}), 
            colors, 
            project_name, 
            component_order, 
            components
        )
        
        # Build ALL sections sequentially
        sections_html = []
        for idx, comp_id in enumerate(component_order):
            comp = components.get(comp_id, {})
            comp_type = comp.get("type", "Unknown")
            actual_id = comp.get("id", comp_type.lower())
            
            # Select variant for variety
            variant = self._select_variant(comp_type, template_history)
            used_variants[comp_type] = variant
            
            print(f"[HTMLGenerator] 📄 Adding section: {actual_id} (variant: {variant})")
            
            # Render component with ID for anchor linking
            section_html = self._render_component_with_anchor(comp, colors, actual_id)
            if section_html:
                sections_html.append(section_html)
        
        # Build footer
        footer_html = self._render_footer(navigation.get("footer", {}), colors, project_name)
        
        # Build GSAP animations
        gsap_animations = self._build_gsap_animations()
        
        # Combine everything into a single HTML file
        full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{seo.get("title", project_name)}</title>
    <meta name="description" content="{seo.get("description", "")}">
    <meta name="keywords" content="{", ".join(seo.get("keywords", []))}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{self._get_google_fonts_url(fonts)}" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="{self.TAILWIND_CDN}"></script>
    <script>{tailwind_config}</script>
    
    <!-- Custom Styles -->
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: '{fonts["body"]}', sans-serif;
            background-color: {colors["background"]};
            color: {colors["text"]};
            overflow-x: hidden;
        }}
        h1, h2, h3, h4, h5, h6 {{ font-family: '{fonts["heading"]}', sans-serif; }}
        .gradient-text {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            color: white;
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 40px {colors["primary"]}40;
        }}
        .btn-secondary {{
            background: transparent;
            color: {colors["text"]};
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            border: 2px solid {colors["primary"]}30;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-secondary:hover {{
            border-color: {colors["primary"]};
            background: {colors["primary"]}10;
        }}
        .section {{ padding: 100px 0; }}
        .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
        .animate-on-scroll {{ opacity: 0; transform: translateY(40px); }}
        .nav-link {{ transition: color 0.3s ease; }}
        .nav-link:hover {{ color: {colors["primary"]}; }}
        .nav-link.active {{ color: {colors["primary"]}; font-weight: 600; }}
    </style>
</head>
<body>
    {header_html}
    
    <main>
        {"".join(sections_html)}
    </main>
    
    {footer_html}
    
    <!-- GSAP -->
    <script src="{self.GSAP_CDN}"></script>
    <script src="{self.GSAP_SCROLL_CDN}"></script>
    <script>{gsap_animations}</script>
    
    <!-- Smooth scroll and active nav highlighting -->
    <script>
        // Highlight active nav link on scroll
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        window.addEventListener('scroll', () => {{
            let current = '';
            sections.forEach(section => {{
                const sectionTop = section.offsetTop - 100;
                if (window.scrollY >= sectionTop) {{
                    current = section.getAttribute('id');
                }}
            }});
            
            navLinks.forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) {{
                    link.classList.add('active');
                }}
            }});
        }});
    </script>
</body>
</html>'''
        
        # Save variants to history
        used_variants["Header"] = selected_header_style
        self._save_template_history(used_variants)
        
        # Record in CombinationTracker
        if HAS_TEMPLATE_REGISTRY and CombinationTracker:
            try:
                session_variants = CombinationTracker.get_session_variants()
                final_combination = {**used_variants, **self._used_variants_in_current_gen, **session_variants}
                CombinationTracker.record_generation(
                    website_type=self._website_type,
                    used_variants=final_combination
                )
            except Exception as e:
                print(f"[HTMLGenerator] Failed to record in CombinationTracker: {e}")
        
        pages = {"index.html": full_html}
        
        # Save to file if output_dir provided
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, "index.html")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"[HTMLGenerator] 💾 Saved: {file_path}")
        
        # ============================================================
        # COMPLIANCE VALIDATION: Check website matches blueprint
        # ============================================================
        if HAS_COMPLIANCE_VALIDATOR and BlueprintComplianceValidator:
            try:
                session_id = blueprint.get("session_id", blueprint.get("blueprint_id", "unknown"))
                compliance_report = BlueprintComplianceValidator.generate_compliance_report(
                    blueprint=blueprint,
                    generated_html=pages,
                    session_id=session_id
                )
                
                # Track generation
                if BlueprintWebsiteTracker:
                    BlueprintWebsiteTracker.record_generation(
                        session_id=session_id,
                        blueprint=blueprint,
                        generated_html=pages,
                        used_variants=final_combination if 'final_combination' in dir() else used_variants
                    )
                
                if compliance_report["compliance_score"] < 70:
                    print(f"[HTMLGenerator] ⚠️ LOW COMPLIANCE SCORE: {compliance_report['compliance_score']}/100")
            except Exception as e:
                print(f"[HTMLGenerator] Compliance validation error: {e}")
        
        print(f"[HTMLGenerator] ✅ Generated SINGLE PAGE website!")
        return pages
    
    def _render_header_single_page(self, header: Dict[str, Any], colors: Dict[str, str], project_name: str, component_order: List[str], all_components: Dict[str, Any]) -> str:
        """Render navigation header with ANCHOR links for single page mode"""
        
        logo = header.get("logo", {})
        logo_text = logo.get("text", project_name) if isinstance(logo, dict) else project_name
        cta = header.get("cta", {})
        
        # Build anchor navigation links
        nav_items = []
        for idx, comp_id in enumerate(component_order):
            comp = all_components.get(comp_id, {})
            comp_type = comp.get("type", "")
            comp_name = comp.get("name", comp_type)
            actual_id = comp.get("id", comp_type.lower())
            
            # Skip CTA, Testimonials, Features from nav (too many links)
            if comp_type.lower() in ["cta", "testimonials"]:
                continue
            
            if idx == 0 or actual_id.lower() == "hero":
                nav_items.append({"text": "Home", "href": "#hero"})
            else:
                nav_items.append({"text": comp_name, "href": f"#{actual_id.lower()}"})
        
        # Use pre-selected header style
        selected_style = getattr(self, '_current_header_style', 'minimal')
        
        # Map style name to method (use anchor versions)
        style_methods = {
            "minimal": self._header_anchor_minimal,
            "centered": self._header_anchor_centered,
            "floating": self._header_anchor_floating,
            "dark": self._header_anchor_dark,
            "gradient": self._header_anchor_gradient
        }
        
        style_method = style_methods.get(selected_style, self._header_anchor_minimal)
        return style_method(logo_text, nav_items, cta, colors)
    
    def _header_anchor_minimal(self, logo_text, nav_items, cta, colors):
        """Minimal header with anchor links"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary font-medium">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="#hero" class="text-2xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                <a href="#contact" class="btn-primary hidden sm:inline-block">{cta.get("text", "Contact Us")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_anchor_centered(self, logo_text, nav_items, cta, colors):
        """Centered header with anchor links"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-600 hover:text-primary">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-white shadow-sm">
        <div class="container mx-auto px-6 py-5">
            <div class="flex flex-col items-center">
                <a href="#hero" class="text-3xl font-bold font-heading mb-3" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-10">{nav_links}</nav>
            </div>
        </div>
    </header>'''
    
    def _header_anchor_floating(self, logo_text, nav_items, cta, colors):
        """Floating pill header with anchor links"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary text-sm">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-4 left-1/2 -translate-x-1/2 z-50 w-[90%] max-w-5xl">
        <div class="bg-white/95 backdrop-blur-lg rounded-full shadow-lg px-8 py-3">
            <div class="flex items-center justify-between">
                <a href="#hero" class="text-xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-6">{nav_links}</nav>
                <a href="#contact" class="bg-primary text-white px-5 py-2 rounded-full text-sm font-semibold hover:shadow-lg transition-all" style="background: {colors["primary"]}">{cta.get("text", "Contact")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_anchor_dark(self, logo_text, nav_items, cta, colors):
        """Dark header with anchor links"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-300 hover:text-white">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-gray-900/95 backdrop-blur-md">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="#hero" class="text-2xl font-bold font-heading text-white">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                <a href="#contact" class="border border-white/30 text-white px-6 py-2 rounded-lg hover:bg-white hover:text-gray-900 transition-all">{cta.get("text", "Contact Us")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_anchor_gradient(self, logo_text, nav_items, cta, colors):
        """Gradient accent header with anchor links"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary font-medium">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50">
        <div class="h-1 bg-gradient-to-r" style="background: linear-gradient(90deg, {colors["primary"]}, {colors["secondary"]})"></div>
        <div class="bg-white shadow-sm">
            <div class="container mx-auto px-6 py-4">
                <div class="flex items-center justify-between">
                    <a href="#hero" class="text-2xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                    <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                    <a href="#contact" class="btn-primary">{cta.get("text", "Contact Us")}</a>
                </div>
            </div>
        </div>
    </header>'''
    
    def _render_component_with_anchor(self, comp: Dict[str, Any], colors: Dict[str, str], anchor_id: str) -> str:
        """Render a component wrapped with an anchor ID for single page navigation"""
        comp_type = comp.get("type", "Unknown").lower()
        
        # Use the existing render method
        inner_html = self._render_component(comp, colors)
        
        if not inner_html:
            return ""
        
        # Wrap with section ID for anchor navigation
        # Note: Some components might already have section tags, so we handle that
        if f'id="{anchor_id}"' in inner_html or f"id='{anchor_id}'" in inner_html:
            return inner_html
        
        # If it already starts with a <section> tag, inject the ID
        if inner_html.strip().startswith('<section'):
            # Inject id into existing section tag
            return inner_html.replace('<section', f'<section id="{anchor_id}"', 1)
        else:
            # Wrap in a section with ID
            return f'<section id="{anchor_id}">{inner_html}</section>'
    
    def _load_template_history(self) -> Dict[str, List[str]]:
        """Load last 10 generations' template variants from file"""
        history_file = os.path.join(os.path.dirname(__file__), ".template_history.json")
        try:
            if os.path.exists(history_file):
                with open(history_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"[HTMLGenerator] Could not load history: {e}")
        return {}
    
    def _save_template_history(self, used_variants: Dict[str, str]):
        """Save used variants to history, keeping last 10 per component type"""
        history_file = os.path.join(os.path.dirname(__file__), ".template_history.json")
        try:
            history = self._load_template_history()
            
            for comp_type, variant in used_variants.items():
                # Ensure we only save strings, not nested lists
                if not isinstance(variant, str):
                    continue
                    
                if comp_type not in history:
                    history[comp_type] = []
                
                # Only append if it's a string
                if isinstance(variant, str):
                    history[comp_type].append(variant)
                
                # Keep only last 10 and ensure all are strings
                history[comp_type] = [v for v in history[comp_type] if isinstance(v, str)][-10:]
            
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
        except Exception as e:
            print(f"[HTMLGenerator] Could not save history: {e}")
    
    def _select_variant(self, comp_type: str, history: Dict[str, List[str]]) -> str:
        """Select a variant that wasn't used in last 10 generations"""
        import random
        
        # Available variants per component type
        variants = {
            "Hero": ["centered", "split", "gradient", "minimal", "video-bg", "parallax"],
            "Home": ["centered", "split", "gradient", "minimal", "video-bg", "parallax"],  # Same as Hero
            "About": ["split-left", "split-right", "centered", "timeline", "cards", "story"],
            "Features": ["grid-3", "grid-4", "cards", "icons", "alternating", "minimal"],
            "Menu": ["grid", "list", "tabs", "accordion", "cards", "minimal"],
            "Gallery": ["masonry", "grid", "carousel", "lightbox", "minimal", "full-width"],
            "Testimonials": ["carousel", "grid-3", "cards", "minimal", "quotes", "slider"],
            "Contact": ["split", "centered", "map-bg", "minimal", "cards", "form-only"],
            "CTA": ["gradient", "minimal", "split", "centered", "pattern", "image-bg"],
            "FAQ": ["accordion", "grid", "tabs", "minimal", "cards", "expandable"],
            "Pricing": ["grid-3", "cards", "comparison", "minimal", "toggle", "featured"],
        }
        
        available = variants.get(comp_type, ["default"])
        recently_used = history.get(comp_type, [])
        
        # Filter out recently used variants
        fresh_variants = [v for v in available if v not in recently_used]
        
        # If all variants were used, reset and use any
        if not fresh_variants:
            fresh_variants = available
        
        return random.choice(fresh_variants)
    
    def _generate_standalone_page(
        self,
        page_name: str,
        project_name: str,
        seo: Dict[str, Any],
        colors: Dict[str, str],
        fonts: Dict[str, str],
        navigation: Dict[str, Any],
        component: Dict[str, Any],
        component_type: str,
        variant: str,
        tailwind_config: str,
        all_components: Dict[str, Any],
        component_order: List[str]
    ) -> str:
        """Generate a standalone page with header, rich content, and footer"""
        
        props = component.get("props", {})
        comp_id = component.get("id", component_type.lower())
        
        # Build header with navigation to all pages
        header_html = self._render_header_multipage(navigation.get("header", {}), colors, project_name, component_order, all_components)
        
        # Render MAIN component's content
        main_content_html = self._render_component(component, colors)
        
        # Add ADDITIONAL supporting sections based on component type
        supporting_html = self._render_supporting_sections(component_type, props, colors, project_name)
        
        # Add CTA section at bottom (except for Contact page)
        cta_html = ""
        if component_type.lower() not in ["contact", "cta"]:
            # Find CTA component from blueprint
            cta_data = None
            for comp_id, comp in all_components.items():
                if comp.get("type", "").lower() == "cta":
                    cta_data = comp
                    break
            cta_html = self._render_page_cta(colors, project_name, cta_data)
        
        # Combine all content
        content_html = main_content_html + supporting_html + cta_html
        
        # Build footer
        footer_html = self._render_footer(navigation.get("footer", {}), colors, project_name)
        
        # Build GSAP animations
        gsap_animations = self._build_gsap_animations()
        
        # Get page title
        page_title = props.get("title") or props.get("sectionTitle") or component_type
        full_title = f"{page_title} - {project_name}" if page_name != "index.html" else seo.get("title", project_name)
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{full_title}</title>
    <meta name="description" content="{seo.get("description", "")}">
    <meta name="keywords" content="{", ".join(seo.get("keywords", []))}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{self._get_google_fonts_url(fonts)}" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="{self.TAILWIND_CDN}"></script>
    <script>{tailwind_config}</script>
    
    <!-- Custom Styles -->
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: '{fonts["body"]}', sans-serif;
            background-color: {colors["background"]};
            color: {colors["text"]};
            overflow-x: hidden;
        }}
        h1, h2, h3, h4, h5, h6 {{ font-family: '{fonts["heading"]}', sans-serif; }}
        .gradient-text {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            color: white;
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 40px {colors["primary"]}40;
        }}
        .btn-secondary {{
            background: transparent;
            color: {colors["text"]};
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            border: 2px solid {colors["primary"]}30;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-secondary:hover {{
            border-color: {colors["primary"]};
            background: {colors["primary"]}10;
        }}
        .section {{ padding: 100px 0; }}
        .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
        .animate-on-scroll {{ opacity: 0; transform: translateY(40px); }}
        .nav-link {{ transition: color 0.3s ease; }}
        .nav-link:hover {{ color: {colors["primary"]}; }}
        .nav-link.active {{ color: {colors["primary"]}; font-weight: 600; }}
    </style>
</head>
<body>
    {header_html}
    
    <main>
        {content_html}
    </main>
    
    {footer_html}
    
    <!-- GSAP -->
    <script src="{self.GSAP_CDN}"></script>
    <script src="{self.GSAP_SCROLL_CDN}"></script>
    <script>{gsap_animations}</script>
</body>
</html>'''
    
    def _render_header_multipage(self, header: Dict[str, Any], colors: Dict[str, str], project_name: str, component_order: List[str], all_components: Dict[str, Any]) -> str:
        """Render navigation header - uses consistent style selected at generation start"""
        
        logo = header.get("logo", {})
        logo_text = logo.get("text", project_name) if isinstance(logo, dict) else project_name
        cta = header.get("cta", {})
        
        # Build navigation links
        nav_items = []
        for idx, comp_id in enumerate(component_order):
            comp = all_components.get(comp_id, {})
            comp_type = comp.get("type", "")
            comp_name = comp.get("name", comp_type)
            
            if idx == 0 or comp_type.lower() == "hero":
                nav_items.append({"text": "Home", "href": "index.html"})
            elif comp_type.lower() not in ["cta", "testimonials", "features"]:
                nav_items.append({"text": comp_name, "href": f"{comp_type.lower()}.html"})
        
        # Use pre-selected header style (same for all pages)
        selected_style = getattr(self, '_current_header_style', 'minimal')
        
        # Map style name to method
        style_methods = {
            "minimal": self._header_style_minimal,
            "centered": self._header_style_centered,
            "floating": self._header_style_floating,
            "dark": self._header_style_dark,
            "gradient": self._header_style_gradient
        }
        
        style_method = style_methods.get(selected_style, self._header_style_minimal)
        return style_method(logo_text, nav_items, cta, colors)
    
    def _header_style_minimal(self, logo_text, nav_items, cta, colors):
        """Minimal transparent header"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary font-medium">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="index.html" class="text-2xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                <a href="contact.html" class="btn-primary hidden sm:inline-block">{cta.get("text", "Contact Us")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_style_centered(self, logo_text, nav_items, cta, colors):
        """Centered logo header"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-600 hover:text-primary">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-white shadow-sm">
        <div class="container mx-auto px-6 py-5">
            <div class="flex flex-col items-center">
                <a href="index.html" class="text-3xl font-bold font-heading mb-3" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-10">{nav_links}</nav>
            </div>
        </div>
    </header>'''
    
    def _header_style_floating(self, logo_text, nav_items, cta, colors):
        """Floating pill header"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary text-sm">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-4 left-1/2 -translate-x-1/2 z-50 w-[90%] max-w-5xl">
        <div class="bg-white/95 backdrop-blur-lg rounded-full shadow-lg px-8 py-3">
            <div class="flex items-center justify-between">
                <a href="index.html" class="text-xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-6">{nav_links}</nav>
                <a href="contact.html" class="bg-primary text-white px-5 py-2 rounded-full text-sm font-semibold hover:shadow-lg transition-all" style="background: {colors["primary"]}">{cta.get("text", "Contact")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_style_dark(self, logo_text, nav_items, cta, colors):
        """Dark elegant header"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-300 hover:text-white">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50 bg-gray-900/95 backdrop-blur-md">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="index.html" class="text-2xl font-bold font-heading text-white">{logo_text}</a>
                <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                <a href="contact.html" class="border border-white/30 text-white px-6 py-2 rounded-lg hover:bg-white hover:text-gray-900 transition-all">{cta.get("text", "Contact Us")}</a>
            </div>
        </div>
    </header>'''
    
    def _header_style_gradient(self, logo_text, nav_items, cta, colors):
        """Gradient accent header"""
        nav_links = "".join([f'<a href="{item["href"]}" class="nav-link text-gray-700 hover:text-primary font-medium">{item["text"]}</a>' for item in nav_items])
        return f'''
    <header class="fixed top-0 left-0 right-0 z-50">
        <div class="h-1 bg-gradient-to-r" style="background: linear-gradient(90deg, {colors["primary"]}, {colors["secondary"]})"></div>
        <div class="bg-white shadow-sm">
            <div class="container mx-auto px-6 py-4">
                <div class="flex items-center justify-between">
                    <a href="index.html" class="text-2xl font-bold font-heading" style="color: {colors["primary"]}">{logo_text}</a>
                    <nav class="hidden md:flex items-center gap-8">{nav_links}</nav>
                    <a href="contact.html" class="btn-primary">{cta.get("text", "Contact Us")}</a>
                </div>
            </div>
        </div>
    </header>'''
    
    def _render_supporting_sections(self, component_type: str, props: Dict[str, Any], colors: Dict[str, str], project_name: str) -> str:
        """Render additional supporting content based on page type"""
        comp_lower = component_type.lower()
        
        # NOTE: Disabled hardcoded supporting sections - use blueprint components instead
        # These were causing repetitive generic content across all websites
        return ""
        
        # Old code below (kept for reference but not executed)
        if comp_lower == "hero":
            # Hero page gets features highlight
            return self._render_features_highlight(colors, project_name)
        elif comp_lower == "about":
            # About page gets values/team section
            return self._render_values_section(colors)
        elif comp_lower == "menu":
            # Menu page gets specials section
            return self._render_specials_section(colors)
        elif comp_lower == "gallery":
            # Gallery page gets Instagram section
            return self._render_instagram_section(colors)
        elif comp_lower == "contact":
            # Contact page gets map/hours section
            return self._render_hours_section(colors, project_name)
        else:
            return ""
    
    def _render_features_highlight(self, colors: Dict[str, str], project_name: str) -> str:
        """Features highlight for Hero page"""
        return f'''
        <section class="py-20 bg-gray-50">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl font-bold font-heading text-center mb-12">Why Choose Us</h2>
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                        <div class="w-16 h-16 mx-auto mb-6 rounded-full flex items-center justify-center" style="background: {colors["primary"]}20">
                            <svg class="w-8 h-8" style="color: {colors["primary"]}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Premium Quality</h3>
                        <p class="text-gray-600">Only the finest ingredients and materials, carefully selected for excellence.</p>
                    </div>
                    <div class="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                        <div class="w-16 h-16 mx-auto mb-6 rounded-full flex items-center justify-center" style="background: {colors["primary"]}20">
                            <svg class="w-8 h-8" style="color: {colors["primary"]}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Always Fresh</h3>
                        <p class="text-gray-600">Made fresh daily with passion and attention to every detail.</p>
                    </div>
                    <div class="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                        <div class="w-16 h-16 mx-auto mb-6 rounded-full flex items-center justify-center" style="background: {colors["primary"]}20">
                            <svg class="w-8 h-8" style="color: {colors["primary"]}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Made with Love</h3>
                        <p class="text-gray-600">Every creation is crafted with care and dedication to your satisfaction.</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def _render_values_section(self, colors: Dict[str, str]) -> str:
        """Values section for About page"""
        return f'''
        <section class="py-20 bg-white">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl font-bold font-heading text-center mb-4">Our Values</h2>
                <p class="text-gray-600 text-center max-w-2xl mx-auto mb-12">The principles that guide everything we do</p>
                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="p-6 border-l-4 bg-gray-50 rounded-r-xl" style="border-color: {colors["primary"]}">
                        <h3 class="text-lg font-bold mb-2">Quality First</h3>
                        <p class="text-gray-600 text-sm">Never compromising on the quality of our offerings.</p>
                    </div>
                    <div class="p-6 border-l-4 bg-gray-50 rounded-r-xl" style="border-color: {colors["primary"]}">
                        <h3 class="text-lg font-bold mb-2">Customer Focus</h3>
                        <p class="text-gray-600 text-sm">Your satisfaction is at the heart of everything we do.</p>
                    </div>
                    <div class="p-6 border-l-4 bg-gray-50 rounded-r-xl" style="border-color: {colors["primary"]}">
                        <h3 class="text-lg font-bold mb-2">Innovation</h3>
                        <p class="text-gray-600 text-sm">Constantly evolving to bring you the latest and best.</p>
                    </div>
                    <div class="p-6 border-l-4 bg-gray-50 rounded-r-xl" style="border-color: {colors["primary"]}">
                        <h3 class="text-lg font-bold mb-2">Sustainability</h3>
                        <p class="text-gray-600 text-sm">Committed to practices that protect our planet.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="py-20 bg-gray-50">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl font-bold font-heading text-center mb-12">Meet Our Team</h2>
                <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
                    <div class="text-center">
                        <div class="w-32 h-32 mx-auto mb-4 rounded-full bg-gray-200 overflow-hidden">
                            <img src="https://i.pravatar.cc/150?img=1" alt="Team Member" class="w-full h-full object-cover">
                        </div>
                        <h3 class="font-bold text-lg">Sarah Johnson</h3>
                        <p class="text-gray-500">Founder & CEO</p>
                    </div>
                    <div class="text-center">
                        <div class="w-32 h-32 mx-auto mb-4 rounded-full bg-gray-200 overflow-hidden">
                            <img src="https://i.pravatar.cc/150?img=3" alt="Team Member" class="w-full h-full object-cover">
                        </div>
                        <h3 class="font-bold text-lg">Michael Chen</h3>
                        <p class="text-gray-500">Head Chef</p>
                    </div>
                    <div class="text-center">
                        <div class="w-32 h-32 mx-auto mb-4 rounded-full bg-gray-200 overflow-hidden">
                            <img src="https://i.pravatar.cc/150?img=5" alt="Team Member" class="w-full h-full object-cover">
                        </div>
                        <h3 class="font-bold text-lg">Emily Davis</h3>
                        <p class="text-gray-500">Operations Manager</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def _render_specials_section(self, colors: Dict[str, str]) -> str:
        """Specials section for Menu page"""
        return f'''
        <section class="py-20" style="background: linear-gradient(135deg, {colors["primary"]}10, {colors["secondary"]}10)">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <span class="px-4 py-2 rounded-full text-sm font-semibold mb-4 inline-block" style="background: {colors["primary"]}20; color: {colors["primary"]}">Limited Time</span>
                    <h2 class="text-3xl font-bold font-heading">Today's Specials</h2>
                </div>
                <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <div class="bg-white p-8 rounded-2xl shadow-lg flex gap-6 items-center">
                        <div class="w-24 h-24 rounded-xl bg-gray-200 shrink-0 overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=150" alt="Special" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <h3 class="font-bold text-xl mb-2">Chef's Special</h3>
                            <p class="text-gray-600 text-sm mb-2">A unique creation featuring the finest seasonal ingredients.</p>
                            <p class="font-bold text-xl" style="color: {colors["primary"]}">$24.99</p>
                        </div>
                    </div>
                    <div class="bg-white p-8 rounded-2xl shadow-lg flex gap-6 items-center">
                        <div class="w-24 h-24 rounded-xl bg-gray-200 shrink-0 overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=150" alt="Special" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <h3 class="font-bold text-xl mb-2">Signature Blend</h3>
                            <p class="text-gray-600 text-sm mb-2">Our award-winning house specialty, crafted to perfection.</p>
                            <p class="font-bold text-xl" style="color: {colors["primary"]}">$8.99</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def _render_instagram_section(self, colors: Dict[str, str]) -> str:
        """Instagram feed section for Gallery page"""
        return f'''
        <section class="py-20 bg-white">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold font-heading mb-4">Follow Us on Instagram</h2>
                    <a href="#" class="inline-flex items-center gap-2 font-semibold" style="color: {colors["primary"]}">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63z"/></svg>
                        @our_instagram
                    </a>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=1" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=2" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=3" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=4" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=5" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                    <div class="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:opacity-80 transition-opacity cursor-pointer">
                        <img src="https://picsum.photos/300/300?random=6" alt="Instagram" class="w-full h-full object-cover">
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def _render_hours_section(self, colors: Dict[str, str], project_name: str) -> str:
        """Hours and location section for Contact page"""
        return f'''
        <section class="py-20 bg-gray-50">
            <div class="container mx-auto px-6">
                <div class="grid md:grid-cols-2 gap-12 max-w-4xl mx-auto">
                    <div>
                        <h2 class="text-2xl font-bold font-heading mb-6">Opening Hours</h2>
                        <div class="space-y-4">
                            <div class="flex justify-between py-3 border-b border-gray-200">
                                <span class="font-medium">Monday - Friday</span>
                                <span class="text-gray-600">7:00 AM - 9:00 PM</span>
                            </div>
                            <div class="flex justify-between py-3 border-b border-gray-200">
                                <span class="font-medium">Saturday</span>
                                <span class="text-gray-600">8:00 AM - 10:00 PM</span>
                            </div>
                            <div class="flex justify-between py-3 border-b border-gray-200">
                                <span class="font-medium">Sunday</span>
                                <span class="text-gray-600">9:00 AM - 8:00 PM</span>
                            </div>
                        </div>
                    </div>
                    <div>
                        <h2 class="text-2xl font-bold font-heading mb-6">Find Us</h2>
                        <div class="bg-gray-200 rounded-xl h-48 mb-4 overflow-hidden">
                            <img src="https://maps.googleapis.com/maps/api/staticmap?center=New+York&zoom=14&size=600x300&maptype=roadmap&key=placeholder" alt="Map" class="w-full h-full object-cover opacity-50">
                        </div>
                        <p class="text-gray-600">123 Main Street, Suite 100<br>New York, NY 10001</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def _render_page_cta(self, colors: Dict[str, str], project_name: str, cta_data: Dict[str, Any] = None) -> str:
        """CTA section for bottom of pages - uses blueprint data if available"""
        # Use blueprint CTA data if provided, otherwise use project-specific defaults
        if cta_data:
            props = cta_data.get("props", {})
            cta_title = props.get("title", f"Ready to Get Started with {project_name}?")
            cta_desc = props.get("description", f"Contact us today to learn more about what {project_name} can offer you.")
            cta_btn = props.get("ctaText", "Get in Touch")
        else:
            cta_title = f"Ready to Get Started with {project_name}?"
            cta_desc = f"Contact us today to discover what makes {project_name} special."
            cta_btn = "Contact Us"
        
        return f'''
        <section class="py-24 relative overflow-hidden" style="background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]})">
            <div class="absolute inset-0 opacity-10">
                <div class="absolute top-10 left-10 w-32 h-32 bg-white rounded-full blur-3xl"></div>
                <div class="absolute bottom-10 right-10 w-48 h-48 bg-white rounded-full blur-3xl"></div>
            </div>
            <div class="container mx-auto px-6 text-center relative z-10">
                <h2 class="text-3xl md:text-4xl font-bold font-heading text-white mb-4">{cta_title}</h2>
                <p class="text-white/80 text-lg max-w-2xl mx-auto mb-8">{cta_desc}</p>
                <div class="flex flex-wrap gap-4 justify-center">
                    <a href="contact.html" class="bg-white px-8 py-4 rounded-full font-semibold text-lg hover:shadow-xl transition-all hover:-translate-y-1" style="color: {colors["primary"]}">
                        {cta_btn}
                    </a>
                </div>
            </div>
        </section>
        '''
    
    def _extract_colors(self, theme: Dict[str, Any]) -> Dict[str, str]:
        """Extract color palette from theme with smart text color validation"""
        palette = theme.get("colorPalette", {})
        
        # Extract basic colors
        background = palette.get("background", "#FFFFFF")
        text = palette.get("text", "#1F2937")
        primary = palette.get("primary", theme.get("primaryColor", "#4F46E5"))
        
        # Validate text contrast and fix if needed
        if HAS_COLOR_UTILS:
            # Check if text has sufficient contrast with background
            contrast = ColorUtils.get_contrast_ratio(background, text)
            if contrast < 4.5:  # WCAG AA standard
                text = ColorUtils.get_text_color_for_background(background)
                print(f"[HTMLGenerator] ⚠️ Fixed text color for better contrast: {text}")
            
            # Generate text_on_primary for buttons/CTAs
            text_on_primary = ColorUtils.get_text_color_for_background(primary)
        else:
            text_on_primary = "#FFFFFF"
        
        return {
            "primary": primary,
            "secondary": palette.get("secondary", "#10B981"),
            "accent": palette.get("accent", "#F59E0B"),
            "background": background,
            "surface": palette.get("surface", "#F9FAFB"),
            "text": text,
            "text_muted": palette.get("textMuted", "#6B7280"),
            "text_on_primary": text_on_primary,
            "text_on_dark": "#FFFFFF",
            "text_on_light": "#1A1A1A"
        }
    
    def _extract_fonts(self, global_styles: Dict[str, Any]) -> Dict[str, str]:
        """Extract font families from global styles"""
        typography = global_styles.get("typography", {})
        heading_font = typography.get("headingFont", {})
        body_font = typography.get("bodyFont", {})
        
        return {
            "heading": heading_font.get("family", "Inter"),
            "body": body_font.get("family", "Inter"),
            "heading_weights": heading_font.get("weights", [400, 600, 700]),
            "body_weights": body_font.get("weights", [300, 400, 500])
        }
    
    def _build_tailwind_config(self, colors: Dict[str, str], fonts: Dict[str, str]) -> str:
        """Build Tailwind CSS configuration"""
        return f"""
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            primary: '{colors["primary"]}',
            secondary: '{colors["secondary"]}',
            accent: '{colors["accent"]}',
            surface: '{colors["surface"]}',
          }},
          fontFamily: {{
            heading: ['{fonts["heading"]}', 'sans-serif'],
            body: ['{fonts["body"]}', 'sans-serif'],
          }},
        }},
      }},
    }}
        """
    
    def _get_google_fonts_url(self, fonts: Dict[str, str]) -> str:
        """Generate Google Fonts URL"""
        families = []
        
        heading = fonts["heading"].replace(" ", "+")
        heading_weights = ",".join(map(str, fonts["heading_weights"]))
        families.append(f"family={heading}:wght@{heading_weights}")
        
        if fonts["body"] != fonts["heading"]:
            body = fonts["body"].replace(" ", "+")
            body_weights = ",".join(map(str, fonts["body_weights"]))
            families.append(f"family={body}:wght@{body_weights}")
        
        return f"https://fonts.googleapis.com/css2?{'&'.join(families)}&display=swap"
    
    def _generate_index_page(
        self,
        project_name: str,
        seo: Dict[str, Any],
        theme: Dict[str, Any],
        colors: Dict[str, str],
        fonts: Dict[str, str],
        navigation: Dict[str, Any],
        components: Dict[str, Any],
        component_order: List[str],
        tailwind_config: str
    ) -> str:
        """Generate main index.html with all components"""
        
        # Build header
        header_html = self._render_header(navigation.get("header", {}), colors, project_name)
        
        # Build all sections
        sections_html = []
        for comp_id in component_order:
            comp = components.get(comp_id, {})
            section_html = self._render_component(comp, colors)
            if section_html:
                sections_html.append(section_html)
        
        # Build footer
        footer_html = self._render_footer(navigation.get("footer", {}), colors, project_name)
        
        # Build GSAP animations
        gsap_animations = self._build_gsap_animations()
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{seo.get("title", project_name)}</title>
    <meta name="description" content="{seo.get("description", "")}">
    <meta name="keywords" content="{", ".join(seo.get("keywords", []))}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{self._get_google_fonts_url(fonts)}" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="{self.TAILWIND_CDN}"></script>
    <script>{tailwind_config}</script>
    
    <!-- Custom Base Styles -->
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        html {{
            scroll-behavior: smooth;
        }}
        body {{
            font-family: '{fonts["body"]}', sans-serif;
            background-color: {colors["background"]};
            color: {colors["text"]};
            overflow-x: hidden;
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-family: '{fonts["heading"]}', sans-serif;
        }}
        .gradient-text {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            color: white;
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 40px {colors["primary"]}40;
        }}
        .btn-secondary {{
            background: transparent;
            color: {colors["text"]};
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            border: 2px solid {colors["primary"]}30;
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }}
        .btn-secondary:hover {{
            border-color: {colors["primary"]};
            background: {colors["primary"]}10;
        }}
        .section {{
            padding: 100px 0;
        }}
        .container {{
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        .animate-on-scroll {{
            opacity: 0;
            transform: translateY(40px);
        }}
    </style>
</head>
<body>
    {header_html}
    
    <main>
        {"".join(sections_html)}
    </main>
    
    {footer_html}
    
    <!-- GSAP Animation Library -->
    <script src="{self.GSAP_CDN}"></script>
    <script src="{self.GSAP_SCROLL_CDN}"></script>
    
    <!-- Animations -->
    <script>
        {gsap_animations}
    </script>
</body>
</html>'''
    
    def _render_header(self, header: Dict[str, Any], colors: Dict[str, str], project_name: str) -> str:
        """Render navigation header with Tailwind"""
        logo = header.get("logo", {})
        logo_text = logo.get("text", project_name) if isinstance(logo, dict) else project_name
        links = header.get("links", [])
        cta = header.get("cta", {})
        
        # Build navigation links
        nav_links = ""
        for link in links:
            if link.get("text", "").lower() != "login":
                nav_links += f'''
                <a href="{link.get("href", "#")}" 
                   class="text-gray-700 hover:text-primary transition-colors font-medium">
                    {link.get("text", "Link")}
                </a>'''
        
        # Login link
        login_link = ""
        for link in links:
            if link.get("text", "").lower() == "login":
                login_link = f'''
                <a href="{link.get("href", "/login")}" 
                   class="text-gray-600 hover:text-primary transition-colors">
                    Login
                </a>'''
        
        return f'''
    <!-- Header -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-lg border-b border-gray-100">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <!-- Logo -->
                <a href="#" class="text-2xl font-bold font-heading" style="color: {colors["primary"]}">
                    {logo_text}
                </a>
                
                <!-- Navigation -->
                <nav class="hidden md:flex items-center gap-8">
                    {nav_links}
                </nav>
                
                <!-- Right Side -->
                <div class="flex items-center gap-4">
                    {login_link}
                    <a href="{cta.get("href", "#contact")}" class="btn-primary hidden sm:inline-block">
                        {cta.get("text", "Get Started")}
                    </a>
                    
                    <!-- Mobile Menu Button -->
                    <button class="md:hidden p-2" onclick="toggleMobileMenu()">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile Menu -->
        <div id="mobileMenu" class="hidden md:hidden bg-white border-t border-gray-100 py-4">
            <nav class="container mx-auto px-6 flex flex-col gap-4">
                {nav_links}
                <a href="{cta.get("href", "#contact")}" class="btn-primary text-center">
                    {cta.get("text", "Get Started")}
                </a>
            </nav>
        </div>
    </header>
    
    <script>
        function toggleMobileMenu() {{
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('hidden');
        }}
    </script>
        '''
    
    def _render_component(self, comp: Dict[str, Any], colors: Dict[str, str]) -> str:
        """
        Route to appropriate component renderer using template classes.
        Uses TYPE-SPECIFIC templates based on website type (cafe, gaming, etc.).
        Falls back to generic templates if type-specific not available.
        """
        import random
        
        comp_type = comp.get("type", "")
        props = comp.get("props", {})
        comp_id = comp.get("id", comp_type.lower())
        website_type = getattr(self, '_website_type', None) or 'agency'
        
        # Try TYPE-SPECIFIC templates first (via TemplateRegistry)
        if HAS_TEMPLATE_REGISTRY:
            try:
                # Get type-specific template HTML
                html = TemplateRegistry.get_section_template(
                    website_type=website_type,
                    section_type=comp_type.lower(),
                    props=props,
                    colors=colors,
                    variant=None  # Let it choose random variant
                )
                
                if html:
                    print(f"[HTMLGenerator] 🎨 {comp_type}: Using {website_type}-specific template")
                    
                    # Try to capture which variant was used if we can detect it
                    # (Registry.get_section_template now handles tracker internally if no variant passed)
                    return html
            except Exception as e:
                print(f"[HTMLGenerator] Type-specific template error: {e}, falling back to generic")
        
        # Fallback to GENERIC templates
        try:
            from ..templates import (
                HeroTemplates,
                AboutTemplates,
                FeaturesTemplates,
                MenuTemplates,
                GalleryTemplates,
                TestimonialsTemplates,
                CTATemplates,
                ContactTemplates,
                FAQTemplates,
                PricingTemplates
            )
        except ImportError as e:
            print(f"[HTMLGenerator] Template import error: {e}")
            return self._render_component_fallback(comp, colors)
        
        # Map component types to generic template classes
        template_map = {
            "Hero": HeroTemplates,
            "About": AboutTemplates,
            "Features": FeaturesTemplates,
            "Menu": MenuTemplates,
            "Gallery": GalleryTemplates,
            "Testimonials": TestimonialsTemplates,
            "CTA": CTATemplates,
            "Contact": ContactTemplates,
            "FAQ": FAQTemplates,
            "Pricing": PricingTemplates,
        }
        
        template_class = template_map.get(comp_type)
        if template_class:
            # Load history to avoid recent variants
            history = self._load_template_history()
            recently_used = history.get(comp_type, [])
            
            # Get available variants
            declared_variants = getattr(template_class, 'VARIANTS', ['default'])
            available_variants = []
            
            # Check for _variant_ methods (legacy)
            for v in declared_variants:
                method_name = f"_variant_{v.replace('-', '_')}"
                if hasattr(template_class, method_name):
                    available_variants.append(v)
            
            # If no _variant_ methods, but class has render or get_variant, use declared_variants as is
            if not available_variants and (hasattr(template_class, 'render') or hasattr(template_class, 'get_variant')):
                available_variants = declared_variants
            
            if not available_variants:
                print(f"[HTMLGenerator] ⚠️ No variants found for {comp_type}, using fallback")
                return self._render_component_fallback(comp, colors)
            
            # Filter out recently used
            fresh_variants = [v for v in available_variants if v not in recently_used]
            if not fresh_variants:
                fresh_variants = available_variants
            
            selected_variant = random.choice(fresh_variants)
            print(f"[HTMLGenerator] 🎨 {comp_type}: Using generic variant '{selected_variant}'")
            
            try:
                # Try .render first (modern), then .get_variant (legacy)
                if hasattr(template_class, 'render'):
                    html = template_class.render(props, colors, selected_variant)
                else:
                    html = template_class.get_variant(selected_variant, props, colors)
                    
                self._save_template_history({comp_type: selected_variant})
                return html
            except Exception as e:
                print(f"[HTMLGenerator] Template render error for {comp_type}: {e}")
                return self._render_component_fallback(comp, colors)

        
        return ""
    
    def _render_component_fallback(self, comp: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Fallback to hardcoded renderers if templates fail"""
        comp_type = comp.get("type", "")
        props = comp.get("props", {})
        comp_id = comp.get("id", comp_type.lower())
        
        fallback_renderers = {
            "hero": self._render_hero,
            "home": self._render_hero,
            "about": self._render_about,
            "features": self._render_features,
            "services": self._render_services,
            "menu": self._render_menu,
            "specials": self._render_specials,
            "hours": self._render_hours,
            "gallery": self._render_gallery,
            "testimonials": self._render_testimonials,
            "cta": self._render_cta,
            "contact": self._render_contact,
            "reservation": self._render_contact,  # Use contact as fallback for reservation
            "reservations": self._render_contact,
            "faq": self._render_faq,
            "pricing": self._render_pricing,
        }
        
        # Case-insensitive lookup
        renderer = fallback_renderers.get(comp_type.lower())
        if renderer:
            print(f"[HTMLGenerator] ⚠️ Using fallback renderer for {comp_type}")
            return renderer(props, colors, comp_id)
        
        print(f"[HTMLGenerator] ❌ No renderer found for component type: {comp_type}")
        return ""
    
    def _render_hero(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Hero section with Tailwind + GSAP"""
        title = props.get("title", "Welcome")
        subtitle = props.get("subtitle", "")
        description = props.get("description", "")
        cta = props.get("cta", "Get Started")
        cta_secondary = props.get("ctaSecondary", "Learn More")
        
        return f'''
    <!-- Hero Section -->
    <section id="{section_id}" class="min-h-screen flex items-center pt-20 relative overflow-hidden">
        <!-- Background Gradient -->
        <div class="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-secondary/5"></div>
        <div class="absolute top-20 right-0 w-96 h-96 bg-primary/10 rounded-full blur-3xl"></div>
        <div class="absolute bottom-20 left-0 w-80 h-80 bg-secondary/10 rounded-full blur-3xl"></div>
        
        <div class="container mx-auto px-6 relative z-10">
            <div class="max-w-4xl mx-auto text-center">
                <!-- Badge -->
                <div class="animate-on-scroll inline-block px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-semibold mb-6">
                    Welcome ✨
                </div>
                
                <!-- Title -->
                <h1 class="animate-on-scroll text-5xl md:text-7xl font-bold font-heading leading-tight mb-6">
                    <span class="gradient-text">{title}</span>
                </h1>
                
                <!-- Subtitle -->
                <p class="animate-on-scroll text-xl md:text-2xl text-gray-500 mb-4">
                    {subtitle}
                </p>
                
                <!-- Description -->
                <p class="animate-on-scroll text-lg text-gray-600 max-w-2xl mx-auto mb-10 leading-relaxed">
                    {description}
                </p>
                
                <!-- CTA Buttons -->
                <div class="animate-on-scroll flex flex-wrap gap-4 justify-center">
                    <a href="#contact" class="btn-primary text-lg px-8 py-4">
                        {cta}
                    </a>
                    <a href="#about" class="btn-secondary text-lg px-8 py-4">
                        {cta_secondary}
                    </a>
                </div>
                
                <!-- Scroll Indicator -->
                <div class="animate-on-scroll mt-20">
                    <div class="w-6 h-10 border-2 border-gray-300 rounded-full mx-auto flex justify-center">
                        <div class="w-1.5 h-3 bg-gray-400 rounded-full mt-2 animate-bounce"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
        '''
    
    def _render_about(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render About section"""
        title = props.get("title", "About Us")
        story = props.get("story", "")
        stats = props.get("stats", [])
        
        # Build stats HTML
        stats_html = ""
        for stat in stats[:4]:
            stats_html += f'''
            <div class="text-center">
                <div class="text-4xl font-bold text-primary mb-2">{stat.get("value", "0")}</div>
                <div class="text-gray-500">{stat.get("label", "")}</div>
            </div>'''
        
        # Split story into paragraphs
        paragraphs = story.split("\n\n") if story else [""]
        story_html = "".join([f'<p class="text-gray-600 leading-relaxed mb-4">{p}</p>' for p in paragraphs])
        
        return f'''
    <!-- About Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-16 items-center">
                <!-- Content -->
                <div class="animate-on-scroll">
                    <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">About Us</span>
                    <h2 class="text-4xl md:text-5xl font-bold font-heading mb-8">{title}</h2>
                    <div class="space-y-4">
                        {story_html}
                    </div>
                </div>
                
                <!-- Stats -->
                <div class="animate-on-scroll">
                    <div class="bg-white rounded-3xl p-10 shadow-xl">
                        <div class="grid grid-cols-2 gap-8">
                            {stats_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
        '''
    
    def _render_features(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Features section"""
        title = props.get("sectionTitle", "Our Features")
        subtitle = props.get("sectionSubtitle", "")
        features = props.get("featureList", [])
        
        features_html = ""
        for i, feature in enumerate(features):
            features_html += f'''
            <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all hover:-translate-y-2 group">
                <div class="w-16 h-16 bg-primary/10 rounded-2xl flex items-center justify-center text-3xl mb-6 group-hover:scale-110 transition-transform">
                    {feature.get("icon", "✨")}
                </div>
                <h3 class="text-xl font-bold font-heading mb-3">{feature.get("title", "Feature")}</h3>
                <p class="text-gray-600 leading-relaxed">{feature.get("description", "")}</p>
            </div>'''
        
        return f'''
    <!-- Features Section -->
    <section id="{section_id}" class="section">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Features</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
                <p class="text-xl text-gray-500">{subtitle}</p>
            </div>
            
            <!-- Features Grid -->
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                {features_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_services(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Services/Menu section - handles both Services and Menu items"""
        title = props.get("sectionTitle", "Our Services")
        categories = props.get("categories", [])
        items = props.get("items", [])
        
        # If no items provided, return a placeholder
        if not items:
            return f'''
    <!-- Services Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Services</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all">
                    <div class="w-16 h-16 bg-primary/10 rounded-2xl flex items-center justify-center text-3xl mb-6">🍽️</div>
                    <h3 class="text-xl font-bold font-heading mb-3">Quality Food</h3>
                    <p class="text-gray-600">Fresh ingredients prepared with care</p>
                </div>
                <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all">
                    <div class="w-16 h-16 bg-primary/10 rounded-2xl flex items-center justify-center text-3xl mb-6">⭐</div>
                    <h3 class="text-xl font-bold font-heading mb-3">Premium Service</h3>
                    <p class="text-gray-600">Exceptional dining experience guaranteed</p>
                </div>
                <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all">
                    <div class="w-16 h-16 bg-primary/10 rounded-2xl flex items-center justify-center text-3xl mb-6">🚚</div>
                    <h3 class="text-xl font-bold font-heading mb-3">Fast Delivery</h3>
                    <p class="text-gray-600">Quick delivery to your doorstep</p>
                </div>
            </div>
        </div>
    </section>
            '''
        
        # Group items by category
        items_by_category = {}
        for item in items:
            cat = item.get("category", "Other")
            if cat not in items_by_category:
                items_by_category[cat] = []
            items_by_category[cat].append(item)
        
        # Build service items HTML
        services_html = ""
        for cat in categories if categories else list(items_by_category.keys()):
            cat_items = items_by_category.get(cat, [])
            if cat_items:
                items_html = ""
                for item in cat_items:
                    items_html += f'''
                    <div class="animate-on-scroll flex justify-between items-start p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition-all group">
                        <div class="flex-1">
                            <h4 class="font-bold text-lg font-heading mb-2 group-hover:text-primary transition-colors">{item.get("name", "Item")}</h4>
                            <p class="text-gray-500 text-sm leading-relaxed">{item.get("description", "")}</p>
                        </div>
                        <div class="text-xl font-bold text-primary ml-4">{item.get("price", "")}</div>
                    </div>'''
                
                services_html += f'''
                <div class="mb-12">
                    <h3 class="animate-on-scroll text-2xl font-bold font-heading mb-6 flex items-center">
                        <span class="w-8 h-1 bg-primary rounded-full mr-4"></span>
                        {cat}
                    </h3>
                    <div class="grid md:grid-cols-2 gap-4">
                        {items_html}
                    </div>
                </div>'''
        
        return f'''
    <!-- Services Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Our Offerings</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
            </div>
            
            <!-- Services/Menu Items -->
            <div class="max-w-4xl mx-auto">
                {services_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_menu(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Menu section for restaurants/cafes"""
        title = props.get("sectionTitle", "Our Menu")
        categories = props.get("categories", [])
        raw_items = props.get("items", [])
        
        # Normalize items to dict format
        items = []
        for item in raw_items:
            if isinstance(item, str):
                items.append({"name": item, "category": "Menu", "price": "", "description": ""})
            elif isinstance(item, dict):
                items.append(item)
            else:
                items.append({"name": str(item), "category": "Menu", "price": "", "description": ""})
        
        # Group items by category
        items_by_category = {}
        for item in items:
            cat = item.get("category", "Other")
            if cat not in items_by_category:
                items_by_category[cat] = []
            items_by_category[cat].append(item)
        
        # Build menu HTML
        menu_html = ""
        for cat in categories:
            cat_items = items_by_category.get(cat, [])
            if cat_items:
                items_html = ""
                for item in cat_items:
                    items_html += f'''
                    <div class="animate-on-scroll flex justify-between items-start p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition-all group">
                        <div class="flex-1">
                            <h4 class="font-bold text-lg font-heading mb-2 group-hover:text-primary transition-colors">{item.get("name", "Item")}</h4>
                            <p class="text-gray-500 text-sm leading-relaxed">{item.get("description", "")}</p>
                        </div>
                        <div class="text-xl font-bold text-primary ml-4">{item.get("price", "")}</div>
                    </div>'''
                
                menu_html += f'''
                <div class="mb-12">
                    <h3 class="animate-on-scroll text-2xl font-bold font-heading mb-6 flex items-center">
                        <span class="w-8 h-1 bg-primary rounded-full mr-4"></span>
                        {cat}
                    </h3>
                    <div class="grid md:grid-cols-2 gap-4">
                        {items_html}
                    </div>
                </div>'''
        
        return f'''
    <!-- Menu Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Menu</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
            </div>
            
            <!-- Menu Items -->
            <div class="max-w-4xl mx-auto">
                {menu_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_gallery(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Gallery section"""
        title = props.get("title", "Gallery")
        subtitle = props.get("subtitle", "")
        images = props.get("images", [])
        
        # Generate placeholder images if none provided
        if not images or all("example.com" in img for img in images):
            images = [
                f"https://picsum.photos/600/400?random={i}" for i in range(8)
            ]
        
        images_html = ""
        for i, img in enumerate(images[:8]):
            size_class = "md:col-span-2 md:row-span-2" if i == 0 or i == 3 else ""
            images_html += f'''
            <div class="animate-on-scroll {size_class} overflow-hidden rounded-2xl group">
                <img src="{img}" alt="Gallery {i+1}" 
                     class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                     loading="lazy">
            </div>'''
        
        return f'''
    <!-- Gallery Section -->
    <section id="{section_id}" class="section">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Gallery</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
                <p class="text-xl text-gray-500">{subtitle}</p>
            </div>
            
            <!-- Masonry Grid -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                {images_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_testimonials(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Testimonials section"""
        title = props.get("sectionTitle", "What Our Customers Say")
        testimonials = props.get("testimonials", [])
        
        testimonials_html = ""
        for testimonial in testimonials[:3]:
            testimonials_html += f'''
            <div class="animate-on-scroll bg-white rounded-3xl p-8 shadow-lg">
                <!-- Quote -->
                <div class="text-primary text-4xl mb-4">"</div>
                <p class="text-gray-600 text-lg leading-relaxed mb-6">{testimonial.get("quote", "")}</p>
                
                <!-- Author -->
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center text-primary font-bold">
                        {testimonial.get("author", "A")[0]}
                    </div>
                    <div>
                        <div class="font-bold">{testimonial.get("author", "Anonymous")}</div>
                        <div class="text-gray-500 text-sm">{testimonial.get("role", "Customer")}</div>
                    </div>
                </div>
            </div>'''
        
        return f'''
    <!-- Testimonials Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Testimonials</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading">{title}</h2>
            </div>
            
            <!-- Testimonials Grid -->
            <div class="grid md:grid-cols-3 gap-8">
                {testimonials_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_cta(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render CTA section"""
        title = props.get("title", "Ready to Get Started?")
        description = props.get("description", "")
        cta_text = props.get("ctaText", "Book Now")
        
        return f'''
    <!-- CTA Section -->
    <section id="{section_id}" class="py-24 relative overflow-hidden" style="background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]})">
        <!-- Background Pattern -->
        <div class="absolute inset-0 opacity-10">
            <div class="absolute inset-0" style="background-image: radial-gradient(circle, white 1px, transparent 1px); background-size: 30px 30px;"></div>
        </div>
        
        <div class="container mx-auto px-6 relative z-10">
            <div class="animate-on-scroll text-center max-w-3xl mx-auto text-white">
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-6">{title}</h2>
                <p class="text-xl opacity-90 mb-10">{description}</p>
                <a href="#contact" class="inline-block bg-white text-primary px-10 py-4 rounded-xl font-bold text-lg hover:shadow-2xl transition-all hover:-translate-y-1">
                    {cta_text}
                </a>
            </div>
        </div>
    </section>
        '''
    
    def _render_contact(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Contact section"""
        title = props.get("title", "Contact Us")
        subtitle = props.get("subtitle", "")
        email = props.get("email", "hello@example.com")
        phone = props.get("phone", "+1 234 567 890")
        address = props.get("address", "")
        hours = props.get("openingHours", "")
        
        return f'''
    <!-- Contact Section -->
    <section id="{section_id}" class="section">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-16">
                <!-- Contact Info -->
                <div class="animate-on-scroll">
                    <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Contact</span>
                    <h2 class="text-4xl md:text-5xl font-bold font-heading mb-6">{title}</h2>
                    <p class="text-gray-600 text-lg mb-10">{subtitle}</p>
                    
                    <div class="space-y-6">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center text-xl">📧</div>
                            <div>
                                <div class="font-bold mb-1">Email</div>
                                <a href="mailto:{email}" class="text-gray-500 hover:text-primary transition-colors">{email}</a>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center text-xl">📞</div>
                            <div>
                                <div class="font-bold mb-1">Phone</div>
                                <a href="tel:{phone}" class="text-gray-500 hover:text-primary transition-colors">{phone}</a>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center text-xl">📍</div>
                            <div>
                                <div class="font-bold mb-1">Address</div>
                                <div class="text-gray-500">{address}</div>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center text-xl">🕐</div>
                            <div>
                                <div class="font-bold mb-1">Hours</div>
                                <div class="text-gray-500">{hours}</div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Contact Form -->
                <div class="animate-on-scroll">
                    <form class="bg-gray-50 rounded-3xl p-8 md:p-10">
                        <div class="space-y-6">
                            <div>
                                <input type="text" placeholder="Your Name *" required
                                       class="w-full px-6 py-4 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all">
                            </div>
                            <div>
                                <input type="email" placeholder="Your Email *" required
                                       class="w-full px-6 py-4 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all">
                            </div>
                            <div>
                                <textarea placeholder="Your Message *" rows="5" required
                                          class="w-full px-6 py-4 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all resize-none"></textarea>
                            </div>
                            <button type="submit" class="btn-primary w-full py-4 text-lg">
                                Send Message
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
        '''
    
    def _render_faq(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render FAQ section"""
        title = props.get("sectionTitle", "Frequently Asked Questions")
        faq_list = props.get("faqList", [])
        
        faq_html = ""
        for i, faq in enumerate(faq_list):
            faq_html += f'''
            <div class="animate-on-scroll border-b border-gray-200">
                <button onclick="toggleFAQ({i})" 
                        class="w-full flex justify-between items-center py-6 text-left hover:text-primary transition-colors">
                    <span class="font-bold text-lg pr-4">{faq.get("question", "Question?")}</span>
                    <span id="faq-icon-{i}" class="text-2xl transition-transform">+</span>
                </button>
                <div id="faq-answer-{i}" class="hidden pb-6 text-gray-600 leading-relaxed">
                    {faq.get("answer", "")}
                </div>
            </div>'''
        
        return f'''
    <!-- FAQ Section -->
    <section id="{section_id}" class="section bg-gray-50">
        <div class="container mx-auto px-6">
            <div class="max-w-3xl mx-auto">
                <!-- Header -->
                <div class="animate-on-scroll text-center mb-12">
                    <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">FAQ</span>
                    <h2 class="text-4xl md:text-5xl font-bold font-heading">{title}</h2>
                </div>
                
                <!-- FAQ List -->
                <div class="bg-white rounded-3xl p-8">
                    {faq_html}
                </div>
            </div>
        </div>
    </section>
    
    <script>
        function toggleFAQ(index) {{
            const answer = document.getElementById('faq-answer-' + index);
            const icon = document.getElementById('faq-icon-' + index);
            
            if (answer.classList.contains('hidden')) {{
                answer.classList.remove('hidden');
                icon.textContent = '−';
                icon.style.transform = 'rotate(180deg)';
            }} else {{
                answer.classList.add('hidden');
                icon.textContent = '+';
                icon.style.transform = 'rotate(0deg)';
            }}
        }}
    </script>
        '''
    
    def _render_pricing(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Pricing section"""
        title = props.get("sectionTitle", "Pricing")
        plans = props.get("plans", [])
        
        plans_html = ""
        for i, plan in enumerate(plans[:3]):
            is_featured = plan.get("featured", i == 1)
            featured_class = "border-primary shadow-2xl scale-105" if is_featured else "border-gray-200"
            
            features_html = ""
            for feature in plan.get("features", []):
                features_html += f'<li class="flex items-center gap-3"><span class="text-primary">✓</span> {feature}</li>'
            
            plans_html += f'''
            <div class="animate-on-scroll bg-white rounded-3xl p-8 border-2 {featured_class} transition-all hover:shadow-xl">
                {"<div class='text-center mb-4'><span class='bg-primary text-white px-4 py-1 rounded-full text-sm font-semibold'>Popular</span></div>" if is_featured else ""}
                <div class="text-center mb-6">
                    <h3 class="text-2xl font-bold font-heading mb-2">{plan.get("name", "Plan")}</h3>
                    <div class="text-4xl font-bold text-primary">{plan.get("price", "$0")}</div>
                    <div class="text-gray-500">{plan.get("period", "/month")}</div>
                </div>
                <ul class="space-y-4 mb-8">
                    {features_html}
                </ul>
                <a href="#contact" class="btn-{'primary' if is_featured else 'secondary'} w-full text-center">
                    {plan.get("cta", "Get Started")}
                </a>
            </div>'''
        
        return f'''
    <!-- Pricing Section -->
    <section id="{section_id}" class="section">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">Pricing</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading">{title}</h2>
            </div>
            
            <!-- Pricing Grid -->
            <div class="grid md:grid-cols-3 gap-8 items-center max-w-5xl mx-auto">
                {plans_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_specials(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Today's Specials section for cafes/restaurants"""
        title = props.get("sectionTitle", "Today's Specials")
        specials = props.get("items", [])
        
        # Default specials if none provided
        if not specials:
            specials = [
                {"name": "Chef's Special", "description": "A delightful creation by our head chef, using the freshest seasonal ingredients", "price": "$15.99", "badge": "Popular"},
                {"name": "Soup of the Day", "description": "Homemade soup prepared fresh every morning", "price": "$6.99", "badge": "New"},
                {"name": "Daily Combo", "description": "Main course + drink + dessert at a special price", "price": "$19.99", "badge": "Best Value"}
            ]
        
        specials_html = ""
        for special in specials:
            badge = special.get("badge", "")
            badge_html = f'<span class="absolute -top-3 -right-3 bg-accent text-white text-xs font-bold px-3 py-1 rounded-full">{badge}</span>' if badge else ""
            
            specials_html += f'''
            <div class="animate-on-scroll relative bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all border-l-4 border-primary">
                {badge_html}
                <h4 class="text-xl font-bold font-heading mb-2">{special.get("name", "Special")}</h4>
                <p class="text-gray-500 mb-4">{special.get("description", "")}</p>
                <div class="flex items-center justify-between">
                    <span class="text-2xl font-bold text-primary">{special.get("price", "")}</span>
                    <a href="#contact" class="text-primary hover:underline font-semibold">Order Now →</a>
                </div>
            </div>'''
        
        return f'''
    <!-- Today's Specials Section -->
    <section id="{section_id}" class="section bg-gradient-to-br from-primary/5 to-secondary/5">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">🔥 Limited Time</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading mb-4">{title}</h2>
                <p class="text-xl text-gray-500">Fresh selections prepared just for today</p>
            </div>
            
            <!-- Specials Grid -->
            <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
                {specials_html}
            </div>
        </div>
    </section>
        '''
    
    def _render_hours(self, props: Dict[str, Any], colors: Dict[str, str], section_id: str) -> str:
        """Render Hours & Location section for local businesses"""
        title = props.get("title", "Hours & Location")
        address = props.get("address", "123 Main Street, City, State 12345")
        phone = props.get("phone", "(555) 123-4567")
        email = props.get("email", "hello@example.com")
        
        hours = props.get("hours", [
            {"day": "Monday - Friday", "time": "7:00 AM - 9:00 PM"},
            {"day": "Saturday", "time": "8:00 AM - 10:00 PM"},
            {"day": "Sunday", "time": "9:00 AM - 8:00 PM"}
        ])
        
        hours_html = ""
        for h in hours:
            hours_html += f'''
            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                <span class="font-medium">{h.get("day", "")}</span>
                <span class="text-primary font-semibold">{h.get("time", "")}</span>
            </div>'''
        
        return f'''
    <!-- Hours & Location Section -->
    <section id="{section_id}" class="section">
        <div class="container mx-auto px-6">
            <!-- Header -->
            <div class="animate-on-scroll text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-semibold text-sm uppercase tracking-wider mb-4 block">📍 Visit Us</span>
                <h2 class="text-4xl md:text-5xl font-bold font-heading">{title}</h2>
            </div>
            
            <div class="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
                <!-- Hours -->
                <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg">
                    <h3 class="text-2xl font-bold font-heading mb-6 flex items-center">
                        <span class="text-3xl mr-3">🕐</span> Opening Hours
                    </h3>
                    <div class="space-y-2">
                        {hours_html}
                    </div>
                </div>
                
                <!-- Location & Contact -->
                <div class="animate-on-scroll bg-white rounded-2xl p-8 shadow-lg">
                    <h3 class="text-2xl font-bold font-heading mb-6 flex items-center">
                        <span class="text-3xl mr-3">📍</span> Find Us
                    </h3>
                    <div class="space-y-4">
                        <div class="flex items-start gap-4">
                            <span class="text-2xl">🏠</span>
                            <div>
                                <p class="font-medium">Address</p>
                                <p class="text-gray-500">{address}</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-2xl">📞</span>
                            <div>
                                <p class="font-medium">Phone</p>
                                <p class="text-gray-500">{phone}</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-2xl">✉️</span>
                            <div>
                                <p class="font-medium">Email</p>
                                <p class="text-gray-500">{email}</p>
                            </div>
                        </div>
                    </div>
                    <a href="#contact" class="btn-primary mt-6 inline-block">Get Directions</a>
                </div>
            </div>
        </div>
    </section>
        '''
    
    def _render_footer(self, footer: Dict[str, Any], colors: Dict[str, str], project_name: str) -> str:
        """Render footer with Tailwind"""
        logo = footer.get("logo", project_name)
        tagline = footer.get("tagline", "")
        sections = footer.get("sections", [])
        copyright_text = footer.get("copyright", f"© 2025 {project_name}. All rights reserved.")
        
        # Build section columns
        sections_html = ""
        for section in sections[:3]:
            links_html = ""
            for link in section.get("links", [])[:5]:
                # Handle both string and dict link formats
                if isinstance(link, str):
                    link_href = "#"
                    link_text = link
                elif isinstance(link, dict):
                    link_href = link.get("href", "#")
                    link_text = link.get("text", "Link")
                else:
                    link_href = "#"
                    link_text = str(link)
                    
                links_html += f'''
                <a href="{link_href}" class="text-gray-400 hover:text-white transition-colors block">
                    {link_text}
                </a>'''
            
            sections_html += f'''
            <div>
                <h4 class="font-bold text-white mb-4">{section.get("title", "Links")}</h4>
                <div class="space-y-3">
                    {links_html}
                </div>
            </div>'''
        
        return f'''
    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-300 pt-20 pb-8">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-12 mb-16">
                <!-- Brand -->
                <div class="col-span-2 md:col-span-1">
                    <div class="text-2xl font-bold text-white mb-4">{logo}</div>
                    <p class="text-gray-400 leading-relaxed">{tagline}</p>
                    
                    <!-- Social Links -->
                    <div class="flex gap-4 mt-6">
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-primary transition-colors">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-primary transition-colors">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"/></svg>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-primary transition-colors">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg>
                        </a>
                    </div>
                </div>
                
                {sections_html}
            </div>
            
            <!-- Bottom Bar -->
            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-gray-500 text-sm">{copyright_text}</p>
                <div class="flex gap-6">
                    <a href="#" class="text-gray-500 hover:text-white text-sm transition-colors">Privacy Policy</a>
                    <a href="#" class="text-gray-500 hover:text-white text-sm transition-colors">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
        '''
    
    def _build_gsap_animations(self) -> str:
        """Build GSAP scroll-triggered animations - uses consistent style selected at generation start"""
        
        # Use pre-selected animation style (same for all pages)
        selected_style = getattr(self, '_current_animation_style', 'fade_up')
        
        # Map style name to method
        style_methods = {
            "fade_up": self._animation_style_fade_up,
            "fade_scale": self._animation_style_fade_scale,
            "slide_left": self._animation_style_slide_left,
            "stagger_reveal": self._animation_style_stagger_reveal,
            "bounce": self._animation_style_bounce
        }
        
        style_method = style_methods.get(selected_style, self._animation_style_fade_up)
        return style_method()
    
    def _animation_style_fade_up(self):
        """Classic fade up animation"""
        return '''
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.animate-on-scroll').forEach((element, index) => {
            gsap.fromTo(element, 
                { opacity: 0, y: 60 },
                { opacity: 1, y: 0, duration: 0.9, ease: "power3.out",
                  scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" },
                  delay: index * 0.1 % 0.5
                }
            );
        });
        '''
    
    def _animation_style_fade_scale(self):
        """Fade with scale effect"""
        return '''
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.animate-on-scroll').forEach((element, index) => {
            gsap.fromTo(element, 
                { opacity: 0, scale: 0.9, y: 30 },
                { opacity: 1, scale: 1, y: 0, duration: 0.7, ease: "back.out(1.7)",
                  scrollTrigger: { trigger: element, start: "top 80%", toggleActions: "play none none reverse" },
                  delay: index * 0.08
                }
            );
        });
        '''
    
    def _animation_style_slide_left(self):
        """Slide from left animation"""
        return '''
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.animate-on-scroll').forEach((element, index) => {
            const direction = index % 2 === 0 ? -80 : 80;
            gsap.fromTo(element, 
                { opacity: 0, x: direction },
                { opacity: 1, x: 0, duration: 0.8, ease: "power2.out",
                  scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" },
                  delay: index * 0.1
                }
            );
        });
        '''
    
    def _animation_style_stagger_reveal(self):
        """Staggered reveal animation"""
        return '''
        gsap.registerPlugin(ScrollTrigger);
        const sections = gsap.utils.toArray('section');
        sections.forEach(section => {
            const items = section.querySelectorAll('.animate-on-scroll');
            gsap.fromTo(items, 
                { opacity: 0, y: 40, rotateX: -10 },
                { opacity: 1, y: 0, rotateX: 0, duration: 0.6, stagger: 0.15, ease: "power2.out",
                  scrollTrigger: { trigger: section, start: "top 75%", toggleActions: "play none none reverse" }
                }
            );
        });
        '''
    
    def _animation_style_bounce(self):
        """Bounce entrance animation"""
        return '''
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray('.animate-on-scroll').forEach((element, index) => {
            gsap.fromTo(element, 
                { opacity: 0, y: 100, scale: 0.8 },
                { opacity: 1, y: 0, scale: 1, duration: 1, ease: "elastic.out(1, 0.5)",
                  scrollTrigger: { trigger: element, start: "top 90%", toggleActions: "play none none reverse" },
                  delay: index * 0.05
                }
            );
        });
        '''
    
    def _generate_section_page(
        self,
        project_name: str,
        seo: Dict[str, Any],
        colors: Dict[str, str],
        fonts: Dict[str, str],
        navigation: Dict[str, Any],
        component: Dict[str, Any],
        tailwind_config: str
    ) -> str:
        """Generate standalone page for a section"""
        comp_type = component.get("type", "Page")
        props = component.get("props", {})
        title = props.get("title") or props.get("sectionTitle") or comp_type
        
        # Render the component
        section_html = self._render_component(component, colors)
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {project_name}</title>
    <meta name="description" content="{seo.get("description", "")}">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{self._get_google_fonts_url(fonts)}" rel="stylesheet">
    
    <script src="{self.TAILWIND_CDN}"></script>
    <script>{tailwind_config}</script>
    
    <style>
        body {{
            font-family: '{fonts["body"]}', sans-serif;
            background-color: {colors["background"]};
            color: {colors["text"]};
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-family: '{fonts["heading"]}', sans-serif;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]});
            color: white;
            padding: 14px 32px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        .section {{
            padding: 100px 0;
        }}
    </style>
</head>
<body>
    <!-- Back to Home -->
    <div class="fixed top-4 left-4 z-50">
        <a href="index.html" class="inline-flex items-center gap-2 bg-white shadow-lg px-4 py-2 rounded-full text-gray-700 hover:text-primary transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
            </svg>
            Back to Home
        </a>
    </div>
    
    <main class="pt-16">
        {section_html}
    </main>
    
    <script src="{self.GSAP_CDN}"></script>
    <script src="{self.GSAP_SCROLL_CDN}"></script>
    <script>
        {self._build_gsap_animations()}
    </script>
</body>
</html>'''


# Singleton instance
_html_generator_service = None

def get_html_generator_service() -> HTMLGeneratorService:
    """Get or create HTMLGeneratorService singleton"""
    global _html_generator_service
    if _html_generator_service is None:
        _html_generator_service = HTMLGeneratorService()
    return _html_generator_service
