from docx import Document 
from googletrans import Translator
import streamlit as st

def main():
    st.title("DOCX Translation App")
    target_lang = st.selectbox("Select Target Language", ["ta", "bn", "es", "fr", "de"])
    # Upload DOCX file
    docx_file = st.file_uploader("Upload a DOCX file", type=["docx"])
    
    
    if docx_file:
        doc = Document(docx_file)
        extracted_text = ""
        for paragraph in doc.paragraphs:
            extracted_text += paragraph.text + "\n"
        
        chunk_size = 500  # Adjust as needed
        chunks = [extracted_text[i:i + chunk_size] for i in range(0, len(extracted_text), chunk_size)]
        
        translator = Translator()
        translated_chunks = []
        
        for chunk in chunks:
            translation = translator.translate(chunk, dest=target_lang)
            translated_chunks.append(translation.text)
        
        translated_text = "\n".join(translated_chunks)
        
        st.subheader("Extracted Text")
        st.text(extracted_text)
        
        st.subheader("Translated Text")
        st.text(translated_text)
        download_button = st.download_button(
            label="Download Translated Text (DOCX)",
            data=translated_text.encode("utf-8"),
            file_name="translated_text.docx",
            key="download_btn"
        )

if __name__ == "__main__":
    main()
