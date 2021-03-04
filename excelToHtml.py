import pandas as pd

dataSet = pd.read_excel('data/test.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dataSet, columns=["일자","언론사", "제목","원본주소"])
# print(df)
html = df.to_html(
        index=False, 
        classes="table", 
        justify="center")
# print(html)

f = open('layout.html','r', encoding='utf-8')
layout = f.read()
f.close()

# print(layout)

render = layout.replace("{{content}}", html)
# print(render)

f = open('output.html', 'w',encoding='utf-8')
f.write(render)
f.close()
# print(fd)
