
Build a deep learning model using Keras and Tensorflow to predict the onset of diabetes using the famous Pima Indians Diabetes dataset.

A copy of the dataset is included. Need to install the following libraries at the command prompt in Vienna command window:

- conda install keras
- conda install tensorflow

Run the code and create the model file. Then download the model and enter the following command to deploy to ACS or locally.

c:\<folderName>az ml service create realtime -f scoring.py -m my_model.h5 -n kerasdiab1 -r scikit-py -p requirements.txt

c:\<folderName>az ml service run realtime -n kerasdiab2 --% -d "1.,85.,66.,29.,0.,26.6,0.351,31."

