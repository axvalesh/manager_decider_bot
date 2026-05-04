import json
from typing import List

from google import genai

from schemas.manager import ManagerBase
from schemas.form import FormSubmission
from core.config import settings

CHAT_MODEL = "gemini-2.5-flash-lite"


class AIService:
    def __init__(self):
        api_key = settings.GEMINI_API_KEY

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")

        self.model = genai.Client(api_key=api_key)


    async def choose_manager(
        self,
        student: FormSubmission,
        managers: List[ManagerBase]
    ) -> dict:

        managers_list = self._format_managers(managers)

        prompt = self._build_prompt(
            managers_list=managers_list,
            student_name=student.name,
            student_level=student.current_english_level,
            student_goal=student.goal
        )

        response = self.model.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=prompt
        )

        raw_text = response.text.strip()

        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(raw_text)
        except Exception:
            return {
                "error": "Invalid JSON from AI",
                "raw_response": raw_text
            }

    def _format_managers(self, managers: List[ManagerBase]) -> str:
        lines = []

        for manager in managers:
            lines.append(
                f"""
                    ID: {manager.telegram_id}
                    Name: {manager.name}
                    Telegram ID: {manager.telegram_id}
                    Level: {manager.level}
                    Specialization: {manager.specialization}
                    """.strip()
            )

        return "\n\n".join(lines)

    def _build_prompt(
        self,
        managers_list: str,
        student_name: str,
        student_level: str,
        student_goal: str
    ) -> str:

        return f"""
    You are an intelligent assistant for the "SchoolTest" online school.
    Your task is to analyze a student's application and assign the most suitable manager.

    Available Managers List:
    {managers_list}

    Student Data:

    Telegram Name: {student_name}
    Current English Level: {student_level}
    Goal: {student_goal}

    Output Requirements:
    Return ONLY valid JSON.

    JSON example:

    {{
    "manager_id": "ID number",
    "manager_name": "Name",
    "manager_telegram_id": "Telegram ID",
    "reason": "Why selected",
    "welcome_message": "Hi {student_name}! I'm [Manager Name], and I'd be happy to help you with {student_goal}.",
    "student_details": {{
        "name": "{student_name}",
        "level": "{student_level}",
        "goal": "{student_goal}"
    }}
    }}
    """.strip()


ai_service = AIService()