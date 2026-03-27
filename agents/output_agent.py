def generate_outputs(text):
    print("📄 Generating outputs...\n")

    blog = f"📝 Blog Version:\n{text}"
    email = f"📧 Email Version:\n{text}"
    social = f"📱 Social Post:\n{text[:50]}..."

    return blog, email, social