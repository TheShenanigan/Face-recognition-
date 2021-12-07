from os import listdir
from os.path import isdir
from PIL import Image
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from createfaceembeddings import get_embedding
from keras.models import load_model

def extract_face(required_size=(160, 160)):
	image = Image.open('vrfy6.jpg')
	image = image.convert('RGB')
	pixels = asarray(image)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	x1, y1, width, height = results[0]['box']
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	face = pixels[y1:y2, x1:x2]
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array
def give_sample():
	testX = extract_face()
	newTestX = list()
	model = load_model('facenet_keras.h5')
	print('Loaded Model')
	embedding = get_embedding(model, testX)
	newTestX.append(embedding)
	newTestX = asarray(newTestX)
	return newTestX
