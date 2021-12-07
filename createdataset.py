from os import listdir
from os.path import isdir
from PIL import Image
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN

def ext_face(filename, required_size=(160, 160)):
	img = Image.open(filename)
	img = img.convert('RGB')
	pixels = asarray(img)
	detect = MTCNN()
	res = detect.detect_faces(pixels)
	x1, y1, width, height = res[0]['box']
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	vision = pixels[y1:y2, x1:x2]
	img1 = Image.fromarray(vision)
	img1 = img1.resize(required_size)
	convert_array = asarray(img1)
	return convert_array

def load_faces(directory):
	faces = list()
	for file in listdir(directory):
		path = directory + file
		face = ext_face(path)
		faces.append(face)
	return faces


def load_data(directory):
	X, y = list(), list()
	for subdir in listdir(directory):
		path = directory + subdir + '/'
		if not isdir(path):
			continue
		faces = load_faces(path)
		labels = [subdir for _ in range(len(faces))]
		print('>loaded %d examples for class: %s' % (len(faces), subdir))
		X.extend(faces)
		y.extend(labels)
	return asarray(X), asarray(y)

trainX, trainy = load_data(r'archive/train/')
print(trainX.shape, trainy.shape)
testX, testy = load_data(r'archive/val/')
savez_compressed('dataset.npz',trainX,trainy,testX, testy)