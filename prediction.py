from random import choice
from numpy import load
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from numpy import asarray
from PIL import Image
from supporttransform import give_sample
def final_predict():
    val = input("Enter name")
    data = load('dataset.npz')
    testX_faces = data['arr_2']
    data = load('embeddings.npz')
    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    encode = Normalizer(norm='l2')
    trainX = encode.transform(trainX)
    testX = encode.transform(testX)
    labelling = LabelEncoder()
    labelling.fit(trainy)
    trainy = labelling.transform(trainy)
    testy = labelling.transform(testy)
    model = SVC(kernel='linear', probability=True)
    model.fit(trainX, trainy)
    sel = give_sample()
    yhat_class = model.predict(sel)
    yhat_prob = model.predict_proba(sel)
    class_index = yhat_class[0]
    class_probability = yhat_prob[0,class_index] * 100
    predict_names = labelling.inverse_transform(yhat_class)
    if predict_names[0] == val:
        print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
    else:
        print('exit')