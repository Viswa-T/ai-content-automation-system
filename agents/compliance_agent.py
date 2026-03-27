def check_compliance(text):
    
    if "bad" in text:
        return "⚠️ Content needs review"
    
    return "✅ Content is compliant"