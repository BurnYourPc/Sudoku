import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def CreateSudoImg(A,sym):   #Adds new Sudoku problem as png image to the desirable folder
    font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 18)
    img=Image.open("/foul_path_to/src/burnImage/image.png")
    draw = ImageDraw.Draw(img)
    for i in range(9):
        for j in range(9):
            if (A[i,j]!=0):
                draw.text((j*25+8,i*25+3), str(A[i,j]),font=font,fill=2)
                draw = ImageDraw.Draw(img)
    if (sym):
        path2save="/foul_path_to/SudoProblems/Symmetrical"
        
        file_list = os.listdir(path2save) # dir is your directory path
        file_count = len(file_list)+1
        
        imgname="/SymProb"+str(file_count)+".png"
        img.save(path2save+imgname)
    else:
        path2save="/foul_path_to/SudoProblems/NonSymmetrical"
        
        file_list = os.listdir(path2save) # dir is your directory path
        file_count = len(file_list)+1
        
        imgname="/NonSymProb"+str(file_count)+".png"
        img.save(path2save+imgname)



