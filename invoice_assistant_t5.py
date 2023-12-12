import os
import pandas as pd
from mlc_chat import ChatModule
from mlc_chat.callback import StreamToStdout

data_points = ["Total amount", 
               "Hourly Rate",
               "Invoice number",
               "Project name",
               "Due date",
               "Sales Representative"]
args = tuple(data_points)
data_points_str = '''
  - {0}
  - {1}
  - {2}
  - {3}
  - {4}
  - {5}
'''.format(*args)

MODEL_NAME = os.getenv('LLAMA_MODEL_NAME', "Llama-2-7b-chat-hf-q4f16_1")

def extract_invoice_data(text):
    # load model
    cm = ChatModule(model=f"{MODEL_NAME}")
  
    # Define a prompt for the model
    prompt = f"Analyze the following invoice email and capture the following data points.  print the data points in json format:{data_points_str}\n\n{text}"
    print(prompt)

    output = cm.generate(prompt=prompt)
    print(output)
    # Split the generated text into lines
    lines = output.split('\n')
    print(lines)

    # Extract data from the generated lines
    extracted_data = {}
    for line in lines:
        if any(substring.lower() in line.lower() for substring in data_points):
          field, value = line.split(':')
          extracted_data[field.strip()] = value.strip()

    print(extracted_data)
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
    invoices_directory = './invoices'

    # Process invoices and extract data
    all_invoices_data = process_invoices(invoices_directory)

    # Export the extracted data to a CSV file
    export_to_csv(all_invoices_data)
