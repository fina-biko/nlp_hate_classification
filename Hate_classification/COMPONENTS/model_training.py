
from _typeshed import Self
from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes
from Hate_classification.ATTRIBUTES.attributes_entity import FeatureEngineerringAttributes
from tensorflow.keras.layers import Layer# for subclassing the  layer class
from tensorfloww.keras import Model
from tensorflow.keras import layers# for the layers used in the model
from tensorflow import keras
from  tensorflow.keras import activations 


import pandas as pd
import numpy as np

'''The model to be used will be the deep learning models and the Traditional model , then evaluation of the models performed to determine the model that will be used for training  and evaluation of the models 
'''

class CNNLayers(Layer):
  def __init__(self) :

    super(CNNLayers).__init__()
    #block1 of the cnnlayers
    self.conv1=layers.conv1(filters=32,kernel_size=(3,3),strides=1,padding=None,activation=None)
   
    #block2 of the cnn layers
    self.conv2=layers.conv1D(filters=32,kernel_size=(3,3),strides=1,padding=None,activation=None)
    self.BN=layers.BatchNormalization(axis=-1, momentum=0.99)
    self.max_pool_1d = layers.MaxPooling1D(pool_size=2,strides=2, padding="valid")


  def call(self,input_tensor):
    #block1
    x=self.conv1(input_tensor)
    #block2
    x=self.conv2(x)
    x=self.BN(x)
    x=self.maxpool1(x)
    return x  


class DenseLayers(Layer):
  def __init__(self) :
    super(DenseLayers).__init__()
    self.Dense1=layers.Dense(units=1,acivation='Relu')
    self.dropout=layers.Dropout(rate=0.2, noise_shape=None, seed=None)


  def call(self,input_tensor):
    x=self.Dense1(input_tensor)
    x=self.dropout(x)
    return x
    

class CustomModel(Model):
  def __init__(self) :
    super().__init__()
    #block1
    self.conv1=CNNLayers()
    #block2
    self.conv2=CNNLayers()
    #block3
    self.flatten=layers.Flatten()
    self.dense=DenseLayers()

  def call(self,input_tensor):
    conv1=self.conv1(input_tensor)#class 1
    conv2=self.conv2(conv1)#class 1
    flatten=self.flatten(conv2)
    dense=self.dense(flatten)#class 2
    return dense

class ModelTrainingAbstract(ABC):
  def __init__(self) :
    pass
    
  @abstractmethod
  def preprocess(self):
    pass

class ModelTraining(ModelTrainingAbstract):
  '''Takes in the custom model defined earlier'''
  def __init__(self, input_tensor, model=None):
      super().__init__()  # Initialize the abstract base class
      self.input = input_tensor
      self.model = model() if model is not None else CustomModel()  # Create an instance of the model

  def preprocess(self):
     model=self.modeltrain()
     self.save_model()
     return model

  def modeltrain(self):
      model=self.Model
      model.compile(optimizer='adams',loss=None,loss_weights=None,metrics=None,run_eagerly=False,steps_per_execution=1,
             auto_scale_loss=True)

      model=model.fit(self.input)
      return model

  def save_model(self):
      pass



    
















