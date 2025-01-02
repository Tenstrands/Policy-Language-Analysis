import fitz
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    '''Function to extract text from PDF'''
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        if text.strip() == "":
            text = extract_text_with_ocr(pdf_path)
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None
    
def extract_text_with_ocr(pdf_path):
    '''Function to extract text from an image-based PDF using OCR'''
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing {pdf_path} with OCR: {e}")
        return None
    
def extract_and_update_pdf_texts(policy_pdfs, path_column, text_column):
    """
    Extracts text from PDFs whose paths are specified and updates the 'PDF Text' column 
    if the text is missing and the path to PDF is not null.
    
    Parameters:
    - policy_pdfs (pd.DataFrame): DataFrame containing 'Path to PDF' and 'PDF Text' columns.
    - path_column (str): name of the column that contains pdfs to read.
    - text_column (str): name of the column to extract text into.
    
    Returns:
    - pd.DataFrame: Updated DataFrame with extracted text in 'PDF Text' column where applicable.
    """
    # filter rows where the respective 'Path to PDF' is not null and 'PDF Text' is null
    filtered_policy_pdfs = policy_pdfs[policy_pdfs[path_column].notna() & policy_pdfs[text_column].isna()]
    
    # iteratte through the filtered DataFrame and extract text
    for index, row in filtered_policy_pdfs.iterrows():
        pdf_path = row[path_column]
        text = extract_text_from_pdf(pdf_path)
        if text:
            policy_pdfs.at[index, text_column] = text
    
    return policy_pdfs

def check_and_report_missing_texts(policy_pdfs, policy_name_column, path_column, text_column):
    """
    Checks if all rows with a specific column value and non-null PDF paths have text extracted,
    and reports any rows that are missing text.
    
    Parameters:
    - policy_pdfs (pd.DataFrame): DataFrame containing 'Path to PDF' and 'PDF Text' columns.
    - policy_name_column (str): The column name to check for a specific value (e.g., 'BP: 6142.5 Environmental Education').
    - path_column (str): name of the column that contains pdfs to read.
    - text_column (str): name of the column to extract text into.
    
    """
    # fitler rows where the specified column has a value of 1 and 'Path to PDF' is not null
    check_df = policy_pdfs[(policy_pdfs[policy_name_column] == 1) & (policy_pdfs[path_column].notna())]
    
    # check for rows where 'PDF Text' is null
    missing_texts = check_df[check_df[text_column].isna()][path_column]
    
    if missing_texts.empty:
        print("All relevant rows have text extracted.")
    else:
        print("Some rows are missing text:")
        print(missing_texts)