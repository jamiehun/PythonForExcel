"""rglob(globbing)을 통해 서브디렉터리 전체에서 일치하는 파일 찾아 데이터 변환"""

from pathlib import Path
import pandas as pd 

# 이 파일의 디렉터리 
this_dir = Path(__file__).resolve().parent 

# sales_data의 서브디렉터리에 있는 엑셀파일을 모두 읽음
parts = []
for path in (this_dir / "sales_data").rglob("*.xls*"):
    print(f'Reading {path.name}')
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)

# 각 파일의 데이터프레임을 하나로 조합
# 열 정렬은 판다스가 알아서 함
df = pd.concat(parts)

# 피벗 사용하여 각 대리점을 열 하나로 모으고 일별 거래량을 합산
pivot = pd.pivot_table(df, 
                       index="transaction_date", columns="store",
                       values="amount", aggfunc="sum")
                       

# 월말로 리샘플링을 적용하고 인덱스 이름을 할당
summary = pivot.resample("M").sum()
summary.index.name = "Month"

# 요약 보고서를 엑셀파일로 만듦
summary.to_excel(this_dir / "sales_report_pandas.xlsx")