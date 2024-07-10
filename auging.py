import os
from aug import *

def process(reg_img,num,drt):
    img=reg_img[:][:]
    count=0
    for i in range(0,2):
        
        
        for j in range(0,6):

            for k in range(0,2):
               
                for l in range(0,2):
                    if i==1:
                        if img.shape[0]>700:
                            img=cuting(img)
                        else:
                            continue
                    
                    #----
                    if j<=1:
                        if j==0:
                            contrasting(img,1)
                        else:
                            contrasting(img,0)
                    elif j>=4:
                        if j==4:
                            img=laplacian_sharpen(img)
                    else:
                        if j==2:
                            img=lumining(img,1)
                        else:
                            img=lumining(img,0)
                    #----
                    if k==1:
                        img=bluring(img)
                    #---
                    if l==1:
                        img=gaussian_noise(img)
                    count+=1
                    img_out=str(num)+"_"+str(count)+".jpg" 
                    print(i,j,k,l)   
                    cv2.imwrite(os.path.join(drt,img_out),img)
                    img=reg_img[:][:]

def runing(directory,drt):  
    """  
    使用os.walk列出给定目录及其所有子目录下的所有文件。 
    """  
    count=0
    for root, dirs, files in os.walk(directory):  
        for filename in files:  
            # os.path.join用于将目录路径和文件名合并成完整的文件路径
            if filename.split('.')[-1] in ['jpg','png','jpeg']:  
                print(filename)
                img_path=os.path.join(root, filename)
                img=cv2.imread(img_path)
                process(img,count,drt)
                count+=1
                


src_path=input("src:")
drt_path=input("drt:")
runing(src_path,drt_path)



            
