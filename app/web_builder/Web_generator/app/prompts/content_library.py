"""
Industry Content Library
Rich, diverse content banks for each industry type
Ensures content variety and quality
"""

from typing import Dict, List, Any
import random


class IndustryContentLibrary:
    """
    Comprehensive content library for various industries.
    Each industry has multiple options for:
    - Headlines (hero section)
    - Subheadlines
    - Descriptions
    - CTAs
    - Adjectives (for dynamic content)
    - Phrases (industry-specific)
    """
    
    # ============================================================
    # CAFE / COFFEE SHOP
    # ============================================================
    CAFE = {
        "headlines": [
            "Where Every Cup Tells a Story",
            "Crafted with Passion, Served with Love",
            "Your Daily Dose of Happiness",
            "Fresh Roasted, Perfectly Brewed",
            "The Art of Artisan Coffee",
            "More Than Coffee, It's an Experience",
            "Wake Up to Something Special",
            "Brewed for Those Who Know",
            "Small Batch. Big Flavor.",
            "Coffee Worth Waking Up For",
            "Your Perfect Cup Awaits",
            "Where Coffee Meets Community",
            "Sip. Savor. Repeat.",
            "Handcrafted with Heart",
            "From Bean to Bliss"
        ],
        "subheadlines": [
            "Specialty coffee roasted in-house daily",
            "Single-origin beans, expertly crafted",
            "A cozy corner for coffee lovers",
            "Where quality meets comfort",
            "Locally roasted, globally inspired"
        ],
        "descriptions": [
            "We source our beans from sustainable farms around the world, roasting them in small batches to bring out their unique flavors. Every cup is crafted with care.",
            "Step into our warm, welcoming space where the aroma of freshly roasted coffee fills the air. Stay a while, meet friends, or find your focus.",
            "Our baristas are passionate about their craft, trained to perfect every pour and create beautiful latte art that makes your coffee as pleasing to look at as it is to drink.",
            "From our signature espresso blends to seasonal single-origins, we're on a mission to elevate your coffee experience one cup at a time.",
            "More than just a coffee shop – we're a gathering place for the community. Great coffee, meaningful conversations, and memories brewed fresh daily."
        ],
        "ctas": [
            "Order Your Favorite",
            "Find Your Blend",
            "Start Your Day Right",
            "Explore Our Menu",
            "Visit Us Today",
            "Join Our Community",
            "Discover Fresh Flavors",
            "Get Your First Cup"
        ],
        "adjectives": [
            "artisanal", "handcrafted", "fresh-roasted", "small-batch", "single-origin",
            "locally sourced", "sustainably grown", "ethically traded", "expertly brewed",
            "rich", "smooth", "bold", "aromatic", "velvety", "creamy"
        ],
        "phrases": [
            "fresh from the roaster",
            "brewed to perfection",
            "the perfect cup",
            "a coffee experience",
            "craft coffee culture",
            "bean-to-cup journey"
        ]
    }
    
    # ============================================================
    # RESTAURANT
    # ============================================================
    RESTAURANT = {
        "headlines": [
            "Experience Culinary Excellence",
            "Where Flavor Meets Tradition",
            "A Feast for Your Senses",
            "Taste the Extraordinary",
            "Fine Dining Redefined",
            "Every Dish Tells a Story",
            "Crafted by Passion, Served with Pride",
            "The Art of Fine Cuisine",
            "Where Memories Are Made",
            "Savor Every Moment",
            "Elevate Your Dining Experience",
            "Fresh. Local. Exceptional.",
            "Flavors That Inspire",
            "A Culinary Journey Awaits",
            "Creating Moments Worth Savoring"
        ],
        "subheadlines": [
            "Farm-to-table ingredients, chef-crafted dishes",
            "Contemporary cuisine with timeless flavors",
            "Award-winning dining in an elegant setting",
            "Where every meal becomes a celebration",
            "Fine dining meets warm hospitality"
        ],
        "descriptions": [
            "Our chefs combine time-honored techniques with modern innovation, creating dishes that surprise and delight. Each plate is a work of art, crafted with the finest seasonal ingredients.",
            "From intimate dinners to special celebrations, we provide an unforgettable dining experience. Our attention to detail ensures every visit feels extraordinary.",
            "We believe great food starts with exceptional ingredients. That's why we partner with local farmers and producers to bring you the freshest flavors of the season.",
            "Step into a world where culinary artistry meets warm hospitality. Our menu changes with the seasons, but the quality never wavers.",
            "More than a restaurant – we're a destination. Join us for an evening of exquisite flavors, impeccable service, and memories that last a lifetime."
        ],
        "ctas": [
            "Reserve a Table",
            "View Our Menu",
            "Book Your Experience",
            "Make a Reservation",
            "Explore the Menu",
            "Plan Your Visit",
            "Order Now",
            "Experience the Magic"
        ],
        "adjectives": [
            "exquisite", "sumptuous", "divine", "delectable", "gourmet",
            "farm-fresh", "locally sourced", "chef-crafted", "seasonal",
            "artfully plated", "mouth-watering", "savory", "indulgent"
        ],
        "phrases": [
            "culinary artistry",
            "a feast for the senses",
            "dining experience",
            "crafted with passion",
            "fresh from the farm",
            "every plate a masterpiece"
        ]
    }
    
    # ============================================================
    # GAMING
    # ============================================================
    GAMING = {
        "headlines": [
            "Level Up Your Experience",
            "Enter a New Dimension",
            "Where Legends Are Made",
            "Play Beyond Limits",
            "The Ultimate Gaming Experience",
            "Prepare for Battle",
            "Your Adventure Awaits",
            "Power Up Your Play",
            "Dominate the Arena",
            "Worlds Without Limits",
            "Join the Elite",
            "Beyond the Ordinary",
            "Where Champions Rise",
            "Forge Your Legacy",
            "Unlock the Impossible"
        ],
        "subheadlines": [
            "Next-gen gameplay meets cutting-edge graphics",
            "Immersive worlds, infinite possibilities",
            "Compete. Conquer. Celebrate.",
            "The community where gamers belong",
            "Push the boundaries of what's possible"
        ],
        "descriptions": [
            "Dive into immersive worlds crafted with stunning detail. Whether you're a casual player or hardcore competitor, we've got something epic waiting for you.",
            "Join millions of players worldwide in the ultimate gaming experience. Real-time battles, stunning graphics, and a community that never sleeps.",
            "We're gamers building for gamers. Every feature, every update, every detail is designed to elevate your experience and keep you coming back.",
            "From solo adventures to massive multiplayer battles, experience gaming the way it was meant to be – intense, immersive, and unforgettable.",
            "The future of gaming is here. Cutting-edge technology meets creative storytelling in worlds you won't want to leave."
        ],
        "ctas": [
            "Play Now",
            "Join the Battle",
            "Start Your Journey",
            "Download Free",
            "Enter the Arena",
            "Create Account",
            "Watch Trailer",
            "Pre-Order Now"
        ],
        "adjectives": [
            "immersive", "epic", "intense", "stunning", "next-gen",
            "competitive", "legendary", "ultimate", "cutting-edge",
            "action-packed", "thrilling", "dynamic", "powerful"
        ],
        "phrases": [
            "level up",
            "join the battle",
            "forge your path",
            "rise to glory",
            "claim victory",
            "become legendary"
        ]
    }
    
    # ============================================================
    # PORTFOLIO (Developer/Designer/Freelancer)
    # ============================================================
    PORTFOLIO = {
        "headlines": [
            "Crafting Digital Experiences",
            "Design That Makes a Difference",
            "Bringing Ideas to Life",
            "Where Creativity Meets Code",
            "Designing Tomorrow, Today",
            "Pixels, Purpose, Passion",
            "Building Beautiful Solutions",
            "From Concept to Creation",
            "Creating Impact Through Design",
            "Your Vision, My Craft",
            "Making the Digital World Beautiful",
            "Code. Create. Elevate.",
            "Where Innovation Takes Shape",
            "Transforming Ideas Into Reality",
            "Design-Driven Development"
        ],
        "subheadlines": [
            "Full-stack developer with a passion for clean code",
            "UI/UX designer crafting intuitive experiences",
            "Creative problem solver, digital craftsman",
            "Building products that people love to use",
            "Where strategy meets stunning execution"
        ],
        "descriptions": [
            "With years of experience in design and development, I help businesses create digital products that users love. From concept to launch, I'm your partner in bringing ideas to life.",
            "I believe great design is invisible – it just works. My approach combines user-centered thinking with technical excellence to deliver solutions that truly make an impact.",
            "Every project is a new adventure. I dive deep into understanding your challenges, then craft solutions that are as beautiful as they are functional.",
            "I'm not just a developer – I'm your technical partner. I care about your success as much as you do, and I bring that dedication to every project.",
            "Clean code, stunning design, and measurable results. That's what I deliver. Let's work together to build something amazing."
        ],
        "ctas": [
            "View My Work",
            "Let's Connect",
            "Start a Project",
            "See Portfolio",
            "Get in Touch",
            "Hire Me",
            "Download Resume",
            "Book a Call"
        ],
        "adjectives": [
            "innovative", "creative", "pixel-perfect", "user-centered",
            "responsive", "accessible", "modern", "clean", "intuitive",
            "scalable", "performant", "thoughtful", "strategic"
        ],
        "phrases": [
            "turning ideas into reality",
            "crafting digital experiences",
            "design meets development",
            "pixel-perfect execution",
            "user-first approach",
            "building what matters"
        ]
    }
    
    # ============================================================
    # AGENCY
    # ============================================================
    AGENCY = {
        "headlines": [
            "We Build What's Next",
            "Your Growth, Our Mission",
            "Transform Your Vision",
            "Ideas That Move Markets",
            "Digital Excellence, Delivered",
            "Think Big. Start Now.",
            "Results That Speak",
            "Where Strategy Meets Creativity",
            "Innovate. Evolve. Succeed.",
            "Bold Ideas, Brilliant Execution",
            "Partners in Your Success",
            "Creativity Without Limits",
            "Driving Digital Transformation",
            "Making Brands Unforgettable",
            "Your Success Story Starts Here"
        ],
        "subheadlines": [
            "Full-service digital agency helping brands grow",
            "Strategy, design, and technology under one roof",
            "We don't just build websites – we build businesses",
            "Award-winning team, exceptional results",
            "Where data-driven meets creative excellence"
        ],
        "descriptions": [
            "We're a team of strategists, designers, and developers who believe in the power of great work. From startups to enterprises, we help brands connect with their audience in meaningful ways.",
            "Digital transformation isn't just about technology – it's about people. We combine human insights with cutting-edge solutions to drive real business results.",
            "No ego, no jargon, just results. We partner with ambitious brands to tackle their biggest challenges and unlock new opportunities for growth.",
            "Our process is collaborative, our approach is strategic, and our results speak for themselves. Let's create something extraordinary together.",
            "We don't just execute – we elevate. Every project is an opportunity to push boundaries and exceed expectations."
        ],
        "ctas": [
            "Start a Project",
            "Get a Quote",
            "Let's Create",
            "Work With Us",
            "Book a Strategy Call",
            "See Our Work",
            "Contact Us",
            "Request Proposal"
        ],
        "adjectives": [
            "innovative", "strategic", "creative", "data-driven",
            "results-focused", "collaborative", "award-winning",
            "experienced", "agile", "impactful", "transformative"
        ],
        "phrases": [
            "driving growth",
            "unlocking potential",
            "creative excellence",
            "strategic partnership",
            "measurable impact",
            "digital transformation"
        ]
    }
    
    # ============================================================
    # ECOMMERCE
    # ============================================================
    ECOMMERCE = {
        "headlines": [
            "Shop the Difference",
            "Quality You Can Trust",
            "Your Style, Delivered",
            "Discover Something New",
            "Curated for You",
            "Everyday Essentials, Elevated",
            "Find What You Love",
            "Shop Smarter",
            "Premium Products, Fair Prices",
            "Designed for Your Life",
            "Where Quality Meets Value",
            "The Good Stuff",
            "Collections You'll Love",
            "Made for You",
            "Discover Your Next Favorite"
        ],
        "subheadlines": [
            "Premium products, delivered to your door",
            "Free shipping on orders over $50",
            "Curated collections for every occasion",
            "Quality guaranteed, hassle-free returns",
            "Shop the latest trends and timeless classics"
        ],
        "descriptions": [
            "We obsess over quality so you don't have to. Every product is carefully selected to meet our high standards and bring value to your life.",
            "Shopping should be easy and enjoyable. Browse our curated collections, find what you love, and enjoy fast, free shipping on every order.",
            "From everyday essentials to special finds, we've got something for everyone. Quality products, fair prices, and exceptional customer service.",
            "We believe good things shouldn't be hard to find. That's why we've done the work of finding the best products and bringing them all to one place.",
            "More than just a store – we're your go-to destination for products that make life better. Shop with confidence, knowing quality is guaranteed."
        ],
        "ctas": [
            "Shop Now",
            "Explore Collection",
            "Find Your Style",
            "Discover More",
            "Add to Cart",
            "Browse Products",
            "Start Shopping",
            "Get Yours"
        ],
        "adjectives": [
            "premium", "curated", "exclusive", "trending", "quality",
            "affordable", "stylish", "essential", "handpicked",
            "limited-edition", "bestselling", "must-have"
        ],
        "phrases": [
            "free shipping",
            "easy returns",
            "quality guaranteed",
            "customer favorite",
            "trending now",
            "limited stock"
        ]
    }
    
    # ============================================================
    # SALON / SPA
    # ============================================================
    SALON = {
        "headlines": [
            "Transform Your Look",
            "Where Beauty Meets Expertise",
            "Reveal Your Radiance",
            "Your Best Look Awaits",
            "Elevate Your Style",
            "Beauty, Perfected",
            "Indulge in Self-Care",
            "Look Good, Feel Amazing",
            "The Art of Beauty",
            "Your Glow-Up Starts Here",
            "Confidence Looks Good on You",
            "A Fresh New You",
            "Beauty That's All You",
            "Style That Speaks",
            "Pamper. Glow. Repeat."
        ],
        "subheadlines": [
            "Expert stylists, premium products, exceptional results",
            "Your personalized beauty experience awaits",
            "Where relaxation meets transformation",
            "Because you deserve to look and feel your best",
            "Creating looks as unique as you are"
        ],
        "ctas": [
            "Book Your Transformation",
            "Schedule Appointment",
            "Treat Yourself",
            "Book Now",
            "Find Your Look",
            "Get Started",
            "Reserve Your Spot"
        ],
        "adjectives": [
            "radiant", "luxurious", "transformative", "expert",
            "personalized", "premium", "relaxing", "rejuvenating",
            "pampering", "stunning", "flawless", "glamorous"
        ],
        "phrases": [
            "self-care sanctuary",
            "beauty transformation",
            "expert styling",
            "personalized service",
            "luxury experience",
            "your best self"
        ]
    }
    
    # ============================================================
    # FITNESS / GYM
    # ============================================================
    FITNESS = {
        "headlines": [
            "Transform Your Body",
            "Push Your Limits",
            "Your Fitness Journey Starts Here",
            "Stronger Every Day",
            "Achieve Your Goals",
            "No Excuses. Just Results.",
            "Unlock Your Potential",
            "Built for Champions",
            "Where Results Happen",
            "Your Body, Your Rules",
            "Train Like a Champion",
            "Commit. Transform. Succeed.",
            "The Gains Start Here",
            "Power Up Your Life",
            "Sweat Now, Shine Later"
        ],
        "subheadlines": [
            "World-class equipment, expert trainers, real results",
            "Join a community that pushes you forward",
            "Personal training, group classes, 24/7 access",
            "Transform your body and mind",
            "Where every workout counts"
        ],
        "ctas": [
            "Start Your Journey",
            "Join Today",
            "Get Your Free Trial",
            "Transform Now",
            "Book a Tour",
            "Try Us Free",
            "View Memberships",
            "Start Training"
        ],
        "adjectives": [
            "powerful", "transformative", "intense", "effective",
            "energizing", "motivating", "supportive", "results-driven",
            "challenging", "empowering", "dynamic"
        ],
        "phrases": [
            "crush your goals",
            "no limits",
            "transform your body",
            "push beyond",
            "results guaranteed",
            "stronger together"
        ]
    }
    
    # ============================================================
    # DEFAULT / BUSINESS
    # ============================================================
    DEFAULT = {
        "headlines": [
            "Welcome to the Future",
            "Excellence in Every Detail",
            "Your Success, Our Priority",
            "Solutions That Work",
            "Quality You Can Count On",
            "Building Tomorrow, Today",
            "Trusted. Reliable. Professional.",
            "Where Quality Meets Service",
            "Partners in Your Success",
            "Committed to Excellence",
            "Your Trusted Partner",
            "Making a Difference",
            "Results You Can Trust",
            "Professional Solutions",
            "Excellence Delivered"
        ],
        "subheadlines": [
            "Professional services tailored to your needs",
            "Quality solutions for modern challenges",
            "Expertise you can rely on",
            "Dedicated to your success",
            "Experience the difference"
        ],
        "descriptions": [
            "We're committed to delivering exceptional quality and outstanding service. Our team brings years of experience and a dedication to excellence in everything we do.",
            "Your success is our success. We work closely with you to understand your needs and deliver solutions that exceed expectations.",
            "Quality, integrity, and results – these are the values that guide everything we do. Discover why clients trust us with their most important projects.",
            "We believe in building lasting relationships through honest communication and exceptional work. Let us show you what true partnership looks like.",
            "From the first conversation to project completion, we're with you every step of the way. Experience service that puts you first."
        ],
        "ctas": [
            "Get Started",
            "Contact Us",
            "Learn More",
            "Request Quote",
            "Schedule Consultation",
            "Discover More",
            "Get in Touch",
            "Start Now"
        ],
        "adjectives": [
            "professional", "reliable", "trusted", "quality",
            "exceptional", "dedicated", "experienced", "committed",
            "innovative", "proven", "certified"
        ],
        "phrases": [
            "your trusted partner",
            "quality assured",
            "exceeding expectations",
            "results-driven",
            "customer-focused",
            "professional excellence"
        ]
    }
    
    # ============================================================
    # CONTENT RETRIEVAL METHODS
    # ============================================================
    
    @classmethod
    def get_content_bank(cls, industry: str) -> Dict[str, List[str]]:
        """Get the content bank for a specific industry"""
        industry_map = {
            "cafe": cls.CAFE,
            "coffee": cls.CAFE,
            "coffee_shop": cls.CAFE,
            "restaurant": cls.RESTAURANT,
            "dining": cls.RESTAURANT,
            "gaming": cls.GAMING,
            "game": cls.GAMING,
            "esports": cls.GAMING,
            "portfolio": cls.PORTFOLIO,
            "developer": cls.PORTFOLIO,
            "designer": cls.PORTFOLIO,
            "freelancer": cls.PORTFOLIO,
            "agency": cls.AGENCY,
            "marketing": cls.AGENCY,
            "creative": cls.AGENCY,
            "ecommerce": cls.ECOMMERCE,
            "shop": cls.ECOMMERCE,
            "store": cls.ECOMMERCE,
            "retail": cls.ECOMMERCE,
            "salon": cls.SALON,
            "spa": cls.SALON,
            "beauty": cls.SALON,
            "fitness": cls.FITNESS,
            "gym": cls.FITNESS,
            "yoga": cls.FITNESS,
        }
        
        industry_lower = industry.lower().replace(" ", "_").replace("-", "_")
        return industry_map.get(industry_lower, cls.DEFAULT)
    
    @classmethod
    def get_random_headline(cls, industry: str, exclude: List[str] = None) -> str:
        """Get a random headline that hasn't been used"""
        bank = cls.get_content_bank(industry)
        headlines = bank.get("headlines", cls.DEFAULT["headlines"])
        
        if exclude:
            headlines = [h for h in headlines if h not in exclude]
        
        if not headlines:
            headlines = bank.get("headlines", cls.DEFAULT["headlines"])
        
        return random.choice(headlines)
    
    @classmethod
    def get_random_description(cls, industry: str, exclude: List[str] = None) -> str:
        """Get a random description that hasn't been used"""
        bank = cls.get_content_bank(industry)
        descriptions = bank.get("descriptions", cls.DEFAULT["descriptions"])
        
        if exclude:
            descriptions = [d for d in descriptions if d not in exclude]
        
        if not descriptions:
            descriptions = bank.get("descriptions", cls.DEFAULT["descriptions"])
        
        return random.choice(descriptions)
    
    @classmethod
    def get_random_cta(cls, industry: str, exclude: List[str] = None) -> str:
        """Get a random CTA that hasn't been used"""
        bank = cls.get_content_bank(industry)
        ctas = bank.get("ctas", cls.DEFAULT["ctas"])
        
        if exclude:
            ctas = [c for c in ctas if c not in exclude]
        
        if not ctas:
            ctas = bank.get("ctas", cls.DEFAULT["ctas"])
        
        return random.choice(ctas)
    
    @classmethod
    def get_adjectives(cls, industry: str) -> List[str]:
        """Get industry-specific adjectives"""
        bank = cls.get_content_bank(industry)
        return bank.get("adjectives", cls.DEFAULT["adjectives"])
    
    @classmethod
    def enhance_text(cls, text: str, industry: str) -> str:
        """
        Enhance generic text with industry-specific adjectives.
        Replaces [ADJECTIVE] placeholders with random industry adjectives.
        """
        if "[ADJECTIVE]" not in text:
            return text
        
        adjectives = cls.get_adjectives(industry)
        while "[ADJECTIVE]" in text:
            text = text.replace("[ADJECTIVE]", random.choice(adjectives), 1)
        
        return text


