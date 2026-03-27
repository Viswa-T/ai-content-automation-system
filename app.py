from agents.ocr_agent import extract_text
from agents.content_agent import enhance_content
from agents.optimization_agent import optimize_content
from agents.output_agent import generate_outputs
from agents.compliance_agent import check_compliance
from agents.insight_agent import generate_insights

from utils.file_handler import read_file
from utils.text_processor import clean_text

import time 

def main():
    print("\n🚀 AI Content Automation System\n")

    file = input("Enter file name: ")

    print("\n🔄 Starting AI Pipeline...\n")

    print("📂 Reading file...")
    time.sleep(0.8)
    raw_data = read_file(file)

    print("🔍 OCR processing...")
    time.sleep(0.8)
    text = extract_text(raw_data)

    print("🧹 Cleaning text...")
    time.sleep(0.8)
    text = clean_text(text)

    print("✍️ Enhancing content...")
    time.sleep(0.8)
    text = enhance_content(text)

    print("⚙️ Optimizing content...")
    time.sleep(0.8)
    text = optimize_content(text)

    print("🛡️ Checking compliance...")
    time.sleep(0.8)
    compliance = check_compliance(text)

    print("📄 Generating outputs...")
    time.sleep(1)
    blog, email, social = generate_outputs(text)

    print("📊 Generating insights...")
    time.sleep(0.8)
    insights = generate_insights(text)

    # Final Output
    print("\n" + "="*50)
    print("✅ FINAL OUTPUT")
    print("="*50 + "\n")

    print(blog)
    print("\n" + "-"*50 + "\n")
    print(email)
    print("\n" + "-"*50 + "\n")
    print(social)

    print("\n" + "="*50)
    print("🛡️ Compliance Status:")
    print(compliance)

    print("\n📊 Insights:")
    for key, value in insights.items():
        print(f"• {key.replace('_',' ').title()}: {value}")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()