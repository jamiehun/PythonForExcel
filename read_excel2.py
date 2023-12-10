""" PART 1 
    판다스 셀 범위 지정     
"""
import pandas as pd

df = pd.read_excel("xl/stores.xlsx", sheet_name="2019", skiprows=1, usecols="B:F")

print(df)
df.info()


""" PART 2
    특정 열 object -> bool 
    (람다 표현식 활용)
"""
def fix_missing(x):
    return False if x in ["", "MISSING"] else x 

df = pd.read_excel("xl/stores.xlsx", sheet_name="2019", skiprows=1, usecols="B:F", converters={"Flagship" : fix_missing})

print("*" * 50)
print(df)


""" PART 3
    시트 이름 리스트도 인자로 받음
    (sheet_name=None은 모든 시트)    
"""
sheets = pd.read_excel("xl/stores.xlsx", sheet_name=["2019", "2020"],
                       skiprows=1, usecols=["Store", "Employees"])
print("*" * 50)
print(sheets["2019"].head(2))


""" PART 4
    sheet_name은 시트 인덱스를 받을 수도 있음
"""
df = pd.read_excel("xl/stores.xlsx", sheet_name=1,
                    skiprows=2, skipfooter=3,
                    usecols="B:C,F", header=None,
                    names=["Branch", "Employee_Count", "Is_Flagship"])
print("*" * 50)
print(df)

