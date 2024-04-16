# PyMuPDF library for PDF handling
import fitz

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to preprocess text (convert to lowercase, remove punctuation, etc.)
def preprocess_text(text):
    processed_text = text.lower()  # Convert text to lowercase
    # Add more preprocessing steps as needed (e.g., removing punctuation, stopwords, etc.)
    return processed_text

# Function to calculate plagiarism percentage
def calculate_plagiarism_percentage(text):
    words = text.split()
    unique_words = set(words)
    
    # If there are no unique words (i.e., no words in the document), return 0% plagiarism
    if len(unique_words) == 0:
        return 0
    
    # Calculate plagiarism percentage (assuming repeated words indicate plagiarism)
    plagiarism_percentage = 100 * (len(words) - len(unique_words)) / len(words)
    return plagiarism_percentage

# Path to the PDF file
pdf_file = 'filepath.pdf'

# Extract text from PDF file
text = extract_text_from_pdf(pdf_file)

# Preprocess text
processed_text = preprocess_text(text)

# Calculate plagiarism percentage
plagiarism_percentage = calculate_plagiarism_percentage(processed_text)

# Display plagiarism percentage
print(f"The plagiarism percentage within the PDF file is: {plagiarism_percentage:.2f}%")
