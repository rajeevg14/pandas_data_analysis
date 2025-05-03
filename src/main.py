import pandas as pd
from pathlib import Path

master_file_path = Path("data/input/Master Data.xlsx")
transaction_file_path = Path("data/input/Transaction Data.xlsx")

# Read from the first sheet
master_df = pd.read_excel(master_file_path)
transaction_df = pd.read_excel(transaction_file_path)

print(master_df)
print(transaction_df)

'''
Compare Transaction DF with Master DF and Style the cells in Transaction DF in red which do not match Master DF and store with color in EXcel
'''