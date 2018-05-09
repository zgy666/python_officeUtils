import os
import PyPDF2

pdfFiles = []
path = '/Users/zhouguangyue/Desktop/caiwu/'

for fileName in os.listdir(path):
    if fileName.endswith('.pdf'):
        pdfFiles.append(fileName)

print("files", pdfFiles)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for fileName in pdfFiles:
    pdfFileObj = open(path + fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #从第一个开始合并
    for pageNum in range(0, pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


pdfOutput = open(path + 'hebing.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
