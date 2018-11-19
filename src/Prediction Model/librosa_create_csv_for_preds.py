'''

This file is used to create a csv file for mood predictions based on a pre-trained model with a pre-existing testing set.
The model is in .pkl file format and the testing set is in .mp3 format.
Necessary functions/libraries are numpy, librosa, joblib, pre-existing config file, csv, and os
'''


import numpy
import librosa
import sklearn
import joblib
import config
import numpy as np
import csv
import os


def main():
    '''
    Main() for the predictive music mood classification after obtaining the model as well as the training data. 
    Main() does not have any parameters as it returns a csv file for further processing.
    Saves the labelled normalised data is a .csv file.
    '''
    path = librosa.util.find_files(config.Test.TEST_DATA_PATH)
    sample_rate = config.CreateDataset.SAMPLING_RATE
    hop_size = config.CreateDataset.HOP_SIZE
    frame_size = config.CreateDataset.FRAME_SIZE

    songs = []
    song_name = []
    new_song_name = []
    print("Extracting sample arrays for files...")

    #Extracting the features of the test songs
    for p in path:
        x, sr = librosa.load(p, sr=sample_rate, duration=5.0)
        songs.append(x)
        song_name.append(p)
    for i in song_name:
        directory_name,new_song_title = os.path.split(i)
        new_song_name.append(new_song_title)
    print("DONE!")

    print("Extracting features from sample arrays...")

    #Readies data for prediction by transforming it to a numpy array.
    data = numpy.array([extract_features(x, sample_rate, frame_size, hop_size) for x in songs])

    print("DONE!")
    #Normalises Data to match with the pre-exisiting model
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
    fitted_data = scaler.fit_transform(data)

    # get the model from pkl file
    svm = joblib.load('model.pkl')

    print("----------------------------------- Predicted Labels -----------------------------------\n")
    
    preds = svm.predict(fitted_data)
    #Predicts the probability for the song to fit each category
    probs_check = svm.predict_proba(fitted_data)

    predlist = [i for i in preds]
    prob_check_list = [i for i in probs_check]
    features_check = [predlist,prob_check_list]
    
    zipped_analysis = dict()
    for i in range(len(new_song_name)):
        zipped_analysis[new_song_name[i]] = [predlist[i],prob_check_list[i]]
    print(zipped_analysis)

    currentPath = os.getcwd()
    dict_data = []
    csv_columns = ['Song Title','Predicted Mood','Confidence_Level']

    '''
    Processes data to be in the format:
    data := {'Song Title': Song Name, 'Predicted Mood': Most Suitable Mood, 'Confidence_Level': Probability level}
    '''
    
    for i in range(len(new_song_name)):
        create_dict = {csv_columns[0]:new_song_name[i],csv_columns[1]:predlist[i], csv_columns[2]:np.max(prob_check_list[i])}
        dict_data.append(create_dict)

    csv_file = currentPath + "/Confidence_Level.csv"
    WriteDictToCSV(csv_file,csv_columns,dict_data)
    print('CSV file has been created.')


def WriteDictToCSV(csv_file,csv_columns,dict_data):
    '''
    This function takes in the csv file name, the feature label, and the features as parameters to save a csv file 
    '''
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as err:
            print(err)    
    return    


def sort_songs_by_emotion(d_emotion):
    """This function takes in a dictionary matching the following format:
    d := {song_name : song_predicted_emotion}
    and then returns a dictionary defined in the following format:
    returned := {song_predicted_emotion, [song_name,[song_name2, ...]]}"""
    returned = {}
    for i in d_emotion:
        if d_emotion[i] in returned:
            returned[d_emotion[i]].append(i)
        else:
            returned[d_emotion[i]] = [i]
    return returned


    


def extract_features(signal, sample_rate, frame_size, hop_size):
    """
    This function takes in the signal from the song, sample rate, frame size, hop size for wach song and extracts features forfurther analysis in main()
    returns a list with all the necessary features for the song to be fitted in the SVM modelin the following format
    features : = [mean & standard deviation of zero crossing rate,spectral centroid,contrast,bandwidth,rolloff, mfcc]
    """

    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=signal, frame_length=frame_size, hop_length=hop_size)
    spectral_centroid = librosa.feature.spectral_centroid(y=signal, sr=sample_rate, n_fft=frame_size,
                                                          hop_length=hop_size)
    spectral_contrast = librosa.feature.spectral_contrast(y=signal, sr=sample_rate, n_fft=frame_size,
                                                          hop_length=hop_size)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=signal, sr=sample_rate, n_fft=frame_size,
                                                            hop_length=hop_size)
    spectral_rolloff = librosa.feature.spectral_rolloff(y=signal, sr=sample_rate, n_fft=frame_size,
                                                        hop_length=hop_size)
    mfccs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_fft=frame_size, hop_length=hop_size)

    avgbpm = librosa.beat.tempo(y = signal,sr = sample_rate, hop_length = hop_size)
    rmse = librosa.feature.rmse(y=signal)
    return [

        numpy.mean(zero_crossing_rate),
        numpy.std(zero_crossing_rate),
        numpy.mean(spectral_centroid),
        numpy.std(spectral_centroid),
        numpy.mean(spectral_contrast),
        numpy.std(spectral_contrast),
        numpy.mean(spectral_bandwidth),
        numpy.std(spectral_bandwidth),
        numpy.mean(spectral_rolloff),
        numpy.std(spectral_rolloff),

        numpy.mean(mfccs[1, :]),
        numpy.std(mfccs[1, :]),
        numpy.mean(mfccs[2, :]),
        numpy.std(mfccs[2, :]),
        numpy.mean(mfccs[3, :]),
        numpy.std(mfccs[3, :]),
        numpy.mean(mfccs[4, :]),
        numpy.std(mfccs[4, :]),
        numpy.mean(mfccs[5, :]),
        numpy.std(mfccs[5, :]),
        numpy.mean(mfccs[6, :]),
        numpy.std(mfccs[6, :]),
        numpy.mean(mfccs[7, :]),
        numpy.std(mfccs[7, :]),
        numpy.mean(mfccs[8, :]),
        numpy.std(mfccs[8, :]),
        numpy.mean(mfccs[9, :]),
        numpy.std(mfccs[9, :]),
        numpy.mean(mfccs[10, :]),
        numpy.std(mfccs[10, :]),
        numpy.mean(mfccs[11, :]),
        numpy.std(mfccs[11, :]),
        numpy.mean(mfccs[12, :]),
        numpy.std(mfccs[12, :]),
        numpy.mean(mfccs[13, :]),
        numpy.std(mfccs[13, :]),
        numpy.mean(mfccs[14, :]),
        numpy.std(mfccs[14, :]),
        numpy.mean(mfccs[15, :]),
        numpy.std(mfccs[15, :]),
        numpy.mean(mfccs[16, :]),
        numpy.std(mfccs[16, :]),
        numpy.mean(mfccs[17, :]),
        numpy.std(mfccs[17, :]),
        numpy.mean(mfccs[18, :]),
        numpy.std(mfccs[18, :]),
        numpy.mean(mfccs[19, :]),
        numpy.std(mfccs[19, :]),

    ]


if __name__ == '__main__':
    main()