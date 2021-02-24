#importing all the necessary libraries
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import pylab as pl
import numpy as np
import tkinter as tk
import time 

af = pd.read_csv('fish.csv') #taking the dataset
print(af.head())

# # af = df[['Rank','Rating','Votes']]
# # print(af.head())
# # # plt.scatter(af['Blast Furnace Slag'], af.Strength,  color='blue')
# # # plt.xlabel("Engine size")
# # # plt.ylabel("Emission")
# # # plt.show()

msk = np.random.rand(len(af)) < 0.8      #dividing data set into train/test 8:2
train = af[msk]
test = af[~msk]

# # plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# # plt.xlabel("Engine size")
# # plt.ylabel("Emission")
# # plt.show()

regr = linear_model.LinearRegression()
#choosing the train array
x = np.asanyarray(train[['Length1','Length2','Length3','Height','Width']]) 
y = np.asanyarray(train[['Weight']])

regr.fit(x, y)
# The coefficients
# print('Coefficients: ', regr.coef_)

#predicting the values
y_hat = regr.predict(test[['Length1','Length2','Length3','Height','Width']])
# y_hat=regr.predict(np.asanyarray([[23.2, 25.4, 30.0, 11.52, 4.02]]))
# print(y_hat)
x = np.asanyarray(test[['Length1','Length2','Length3','Height','Width']])
y = np.asanyarray(test[['Weight']])

#finding the error
print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))

def output(arr):
    y_hat=regr.predict(np.asanyarray([arr]))
    return y_hat[0]

#fields for tkinter
fields = 'Vertical Length', 'Diagonal Length', 'Cross Length', 'Height', 'Width'

arr = []

#fetching data from the user
def fetch(entries):
    arr = []
    
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        arr.append(float(text))
        print('%s: "%s"' % (field, text))     
    print(arr)
    t = "Predicted weight: " + str(output(arr))     
    #getting predicted values from the model
    w = tk.Label(root, text=t)
    w.pack()

#creating the GUI in tkinter
def makeform(root, fields):
    root.title("Fishy Weight")
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

#main loop
if __name__ == '__main__':
    root = tk.Tk()

    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    # w = tk.Label(root, text=arr[2])
    # w.pack()
    root.mainloop()