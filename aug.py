import cv2
import random
import numpy as np

  
def gaussian_noise(image, mean=0, sigma=10):  
    """  
    向图像添加高斯噪声  
    :param image: 输入图像（numpy数组）  
    :param mean: 噪声的均值（通常为0）  
    :param sigma: 噪声的标准差  
    :return: 添加了高斯噪声的图像  
    """  
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))  
    gauss = gauss.reshape(row, col, ch)  
    noisy = image + gauss  
      
    # 将像素值裁剪到0-255之间  
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)  
      
    return noisy

def cuting(image):
    h=int(image.shape[0]/2)
    w=int(image.shape[1]/2)
    x=int(w/2)
    y=int(h/2)
    cropped_img = image[y:y+h, x:x+w]  
      
    return cropped_img



def lumining(image,direct):
    if direct>0:
        beta = random.uniform(20, 40)  # 亮度控制
    else:
        beta = random.uniform(-40,-20)
    new=cv2.convertScaleAbs(image,beta=beta)
    return new



def bluring(image):
    core=random.randint(10,21)*2+1
    new = cv2.GaussianBlur(image, (core, core), 0) 
    return new


def laplacian_sharpen(image):  
    """  
    对图像进行拉普拉斯锐化  
    :param image: 原始图像  
    :param alpha: 锐化强度，alpha越大，锐化效果越明显  
    :return: 锐化后的图像  
    """  
    alpha=random.uniform(0.3,0.7)
    # 计算拉普拉斯变换  
    laplacian = cv2.Laplacian(image, cv2.CV_16S)  
      
    # 将拉普拉斯变换的结果转换回uint8，注意处理溢出  
    laplacian = np.uint8(np.absolute(laplacian))  
      
    # 将拉普拉斯变换的结果与原始图像混合，实现锐化  
    sharpened = cv2.addWeighted(image, 1.0 + alpha, laplacian, -alpha, 0)  
      
    return sharpened


def contrasting(img,direct):
    if direct>0:
        gamma=random.randint(2,5)
    else:
        gamma=random.uniform(0.5,0.9)
    
    img = img / 255.0  # 归一化到0-1 
    new=np.where(img <= 0.5, (2**(gamma-1)) * img**gamma, -2**(gamma-1) * ((1 - img)**gamma) + 1)
    new=(new*255).astype(np.int16)
    
    return new


if __name__=='__main__':
    img=cv2.imread('test.jpg')
    nimg=contrasting(img,0)
    cv2.imwrite('out.jpg',nimg)
    nnimg=cv2.imread('out.jpg')
    cv2.imshow('show',nnimg)
    cv2.waitKey(0)  
    cv2.destroyAllWindows() 