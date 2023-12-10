""" ExcelFile Class
    1. 구형 xls 형식에서 시트 여러개 읽을 때 사용
    2. 판다스가 파일 전체를 여러번 읽는 경우가 없어 빠름
"""
import pandas as pd

with pd.ExcelFile("xl/stores.xls") as f:
    df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
    df2 = pd.read_excel(f, "2020", skiprows=2, usecols="B:F", nrows=2)

print(df1)


""" 
    3. 시트의 이름 반환
"""
stores = pd.ExcelFile("xl/stores.xlsx")
print("*" * 50)
print(stores.sheet_names)


"""
    4. 엑셀파일을 URL에서 읽기     
"""
url = ("https://github.com/jamiehun/PythonForExcel/blob/main/xl/stores.xls")
print("*" * 50)
pd.read_excel(url, skiprows=1, usecols="B:E", nrows=2)