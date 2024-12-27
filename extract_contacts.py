import PyPDF2
import pandas as pd

def extract_contacts_from_pdf(file_path):
    contacts = []
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                if '@' in line:  
                    parts = line.split()
                    email = [part for part in parts if '@' in part][0]
                    name = " ".join(parts[:parts.index(email)])  # Name appears before email
                    contacts.append({'Name': name, 'Email': email})
    return contacts

if __name__ == "__main__":
    input_pdf = "CompanyWise HR contact (1).pdf"
    contacts = extract_contacts_from_pdf(input_pdf)
    df_contacts = pd.DataFrame(contacts)
    df_contacts.to_csv("contacts.csv", index=False)
    print("Contacts saved to contacts.csv")
