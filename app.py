from agents.ocr_agent import extract_text
from agents.content_agent import enhance_content
from agents.optimization_agent import optimize_content
from agents.output_agent import generate_outputs
from utils.file_handler import read_file
from utils.text_processor import clean_text

def main():
    print("🚀 AI Content Automation System\n")

    file = input("Enter file name: ")

    raw_data = read_file(file)
    text = extract_text(raw_data)
    text = clean_text(text)
    text = enhance_content(text)
    text = optimize_content(text)

    blog, email, social = generate_outputs(text)

    print("\n✅ OUTPUTS:\n")
    print(blog)
    print("\n" + email)
    print("\n" + social)

if __name__ == "__main__":
    main()