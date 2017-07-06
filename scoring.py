# Prepare the web service definition by authoring
# init() and run() functions. 
def init():
    import os
    os.environ['KERAS_BACKEND']='tensorflow'

    # read in the model file
    from keras.models import Sequential
    from keras.layers import Dense
    import numpy
    from keras.models import load_model
    
    # load the model
    global trainedmodel
    trainedmodel = load_model("my_model.h5")
    
def run(inputstring):
    import numpy
    #input1 = numpy.array([[1.,85.,66.,29.,0.,26.6,0.351,31.]])
    input1 = numpy.fromstring(inputstring,dtype=float, sep=',').reshape((1,8))
    score=trainedmodel.predict(input1)
    return str(score[0][0])