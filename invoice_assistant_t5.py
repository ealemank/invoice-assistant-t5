import os
import pandas as pd
from transformers import T5ForConditionalGeneration, T5Tokenizer

def extract_invoice_data(text):
    # Load the T5 model and tokenizer
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Define a prompt for the model
    prompt = f"Extract the following fields from the invoice text:\n{text}"

    # Tokenize and generate output
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output_ids = model.generate(input_ids)

    # Decode the generated output
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Split the generated text into lines
    lines = generated_text.split('\n')

    # Extract data from the generated lines
    extracted_data = {}
    for line in lines:
        field, value = line.split(':')
        extracted_data[field.strip()] = value.strip()

    return extracted_data

def process_invoices(directory_path):
    # Initialize a list to store extracted data for all invoices
    all_invoices_data = []

    # Loop through each file in the specified directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)

            # Read the content of the file
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Extract data from the invoice
            invoice_data = extract_invoice_data(file_content)

            # Add the extracted data to the list
            all_invoices_data.append(invoice_data)

    return all_invoices_data

def export_to_csv(data, csv_filename='invoices_data.csv'):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Export DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)
    print(f'Data exported to {csv_filename}')

if __name__ == "__main__":
    # Specify the directory path containing invoice text files
    invoices_directory = '/path/to/invoices'

    # Process invoices and extract data
    all_invoices_data = process_invoices(invoices_directory)

    # Export the extracted data to a CSV file
    export_to_csv(all_invoices_data)
