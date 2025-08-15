import pandas as pd
import time

# Function to simulate automated data entry
def auto_data_entry(data):
    for i, row in data.iterrows():
        print(f"Entering row {i+1}: {row.to_dict()}")
        time.sleep(1)  # Simulate time for entry
    print("✅ All data has been entered successfully!")

# Load sample data
def load_sample_data():
    data = {
        "Name": ["Ahmed", "Mona", "Karim"],
        "Email": ["ahmed@mail.com", "mona@mail.com", "karim@mail.com"],
        "Age": [29, 34, 41]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = load_sample_data()
    auto_data_entry(df)
