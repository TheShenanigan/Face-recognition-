from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
from keras.models import load_model

def get_embedding(model, face_feat):
	face_feat = face_feat.astype('float32')
	mean, std = face_feat.mean(), face_feat.std()
	face_feat = (face_feat - mean) / std
	example = expand_dims(face_feat, axis=0)
	yhat = model.predict(example)
	return yhat[0]

data = load('dataset.npz')
trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
model = load_model('facenet_keras.h5')
nTrainX = list()
for face_pixels in trainX:
	embedding = get_embedding(model, face_pixels)
	nTrainX.append(embedding)
nTrainX = asarray(nTrainX)
nTestX = list()
for face_pixels in testX:
	embedding = get_embedding(model, face_pixels)
	nTestX.append(embedding)
nTestX = asarray(nTestX)
savez_compressed('embeddings.npz', nTrainX, trainy, nTestX, testy)