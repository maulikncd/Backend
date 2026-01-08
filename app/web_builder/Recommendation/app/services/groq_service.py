import json
import random
import re
from typing import Dict, Any, List, Optional, Set, Tuple

from groq import Groq

from app.Auth.core.config import get_settings


class GroqService:
    _LANGUAGE_SYNONYMS: Dict[str, str] = {
        # English
        "en": "English",
        "eng": "English",
        "english": "English",
        # Hindi
        "hi": "Hindi",
        "hin": "Hindi",
        "hindi": "Hindi",
        "हिंदी": "Hindi",
        # Gujarati
        "gu": "Gujarati",
        "guj": "Gujarati",
        "gujarati": "Gujarati",
        "ગુજરાતી": "Gujarati",
    }
    _HINDI_CODES: Set[str] = {"hindi", "hi", "hin", "हिंदी"}
    _GUJARATI_CODES: Set[str] = {"gujarati", "gu", "guj", "ગુજરાતી"}
    _LATIN_RE = re.compile(r"[A-Za-z]")
    _DEVANAGARI_RE = re.compile(r"[\u0900-\u097F]")
    _GUJARATI_RE = re.compile(r"[\u0A80-\u0AFF]")

    _QUESTION_TOPICS: Dict[str, Dict[str, Any]] = {
        "audience": {"keywords": ["audience", "visitor", "persona", "user", "customer"], "label": "target visitors"},
        "story": {"keywords": ["story", "narrative", "mission", "values", "about"], "label": "brand story"},
        "layout": {
            "keywords": ["layout", "section order", "page structure", "single page", "multi section", "grid", "sections"],
            "label": "layout structure",
        },
        "hero": {
            "keywords": ["hero", "first impression", "headline", "landing", "hero section", "hero message", "tagline"],
            "label": "hero section",
        },
        "animation": {
            "keywords": ["animation", "animate", "transition", "scroll effect", "parallax", "hover", "motion", "dynamic"],
            "label": "animation style",
        },
        "imagery": {
            "keywords": ["imagery", "photography", "illustration", "video", "visual assets", "images", "photos", "icons"],
            "label": "imagery style",
        },
        "tone": {"keywords": ["tone", "voice", "style", "feel", "mood", "formal", "casual", "playful"], "label": "content tone"},
        "navigation": {
            "keywords": ["navigation", "menu", "links", "section list", "navbar", "header"],
            "label": "navigation flow",
        },
        "interactivity": {
            "keywords": ["interactive", "form", "slider", "gallery", "carousel", "accordion", "modal", "popup"],
            "label": "interactive elements",
        },
        "conversion": {"keywords": ["conversion", "cta", "call to action", "lead", "button", "action"], "label": "call to action"},
        "features": {
            "keywords": ["feature", "testimonial", "social", "newsletter", "blog", "map", "contact"],
            "label": "special features",
        },
        "content": {"keywords": ["content", "copy", "text", "messaging", "headline"], "label": "content requirements"},
    }
    _QUESTION_BANNED_KEYWORDS: Tuple[str, ...] = (
        "internet connection",
        "slower internet",
        "slow internet",
        "bandwidth",
        "network speed",
        "connection speed",
        "offline mode",
        "mobile device",
        "mobile devices",
        "mobile phone",
        "mobile phones",
        "mobile friendly",
        "desktop only",
        "responsive design",
        "responsiveness",
        "tablet",
        "tablet friendly",
        "phone friendly",
        "works on mobile",
        "desktop versus mobile",
        "desktop vs mobile",
        "cart",
        "checkout",
        "payment",
        "payments",
        "ordering system",
        "order tracking",
        "inventory",
        "backend",
        "database",
        "admin panel",
        "login system",
        "user accounts",
    )
    _QUESTION_BLUEPRINT: Dict[int, Dict[str, Any]] = {
        3: {
            "topic_label": "hero section",
            "hint": "Ask about the main message, tagline, or value proposition that should grab attention in the hero section.",
            "fallback": "What headline or promise should visitors see first on your {business_type} website?",
        },
        4: {
            "topic_label": "animation style",
            "hint": "Understand the animation preferences - smooth transitions, parallax scrolling, hover effects, or bold movements.",
            "fallback": "What animation style do you prefer - subtle and elegant, or bold and dynamic?",
        },
        5: {
            "topic_label": "website sections",
            "hint": "Identify the key sections or pages needed - About, Services, Gallery, Contact, Testimonials, etc.",
            "fallback": "What main sections should your {business_type} website have?",
        },
        6: {
            "topic_label": "content tone",
            "hint": "Capture the writing style and voice - professional, casual, playful, luxurious, friendly.",
            "fallback": "What tone should your website content have - formal, casual, or playful?",
        },
        7: {
            "topic_label": "imagery style",
            "hint": "Ask about visual preferences - photography, illustrations, icons, videos, or 3D elements.",
            "fallback": "What type of visuals work best for your {business_type} - photos, illustrations, or videos?",
        },
        8: {
            "topic_label": "interactive elements",
            "hint": "Discover which interactive features they want - forms, sliders, galleries, accordions, carousels.",
            "fallback": "What interactive elements should your website include - forms, galleries, or sliders?",
        },
        9: {
            "topic_label": "call to action",
            "hint": "Identify the primary action visitors should take - contact, book, buy, subscribe, learn more.",
            "fallback": "What is the main action you want visitors to take on your {business_type} website?",
        },
        10: {
            "topic_label": "special features",
            "hint": "Ask about any unique requirements - social media integration, testimonials, blog, newsletter, maps.",
            "fallback": "Any special features you need - testimonials, social feeds, newsletter signup, or maps?",
        },
    }

    def _language_script_hint(self, language: Optional[str]) -> str:
        lowered = (language or "").strip().lower()
        if lowered in self._HINDI_CODES:
            return "Write fully in modern Hindi using देवनागरी script with extremely simple, 10-12 word sentences. Keep the tone contemporary and conversational."
        if lowered in self._GUJARATI_CODES:
            return "Write fully in modern Gujarati using ગુજરાતી લિપિ with extremely simple, 10-12 word sentences. Keep the tone contemporary and conversational."
        if lowered:
            return f"Write entirely in {language} using plain, everyday words."
        return "Use clear, everyday words."

    def _is_expected_script(self, text: str, language: Optional[str]) -> bool:
        if not text:
            return False
        lowered = (language or "").strip().lower()
        letters = [ch for ch in text if ch.isalpha()]
        if not letters:
            return True
        total = len(letters)
        if lowered in self._HINDI_CODES:
            dev = len(self._DEVANAGARI_RE.findall(text))
            latin = len(self._LATIN_RE.findall(text))
            return dev >= max(1, latin * 2) or dev / total >= 0.6
        if lowered in self._GUJARATI_CODES:
            guj = len(self._GUJARATI_RE.findall(text))
            latin = len(self._LATIN_RE.findall(text))
            return guj >= max(1, latin * 2) or guj / total >= 0.6
        return True

    def _rewrite_question_in_language(
        self, text: str, language: str, business_type: str
    ) -> Optional[str]:
        if not text:
            return None
        try:
            prompt = (
                "You are a professional translator and content writer. "
                "Rewrite the following website-planning question in {language} only. "
                "The output must be in the native script of the language (e.g., Devanagari for Hindi). "
                "Keep it short (8-15 words), simple, and natural sounding. "
                "Do NOT use hallucinations or gibberish. Use proper grammar. "
                "{script_hint} "
                "\n\nQuestion: {question}"
            ).format(
                language=language,
                script_hint=self._language_script_hint(language),
                question=text,
            )
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You strictly output ONLY the rewritten sentence in the requested language. "
                            "Do not add quotes, explanations, or English translations."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=100,
                temperature=0.1,
            )
            return completion.choices[0].message.content.strip()
        except Exception:
            return None

    def _ensure_simple_language(
        self, question: Dict[str, Any], language: Optional[str], business_type: str
    ) -> None:
        if not question:
            return
        text = (question.get("question") or "").strip()
        if not text:
            return
        lowered = (language or "").strip().lower()
        source = question.get("_source_question") or text
        needs_rewrite = False

        if lowered in self._HINDI_CODES or lowered in self._GUJARATI_CODES:
            if not self._is_expected_script(text, language):
                needs_rewrite = True
        else:
            if len(text.split()) > 14:
                needs_rewrite = True

        if needs_rewrite and source:
            rewritten = self._rewrite_question_in_language(
                source,
                self._LANGUAGE_SYNONYMS.get(lowered, language or "English"),
                business_type,
            )
            if rewritten:
                question["question"] = rewritten.strip()

    def has_blueprint_question(self, index: int) -> bool:
        return index in self._QUESTION_BLUEPRINT

    def build_mandatory_question(
        self,
        kind: str,
        next_index: int,
        language: str,
        business_type: str,
        prompt: str,
    ) -> Dict[str, Any]:
        if kind == "business":
            # Analyze prompt and business_type to ask the right question
            prompt_lower = (prompt or "").lower()
            type_lower = (business_type or "").lower()
            
            # Determine the right question based on context
            if any(word in prompt_lower or word in type_lower for word in ["portfolio", "personal", "resume", "cv", "freelance"]):
                base_question = "What is your name that should appear on the website?"
                topic_label = "personal name"
            elif any(word in prompt_lower or word in type_lower for word in ["blog", "journal", "diary"]):
                base_question = "What name should your blog have?"
                topic_label = "blog name"
            elif any(word in prompt_lower or word in type_lower for word in ["agency", "studio", "firm", "company", "business", "startup"]):
                base_question = "What is your company or brand name?"
                topic_label = "business name"
            elif any(word in prompt_lower or word in type_lower for word in ["restaurant", "cafe", "bakery", "food", "kitchen"]):
                base_question = "What is your restaurant or food business name?"
                topic_label = "business name"
            elif any(word in prompt_lower or word in type_lower for word in ["shop", "store", "boutique"]):
                base_question = "What is your store or shop name?"
                topic_label = "business name"
            elif any(word in prompt_lower or word in type_lower for word in ["event", "wedding", "party"]):
                base_question = "What is your event or service name?"
                topic_label = "event name"
            elif any(word in prompt_lower or word in type_lower for word in ["nonprofit", "charity", "organization", "ngo"]):
                base_question = "What is your organization's name?"
                topic_label = "organization name"
            elif any(word in prompt_lower or word in type_lower for word in ["band", "music", "artist", "musician"]):
                base_question = "What is your artist or band name?"
                topic_label = "artist name"
            else:
                # Default - ask for website/brand name generically
                base_question = "What name should appear on your website?"
                topic_label = "website name"
            
            payload = {
                "id": f"q{next_index}",
                "question": base_question,
                "type": "text",  # Short free text input
            }
        elif kind == "color":
            base_question = "Which colors should appear in your website palette?"
            topic_label = "visual design"
            payload = {
                "id": f"q{next_index}",
                "question": base_question,
                "type": "textarea",  # Free-form description
            }
        else:
            raise ValueError(f"Unknown mandatory question type: {kind}")

        payload["_topic_label"] = topic_label
        payload["_source_question"] = base_question
        localized = self._localize_questions(
            [payload], language, business_type, prompt
        )
        result = localized[0] if localized else payload
        result["_topic_label"] = topic_label
        result.setdefault("_source_question", base_question)
        self._ensure_simple_language(result, language, business_type)
        return result

    def build_blueprint_question(
        self,
        next_index: int,
        language: str,
        business_type: str,
        prompt: str,
        disallowed_questions: Optional[Set[str]],
        disallowed_topics: Optional[Set[str]],
    ) -> Optional[Dict[str, Any]]:
        blueprint = self._QUESTION_BLUEPRINT.get(next_index)
        if not blueprint:
            return None

        topic_label = blueprint.get("topic_label")
        if topic_label and disallowed_topics and topic_label in disallowed_topics:
            return None

        source_question = None
        candidate = None
        topic_hint = blueprint.get("hint")
        fallback_template = blueprint.get("fallback", "")
        fallback_text = fallback_template.format(
            business_type=business_type or "your business"
        )

        if topic_hint:
            candidate = self._request_single_ai_question(
                prompt=prompt,
                language=language,
                business_type=business_type,
                next_index=next_index,
                topic_hint=topic_hint,
            )
            if candidate:
                source_question = candidate.get("question")
                candidate["_source_question"] = source_question
                detected_topic = self._classify_question_topic(candidate)
                normalized = self._normalize_question_text(source_question)
                if (
                    normalized
                    and disallowed_questions
                    and normalized in disallowed_questions
                ):
                    candidate = None
                elif (
                    topic_label
                    and detected_topic
                    and detected_topic != topic_label
                ):
                    candidate = None

        if not candidate:
            candidate = {
                "id": f"q{next_index}",
                "question": fallback_text,
                "_source_question": fallback_text,
            }

        localized = self._localize_questions(
            [candidate],
            language,
            business_type,
            prompt,
        )
        result = localized[0] if localized else candidate
        result["_topic_label"] = topic_label
        result["_source_question"] = candidate.get(
            "_source_question", candidate.get("question")
        )
        self._ensure_simple_language(result, language, business_type)

        normalized_local = self._normalize_question_text(result.get("question"))
        if normalized_local and disallowed_questions and normalized_local in disallowed_questions:
            return None
        return result
    _FEATURE_LIBRARY: Dict[str, Dict[str, str]] = {
        "home": {
            "name": "Home",
            "purpose": "Hero + overview section that sets the tone and key promise.",
        },
        "menu_services": {
            "name": "Menu / Services",
            "purpose": "Menu, services, or offerings presented clearly with pricing cues.",
        },
        "gallery": {
            "name": "Gallery",
            "purpose": "Visual grid or carousel to showcase products, dishes, spaces, or work.",
        },
        "about": {
            "name": "About",
            "purpose": "Story-driven section highlighting mission, team, or origin.",
        },
        "faq": {
            "name": "FAQ",
            "purpose": "Question/answer accordion that reduces common uncertainties.",
        },
        "contact": {
            "name": "Contact",
            "purpose": "Contact details, map, and inquiry form for quick outreach.",
        },
        "newsletter": {
            "name": "Newsletter",
            "purpose": "Signup block inviting users to receive updates or offers.",
        },
        "reviews": {
            "name": "Reviews",
            "purpose": "Testimonials or ratings that reinforce trust.",
        },
        "events_classes": {
            "name": "Events / Classes",
            "purpose": "Calendar or highlight reel for upcoming sessions, tastings, or workshops.",
        },
    }
    _FEATURE_BANNED_KEYWORDS: Set[str] = {
        "cart",
        "checkout",
        "payment",
        "order",
        "ordering",
        "pos",
        "upsell",
        "ecommerce",
        "shop",
        "inventory",
        "fulfillment",
    }
    _CORE_PAGE_TEMPLATES: List[Tuple[str, str, str, str, str]] = [
        (
            "home",
            "Home",
            "Hero landing with headline, subcopy, and primary CTA.",
            "Instant clarity",
            "High",
        ),
        (
            "about",
            "About",
            "Story-driven section covering mission, team, or origin.",
            "Builds trust",
            "High",
        ),
        (
            "services",
            "Services",
            "Grid of offerings or programs with short blurbs.",
            "Explains value",
            "High",
        ),
        (
            "contact",
            "Contact",
            "Map, contact info, and simple inquiry form.",
            "Reduces friction",
            "High",
        ),
    ]
    _SUPPORT_PAGE_TEMPLATES: List[Tuple[str, str, str, str, str]] = [
        (
            "gallery",
            "Gallery",
            "Visual grid showcasing work, menu items, or space.",
            "Shows proof",
            "Medium",
        ),
        (
            "testimonials",
            "Testimonials",
            "Quote carousel or badges to highlight social proof.",
            "Builds credibility",
            "Medium",
        ),
        (
            "faq",
            "FAQ",
            "Accordion answering common pre-sales questions.",
            "Removes doubts",
            "Medium",
        ),
    ]
    _BUSINESS_PAGE_BUNDLES: List[Dict[str, Any]] = [
        {
            "matchers": {"restaurant", "food", "cafe", "bakery"},
            "templates": [
                (
                    "menu_showcase",
                    "Menu Showcase",
                    "Curated dishes or services with pricing cues.",
                    "Sets expectations",
                    "High",
                ),
                (
                    "reservations",
                    "Reservation CTA",
                    "Compact booking or table request band.",
                    "Drives visits",
                    "High",
                ),
            ],
        },
        {
            "matchers": {"portfolio", "agency", "studio", "creative"},
            "templates": [
                (
                    "work_grid",
                    "Work Grid",
                    "Filterable projects with visuals and outcomes.",
                    "Shows capability",
                    "High",
                ),
                (
                    "case_studies",
                    "Case Studies",
                    "Story modules with challenge, approach, results.",
                    "Demonstrates impact",
                    "Medium",
                ),
            ],
        },
        {
            "matchers": {"wellness", "fitness", "spa", "clinic"},
            "templates": [
                (
                    "programs",
                    "Programs",
                    "Highlight sessions, classes, or care packages.",
                    "Clarifies offer",
                    "High",
                ),
                (
                    "schedule",
                    "Schedule & Booking",
                    "Timetable plus booking CTA for appointments.",
                    "Encourages action",
                    "High",
                ),
            ],
        },
        {
            "matchers": {"blog", "publication", "news", "education"},
            "templates": [
                (
                    "latest_posts",
                    "Latest Posts",
                    "Recent articles with categories and tags.",
                    "Drives reading",
                    "High",
                ),
                (
                    "newsletter",
                    "Newsletter",
                    "Lead capture block with teaser content.",
                    "Grows audience",
                    "Medium",
                ),
            ],
        },
        {
            "matchers": {"saas", "software", "product", "app"},
            "templates": [
                (
                    "feature_highlights",
                    "Feature Highlights",
                    "Icon cards explaining key product capabilities.",
                    "Shows value",
                    "High",
                ),
                (
                    "metrics",
                    "Metrics Strip",
                    "KPIs or stats to reinforce credibility.",
                    "Builds trust",
                    "Medium",
                ),
            ],
        },
    ]

    def __init__(self):
        settings = get_settings()
        self.client = Groq(api_key=settings.groq_api_key)

    def normalize_language(self, user_language: Optional[str], detected_language: Optional[str]) -> str:
        """Normalize user provided language (supports ISO codes) and fall back to detected language."""
        user_pref = self._standardize_language(user_language)
        if user_pref:
            return user_pref

        return "English"

    def _standardize_language(self, value: Optional[str]) -> Optional[str]:
        if not value:
            return None

        cleaned = value.strip()
        if not cleaned:
            return None

        lowered = cleaned.lower()
        if lowered in self._LANGUAGE_SYNONYMS:
            return self._LANGUAGE_SYNONYMS[lowered]

        return cleaned

    def detect_language(self, text: str) -> str:
        """Detect the language of the user's prompt"""
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Detect the language of the given text. Respond with only the language name in English (e.g., 'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Hindi', 'gujarati'etc.).",
                    },
                    {
                        "role": "user",
                        "content": text,
                    },
                ],
                max_tokens=10,
                temperature=0.1,
            )
            return completion.choices[0].message.content.strip()
        except Exception:
            return "English"  # Default fallback

    def analyze_business_type(self, prompt: str) -> str:
        """Analyze user's prompt to determine business type"""
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "Analyze the user's prompt and determine what type of business or website they want to create. Respond with a brief business type (e.g., 'E-commerce', 'Restaurant', 'Blog', 'Portfolio', 'SaaS', 'Educational', 'Healthcare', 'Real Estate', etc.).",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_tokens=20,
            )
            return completion.choices[0].message.content.strip()
        except Exception:
            return "Business"  # Default fallback

    def infer_business_type_from_answers(
        self,
        prompt: str,
        answers: Dict[str, str],
        fallback: str,
    ) -> str:
        combined_context = prompt or ""
        if answers:
            answer_blob = "\n".join(
                [
                    f"{qid}: {text}"
                    for qid, text in list(answers.items())[:15]
                    if text
                ]
            )
            combined_context = f"{combined_context}\nUser responses:\n{answer_blob}"

        inferred_type = self.analyze_business_type(combined_context)
        if not inferred_type or inferred_type.lower() == "business":
            return fallback or "Business"
        return inferred_type

    def generate_questions(
        self,
        prompt: str,
        language: str,
        business_type: str,
        max_questions: int = 10,
    ) -> List[Dict[str, Any]]:
        """
        Generate an initial block of questions by iteratively calling generate_question_step.
        Ensures we end up with up to max_questions items, padding with fallbacks if needed.
        """
        questions: List[Dict[str, Any]] = []
        history: List[Dict[str, Any]] = []
        asked_texts: Set[str] = set()
        asked_topics: Set[str] = set()
        color_question_asked = False
        business_question_asked = False
        business_slot, color_slot = self._assign_required_slots(max_questions)

        for idx in range(1, max_questions + 1):
            next_question = None
            enforce_business = not business_question_asked and (business_slot is None or idx == business_slot)
            enforce_color = not color_question_asked and (color_slot is None or idx == color_slot)
            for _ in range(3):
                candidate = self.generate_question_step(
                    prompt=prompt,
                    language=language,
                    business_type=business_type,
                    question_history=history,
                    next_index=idx,
                    max_questions=max_questions,
                    color_question_needed=enforce_color,
                    business_name_needed=enforce_business,
                    disallowed_questions=asked_texts,
                    disallowed_topics=asked_topics,
                )
                if not candidate:
                    break
                normalized = self._normalize_question_text(candidate.get("question"))
                if normalized and normalized in asked_texts:
                    continue
                topic_label = self._classify_question_topic(candidate)
                if topic_label and topic_label in asked_topics:
                    continue
                next_question = candidate
                if normalized:
                    asked_texts.add(normalized)
                if topic_label:
                    asked_topics.add(topic_label)
                break

            if not next_question:
                break

            questions.append(next_question)
            history.append(
                {
                    "id": next_question["id"],
                    "question": next_question["question"],
                    "answer": "",
                }
            )

            color_question_asked = color_question_asked or self.is_color_question(
                next_question
            )
            business_question_asked = business_question_asked or self.is_business_name_question(
                next_question
            )

        if not questions:
            fallback = self._get_fallback_questions(
                language,
                business_type,
                prompt,
                include_color=not color_question_asked,
                include_business_name=not business_question_asked,
                disallowed_topics=asked_topics,
            )
            return self._localize_questions(fallback, language, business_type, prompt)

        # Top up with fallback questions if we did not reach the desired length.
        budgeted = {
            "business": business_question_asked,
            "color": color_question_asked,
        }

        if len(questions) < max_questions:
            fallback_pool = self._get_shuffled_fallback_questions(
                language,
                business_type,
                prompt,
                include_color=not budgeted["color"],
                include_business_name=not budgeted["business"],
                disallowed_topics=asked_topics,
            )
            for stub in fallback_pool:
                if len(questions) >= max_questions:
                    break
                normalized = self._normalize_question_text(stub.get("question"))
                if normalized and normalized in asked_texts:
                    continue
                new_question = dict(stub)
                new_question["id"] = f"q{len(questions) + 1}"
                questions.append(new_question)
                if normalized:
                    asked_texts.add(normalized)
                topic_label = self._classify_question_topic(new_question)
                if topic_label:
                    asked_topics.add(topic_label)

        return (
            self._localize_questions(questions, language, business_type, prompt)
            if language and language.lower() not in {"english", "en", "eng"}
            else questions
        )

    def generate_question_step(
        self,
        prompt: str,
        language: str,
        business_type: str,
        question_history: List[Dict[str, Any]],
        next_index: int,
        max_questions: int = 10,
        color_question_needed: bool = False,
        business_name_needed: bool = False,
        disallowed_questions: Optional[Set[str]] = None,
        disallowed_topics: Optional[Set[str]] = None,
        max_retries: int = 2,
    ) -> Optional[Dict[str, Any]]:
        """
        Generate a single follow-up question grounded in the prompt plus prior answers.

        Returns None when the interview is complete or a fallback question could not be created.
        """
        if next_index > max_questions:
            return None

        try:
            history_payload = [
                {
                    "id": item.get("id", f"q{idx + 1}"),
                    "question": item.get("question", ""),
                    "answer": item.get("answer", ""),
                }
                for idx, item in enumerate(question_history)
            ]
            covered_topics = self._infer_topics_from_history(history_payload)
            remaining_topics = [
                data["label"]
                for data in self._QUESTION_TOPICS.values()
                if data["label"] not in covered_topics
            ]
            topic_guidance = ""
            if covered_topics:
                topic_guidance += (
                    "Already covered topics: "
                    + ", ".join(sorted(covered_topics))
                    + ". Avoid repeating them unless you need clarification. "
                )
            if remaining_topics:
                topic_guidance += (
                    "Prioritize exploring these unmet angles next: "
                    + ", ".join(remaining_topics[:3])
                    + ". "
                )

            color_directive = (
                "You still must ask about visual theme/color preferences because it has not been covered yet. "
                "Center the next question on palette, art direction, or visual mood."
                if color_question_needed
                else "Do not repeat questions about color or visual themes if they already appeared."
            )
            business_name_directive = (
                "You still must capture the exact business or brand name the user wants on the site."
                if business_name_needed
                else "Avoid re-asking for the business or brand name since it has already been captured."
            )

            script_hint = self._language_script_hint(language)
            
            # Build context from previous Q&A to generate relevant follow-up
            prev_qa_context = ""
            if history_payload:
                answered_items = [h for h in history_payload if h.get("answer")]
                if answered_items:
                    prev_qa_context = "PREVIOUS QUESTIONS AND ANSWERS:\n"
                    for i, item in enumerate(answered_items, 1):
                        q = item.get('question', '')[:80]
                        a = item.get('answer', '')[:100]
                        prev_qa_context += f"{i}. Q: {q}\n   A: {a}\n"
            
            system_prompt = f"""You are an expert website designer. Generate ONE smart question to help build a {business_type} website.

USER'S ORIGINAL REQUEST:
"{prompt[:500]}"

{prev_qa_context}

YOUR TASK:
- Read the user's request and previous answers carefully
- Ask a NEW question that helps design their specific website
- The question should help make a design decision (colors, layout, sections, animations, content)
- Build on what the user already told you - don't repeat topics already covered

GOOD QUESTION EXAMPLES:
- "What headline should your hero section display?"
- "Do you prefer smooth animations or bold dynamic effects?"
- "What sections does your website need?"
- "Should the design be minimalist or colorful?"
- "What should the main call-to-action button say?"
- "Do you want a contact form, just email, or social links?"

RULES:
1. Ask something NEW and SPECIFIC to their website
2. Each question must help generate actual website code/design
3. Keep under 15 words, use you/your
4. NEVER repeat a topic already asked
5. NEVER ask about payments, accounts, or backend features
6. Write in ENGLISH only
7. STRICTLY maintain relevance to {business_type} website.
8. NEVER ask about general business operations, legal, or financial matters.
9. Focus ONLY on the website visual, content, and structure.

{business_name_directive}
{color_directive}"""

            user_payload = {
                "user_prompt": prompt,
                "business_type": business_type,
                "language": language,
                "next_question_number": next_index,
                "max_questions": max_questions,
                "history": history_payload,
                "needs_business_name": business_name_needed,
                "needs_color_theme": color_question_needed,
            }

            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            system_prompt
                            + "\nRespond ONLY with a valid JSON object matching this schema: "
                            '{"id": "string", "question": "string", "type": "string", "options": ["optional", "choices"]}. '
                            "IMPORTANT: type must be one of: dropdown (for language/selection), radio (one choice with options), "
                            "checkbox (multiple choices), text (short input), textarea (long description), number (numeric), date. "
                            "If you provide options, use type 'radio' for single choice or 'checkbox' for multiple. "
                            "Set id to the provided next question number (e.g., q7)."
                        ),
                    },
                    {
                        "role": "user",
                        "content": json.dumps(user_payload, ensure_ascii=False),
                    },
                ],
                max_tokens=400,
                temperature=0.6,
            )

            response_text = self._strip_json_wrappers(
                completion.choices[0].message.content
            )

            # Valid question types
            VALID_TYPES = {"dropdown", "radio", "checkbox", "text", "textarea", "number", "date"}

            try:
                question_obj = json.loads(response_text)
                if not isinstance(question_obj, dict):
                    raise ValueError("Invalid Groq question payload")

                # Normalize and validate type
                raw_type = (question_obj.get("type") or "text").lower().strip()
                # Map old types to new standardized types
                type_mapping = {
                    "color": "radio",
                    "select": "dropdown",
                    "choice": "radio",
                    "multichoice": "checkbox",
                    "multi": "checkbox",
                    "input": "text",
                    "long": "textarea",
                    "paragraph": "textarea",
                }
                normalized_type = type_mapping.get(raw_type, raw_type)
                if normalized_type not in VALID_TYPES:
                    normalized_type = "radio" if question_obj.get("options") else "text"

                formatted_question = {
                    "id": f"q{next_index}",
                    "question": question_obj.get("question", "").strip(),
                    "type": normalized_type,
                }
                if question_obj.get("options"):
                    formatted_question["options"] = question_obj["options"]

                if not formatted_question["question"]:
                    raise ValueError("Missing question text")

                source_question = formatted_question["question"]
                english_probe = dict(formatted_question)
                topic_label = self._classify_question_topic(english_probe)
                if not business_name_needed and self.is_business_name_question(english_probe):
                    raise ValueError("Business name already captured")
                if not color_question_needed and self.is_color_question(english_probe):
                    raise ValueError("Color question already captured")
                normalized = self._normalize_question_text(source_question)
                if normalized and disallowed_questions and normalized in disallowed_questions:
                    raise ValueError("Duplicate question detected")
                if topic_label and disallowed_topics and topic_label in disallowed_topics:
                    raise ValueError("Duplicate topic detected")
                if self._contains_banned_question_phrase(source_question):
                    raise ValueError("Banned topic detected")
                formatted_question["_source_question"] = source_question
                if topic_label:
                    formatted_question["_topic_label"] = topic_label

                localized = self._localize_questions(
                    [formatted_question],
                    language,
                    business_type,
                    prompt,
                )
                result = localized[0] if localized else formatted_question
                result["_source_question"] = source_question
                if topic_label:
                    result["_topic_label"] = topic_label
                return result
            except (json.JSONDecodeError, ValueError):
                pass

        except Exception:
            pass

        fallback_question = self._get_dynamic_fallback_question(
            next_index,
            language,
            business_type,
            prompt,
            disallowed_questions,
            include_color=color_question_needed,
            include_business_name=business_name_needed,
            disallowed_topics=disallowed_topics,
        )
        if not fallback_question:
            return None
        localized = self._localize_questions(
            [fallback_question],
            language,
            business_type,
            prompt,
        )
        return localized[0] if localized else fallback_question

    def generate_last_chance_question(
        self,
        prompt: str,
        language: str,
        business_type: str,
        next_index: int,
        disallowed_questions: Optional[Set[str]],
        color_question_needed: bool,
        business_name_needed: bool,
    ) -> Optional[Dict[str, Any]]:
        """
        Ultra-forgiving fallback that relaxes topic constraints to ensure we still reach 10 questions.
        """
        fallback_question = self._get_dynamic_fallback_question(
            next_index,
            language,
            business_type,
            prompt,
            disallowed_questions,
            include_color=color_question_needed,
            include_business_name=business_name_needed,
            disallowed_topics=None,
        )
        if not fallback_question:
            return None
        localized = self._localize_questions(
            [fallback_question],
            language,
            business_type,
            prompt,
        )
        return localized[0] if localized else fallback_question

    def is_color_question(self, question: Dict[str, Any]) -> bool:
        """Detect whether a question already covers color/theme topics."""
        if not question:
            return False

        topic_label = (question.get("_topic_label") or "").strip().lower()
        if topic_label == "visual design":
            return True

        # Explicit color type flag
        if question.get("type") == "color":
            return True

        text = (question.get("_source_question") or question.get("question") or "").lower()
        if not text:
            return False

        keywords = [
            "color",
            "colour",
            "palette",
            "theme",
            "visual mood",
            "art direction",
            "aesthetic",
        ]
        return any(keyword in text for keyword in keywords)

    def _classify_question_topic(self, question: Dict[str, Any]) -> Optional[str]:
        """Return the normalized topic label for a question, if any."""
        if not question:
            return None

        text = (question.get("question") or "").lower()
        if not text:
            return None

        if self.is_business_name_question(question):
            return "business name"
        if self.is_color_question(question):
            return "visual design"

        for data in self._QUESTION_TOPICS.values():
            if any(keyword in text for keyword in data["keywords"]):
                return data["label"]
        return None

    def classify_question_topic(self, question: Dict[str, Any]) -> Optional[str]:
        """Public wrapper used by session service to label topics."""
        return self._classify_question_topic(question)

    def _normalize_question_text(self, text: Optional[str]) -> Optional[str]:
        if not text:
            return None
        return " ".join(text.strip().lower().split())

    def _contains_banned_question_phrase(self, text: str) -> bool:
        lowered = text.lower()
        return any(keyword in lowered for keyword in self._QUESTION_BANNED_KEYWORDS)

    def is_business_name_question(self, question: Dict[str, Any]) -> bool:
        """Detect whether a question explicitly captures the business or brand name."""
        if not question:
            return False

        text = (question.get("question") or "").lower()
        if not text:
            return False

        keywords = [
            "business name",
            "brand name",
            "store name",
            "what should we call",
            "company name",
            "exact name on the site",
        ]
        if any(keyword in text for keyword in keywords):
            return True

        # Broader pattern: mention of "name" plus site/brand/store references.
        if "name" in text and any(
            token in text
            for token in [
                "site",
                "website",
                "brand",
                "business",
                "company",
                "shop",
                "store",
                "studio",
                "label",
                "project",
            ]
        ):
            return True

        return False

    def _infer_topics_from_history(
        self, history: List[Dict[str, Any]]
    ) -> Set[str]:
        """Infer which strategic topics have already been covered."""
        detected: Set[str] = set()
        for item in history:
            text_blobs = [
                str(item.get("question") or ""),
                str(item.get("answer") or ""),
            ]
            for blob in text_blobs:
                lowered = blob.lower()
                for data in self._QUESTION_TOPICS.values():
                    if any(keyword in lowered for keyword in data["keywords"]):
                        detected.add(data["label"])
        return detected

    def _strip_json_wrappers(self, raw: str) -> str:
        """Remove common Markdown code fences or stray whitespace before JSON parsing."""
        if not raw:
            return ""
        cleaned = raw.strip()
        # Remove markdown triple-backtick fences e.g. ```json ... ```
        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.IGNORECASE).strip()
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3].strip()
        # Remove stray leading/trailing code fence markers
        cleaned = cleaned.strip("` \n\r\t")
        return cleaned


    def generate_color_palettes(
        self,
        theme_answer: str,
        business_type: str,
        prompt: str | None = None,
    ) -> List[Dict[str, Any]]:
        """Generate rich color palettes based on theme, business type, and user prompt"""
        import random

        def _fallback_with_shuffle():
            palettes = self._get_fallback_palettes(theme_answer, business_type)
            random.shuffle(palettes)
            return palettes

        try:
            story_context = theme_answer or "User prefers natural tones"
            system_prompt = f"""
            You are an elite brand colorist. Reference ONLY the user's palette answer to craft options.

            Palette brief:
            - Color/theme notes from user: {story_context}

            Requirements:
            1. Propose exactly 8 distinct palettes (p1-p8) with unique titles.
            2. Each palette must include:
               - id: "p1"..."p8"
               - title: 2-3 word poetic label reflecting the user's color answer.
               - inspiration: single sentence describing the vibe based solely on the color answer (ignore business type).
               - colors: array of exactly 5 HEX codes (uppercase, valid #RRGGBB) arranged from base/background to accent.
            3. No palette may repeat the same HEX codes in identical order.
            4. Keep language concise; respond with a valid JSON array only.
            5. Use high temperature creativity; each response must feel fresh with no repeated palettes.
            """

            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": f"Generate 8 palettes for theme: {story_context}",
                    },
                ],
                max_tokens=700,
                temperature=1.1,
                top_p=0.95,
            )

            response = completion.choices[0].message.content.strip()

            try:
                palettes = json.loads(self._strip_json_wrappers(response))
                # Ensure proper format
                formatted_palettes = []
                unique_sets = set()
                for i, p in enumerate(palettes, 1):
                    colors = p.get("colors", ["#000000", "#FFFFFF", "#808080"])
                    color_tuple = tuple(colors)
                    if color_tuple in unique_sets:
                        continue
                    unique_sets.add(color_tuple)
                    formatted_palette = {
                        "id": p.get("id", f"p{i}"),
                        "colors": colors,
                    }
                    if p.get("title"):
                        formatted_palette["title"] = p["title"]
                    if p.get("inspiration"):
                        formatted_palette["inspiration"] = p["inspiration"]
                    formatted_palettes.append(formatted_palette)
                if len(formatted_palettes) < 8:
                    return _fallback_with_shuffle()
                return formatted_palettes
            except json.JSONDecodeError:
                return _fallback_with_shuffle()

        except Exception:
            return _fallback_with_shuffle()

    def _feature_has_banned_keyword(self, text: Optional[str]) -> bool:
        if not text:
            return False
        lowered = text.lower()
        return any(keyword in lowered for keyword in self._FEATURE_BANNED_KEYWORDS)

    def _features_from_templates(self, inferred_type: str) -> List[Dict[str, Any]]:
        def _template_to_feature(template: Tuple[str, str, str, str, str]) -> Dict[str, Any]:
            fid, name, description, benefit, priority = template
            return {
                "id": fid,
                "name": name,
                "description": description,
                "benefit": benefit,
                "priority": priority,
            }

        features: List[Dict[str, Any]] = [_template_to_feature(t) for t in self._CORE_PAGE_TEMPLATES]
        features.extend(_template_to_feature(t) for t in self._SUPPORT_PAGE_TEMPLATES)

        for bundle in self._BUSINESS_PAGE_BUNDLES:
            if any(keyword in inferred_type for keyword in bundle["matchers"]):
                features.extend(_template_to_feature(t) for t in bundle["templates"])

        filtered: List[Dict[str, Any]] = []
        seen_ids: Set[str] = set()
        for feature in features:
            if feature["id"] in seen_ids:
                continue
            if self._feature_has_banned_keyword(feature["name"]) or self._feature_has_banned_keyword(
                feature["description"]
            ):
                continue
            seen_ids.add(feature["id"])
            filtered.append(feature)
        return filtered[:10]

    def generate_features(self, prompt: str, business_type: str, answers: Dict[str, str]) -> List[Dict[str, Any]]:
        """
        Suggest up to 12 website sections based on detected website type's ACTUAL templates.
        
        Priority:
        1. Get sections from website-type-specific templates (MovieTemplates, CafeTemplates, etc.)
        2. Merge with shared templates (Contact, Testimonials, FAQ, CTA)
        3. Use AI generation only as fallback
        
        This ensures every suggested feature has a working template!
        """
        prompt_context = (prompt or "").strip()
        inferred_type = (business_type or "").strip().lower()
        
        # Detect website type from prompt if not explicitly provided
        detected_type = self._detect_website_type_from_prompt(prompt_context, inferred_type)
        
        # Get template-based features
        template_features = self._get_features_from_templates(detected_type)
        
        if template_features:
            print(f"[GroqService] 🎯 Using template-based features for '{detected_type}': {len(template_features)} features")
            return template_features
        
        # Fallback to AI-generated features if no templates
        print(f"[GroqService] ⚠️ No templates for '{detected_type}', using AI generation")
        return self._generate_features_with_ai(prompt_context, inferred_type, answers)
    
    def _detect_website_type_from_prompt(self, prompt: str, business_type: str) -> str:
        """Detect website type from prompt keywords"""
        combined = f"{prompt} {business_type}".lower()
        
        type_keywords = {
            "movie": ["movie", "cinema", "theater", "theatre", "film", "ticket", "showtime", "blockbuster", "premiere", "imax"],
            "cafe": ["cafe", "coffee", "brew", "latte", "espresso", "bakery", "pastry", "barista"],
            "gaming": ["gaming", "game", "esports", "streamer", "twitch", "xbox", "playstation", "gamer"],
            "restaurant": ["restaurant", "dining", "food", "chef", "menu", "reservation", "cuisine"],
            "portfolio": ["portfolio", "personal", "developer", "designer", "freelance", "resume"],
            "ecommerce": ["shop", "store", "ecommerce", "buy", "sell", "product", "cart"],
        }
        
        for wtype, keywords in type_keywords.items():
            if any(kw in combined for kw in keywords):
                return wtype
        
        return "agency"  # Default
    
    def _get_features_from_templates(self, website_type: str) -> List[Dict[str, Any]]:
        """Get features based on available templates for the website type"""
        
        # Template-based features for each website type
        # NOTE: This list is filtered DYNAMICALLY by folder existence below.
        TEMPLATE_FEATURES = {
            "movie": [
                {"id": "hero", "name": "Hero", "description": "Dramatic movie-themed hero banner.", "benefit": "Instant impact", "priority": "High"},
                {"id": "movies", "name": "Now Showing", "description": "Grid of currently playing movies.", "benefit": "Shows offerings", "priority": "High"},
                {"id": "showtimes", "name": "Showtimes", "description": "Interactive schedule.", "benefit": "Easy booking", "priority": "High"},
                {"id": "tickets", "name": "Book Tickets", "description": "Ticket booking section.", "benefit": "Converts visitors", "priority": "High"},
                {"id": "about", "name": "About Cinema", "description": "Cinema story and facilities.", "benefit": "Builds trust", "priority": "Medium"},
                {"id": "gallery", "name": "Gallery", "description": "Photo gallery of cinema halls.", "benefit": "Visual proof", "priority": "Medium"},
                {"id": "contact", "name": "Contact", "description": "Location and contact form.", "benefit": "Easy reach", "priority": "Medium"},
            ],
            "cafe": [
                {"id": "hero", "name": "Hero", "description": "Warm, inviting hero with cafe ambiance.", "benefit": "First impression", "priority": "High"},
                {"id": "menu", "name": "Our Menu", "description": "Coffee, pastries, and food menu.", "benefit": "Shows offerings", "priority": "High"},
                {"id": "about", "name": "Our Story", "description": "The cafe story and values.", "benefit": "Builds connection", "priority": "High"},
                {"id": "gallery", "name": "Gallery", "description": "Photos of your cafe drinks.", "benefit": "Visual appeal", "priority": "Medium"},
                {"id": "specials", "name": "Today's Specials", "description": "Daily specials.", "benefit": "Creates urgency", "priority": "Medium"},
                {"id": "hours", "name": "Hours & Location", "description": "Opening hours and map.", "benefit": "Easy to find", "priority": "High"},
            ],
            "gaming": [
                {"id": "hero", "name": "Hero", "description": "Epic gaming-themed hero banner.", "benefit": "Immediate impact", "priority": "High"},
                {"id": "games", "name": "Games", "description": "Featured games catalog.", "benefit": "Shows content", "priority": "High"},
                {"id": "tournaments", "name": "Tournaments", "description": "Upcoming esports events.", "benefit": "Builds community", "priority": "High"},
                {"id": "community", "name": "Community", "description": "Discord and social links.", "benefit": "Engagement", "priority": "Medium"},
                {"id": "about", "name": "About Us", "description": "Team info and studio story.", "benefit": "Personal touch", "priority": "Medium"},
                {"id": "gallery", "name": "Media Gallery", "description": "Screenshots and trailers.", "benefit": "Visual showcase", "priority": "Medium"},
                {"id": "news", "name": "Updates", "description": "Latest patches and dev logs.", "benefit": "Keeps players informed", "priority": "Low"},
                {"id": "store", "name": "Game Store", "description": "Link to buy games or merch.", "benefit": "Revenue", "priority": "Low"},
            ],
            "restaurant": [
                {"id": "hero", "name": "Hero", "description": "Elegant restaurant hero.", "benefit": "Ambiance", "priority": "High"},
                {"id": "menu", "name": "Full Menu", "description": "Interactive food and drink menu.", "benefit": "Key information", "priority": "High"},
                {"id": "reservations", "name": "Reservations", "description": "Booking slot selector.", "benefit": "Converts", "priority": "High"},
                {"id": "gallery", "name": "Food Gallery", "description": "High-quality food photography.", "benefit": "Visual delight", "priority": "Medium"},
                {"id": "about", "name": "Heritage", "description": "Chef and restaurant history.", "benefit": "Authenticity", "priority": "Medium"},
                {"id": "contact", "name": "Contact", "description": "Location and contact info.", "benefit": "Find us", "priority": "High"},
            ],
            "portfolio": [
                {"id": "hero", "name": "Hero", "description": "Clean personal banner.", "benefit": "Focus", "priority": "High"},
                {"id": "projects", "name": "Projects", "description": "Showcase of your best work.", "benefit": "Proof", "priority": "High"},
                {"id": "about", "name": "Profile", "description": "Your skills and experience.", "benefit": "Personal brand", "priority": "High"},
                {"id": "skills", "name": "Expertise", "description": "Specific tech stack or skills.", "benefit": "Quick info", "priority": "Medium"},
                {"id": "contact", "name": "Connect", "description": "Contact form and links.", "benefit": "Reachability", "priority": "High"},
            ],
            "ecommerce": [
                {"id": "hero", "name": "Hero", "description": "Sales-focused hero banner.", "benefit": "Conversion", "priority": "High"},
                {"id": "products", "name": "Products", "description": "Product catalog with categories.", "benefit": "Revenue", "priority": "High"},
                {"id": "about", "name": "Brand", "description": "Your company mission.", "benefit": "Trust", "priority": "Medium"},
                {"id": "faq", "name": "Store FAQ", "description": "Shipping, returns, and support.", "benefit": "Reduces doubts", "priority": "Medium"},
            ],
        }
        
        # Get list of features for this type
        all_features = TEMPLATE_FEATURES.get(website_type, [])
        if not all_features:
            # Fallback to agency features if type unknown
            all_features = [
                {"id": "hero", "name": "Hero", "description": "Impressive hero banner.", "benefit": "Instant impact", "priority": "High"},
                {"id": "about", "name": "About Us", "description": "Company story.", "benefit": "Builds trust", "priority": "High"},
                {"id": "services", "name": "Services", "description": "What you offer.", "benefit": "Shows value", "priority": "High"},
                {"id": "contact", "name": "Contact", "description": "Contact form.", "benefit": "Easy reach", "priority": "High"},
            ]
            website_type = "agency"

        from pathlib import Path
        type_path = Path(__file__).parent.parent.parent.parent / "Web_generator" / "app" / "templates" / "website_types" / website_type
        
        # FILTER: Only keep features that have a corresponding folder
        filtered_features = []
        for feature in all_features:
            feature_id = feature["id"]
            if (type_path / feature_id).is_dir():
                filtered_features.append(feature)
            else:
                print(f"[GroqService] ⏭️ Filtering out feature '{feature_id}' - no template folder found for '{website_type}'")
        
        return filtered_features
    
    def _generate_features_with_ai(self, prompt: str, business_type: str, answers: Dict[str, str]) -> List[Dict[str, Any]]:
        """Fallback: Generate features using AI (legacy method)"""
        # Build a detailed summary of what we know about the business
        answers_summary = ""
        if answers:
            answers_summary = "\n\nWhat we learned from the user during questionnaire:\n"
            for qid, answer in list(answers.items())[:10]:
                if answer:
                    answers_summary += f"- {answer}\n"
        
        system_prompt = f"""You are an expert website strategist. Based on the user's specific business and their answers, suggest 8 website sections/features that would be PERFECT for their website.

BUSINESS TYPE: {business_type}
USER'S REQUEST: {prompt[:500]}
{answers_summary}

YOUR TASK:
1. Analyze the specific business and what they mentioned
2. Suggest 8 website sections that would be IDEAL for THIS specific business
3. Each feature should directly relate to what the user described
4. Make features specific, not generic (e.g., "Our Menu" for restaurant, not just "Services")

RULES:
- Focus on static website sections (no shopping carts, payments, user accounts)
- Good sections: Hero, About Us, Services/Menu, Gallery, Testimonials, Contact, FAQ, Team, Portfolio, Pricing Display, Location/Map, Newsletter
- Make names and descriptions specific to their business type
- Priority = High for essential sections, Medium for nice-to-have, Low for optional

Respond with a JSON array:
[{{"id":"f1","name":"Section Name","description":"What this section shows","benefit":"Why it helps","priority":"High|Medium|Low"}}]

Generate 8 features tailored specifically to this {business_type} business."""

        user_payload = {
            "business_type": business_type,
            "prompt": prompt[:800],
            "answers": [{"q": qid, "a": text} for qid, text in list(answers.items())[:8] if text],
        }

        try:
            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
                ],
                max_tokens=900,
                temperature=0.5,
            )
            response = self._strip_json_wrappers(completion.choices[0].message.content)
            parsed = json.loads(response)
            if isinstance(parsed, dict) and "features" in parsed:
                parsed = parsed["features"]

            features: List[Dict[str, Any]] = []
            seen_names: Set[str] = set()
            if isinstance(parsed, list):
                for idx, item in enumerate(parsed, start=1):
                    name = (item.get("name") or "").strip()
                    description = (item.get("description") or "").strip()
                    if not name or not description:
                        continue
                    if self._feature_has_banned_keyword(name) or self._feature_has_banned_keyword(description):
                        continue
                    normalized_name = name.lower()
                    if normalized_name in seen_names:
                        continue
                    seen_names.add(normalized_name)
                    feature = {
                        "id": item.get("id") or f"f{idx}",
                        "name": name,
                        "description": description,
                        "benefit": (item.get("benefit") or "Clarifies value").strip(),
                        "priority": (item.get("priority") or "Medium").strip().title(),
                    }
                    features.append(feature)

            if features:
                return features[:8]
        except Exception:
            pass

        fallback = self._features_from_templates(business_type.lower())
        return fallback if fallback else self._features_from_templates("generic")

    def _localize_questions(
        self,
        questions: List[Dict[str, Any]],
        language: str,
        business_type: str,
        prompt: str,
    ) -> List[Dict[str, Any]]:
        """Translate question text to requested language when needed."""
        if not questions:
            return questions

        normalized = (language or "").strip()
        if not normalized:
            return questions

        if normalized.lower() in {"english", "en", "eng"}:
            return questions

        try:
            question_payload = [
                {"id": q["id"], "question": q["question"], **({k: q[k] for k in ("type", "options") if k in q})}
                for q in questions
            ]

            script_guidance = {
                "hindi": "Write every sentence fully in देवनागरी with 8-12 word, child-simple phrasing. Avoid Latin text.",
                "gujarati": "Write every sentence fully in ગુજરાતી લિપિ with 8-12 word, child-simple phrasing. Avoid Latin text.",
            }
            normalized_lower = normalized.lower()
            script_instruction = script_guidance.get(
                normalized_lower,
                "Use plain words and native script when possible.",
            )

            translation_prompt = (
                "You are a professional bilingual UX strategist. Rewrite every question naturally in the requested language. "
                "IMPORTANT: Every word of your response must be in {language_name} and its native script. "
                "Do NOT mention the original prompt text or repeat phrases like 'I want to build'. "
                "Keep each question consultative, concise (8-15 words), and business-appropriate. "
                "Preserve the JSON schema exactly (id, question, optional type/options). "
                "Translate option labels unless they are product names. "
                "Do NOT produce gibberish or hallucinated words. Use proper grammar. "
                f"{script_instruction} "
                "The website type is '{business_type}'. "
                "Respond ONLY with a JSON array matching the input structure."
            ).format(language_name=normalized, business_type=business_type)

            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": translation_prompt,
                    },
                    {
                        "role": "user",
                        "content": json.dumps(
                            {
                                "target_language": normalized,
                                "prompt_context": prompt[:400],
                                "questions": question_payload,
                            },
                            ensure_ascii=False,
                        ),
                    },
                ],
                max_tokens=1000,
                temperature=0.1,
            )

            translated = json.loads(
                self._strip_json_wrappers(
                    completion.choices[0].message.content
                )
            )
            if isinstance(translated, list) and len(translated) == len(questions):
                preserved: List[Dict[str, Any]] = []
                for original, localized in zip(questions, translated):
                    merged = dict(localized)
                    merged["id"] = original.get("id")
                    if "type" not in merged and "type" in original:
                        merged["type"] = original["type"]
                    if "options" not in merged and "options" in original:
                        merged["options"] = original["options"]
                    preserved.append(merged)
                return preserved

        except Exception:
            pass

        return questions

    def _get_fallback_questions(
        self,
        language: str,
        business_type: str,
        prompt: str,
        include_color: bool = True,
        include_business_name: bool = True,
        disallowed_topics: Optional[Set[str]] = None,
    ) -> List[Dict[str, Any]]:
        """Attempt to regenerate a batch of look-and-feel questions via Groq; fall back to static list last."""
        script_hint = self._language_script_hint(language)

        try:
            system_prompt = (
                "You are an expert website designer helping gather requirements for a modern, animated website. "
                "Generate up to 10 short, unique questions about how the website should look, feel, and animate. "
                "The output must be in {language}. "
                "Keep every question under 15 words, use 'you/your', avoid jargon. "
                "Focus on these animated website elements: "
                "- Hero sections and first impressions "
                "- Animation styles (smooth, bold, playful, elegant) "
                "- Scroll effects and transitions "
                "- Hover states and micro-interactions "
                "- Galleries, sliders, and image presentations "
                "- Typography and spacing preferences "
                "- Color accents and visual hierarchy "
                "Do not ask about business types, pricing, payments, or ecommerce. "
                "Each question must relate to creating stunning visual designs and animations. "
                f"{script_hint}"
            ).replace("{language}", language)
            
            user_payload = {
                "business_type": business_type,
                "language": language,
                "prompt": (prompt or "")[:500],
            }
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": json.dumps(user_payload, ensure_ascii=False),
                    },
                ],
                max_tokens=800,
                temperature=0.4,
            )
            response = self._strip_json_wrappers(completion.choices[0].message.content)
            parsed = json.loads(response)
            generated: List[Dict[str, Any]] = []
            for idx, item in enumerate(parsed, 1):
                question_text = (item.get("question") or "").strip()
                if not question_text or self._contains_banned_question_phrase(question_text):
                    continue
                entry = {
                    "id": item.get("id", f"q{idx}"),
                    "question": question_text,
                    "type": item.get("type") or ("radio" if item.get("options") else "text"),
                }
                if item.get("options"):
                    entry["options"] = item["options"]
                topic_label = self._classify_question_topic(entry)
                if (
                    disallowed_topics
                    and topic_label
                    and topic_label in disallowed_topics
                ):
                    continue
                generated.append(entry)
            if generated:
                return generated
        except Exception:
            pass

        return self._build_programmatic_fallback_questions(
            language,
            business_type,
            prompt,
            include_color=include_color,
            include_business_name=include_business_name,
            disallowed_topics=disallowed_topics,
        )

    def _get_fallback_question_by_index(
        self,
        index: int,
        language: str,
        business_type: str,
        prompt: str,
    ) -> Optional[Dict[str, Any]]:
        fallback_questions = self._get_fallback_questions(
            language,
            business_type,
            prompt,
            include_color=True,
            include_business_name=True,
            disallowed_topics=None,
        )
        if 1 <= index <= len(fallback_questions):
            stub = dict(fallback_questions[index - 1])
            stub["id"] = f"q{index}"
            return stub
        return None

    def _assign_required_slots(self, max_questions: int) -> tuple[Optional[int], Optional[int]]:
        if max_questions <= 0:
            return None, None

        slots = list(range(1, max_questions + 1))
        random.shuffle(slots)

        business_slot = slots[0] if slots else None
        color_slot = None
        for slot in slots[1:]:
            if slot != business_slot:
                color_slot = slot
                break
        return business_slot, color_slot

    def _get_shuffled_fallback_questions(
        self,
        language: str,
        business_type: str,
        prompt: str,
        include_color: bool = True,
        include_business_name: bool = True,
        disallowed_topics: Optional[Set[str]] = None,
    ) -> List[Dict[str, Any]]:
        pool = list(
            self._get_fallback_questions(
                language,
                business_type,
                prompt,
                include_color=include_color,
                include_business_name=include_business_name,
                disallowed_topics=disallowed_topics,
            )
        )
        random.shuffle(pool)
        return pool

    def _get_dynamic_fallback_question(
        self,
        next_index: int,
        language: str,
        business_type: str,
        prompt: str,
        disallowed_questions: Optional[Set[str]],
        include_color: bool = True,
        include_business_name: bool = True,
        disallowed_topics: Optional[Set[str]] = None,
    ) -> Optional[Dict[str, Any]]:
        candidates = self._get_shuffled_fallback_questions(
            language,
            business_type,
            prompt,
            include_color=include_color,
            include_business_name=include_business_name,
            disallowed_topics=disallowed_topics,
        )
        for stub in candidates:
            normalized = self._normalize_question_text(stub.get("question"))
            if normalized and disallowed_questions and normalized in disallowed_questions:
                continue
            topic_label = self._classify_question_topic(stub)
            if topic_label and disallowed_topics and topic_label in disallowed_topics:
                continue
            if self._contains_banned_question_phrase(stub.get("question", "")):
                continue
            fallback = dict(stub)
            fallback["id"] = f"q{next_index}"
            return fallback
        return None

    def _build_programmatic_fallback_questions(
        self,
        language: str,
        business_type: str,
        prompt: str,
        include_color: bool = True,
        include_business_name: bool = True,
        disallowed_topics: Optional[Set[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Final backstop: still use Groq, but ask for one question at a time with narrow focus.
        This keeps the experience AI-driven while providing resilience when batch calls fail.
        """
        topic_hints = [
            {
                "hint": "Capture the exact business or brand name that must appear on the site.",
                "fallback": "What exact business name should show on the site?",
                "ensure_type": None,
                "category": "business",
                "topic_label": "business name",
            },
            {
                "hint": "Understand the preferred color palette or visual theme for the site.",
                "fallback": "Which color mood should the site lean toward?",
                "ensure_type": "radio",  # Single choice from options
                "options": ["Light & airy", "Bold contrast", "Dark & moody"],
                "category": "color",
                "topic_label": "visual design",
            },
            {
                "hint": "Clarify the most important first impression or hero moment for visitors.",
                "fallback": "What should visitors notice first when they land?",
                "ensure_type": None,
                "topic_label": "content requirements",
            },
            {
                "hint": "Ask about layout or navigation expectations (single page vs multi-section).",
                "fallback": "Do you imagine a single-page flow or multi-section navigation?",
                "ensure_type": None,
                "topic_label": "site structure",
            },
            {
                "hint": "Probe on imagery or media style (photography, illustration, motion).",
                "fallback": "What imagery style fits you best—photography, illustration, or motion?",
                "ensure_type": None,
                "topic_label": "content requirements",
            },
            {
                "hint": "Check for any accessibility or performance requirements to respect.",
                "fallback": "Are there accessibility or performance requirements we must respect?",
                "ensure_type": None,
                "topic_label": "accessibility/mobile needs",
            },
        ]

        generated: List[Dict[str, Any]] = []
        seen: Set[str] = set()
        brand_hint = self._extract_brand_hint(prompt) or "your brand"
        site_label = business_type or "your site"

        active_topics: List[Dict[str, Any]] = []
        for topic in topic_hints:
            category = topic.get("category")
            if category == "business" and not include_business_name:
                continue
            if category == "color" and not include_color:
                continue
            topic_label = topic.get("topic_label")
            if disallowed_topics and topic_label and topic_label in disallowed_topics:
                continue
            active_topics.append(topic)

        for idx, topic in enumerate(active_topics, start=1):
            question = self._request_single_ai_question(
                prompt=prompt,
                language=language,
                business_type=business_type,
                next_index=idx,
                topic_hint=topic["hint"],
            )
            if not question and topic.get("fallback"):
                fallback_text = topic["fallback"]
                question = {
                    "id": f"q{idx}",
                    "question": fallback_text.replace("{brand}", brand_hint).replace("{site}", site_label),
                }
            if not question:
                continue
            normalized = self._normalize_question_text(question.get("question"))
            if normalized and normalized in seen:
                continue
            seen.add(normalized)

            # Ensure type is always set
            if topic.get("ensure_type"):
                question["type"] = topic.get("ensure_type")
                if topic.get("ensure_type") in ("radio", "checkbox", "dropdown"):
                    question.setdefault("options", topic.get("options"))
            elif "type" not in question:
                question["type"] = "radio" if question.get("options") else "text"

            generated.append(question)

        return generated

    def _request_single_ai_question(
        self,
        prompt: str,
        language: str,
        business_type: str,
        next_index: int,
        topic_hint: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Issue a narrowly scoped Groq request for a single question without falling back to static text.
        Always generates in English - translation happens in _localize_questions.
        """
        try:
            # Generate in English to avoid garbled text - translation happens later
            system_prompt = (
                "You are an expert website designer gathering requirements for a modern, animated {business_type} website. "
                "Ask exactly ONE short (<=15 words) question focused on visual design, animations, layout, or interactivity. "
                "Focus on elements that help create stunning animated websites: hero sections, scroll effects, hover states, galleries, transitions. "
                "Use conversational language (you/your) and avoid technical jargon. "
                "Do not ask what the business does—the context is already known. "
                "WRITE THE QUESTION IN ENGLISH ONLY. "
                f"{topic_hint}"
            ).format(business_type=business_type or "brand")

            user_payload = {
                "user_prompt": (prompt or "")[:400],
                "question_number": next_index,
                "language": language,
                "topic_hint": topic_hint,
            }

            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                        + ' Output JSON: {"question": "...", "type": "optional", "options": ["optional choices"]}',
                    },
                    {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
                ],
                max_tokens=200,
                temperature=0.5,
            )

            payload = self._strip_json_wrappers(completion.choices[0].message.content)
            parsed = json.loads(payload)
            question_text = (parsed.get("question") or "").strip()
            if not question_text:
                return None

            result = {
                "id": f"q{next_index}",
                "question": question_text,
                "type": parsed.get("type") or ("radio" if parsed.get("options") else "text"),
            }
            if parsed.get("options"):
                result["options"] = parsed["options"]
            return result
        except Exception:
            return None

    def _extract_brand_hint(self, prompt: Optional[str]) -> Optional[str]:
        if not prompt:
            return None
        cleaned = re.sub(r"[^A-Za-z0-9\s]", " ", prompt)
        tokens = [token for token in cleaned.split() if len(token) >= 3]
        if not tokens:
            return None
        return " ".join(tokens[:3])

    def _get_fallback_palettes(self, theme: str, business_type: str) -> List[Dict[str, Any]]:
        """Fallback color palettes if Groq API fails"""
        theme_lower = theme.lower()
        business_lower = business_type.lower()

        def _build_palette(pid, title, inspiration, colors):
            return {
                "id": pid,
                "title": title,
                "inspiration": inspiration,
                "colors": colors,
            }

        if "red" in theme_lower or "sunset" in theme_lower:
            return [
                _build_palette("p1", "Vermilion Mist", "Warm gradients echoing sunset storefronts.", ["#4A1F1C", "#7A2D2A", "#B6462C", "#F26B38", "#FFD6A5"]),
                _build_palette("p2", "Crimson Current", "Bold retail energy for conversion-focused layouts.", ["#1A0B14", "#3B0D2E", "#7C163D", "#FF3E4D", "#FFC857"]),
                _build_palette("p3", "Coral Bloom", "Playful creative studios with lively accents.", ["#1F1F2E", "#FF7F50", "#FEC260", "#F8F0E3", "#2A1B3D"]),
                _build_palette("p4", "Molten Luxe", "High-end fashion hero sections with glowing neons.", ["#040308", "#31102B", "#6C1A3A", "#FF4E88", "#FFD53D"]),
            ]

        if "blue" in theme_lower or "ocean" in theme_lower:
            return [
                _build_palette("p1", "Azure Circuit", "Tech-forward SaaS dashboards.", ["#050914", "#0B1F3A", "#123C73", "#28A6FF", "#8BF1FF"]),
                _build_palette("p2", "Nordic Calm", "Minimal wellness brands with airy whites.", ["#101820", "#1F3B4D", "#4B7F94", "#9ED0E6", "#F4FCFF"]),
                _build_palette("p3", "Deep Harbor", "Consulting hero sections with trust-rich blues.", ["#0A0F1E", "#152D4A", "#1F4E79", "#2E8BC0", "#F2FCFF"]),
                _build_palette("p4", "Midnight Pulse", "Cyber aesthetics with electric highlights.", ["#030712", "#101935", "#2C3E87", "#5E72EB", "#37E4FF"]),
            ]

        if "green" in theme_lower or "eco" in theme_lower:
            return [
                _build_palette("p1", "Verdant Flux", "Eco-tech landing pages with citrus accents.", ["#0D1F12", "#234029", "#3F6B3F", "#7BC47F", "#F0FFD8"]),
                _build_palette("p2", "Sage Atelier", "Boutique wellness studios.", ["#1A1712", "#3C3A32", "#6F6A57", "#C5BFA0", "#FAF6EB"]),
                _build_palette("p3", "Neon Herb", "Agritech dashboards needing punchy contrasts.", ["#0D1411", "#1E2C27", "#3A5247", "#94F3A2", "#F8FFE5"]),
                _build_palette("p4", "Moss Drift", "Nature retreats with immersive gradients.", ["#070C0A", "#1B3326", "#2E6145", "#5FA05A", "#E2F1D5"]),
            ]

        # Generic cinematic palettes
        return [
            _build_palette("p1", "Noir Atelier", "Luxury portfolio aesthetics.", ["#050505", "#1C1C1E", "#373640", "#A49393", "#F5E6E8"]),
            _build_palette("p2", "Prism Charge", "Futuristic builder UI with vivid bars.", ["#0C0824", "#2D1163", "#5B1A8D", "#FF4BCD", "#FFC857"]),
            _build_palette("p3", "Pastel Current", "Soft tech marketing pages.", ["#101821", "#343C56", "#6BDAB9", "#F7B2BD", "#FDF6F0"]),
            _build_palette("p4", "Aurora Forge", "Creative agencies with neon warmth.", ["#04050A", "#15212E", "#27425C", "#F15263", "#FFC857"]),
        ]

    def _get_fallback_features(self, business_type: str) -> List[Dict[str, Any]]:
        """Fallback features if Groq API fails"""

        def _feature(fid, name, description, benefit, priority="Medium"):
            return {
                "id": fid,
                "name": name,
                "description": description,
                "benefit": benefit,
                "priority": priority,
            }

        base_features = [
            _feature("f1", "Hero Narrative", "Immersive hero block with bold copy and CTA.", "Instant clarity", "High"),
            _feature("f2", "Credibility Rail", "Testimonials + badges carousel for trust.", "Proof boost", "High"),
            _feature("f3", "Conversion CTA Grid", "Modular CTAs for booking, demo, or contact.", "Drives action", "High"),
            _feature("f4", "Story Highlights", "Scrolling cards to tell the brand story.", "Emotional hook", "Medium"),
            _feature("f5", "Insight Dashboard", "Analytics-ready section for metrics snapshots.", "Shows value", "Medium"),
            _feature("f6", "Content Hub", "Filterable articles/resources area.", "Organic traffic", "Medium"),
            _feature("f7", "Support Footer", "Smart footer with FAQs and live support links.", "Reduces friction", "Low"),
        ]

        business_lower = business_type.lower()
        if "ecommerce" in business_lower or "store" in business_lower:
            base_features.extend(
                [
                    _feature("f8", "Shoppable Showcase", "Lifestyle gallery with quick-add cards.", "Boosts AOV", "High"),
                    _feature("f9", "Smart Cart Drawer", "Sticky cart with upsell logic.", "Conversion lift", "High"),
                ]
            )
        elif "blog" in business_lower or "publication" in business_lower:
            base_features.extend(
                [
                    _feature("f8", "Editorial Calendar", "CMS-ready planner for recurring drops.", "Consistency", "Medium"),
                    _feature("f9", "Subscriber Magnet", "Lead capture with gated newsletter perks.", "Audience growth", "High"),
                ]
            )
        elif "portfolio" in business_lower or "agency" in business_lower:
            base_features.extend(
                [
                    _feature("f8", "Case Study Builder", "Modular layouts for outcomes + metrics.", "Showcases prowess", "High"),
                    _feature("f9", "Capabilities Matrix", "Interactive list of services + tooling.", "Clarifies offer", "Medium"),
                ]
            )
        elif "saas" in business_lower or "product" in business_lower:
            base_features.extend(
                [
                    _feature("f8", "Interactive Demo", "Guided product tour with hotspots.", "Self-serve proof", "High"),
                    _feature("f9", "Pricing Composer", "Tier cards with comparison toggles.", "Decision clarity", "High"),
                ]
            )

        return base_features


# Global instance
groq_service = GroqService()
