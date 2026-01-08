"""
Blueprint Schema Definitions
Pydantic models for type-safe blueprint generation
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum


# ============== ENUMS ==============

class ComponentType(str, Enum):
    HERO = "Hero"
    ABOUT = "About"
    FEATURES = "Features"
    GALLERY = "Gallery"
    TESTIMONIALS = "Testimonials"
    CTA = "CTA"
    CONTACT = "Contact"
    MENU = "Menu"
    PRICING = "Pricing"
    TEAM = "Team"
    FAQ = "FAQ"
    BLOG = "Blog"
    SERVICES = "Services"


class AnimationType(str, Enum):
    FADE_SLIDE_UP = "fade-slide-up"
    REVEAL_MASK = "reveal-mask"
    SCALE_IN = "scale-in"
    PARALLAX = "parallax"
    STAGGER_FADE = "stagger-fade"


# ============== THEME MODELS ==============

class ColorPalette(BaseModel):
    primary: str = Field(..., description="Primary brand color")
    secondary: str = Field(..., description="Secondary color")
    accent: str = Field(..., description="Accent/highlight color")
    background: str = Field(..., description="Background color")
    surface: str = Field(default="#1a1a1a", description="Surface/card color")
    text: str = Field(..., description="Main text color")


class Gradients(BaseModel):
    hero: str = Field(..., description="Hero section gradient")
    accent: str = Field(..., description="Accent gradient for buttons/CTAs")


class Theme(BaseModel):
    themeName: str = Field(..., description="Theme name")
    themeMood: str = Field(..., description="Theme mood (Premium, Warm, Modern, etc.)")
    primaryColor: str = Field(..., description="Primary color hex")
    colorSchemeType: str = Field(default="Analogous", description="Color scheme type")
    colorPalette: ColorPalette
    gradients: Gradients


# ============== ANIMATION MODELS ==============

class AnimationConfig(BaseModel):
    type: str = Field(default="fade-slide-up", description="Animation type")
    duration: int = Field(default=600, description="Animation duration in ms")
    delay: int = Field(default=0, description="Animation delay in ms")
    stagger: Optional[int] = Field(default=100, description="Stagger delay for lists")
    easing: str = Field(default="cubic-bezier(0.25, 1, 0.5, 1)", description="Easing function")
    hover: Optional[str] = Field(default=None, description="Hover effect type")


# ============== COMPONENT MODELS ==============

class HeroProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    title: str = Field(..., description="Main headline")
    subtitle: str = Field(..., description="Sub-headline")
    description: str = Field(..., description="Hero description text")
    cta: str = Field(..., description="Primary CTA text")
    ctaSecondary: Optional[str] = Field(default=None, description="Secondary CTA text")
    backgroundStyle: str = Field(default="gradient-mesh", description="Background style")


class AboutProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    title: str = Field(..., description="Section title")
    story: str = Field(..., description="Business story/description")
    milestones: Optional[List[Dict[str, str]]] = Field(default=None, description="Timeline milestones")
    stats: Optional[List[Dict[str, str]]] = Field(default=None, description="Statistics")


class FeatureItem(BaseModel):
    icon: str = Field(..., description="Icon emoji or class")
    title: str = Field(..., description="Feature title")
    description: str = Field(..., description="Feature description")


class FeaturesProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    sectionTitle: str = Field(..., description="Section title")
    sectionSubtitle: str = Field(..., description="Section subtitle")
    featureList: List[FeatureItem]


class GalleryProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    title: str = Field(..., description="Section title")
    subtitle: str = Field(..., description="Section subtitle")
    categories: Optional[List[str]] = Field(default=None, description="Gallery categories")
    images: List[str] = Field(..., description="Image URLs")


class TestimonialItem(BaseModel):
    quote: str = Field(..., description="Testimonial quote")
    author: str = Field(..., description="Author name")
    role: str = Field(..., description="Author role/designation")


class TestimonialsProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    sectionTitle: str = Field(..., description="Section title")
    testimonials: List[TestimonialItem]


class CTAProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    title: str = Field(..., description="CTA headline")
    description: str = Field(..., description="CTA description")
    ctaText: str = Field(..., description="Button text")


class FormField(BaseModel):
    type: str = Field(..., description="Field type (text, email, textarea)")
    name: str = Field(..., description="Field name")
    placeholder: str = Field(..., description="Placeholder text")
    required: bool = Field(default=False, description="Is field required")
    rows: Optional[int] = Field(default=None, description="Rows for textarea")


class ContactProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    title: str = Field(..., description="Section title")
    subtitle: str = Field(..., description="Section subtitle")
    email: Optional[str] = Field(default=None, description="Contact email")
    phone: Optional[str] = Field(default=None, description="Contact phone")
    address: Optional[str] = Field(default=None, description="Business address")
    formFields: List[FormField]
    ctaText: str = Field(default="Send Message", description="Submit button text")


class MenuItemModel(BaseModel):
    name: str = Field(..., description="Item name")
    description: str = Field(..., description="Item description")
    price: str = Field(..., description="Item price")
    image: Optional[str] = Field(default=None, description="Item image URL")
    category: Optional[str] = Field(default=None, description="Item category")


class MenuProps(BaseModel):
    layoutVariant: str = Field(..., description="Layout variant name")
    sectionTitle: str = Field(..., description="Section title")
    categories: List[str] = Field(..., description="Menu categories")
    items: List[MenuItemModel]


# ============== COMPONENT WRAPPER ==============

class Component(BaseModel):
    id: str = Field(..., description="Component unique ID")
    type: str = Field(..., description="Component type")
    name: str = Field(..., description="Display name")
    props: Dict[str, Any] = Field(..., description="Component properties")
    animation: AnimationConfig = Field(default_factory=AnimationConfig)


# ============== NAVIGATION MODELS ==============

class NavLink(BaseModel):
    label: str = Field(..., description="Link label")
    href: str = Field(..., description="Link href")


class HeaderCTA(BaseModel):
    text: str = Field(..., description="CTA text")
    href: str = Field(..., description="CTA href")
    style: str = Field(default="primary", description="CTA style")


class Logo(BaseModel):
    text: str = Field(..., description="Logo text")
    style: str = Field(default="modern", description="Logo style")


class ScrollBehavior(BaseModel):
    changeOnScroll: bool = Field(default=True)
    scrollThreshold: int = Field(default=100)


class Header(BaseModel):
    logo: Logo
    links: List[NavLink]
    cta: HeaderCTA
    style: str = Field(default="transparent-fixed")
    scrollBehavior: ScrollBehavior = Field(default_factory=ScrollBehavior)


class FooterSection(BaseModel):
    title: str
    links: List[NavLink]


class Footer(BaseModel):
    logo: str
    tagline: str
    sections: List[FooterSection]
    copyright: str


class Navigation(BaseModel):
    header: Header
    footer: Footer


# ============== TYPOGRAPHY & GLOBAL STYLES ==============

class FontConfig(BaseModel):
    family: str = Field(..., description="Font family name")
    weights: List[int] = Field(default=[400, 500, 700])


class Typography(BaseModel):
    headingFont: FontConfig
    bodyFont: FontConfig
    style: str = Field(default="modern")


class Spacing(BaseModel):
    sectionGap: str = Field(default="100px")
    containerMaxWidth: str = Field(default="1280px")


class Effects(BaseModel):
    glassmorphism: bool = Field(default=True)
    gradients: bool = Field(default=True)
    shadows: str = Field(default="elevated")
    animations: str = Field(default="smooth-reveal")


class GlobalStyles(BaseModel):
    typography: Typography
    spacing: Spacing
    effects: Effects
    animationConfig: Dict[str, str] = Field(default_factory=dict)


# ============== SEO ==============

class SEO(BaseModel):
    title: str = Field(..., description="Page title")
    description: str = Field(..., description="Meta description")
    keywords: List[str] = Field(..., description="SEO keywords")


# ============== DESIGN VISION ==============

class DesignVision(BaseModel):
    design_theme: str = Field(..., description="Overall design theme")
    hero_concept: str = Field(..., description="Hero section concept")
    visual_personality: str = Field(..., description="Visual personality description")


# ============== MAIN BLUEPRINT ==============

class Blueprint(BaseModel):
    projectId: str = Field(..., description="Unique project ID")
    projectName: str = Field(..., description="Project name")
    projectType: str = Field(..., description="Project/business type")
    metadata: Dict[str, Any] = Field(..., description="Original metadata preserved")
    seo: SEO
    theme: Theme
    components: Dict[str, Component] = Field(..., description="All page components")
    navigation: Navigation
    globalStyles: GlobalStyles
    designVision: DesignVision


# ============== INPUT METADATA MODELS ==============

class QuestionAnswer(BaseModel):
    id: str
    type: str
    question: str
    options: Optional[List[str]] = None
    user_answer: str


class BusinessExtractedData(BaseModel):
    business_type: str
    industry: str
    goals: str
    services: List[str]
    style_preferences: List[str]


class SelectedPalette(BaseModel):
    id: str
    colors: List[str]


class DesignInput(BaseModel):
    selected_palette: SelectedPalette


class MetadataInput(BaseModel):
    session_id: str
    timestamp: str
    user_prompt: str
    business_extracted_data: BusinessExtractedData
    questionnaire: Dict[str, List[QuestionAnswer]]
    design: DesignInput
    features: List[str]
    final_metadata_ready: bool = True
