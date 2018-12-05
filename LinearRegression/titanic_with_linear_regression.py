import pandas as pd
import numpy as np
dataset=pd.read_csv("../input/-dataset/train (1).csv")
testset=pd.read_csv("../input/-dataset/test.csv")
gender_sub=pd.read_csv("../input//gender_submission.csv")
trainedSurvived=dataset.iloc[:,:1].values
trainedSex=dataset.iloc[:,1].values
sexForPredict=testset.iloc[:,3:4].values
testSurvived=gender_sub.iloc[:,1].values
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor=regressor.fit(trainedSurvived,trainedSex)
predictions=np.around(regressor.predict(sexForPredict))
from sklearn.metrics import accuracy_score
accuracy_score(testSurvived,predictions)


