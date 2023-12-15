import cv2
import os
import time
import os
from google.cloud import vision
import io
from google.cloud.vision_v1 import types
import keyboard
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'imagetotextconv-b1d8801d213e.json'
path = "frameimage.jpg"

startcapture=0
j=['0']
def detect_text(path):
    global startcapture
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations
    print("Recognized TEXT:")
    print("\n")
    print("************************")
    print(texts[0].description)
    print("************************")
    j.append(texts[0].description)
    f = open("out.txt", "w")
    f.write(texts[0].description)
    f.close();
    startcapture=0



cap = cv2.VideoCapture(0) 
cap.set(480, 640) 

cap.read()
while(True):
  
    
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
   
        
    key = cv2.waitKey(1)
    if key == ord('s'):
         print("-- FRAME CAPTURED AND ANALYZING ----")
         if startcapture==0:
            startcapture=1
            cv2.imwrite(path, frame)
            time.sleep(1)
            detect_text(path)
            time.sleep(1)

        
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()