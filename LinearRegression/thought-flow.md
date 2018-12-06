The problem is binary classification based on python or R programming languages . Here, I used python and implemented simple linear regression . <br>
<h3>Data Preparation</h3>
First of all, I calculated correlation coefficient on all data columns in "train(1).csv" using excel .
<br>There is an auto-calculation function for correlation under satistical functions. function name- CORREL. <br> 
You just have to add rows of data that you want to calculate . <br>
I will put the figures later . <br>
If you have no idea of correlation coefficient, you can read <a>here </a>.<br>
After checking on the correlation coefficient results, I found out that "Sex" has the strongest relationship with "Survived" .<br>
I chose only that "Sex" data to use in the model. <br> 
At first , data values for "Sex" are "male" and  "female" . <br> 
 We need to categorize it . That's why I replaced "female" with 1 and "male" with 0 just by using excel . <br>
 I also deleted columns except "Survived" and "Sex" <br> 
 Then the data is ready to fit ! <br> 
 <hr>
 <h3>Implementation</h3>
  as in the code and comments .
  <hr>
  <h3> Conclusion</h3>
  This can't get the good accuracy score as it's very simple. <br>
  But for the sake of the beginners, you won't get bored of machine learning easily and will always find and apply your newly <br>learned algorithms and skills . May your hands get dirtier on ML coding <3 ! 
  
 

