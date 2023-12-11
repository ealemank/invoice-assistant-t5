import os
import random
from datetime import datetime, timedelta

def generate_test_data():
    customers = ["John Doe", "Alice Smith", "Bob Johnson", "Emma Brown", "David Wilson"]
    project_names = ["Website Redesign", "Marketing Campaign", "Product Development", "Event Planning", "Consulting Services"]
    sales_representatives = ["Sarah Miller", "Chris Thompson", "Emily Davis", "Michael White", "Jessica Turner"]

    test_data = []

    for i in range(1, 6):
        customer_name = random.choice(customers)
        project_name = random.choice(project_names)
        invoice_number = f"INV{i}2023"
        total_amount = round(random.uniform(1000, 5000), 2)
        hourly_rate = round(random.uniform(50, 150), 2)
        due_date = (datetime.now() + timedelta(days=random.randint(10, 30))).strftime("%Y-%m-%d")
        sales_rep = random.choice(sales_representatives)

        invoice_content = f"Hi {customer_name},\n" \
                          f"I hope you are doing well. I have an invoice for {project_name} with ID {invoice_number} " \
                          f"for ${total_amount} dollars with a rate of ${hourly_rate}.\n" \
                          f"This payment is due on {due_date}. Please don’t hesitate to reach out in case of any questions.\n" \
                          f"Regards,\n{sales_rep}"

        # Save the content to a text file
        file_name = f"invoice_{i}.txt"
        with open(file_name, 'w') as file:
            file.write(invoice_content)

        test_data.append({
            'Customer Name': customer_name,
            'Project Name': project_name,
            'Invoice Number': invoice_number,
            'Total Amount': total_amount,
            'Hourly Rate': hourly_rate,
            'Due Date': due_date,
            'Sales Representative': sales_rep
        })

    return test_data

if __name__ == "__main__":
    # Create test data
    test_data = generate_test_data()

    print("Test data created successfully.")
