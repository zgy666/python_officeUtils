import cv2
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

ImagePath = "/Users/zhouguangyue/Desktop/homan.jpg"

logging.info("Reading image...")
image = cv2.imread(ImagePath)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

logging.info("Detect faces...")

face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(3, 3))

search_info = "Find %d face."%len(faces) if len(faces) <= 1 else "Find %d face."%len(faces)
logging.info(search_info)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Find faces!", image)
cv2.waitKey(0)





