import pandas as pd

dataSet = pd.read_excel('data/test.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dataSet, columns=["일자","언론사", "제목","원본주소"])
print(df)
html = df.to_html(
        index=False, 
        classes="table", 
        border="none", 
        justify="center")
print(html)
# print(fd)
