# fishyWeightPredictor
<br/>

This project predicts the weight of a fish by taking different dimensions.

It predicts the value of the weight of the fish by using different lengths:
1. Vertical Length
2. Cross Length
3. Diagonal
<br/>and also height and width of the fish

## Why this Dataset?

I used this data set because it can be used help the
local fisherman to predict the price of the fish.
The weight of the fish can be used to find out if the fish is healthy or not. 
<br/>Fitness enthusiasts can use this data to add protein/fat intake in their diet plan and make changes accordingly.
<br/>

## Algorithm Used
Multiple Linear Regression has been used in this code.
80% of the dataset has been used to train the dataset and the other 20% of it has been used for testing. <br/> 
After plotting the data using matplotlib, it was seen that the graph was a straight line with multiple input data. 

The Variance Score of this model comes out to be approximately 0.80. If any linear regression model has a variance score of 
more than 0.60, it is considered to be a good model.
<br/>
<br/>
### Python Libraries Used
* pandas - storing and manipulating data
* matplotlib - plotting graphs
* numpy - doing all the matrices work
* sklearn - library for testing and training data
* tkinter - making the GUI for the model
<br/>

## Source of the data:
The dataset has been taken from kaggle. 
The link is given below:
>[Link to the Dataset](https://www.kaggle.com/aungpyaeap/fish-market?select=Fish.csv)