class AudienceToneAdapter:
    """
    Adapts content tone based on target audience.
    """
    
    AUDIENCE_PROFILES = {
        "young_adults": {
            "age_range": "18-30",
            "formal_level": "low",
            "emoji_use": True,
            "slang_ok": True,
            "sentence_style": "short and punchy",
            "cta_style": "action-oriented, casual",
            "adaptations": {
                "Get Started": "Let's Go",
                "Contact Us": "Hit Us Up",
                "Learn More": "Check It Out",
                "Subscribe": "Join the Crew"
            }
        },
        "professionals": {
            "age_range": "30-55",
            "formal_level": "high",
            "emoji_use": False,
            "slang_ok": False,
            "sentence_style": "clear and professional",
            "cta_style": "professional, action-oriented",
            "adaptations": {
                "Let's Go": "Get Started",
                "Hit Us Up": "Contact Us",
                "Check It Out": "Learn More"
            }
        },
        "families": {
            "age_range": "25-45",
            "formal_level": "medium",
            "emoji_use": True,
            "slang_ok": False,
            "sentence_style": "warm and friendly",
            "cta_style": "welcoming, inclusive",
            "adaptations": {
                "Join Today": "Join Our Family",
                "Get Started": "Start Your Journey",
                "Learn More": "Discover More"
            }
        },
        "seniors": {
            "age_range": "55+",
            "formal_level": "medium-high",
            "emoji_use": False,
            "slang_ok": False,
            "sentence_style": "clear and respectful",
            "cta_style": "straightforward, trustworthy",
            "adaptations": {
                "Let's Go": "Get Started",
                "Hit Us Up": "Call Us Today",
                "Check It Out": "Learn More"
            }
        },
        "tech_savvy": {
            "age_range": "20-40",
            "formal_level": "low-medium",
            "emoji_use": True,
            "slang_ok": True,
            "sentence_style": "concise, modern",
            "cta_style": "action-oriented, techy",
            "adaptations": {
                "Get Started": "Get Started →",
                "Learn More": "Explore Docs",
                "Contact Us": "Join Discord"
            }
        },
        "luxury": {
            "age_range": "30-60",
            "formal_level": "high",
            "emoji_use": False,
            "slang_ok": False,
            "sentence_style": "elegant and refined",
            "cta_style": "exclusive, premium",
            "adaptations": {
                "Get Started": "Begin Your Journey",
                "Shop Now": "Discover Collection",
                "Contact Us": "Request Consultation"
            }
        },
        "default": {
            "age_range": "all",
            "formal_level": "medium",
            "emoji_use": False,
            "slang_ok": False,
            "sentence_style": "clear and friendly",
            "cta_style": "action-oriented",
            "adaptations": {}
        }
    }
    
    @classmethod
    def get_audience_profile(cls, audience: str) -> Dict[str, Any]:
        """Get audience profile by keyword matching"""
        audience_lower = audience.lower()
        
        if any(k in audience_lower for k in ["young", "gen z", "millennial", "student"]):
            return cls.AUDIENCE_PROFILES["young_adults"]
        elif any(k in audience_lower for k in ["professional", "corporate", "business", "b2b"]):
            return cls.AUDIENCE_PROFILES["professionals"]
        elif any(k in audience_lower for k in ["family", "parent", "mom", "dad", "kids"]):
            return cls.AUDIENCE_PROFILES["families"]
        elif any(k in audience_lower for k in ["senior", "elderly", "retired", "50+"]):
            return cls.AUDIENCE_PROFILES["seniors"]
        elif any(k in audience_lower for k in ["tech", "developer", "engineer", "startup"]):
            return cls.AUDIENCE_PROFILES["tech_savvy"]
        elif any(k in audience_lower for k in ["luxury", "premium", "high-end", "exclusive"]):
            return cls.AUDIENCE_PROFILES["luxury"]
        else:
            return cls.AUDIENCE_PROFILES["default"]
    
    @classmethod
    def adapt_cta(cls, cta: str, audience: str) -> str:
        """Adapt CTA text based on audience"""
        profile = cls.get_audience_profile(audience)
        adaptations = profile.get("adaptations", {})
        
        return adaptations.get(cta, cta)
    
    @classmethod
    def should_use_emoji(cls, audience: str) -> bool:
        """Check if emoji should be used for this audience"""
        profile = cls.get_audience_profile(audience)
        return profile.get("emoji_use", False)
    
    @classmethod
    def get_formal_level(cls, audience: str) -> str:
        """Get formality level for audience"""
        profile = cls.get_audience_profile(audience)
        return profile.get("formal_level", "medium")


