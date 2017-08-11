import os
import PIL
import numpy as np
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
    img=Image.open(sourceimg+"/image.png")
    draw = ImageDraw.Draw(img)
    for i in range(9):
        for j in range(9):
            if (A[i,j]!=0):
                draw.text((j*25+8,i*25+3), str(A[i,j]),font=font,fill=2)
                draw = ImageDraw.Draw(img)
       
    file_list = os.listdir(destination)
    file_count = len(file_list)+1
    
    if (file_count>9):
        imgname="/Prob"+str(file_count)+".png"
    else:
        imgname="/Prob"+str(0)+str(file_count)+".png"
    
    img.save(destination+imgname)
        
        


def CreateSudoPdf(nums,pathConst,source,destination):

    alladd1=True
    alladd2=True
    alladd3=True
    alladd4=True
    alladd5=True
    probConst="/Prob"
    num=sum(nums)
    patharray=[]
    diffarray=[]
    count_pages=0
    allmax=[]
    
    for i in range(5):
        pathTemp=pathConst+getStrPathDiff(i+1)
        file_list = os.listdir(pathTemp)
        file_count = len(file_list)
        allmax.append(file_count)
    
    probPicked1=np.arange(allmax[0])+1
    probPicked2=np.arange(allmax[1])+1
    probPicked3=np.arange(allmax[2])+1
    probPicked4=np.arange(allmax[3])+1
    probPicked5=np.arange(allmax[4])+1
    
    counter=0

    for i in range(num):
        
        diff=getNumDiff(i,nums)
        diffpath=getStrPathDiff(diff)
        path=pathConst+diffpath
        file_list = os.listdir(path)
        file_count = len(file_list)
        
        if (diff==1):
            if (probPicked1.size==0):
                if (alladd1):
                    print("Not so many very Easy Generated! Less were added... Generate more Sudoku!\n")
                alladd1=False
                continue
            
            counter=counter+1
            pickItem=randint(1, probPicked1.size)
            pick=probPicked1[pickItem-1]
            diffarray.append(diff)
            erase=np.array([probPicked1[pickItem-1]])
            probPicked1=np.setdiff1d(probPicked1,erase)
        elif (diff==2):
            if (probPicked2.size==0):
                if (alladd2):
                    print("Not so many Easy Generated! Less were added... Generate more Sudoku!\n")
                alladd2=False
                continue
            counter=counter+1
            pickItem=randint(1, probPicked2.size)
            pick=probPicked2[pickItem-1]
            
            diffarray.append(diff)
            
            erase=np.array([probPicked2[pickItem-1]])
            probPicked2=np.setdiff1d(probPicked2,erase)
        elif (diff==3):
            if (probPicked3.size==0):
                if (alladd3):
                    print("Not so many Medium Generated! Less were added... Generate more Sudoku!\n")
                alladd3=False
                continue
            counter=counter+1
            pickItem=randint(1, probPicked3.size)
            pick=probPicked3[pickItem-1]
            diffarray.append(diff)
            erase=np.array([probPicked3[pickItem-1]])
            probPicked3=np.setdiff1d(probPicked3,erase)
        elif (diff==4):
            if (probPicked4.size==0):
                if (alladd4):
                    print("Not so many Hard Generated! Less were added... Generate more Sudoku!\n")
                alladd4=False
                continue
            counter=counter+1
            pickItem=randint(1, probPicked4.size)
            pick=probPicked4[pickItem-1]
            diffarray.append(diff)
            erase=np.array([probPicked4[pickItem-1]])
            probPicked4=np.setdiff1d(probPicked4,erase)
        else:
            if (probPicked5.size==0):
                if (alladd5):
                    print("Not so many very Hard Generated! Less were added... Generate more Sudoku!\n")
                alladd5=False
                continue
            counter=counter+1
            pickItem=randint(1, probPicked5.size)
            pick=probPicked5[pickItem-1]
            diffarray.append(diff)
            erase=np.array([probPicked5[pickItem-1]])
            probPicked5=np.setdiff1d(probPicked5,erase)
        
        if ((counter)%6==1):
            count_pages=count_pages+1
        
        if (pick<10):
            prob=probConst+str(0)+str(pick)+".png"
        else:
            prob=probConst+str(pick)+".png"
        path=path+prob
        patharray.append(path)
        if (len(patharray)==6 or i==num-1):
            BurnSudoOnPdf(patharray,count_pages,diffarray)
            patharray=[]
            diffarray=[]
      
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


def BurnSudoOnPdf(path,numpage,diffarray):
 
    pdf = PdfFileWriter()

    # Using ReportLab Canvas to insert image into PDF
    imgTemp = BytesIO()
    imgDoc = canvas.Canvas(imgTemp, pagesize=A4)
    
    # Draw image on Canvas and save PDF in buffer
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
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
        imgDoc.setFont('VeraIt', 9)
        imgDoc.drawString(x+2,y+203,getStrDiff(diffarray[i]))
    
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


def getStrDiff(difficulty):
    if (difficulty==1):
        return "very Easy"
    elif (difficulty==2):
        return "Easy"
    elif (difficulty==3):
        return "Medium"
    elif (difficulty==4):
        return "Hard"
    else:
        return "very Hard"
        

def getStrPathDiff(difficulty):
    if (difficulty==1):
        return "VeryEasy"
    elif (difficulty==2):
        return "Easy"
    elif (difficulty==3):
        return "Medium"
    elif (difficulty==4):
        return "Hard"
    else:
        return "VeryHard"


def getNumDiff(n,nums):
    n=n+1
    if (n<=nums[0]):
        return 1
    elif (n<=nums[0]+nums[1]):
        return 2
    elif (n<=nums[0]+nums[1]+nums[2]):
        return 3
    elif (n<=nums[0]+nums[1]+nums[2]+nums[3]):
        return 4
    else:
        return 5

