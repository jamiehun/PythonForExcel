""" PART 1.
    Python File to Excel
"""

import numpy as np
import pandas as pd
import datetime as dt

data = [[dt.datetime(2020, 1, 1, 10, 13), 2.222, 1, True],
        [dt.datetime(2020, 1, 2), np.nan, 2, False],
        [dt.datetime(2020, 1, 2), np.inf, 3, True]]

df = pd.DataFrame(data=data, columns=["Dates", "Floats", "Integers", "Booleans"])
df.index.name="index"
print(df)

# 엑셀 파일로 만들기
df.to_excel("practice/written_with_pandas.xlsx", sheet_name="Output",
            startrow=1, startcol=1, index=True, header=True,
            na_rep="<NA>", inf_rep="<INF>")


""" PART 2.
    데이터프레임이 여러개라면 ExcelWriter 클래스를 사용
"""