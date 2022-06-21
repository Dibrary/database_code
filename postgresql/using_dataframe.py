
from connect import cur, conn
import pandas as pd

df = pd.read_sql('select * from users', conn)

print("끝")
print(df)

df.to_json(orient='records') # json 형식으로 출력.


