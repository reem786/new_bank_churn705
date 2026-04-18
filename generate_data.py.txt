import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)
num_records = 10000

data = {
    'CustomerId': range(15600000, 15600000 + num_records),
    'Surname': ['Surname_' + str(i) for i in range(num_records)],
    'CreditScore': np.random.randint(350, 850, size=num_records),
    'Geography': np.random.choice(['France', 'Germany', 'Spain'], size=num_records, p=[0.5, 0.25, 0.25]),
    'Gender': np.random.choice(['Male', 'Female'], size=num_records),
    'Age': np.random.randint(18, 92, size=num_records),
    'Tenure': np.random.randint(0, 11, size=num_records),
    'Balance': np.random.uniform(0, 250000, size=num_records),
    'NumOfProducts': np.random.randint(1, 5, size=num_records),
    'HasCrCard': np.random.choice([0, 1], size=num_records),
    'IsActiveMember': np.random.choice([0, 1], size=num_records),
    'EstimatedSalary': np.random.uniform(10000, 200000, size=num_records),
    'Exited': np.random.choice([0, 1], size=num_records, p=[0.8, 0.2]) # 20% churn
}

# Create DataFrame and save
df = pd.DataFrame(data)
df.to_csv('churn_data.csv', index=False)
print("✅ Success! 'churn_data.csv' has been generated with 10,000 records.")