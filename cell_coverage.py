from pathlib import Path
import pandas as pd


this_dir = Path(__file__).resolve().parent 

df = pd.read_excel("xl/stores.xlsx",
                   sheet_name="2019", skiprows=1, usecols="B:F")
df.info()

# 열 위치 지정
loc_to_go = 1
loc = 3

# 열 나누기
col1 = df.columns[:loc_to_go].to_list()
col2 = df.columns[loc_to_go:loc].to_list()
col_to_go = df.columns[loc:(loc+1)].to_list()
col3 = df.columns[(loc+1):].to_list()

# 테이블 다시 만들기 
new_col = col1 + col_to_go + col2 + col3 
print(new_col)
df = df[new_col]

df.to_excel(this_dir / "cell_coverage_after_lineup.xlsx", index=False)