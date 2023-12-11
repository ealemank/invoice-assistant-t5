import unittest
import os
from invoice_assistant_t5 import process_invoices, export_to_csv

class TestInvoiceAssistant(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create test data files
        self.create_test_files()

    def tearDown(self):
        # Remove the temporary directory and its contents
        os.rmdir(self.test_dir)

    def create_test_files(self):
        # Use the CreateTestData script to generate test files
        os.system("python CreateTestData.py")

    def test_process_invoices(self):
        # Test if the application correctly processes invoices
        all_invoices_data = process_invoices(self.test_dir)

        # Check if data is extracted for each invoice
        self.assertEqual(len(all_invoices_data), 5)

        # Check if the required fields are present in the extracted data
        for invoice_data in all_invoices_data:
            self.assertIn('Total Amount', invoice_data)
            self.assertIn('Hourly Rate', invoice_data)
            self.assertIn('Invoice Number', invoice_data)
            self.assertIn('Project Name', invoice_data)
            self.assertIn('Due Date', invoice_data)
            self.assertIn('Sales Representative', invoice_data)

    def test_export_to_csv(self):
        # Test if the application correctly exports data to CSV
        all_invoices_data = process_invoices(self.test_dir)
        csv_filename = "test_invoices_data.csv"

        # Export the extracted data to a CSV file
        export_to_csv(all_invoices_data, csv_filename)

        # Check if the CSV file is created
        self.assertTrue(os.path.exists(csv_filename))

        # Check if the CSV file contains the correct number of rows
        df = pd.read_csv(csv_filename)
        self.assertEqual(len(df), 5)

        # Check if the required columns are present in the CSV file
        expected_columns = ['Total Amount', 'Hourly Rate', 'Invoice Number', 'Project Name', 'Due Date', 'Sales Representative']
        self.assertListEqual(list(df.columns), expected_columns)

if __name__ == "__main__":
    unittest.main()
