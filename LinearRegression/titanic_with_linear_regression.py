#pandas for dataframes read and write
#numpy for around function used here
import pandas as pd 
import numpy as np
dataset=pd.read_csv("../input/titanic-dataset/train (1).csv") #the path here is according to Kernel in kaggle path . 
testset=pd.read_csv("../input/titanic-dataset/test.csv")
trainedSurvived=dataset.iloc[:,:1].values #get data values from survived column 
trainedSex=dataset.iloc[:,1].values # get data values from Sex column
sexForPredict=testset.iloc[:,3:4].values #data values of "Sex" from testset as we are gonna test whether a person will survive or not by gender .
from sklearn.linear_model import LinearRegression #import LinearRegression from sklearn
regressor=LinearRegression() #create model
regressor=regressor.fit(trainedSurvived,trainedSex) #fit model with data values . Sex and survived.
predictions=np.around(regressor.predict(sexForPredict)) #predict with testset , around() because the values are float but we need a definite , dead or alive result .
data_to_submit = pd.DataFrame({'PassengerId':testset['PassengerId'],'Survived':predictions}) #save dataframe with output values
data_to_submit.to_csv('titanicSubmission.csv', index = False)# final csv is produced.

