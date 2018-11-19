'''
This file is to create a trained model for prediction.
Using Support Vector Classifier from scikit learn library to create a Support Vector Model which is saved in a .pkl format, the file takes in a pre-existing dataset in a .csv file.
This file returns a .pkl model for further analysis.
'''


import numpy
import pandas
import joblib

from sklearn.svm import SVC
'''
This python file trains the Support Vector Machine(SVM) model using Support Vector Classification method imported from sci-kit learn
Gamma Parameter is set to be 0.08 as it is proven to be the most optimal value for our case, but is changeable depending on the need.
Probability is set to be True for further analysis in librosa_predict
'''

def main():

#Main() in this file is the function that executes the model training by taking in a pre-existing csv dataset and train it using SVC method.
#This will dump a new pkl into the current directory and exits the file after it is done.

    data_set = pandas.read_csv('data_set.csv', index_col=False)
    data_set = numpy.array(data_set)
    print("Dataset shape:", data_set.shape)
    number_of_rows, number_of_cols = data_set.shape

    data_x = data_set[:, :number_of_cols - 1]
    data_y = data_set[:, number_of_cols - 1]

    model = SVC(C=100, gamma=0.08, probability=True)
    print("Training the model.....")
    model.fit(data_x, data_y)

    joblib.dump(model, 'model.pkl')
    print("Trained and saved the model to project folder successfully.")


if __name__ == '__main__':
    main()