import pandas as pd
from pathlib import Path

csv_file_path = Path("data/input/sample_dataset.csv")
output_dir = Path("data/output")
output_file = output_dir / f"result.xlsx"

data = {'Name': ['John', 'Jane', 'Bob', 'Mary'],
        'Age': [25, 30, 20, 35],
        'Salary': [50000, 60000, 45000, 70000]}

df = pd.DataFrame(data)

def highlight_salary(s):
    '''
    Highlight cells in Salary column with values above 50000
    '''
    is_above_threshold = s > 50000
    return ['background-color: yellow' if v else '' for v in is_above_threshold]

df.style.apply(highlight_salary, subset=['Salary'])

def highlight_negative(s):
    '''
    Highlight cells with negative values
    '''
    is_negative = s < 0
    return ['background-color: red' if v else '' for v in is_negative]

df.style.apply(highlight_negative)

# Save to Excel
df.style.apply(highlight_salary, subset=['Salary']).to_excel(output_file, index=False)
