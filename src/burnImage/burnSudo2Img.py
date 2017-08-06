import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from random import randint
import shutil


def CreateSudoImg(A,sourceimg,destination):   #Adds new Sudoku problem as png image to the desirable folder
    font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 18)
    #img=Image.open("/home/tolis/Code-All/BurnYourPc/Sudoku/src/burnImage/image.png")
    img=Image.open(sourceimg+"/image.png")
    draw = ImageDraw.Draw(img)
    for i in range(9):
        for j in range(9):
            if (A[i,j]!=0):
                draw.text((j*25+8,i*25+3), str(A[i,j]),font=font,fill=2)
                draw = ImageDraw.Draw(img)
       
    file_list = os.listdir(destination)
    file_count = len(file_list)+1
    
    #if (sym):
    if (file_count>9):
        imgname="/Prob"+str(file_count)+".png"
    else:
        imgname="/Prob"+str(0)+str(file_count)+".png"
    #else:
    #    if (file_count>9):
    #        imgname="/NonSymProb"+str(file_count)+".png"
    #    else:
    #        imgname="/NonSymProb"+str(0)+str(file_count)+".png"
    
    img.save(destination+imgname)
        
        


def CreateSudoPdf(num,path,sym,source,destination):
    if (sym):
        prob="/SymProb"
    else:
        prob="/NonSymProb"
    prob1=prob
    patharray=[]
    file_list = os.listdir(path)
    file_count = len(file_list)
    count_pages=0
    for i in range(num):
        if ((i+1)%6==1):
            count_pages=count_pages+1
        pick=randint(1, file_count)
        if (pick<10):
            prob=prob+str(0)+str(pick)+".png"
        else:
            prob=prob+str(pick)+".png"
        path2png=path+prob
        patharray.append(path2png)
        prob=prob1
        if (len(patharray)==6 or i==num-1):
            BurnSudoOnPdf(patharray,count_pages)
            patharray=[]
      
    output = PdfFileWriter()
    for i in range(count_pages):
        append_pdf(PdfFileReader(open("output"+str(i+1)+".pdf","rb")),output)
    
    file_list = os.listdir(destination)
    file_count = len(file_list)+1
    name="SudokuProblems"+str(file_count)+".pdf"
    output.write(open(name,"wb"))
    
    for i in range(count_pages):
        os.remove(os.path.join(source, "output"+str(i+1)+".pdf"))
    
    shutil.move(source+"/"+name, destination)


def BurnSudoOnPdf(path,numpage):
 
    pdf = PdfFileWriter()

    # Using ReportLab Canvas to insert image into PDF
    imgTemp = BytesIO()
    imgDoc = canvas.Canvas(imgTemp, pagesize=A4)
    
    # Draw image on Canvas and save PDF in buffer
    for i in range(len(path)):
        if ((i+1)%2==0):
            x=345
        else:
            x=55
        if (i<2):
            y=590
        elif (i<4):
            y=320
        else:
            y=50
        imgDoc.drawImage(path[i], x, y,200,200)
    
    
    #imgDoc.drawImage(path[0], 55, 590,200,200)
    #imgDoc.drawImage(path[1], 345, 590,200,200)
    #imgDoc.drawImage(path[2], 55, 320,200,200)
    #imgDoc.drawImage(path[3], 345, 320,200,200)
    #imgDoc.drawImage(path[4], 55, 50,200,200)
    #imgDoc.drawImage(path[5], 345, 50,200,200)
    
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    #pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    
    imgDoc.setFont('Vera', 13)
    imgDoc.drawString(30,820,"BurnYourPc Organization/")
    imgDoc.setFont('VeraBd', 9)
    imgDoc.drawString(197,820,"Sudoku Project")
    imgDoc.setFont('VeraIt', 8)
    imgDoc.drawString(430,20,"By PantelisPanka, nikfot, TolisChal")
    imgDoc.setFont('Vera', 8)
    imgDoc.drawString(550,820,str(numpage))
    
    imgDoc.save()
    
    # Use PyPDF to merge the image-PDF into the template
    pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))

    pdf.write(open("output"+ str(numpage)+".pdf","wb"))


def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


