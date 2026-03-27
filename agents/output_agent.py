def generate_outputs(text):

    # Blog (detailed + structured)
    blog = f"""📝 Blog Version:

{text}

📌 Key Insight:
This content highlights important ideas and provides a structured explanation for better understanding.

✨ Conclusion:
AI-powered automation helps transform raw data into meaningful content efficiently.
"""

    # Email (clean + professional)
    email = f"""📧 Email Version:

Subject: Content Update

Hi,

{text}

Please review the above content and share your feedback.

Regards,  
AI Content Team
"""

    # Social (short + clean + no broken words)
    words = text.split()
    short_text = " ".join(words[:6])  # safer than slicing characters

    social = f"""📱 Social Post:

🚀 {short_text}...

#AI #Automation #Innovation
"""

    return blog, email, social