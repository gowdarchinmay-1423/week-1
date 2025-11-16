import streamlit as st
import docx  # Extract text from Word file
import PyPDF2  # Extract text from PDF

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to extract text from TXT
def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text

# Handle file upload
def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        text = extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    return text

# Streamlit app
def main():
    st.set_page_config(page_title="Resume Upload - Week 1", layout="wide")
    st.title("Resume Upload - Week 1")
    st.markdown("Upload a resume in PDF, DOCX, or TXT format and see the extracted text.")

    uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.success("Text successfully extracted!")
            st.text_area("Extracted Resume Text", resume_text, height=300)
        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")

if __name__ == "__main__":
    main()
