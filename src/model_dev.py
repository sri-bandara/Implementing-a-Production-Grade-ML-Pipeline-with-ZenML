#strategy pattern
import logging
from abc import ABC, abstractmethod

from sklearn.linear_model import LinearRegression

class Model(ABC): #Abstract base class

    @abstractmethod #any child classes must have all parent abstract methods
    def train(self, X_train, y_train):
        pass

class LinearRegressionModel(Model):

    def train(self, X_train, y_train, **kwargs): #**kwargs means accept any number of extra keyword arguments
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg
        except Exception as e:
            logging.error("Error in training model: {}".format(e))
            raise e
