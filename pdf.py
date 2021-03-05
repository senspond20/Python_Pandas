# import pdfkit
# import os

# os.chdir(r'C:\temp')

# options = {'quiet': ''}    
# config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# url = 'http://www.naver.com'

# pdfkit.from_url(url, 'naver.pdf', options=options, configuration=config)

import pdfcrowd
import sys

try:
   client = pdfcrowd.HtmlToPdfClient('demo','ce543');
   output_file = open('leo_bb.pdf','wb')

   pdf = client.covertUrl('https://leo-bb.tistory.com/')

   output_file.write(pdf)
   output_file.close()
except pdfcrowd.Error as why:
