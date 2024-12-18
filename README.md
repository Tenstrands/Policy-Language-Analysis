# Project Setup and Data Processing Guide

## 1. Pull the GitHub Repository

Clone the GitHub repository to your local machine

```bash
git clone <repository_url>
```

Navigate to the project directory:

```bash
cd <repository_name>
```

## 2. Organize Data

Inside the `data` folder, create a new folder with an appropriate name for your policy documents. Use the naming convention `BP_AR_<policy_num>`, where `<policy_num>` corresponds to the policy number.

For example:

```bash
mkdir data/BP_AR_3511
```

## 3. Fill in the Google Sheets

Open the Google Sheets and fill in the appropriate `Path to PDF` columns.

- Column `Path to PDF`: An appropriate name would be similar to `<district_name>_<policy_name>_<BP_or_AR>.pdf`. Note if there are districts with the same name, add the County to the pdf name as well. This allows for easy debugging.

Once you have filled in the columns in the Google Sheets:

1. Download the Google Sheets as an Excel file (`xlsx` format).
2. Save the downloaded file into the `data` folder you created in step 2.

## 4. Prepare the Extraction and Cleaning Notebook

In the `extraction_and_cleaning_notebooks` folder, make a copy of the template notebook provided. Rename the copied notebook appropriately.

For example:

```bash
cp extraction_and_cleaning_notebooks/template.ipynb extraction_and_cleaning_notebooks/BP_AR_3511_extraction_and_cleaning.ipynb
```

## 5. Perform Extraction and Cleaning

Open the newly copied notebook in your preferred Jupyter notebook interface.

Follow the steps in the notebook to perform the extraction and cleaning of the policy data. Ensure that all cells are executed, and any necessary adjustments are made to the extraction and cleaning logic.

## 6. Save Cleaned Data

After completing the extraction and cleaning process, save the cleaned data as a CSV file in the `cleaned_data` folder.

For example, in your notebook, you can save the cleaned DataFrame like this:

```python
cleaned_data.to_csv('../cleaned_data/BP_AR_3511_cleaned.csv', index=False)
```

Make sure to verify that the CSV file is saved correctly in the `cleaned_data` folder.
