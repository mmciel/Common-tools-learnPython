import os
import imageio
import shutil
from PIL import Image,ImageDraw,ImageFont


SOURCE_PATH = '.\\test.gif' # get file
OUTPUT_PATH = '.\\imgs\\'
FRAMES_PATH = '.\\outing\\'

def create_dir():
    path1 = os.path.exists(OUTPUT_PATH)
    path2 = os.path.exists(FRAMES_PATH)
    dir0 = os.getcwd()

    if path1:
        print()
        shutil.rmtree('imgs')
        os.mkdir(dir0+"\\imgs")
    else:
        os.mkdir(dir0+"\\imgs")
    if path2:
        print()
        shutil.rmtree('outing')
        os.mkdir(dir0+"\\outing")
    else:
        os.mkdir(dir0+"\\outing")
        

def processImage(path):
    credits()
    img = Image.open(path)
    index = 0
    print("wait...")
    try:
        while True:
            img.seek(index)
            img.save('.\\imgs\\%d.png' % index)
            index+=1
    except EOFError:
        print("wait...")

def createImg(path):
    str =  '''@B%8&W..*oahk567489564565631bdpqwmZO0QLC`'. '''

    progress = 0
    unit = len(os.listdir(OUTPUT_PATH))/100

    for file in os.listdir(path):
        progress += int(unit+1)
        #print()
        with Image.open(''.join((path,file))) as img:
            wide,high = img.size
            if img.mode !='RGB' : img = img.convert("RGB")
            new_img = Image.new('1',(wide*2,high*2),color=255)
            draw = ImageDraw.Draw(new_img)

            for i in range(1,high,4):
                for j in range(1,wide,4):
                    R,G,B = img.getpixel((j,i))
                    sum = int(R* 0.299+G* 0.587+B* 0.114)
                    index = int(sum/30)
                    draw.text((j*2,i*2),str[index])
                new_img.save(FRAMES_PATH+file)


    print()
def creat_gif(path,filename):
    image_list=[]
    num = len(os.listdir(path))
    for i in range(num):
        image_list.append(FRAMES_PATH+str(i)+'.png')
    frames = []
    for k in image_list:
        frames.append(imageio.imread(k))
    imageio.mimsave(filename,frames,'GIF',duration=0.1)


if __name__ == "__main__":
    create_dir()
    processImage(SOURCE_PATH)
    createImg(OUTPUT_PATH)
    creat_gif(FRAMES_PATH,"QAQ.gif")





    



        













    
