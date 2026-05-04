
def handle_info_to_send(ai_result: dict):
    manager_name = ai_result["manager_name"]
    manager_telegram_id = int(ai_result["manager_telegram_id"])
    reason = ai_result["reason"]
    welcome_message = ai_result["welcome_message"]

    student = ai_result["student_details"]

    student_name = student["name"]
    student_level = student["level"]
    student_goal = student["goal"]

    message = f"""
🚀 <b>New Student Lead Assigned!</b>

Hi {manager_name}, you have been chosen as the manager for this student.

<b>Reason:</b>
<i>{reason}</i>

📌 <b>Student Details:</b>
• <b>Name:</b> {student_name}
• <b>Level:</b> <code>{student_level}</code>
• <b>Goal:</b> {student_goal}

📝 <b>Suggested Welcome Message:</b>
<code>{welcome_message}</code>

✅ <i>Please contact the student as soon as possible.</i>
""".strip()

    return manager_telegram_id, message