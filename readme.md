***Dependencies***
The following are the libraries and modules which are required to run the code.
tensorflow
PIL(Python Image Library)
Numpy
createfaceembeddings
keras
mtcnn
opencv(cv2)
pynput
threading
datetime
sklearn
python2 or higher

All of the above dependencies can be downloaded by typing pip install <dependency> // pip must be installed to run pip install command

Download the 5 Celebrity dataset from this link https://www.kaggle.com/dansbecker/5-celebrity-faces-dataset and place it in the folder where you have extracted all the files.
Download the model from https://drive.google.com/drive/folders/1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn and place it in the folder where you have extracted all the files.
To run the code we are using the following sequence
1. Run the videoregister.py (NOTE: change the path on line 38 to the path where you will place the videoregister.py file.)
2. Select all images starting with videoyash and then place it in the archive>train>Ambarish folder(You can change the name of the folder)
3. You can run the same script to record another set of images and then place it in the archive>val> Ambarish folder.(You can change the name of the folder)
4. Then run the createdataset.py script to create a dataset.
5. Then run the createfaceembeddings.py to create face embeddings from the dataset.
6. Keep the supporttransform.py as it provides codes to final phase.
7. Then run the verifyimagecapture.py to take input from user to verify. A prompt to enter users name(same as dataset) is required. Enter name without space(Enter name<name>)
8. Then run prediction.py to check for prediction of the input image.  
9. If the predicted label is same as users name it will show the results else it will decline and exit.