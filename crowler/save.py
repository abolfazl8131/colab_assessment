import pandas as pd
def save_companies_name():
    company_name = 'company_name.csv'
    filename = 'company.json'

    df = pd.read_json(filename)
    df.to_csv(company_name, index=True)

save_companies_name()