class ContentDiversityTracker:
    """
    Tracks used content to ensure diversity within a single website.
    Prevents repetition of headlines, descriptions, and CTAs.
    """
    
    def __init__(self):
        self.used_headlines: List[str] = []
        self.used_descriptions: List[str] = []
        self.used_ctas: List[str] = []
    
    def mark_used(self, content_type: str, content: str):
        """Mark content as used"""
        if content_type == "headline":
            self.used_headlines.append(content)
        elif content_type == "description":
            self.used_descriptions.append(content)
        elif content_type == "cta":
            self.used_ctas.append(content)
    
    def get_fresh_headline(self, industry: str) -> str:
        """Get a headline that hasn't been used"""
        headline = IndustryContentLibrary.get_random_headline(industry, self.used_headlines)
        self.mark_used("headline", headline)
        return headline
    
    def get_fresh_description(self, industry: str) -> str:
        """Get a description that hasn't been used"""
        desc = IndustryContentLibrary.get_random_description(industry, self.used_descriptions)
        self.mark_used("description", desc)
        return desc
    
    def get_fresh_cta(self, industry: str) -> str:
        """Get a CTA that hasn't been used"""
        cta = IndustryContentLibrary.get_random_cta(industry, self.used_ctas)
        self.mark_used("cta", cta)
        return cta
    
    def reset(self):
        """Reset all tracking"""
        self.used_headlines = []
        self.used_descriptions = []
        self.used_ctas = []
