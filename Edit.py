import cv2
from numpy import *





def threshold():
     for i in range(len(new)):
          for j in range(len(new[i])):
               if (old[i][j][0]+old[i][j][1]+old[i][j][2])>(128+128+127):
                    print(old[i][j][0]+old[i][j][1]+old[i][j][2])
                    new[i][j]=[255,255,255]
               else:
                    new[i][j]=[0,0,0]
               
def switchrg():
     for i in range(len(new)):
          for j in range(len(new[i])):
               new[i][j][2]=old[i][j][1]
               new[i][j][1]=old[i][j][2]

def switchrb():
     for i in range(len(new)):
          for j in range(len(new[i])):
               new[i][j][2]=old[i][j][0]
               new[i][j][0]=old[i][j][2]

def switchgb():
     for i in range(len(new)):
          for j in range(len(new[i])):
               new[i][j][1]=old[i][j][0]
               new[i][j][0]=old[i][j][1]

def poster(soglia):
     for i in range(len(new)):
          for j in range(len(new[i])):
               for k in range (len(new[i][j])):
                    if old[i][j][k]>soglia:
                         new[i][j][k]=255
                    else:
                         new[i][j][k]=0

def glasses(kind,rad):
     for i in range(len(new)):
          for j in range(len(new[i])):
               for k in range (len(new[i][j])):
                    if kind=="cross":
                         try:
                              new[i][j][k]=old[i][j][k]/5+old[i+rad][j][k]/5+old[i][j+rad][k]/5+old[i-rad][j][k]/5+old[i][j-rad][k]/5
                         except:
                              pass
                    elif kind=="square":
                         try:
                              new[i][j][k]=old[i][j][k]/9+old[i+rad][j][k]/9+old[i][j+rad][k]/9+old[i-rad][j][k]/9+old[i][j-rad][k]/9+old[i+rad][j+rad][k]/9+old[i-rad][j-rad][k]/9+old[i-rad][j+rad][k]/9+old[i+rad][j-rad][k]/9
                         except:
                              pass

print("Purple Pear")
print("(by: Blue Apple)")
while True:
     old=None
     new=None
     method=None
     print("")
     print("Enter input pic name (extension included):")
     original = input()
     old = cv2.imread(original,-1)
     new = cv2.imread(original,-1)
##     for i in range(len(new)):
##          for j in range(len(new[i])):
##               for k in range(len(new[i][j])):
##                    new[i][j][k]=0
     print("Enter processing method:")
     method = input()
     if method=="shift":
          print("red horizontal shifting:")
          xr=int(input())
          print("green horizontal shifting:")
          xg=int(input())
          print("blue horizontal shifting:")
          xb=int(input())
          print("red vertical shifting:")
          yr=int(input())
          print("green vertical shifting:")
          yg=int(input())
          print("blue vertical shifting:")
          yb=int(input())
          print("wait...")
          for i in range(len(new)):
               for j in range(len(new[i])):
                    try:
                         new[i][j][2]=old[i+yr][j+xr][2]
                    except:
                         pass
                    try:
                         new[i][j][1]=old[i+yg][j+xg][1]
                    except:
                         pass
                    try:
                         new[i][j][0]=old[i+yb][j+xb][0]
                    except:
                         pass
     if method=="scale":
          print("red horizontal scaling:")
          xr=float(input())
          print("green horizontal scaling:")
          xg=float(input())
          print("blue horizontal scaling:")
          xb=float(input())
          print("red vertical scaling:")
          yr=float(input())
          print("green vertical scaling:")
          yg=float(input())
          print("blue vertical scaling:")
          yb=float(input())
          print("wait...")
          for i in range(len(new)):
               for j in range(len(new[i])):
                    try:
                         new[i][j][2]=old[int(i/yr)][int(j/xr)][2]
                    except:
                         pass
                    try:
                         new[i][j][1]=old[int(i/yg)][int(j/xg)][1]
                    except:
                         pass
                    try:
                         new[i][j][0]=old[int(i/yb)][int(j/xb)][0]
                    except:
                         pass
     if method=="level":
          print("red leveling (type '+' to leave as it is; type '-' to invert):")
          r=input()
          print("green leveling (type '+' to leave as it is; type '-' to invert):")
          g=input()
          print("blue leveling (type '+' to leave as it is; type '-' to invert):")
          b=input()
          print("wait...")
          for i in range(len(new)):
               for j in range(len(new[i])):
                    if not (r=="+" or r=="-"):
                         new[i][j][2]=int(r)
                    if not (g=="+" or g=="-"):
                         new[i][j][1]=int(g)
                    if not (b=="+" or b=="-"):
                         new[i][j][0]=int(b)
                    if r=="-":
                         new[i][j][2]=255-old[i][j][2]
                    if g=="-":
                         new[i][j][1]=255-old[i][j][1]
                    if b=="-":
                         new[i][j][0]=255-old[i][j][0]
                    
     if method=="switch r g":
          print("wait...")
          switchrg()
     if method=="switch r b":
          print("wait...")
          switchrb()
     if method=="switch g b":
          print("wait...")
          switchgb()
     if method=="posterize":
          print("wait...")
          poster(128)
     if method=="glasses":
          print("wait...")
          glasses("cross",16)
     if method=="threshold":
          print("wait...")
          threshold()
     print("...done")
     print("Enter ouput pic name (extension included):")
     modded = input()
     cv2.imwrite(modded,new)
     print("The modified picture has been saved!")
     print(" ")
     print(" ")
     print(" ")
