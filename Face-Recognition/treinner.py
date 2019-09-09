import cv2,os #opencv
import numpy as np # manipula a matriz
from PIL import Image # transformar oarquivo de imagem em matriz

recognizer = cv2.createLBPHFaceRecognizer();
path='dataSet'

def getImagesAndLabels(path):

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
   
    faces=[]
    IDs=[]
    
    for imagePath in imagePaths:
       
        faceImag=Image.open(imagePath).convert('L');
        #Now we are converting the PIL image into numpy array
        faceNp=np.array( faceImag,'uint8')
        #getting the Id from the image
        ID=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return IDs, faces


IDs,faces= getImagesAndLabels('dataSet')
recognizer.train(faces, np.array(IDs))
recognizer.save('trainner/trainner.yml')
#cv.destroyAllWindows()


