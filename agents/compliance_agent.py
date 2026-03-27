def check_compliance(text):
    print("🛡️ Checking brand and compliance rules...")
    
    if "bad" in text:
        return "⚠️ Content needs review"
    
    return "✅ Content is compliant"