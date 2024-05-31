import os
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
  return extract_text(pdf_path)


def convert_to_markdown(text):
  lines = text.split("\\\\n")
  for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.isupper() and len(stripped) < 50:
      lines[i] = f"## {stripped}"
  return "\\\\n".join(lines)


pdf_path = "introduction_to_openai_models.pdf"
# Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Convert extracted text to markdown
markdown_text = convert_to_markdown(extracted_text)

markdown_path = "introduction_to_openai_models.md"

# Save the markdown text
with open(markdown_path, "w") as md_file:
  md_file.write(markdown_text)

print(f"Processed {pdf_path} and saved Markdown to {markdown_path}")
