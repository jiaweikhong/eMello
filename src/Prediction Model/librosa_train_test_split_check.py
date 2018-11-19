import numpy
import pandas
import joblib

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def main():
    data_set = pandas.read_csv('data_set.csv', index_col=False)
    data_set = numpy.array(data_set)
    print("Dataset shape:", data_set.shape)
    number_of_rows, number_of_cols = data_set.shape

    data_x = data_set[:, :number_of_cols - 1]
    data_y = data_set[:, number_of_cols - 1]


    X_train, X_test, y_train, y_test = train_test_split(data_x,data_y, test_size=0.33, random_state=42)



    model = SVC(C=100, gamma=0.08, probability=True)
    print("Training the model.....")
    model.fit(X_train,y_train)
    y_prediction = model.predict(X_test)
    print('Predicting accuracy:')
    print(classification_report(y_test,y_prediction))
    print('Accuracy score is: ',accuracy_score(y_test,y_prediction))


if __name__ == '__main__':
    main()