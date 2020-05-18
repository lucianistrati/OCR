import cv2
import numpy as np
def convertToHoughLines(path):
    """
    This function is drawing red lines in an image where the function
    detects edges using Hough Lines
    """
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
      
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)#Red Color
    cv2.imwrite('houghlinesNormal.jpg',img)
    return img 
    
def convertProbabilisticToHoughLines(path):
    """
    This function is drawing red lines in an image where the function
    detects edges using Probabilistic Hough Lines
    """
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)#Green color
    cv2.imwrite('houghlinesProbabilistics.jpg',img)
    return img
