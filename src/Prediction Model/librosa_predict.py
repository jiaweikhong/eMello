import numpy
import librosa
import sklearn
import joblib
import config
import numpy as np


def main():
    '''
    Main() for the predictive music mood classification after obtaining the model as well as the training data. 
    Main() does not have any parameters as it directly imports the the song(.mp3) files and extracts its features for data analysis using the available model(.pkl)
    Function returns the tagged mood for each tested songs in the form of a python dictionary for further analysis in the project.
    '''
    path = librosa.util.find_files(config.Test.TEST_DATA_PATH)
    sample_rate = config.CreateDataset.SAMPLING_RATE
    hop_size = config.CreateDataset.HOP_SIZE
    frame_size = config.CreateDataset.FRAME_SIZE

    songs = []
    song_name = []
    print("Extracting sample arrays for files...")

    for p in path:
        #extracting the necessary features for extract_feature() parameters.
        x, sr = librosa.load(p, sr=sample_rate, duration=5.0)
        songs.append(x)
        song_name.append(p)

    print("DONE!")

    print("Extracting features from sample arrays...")

    data = numpy.array([extract_features(x, sample_rate, frame_size, hop_size) for x in songs])

    print("DONE!")

    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
    fitted_data = scaler.fit_transform(data)

    # get the model from pkl file
    svm = joblib.load('model.pkl')

    print("----------------------------------- Predicted Labels -----------------------------------\n")
    
    #predicts tag for each song.
    preds = svm.predict(fitted_data)

    probs_check = svm.predict_proba(fitted_data)
    #stores the predicted tags in a list for futher processing
    predlist = [i for i in preds]


    prob_check_list = [i for i in probs_check]
    features_check = [predlist,prob_check_list]
    zipped_analysis = dict(zip(song_name,predlist))
    print(zipped_analysis)

    emotion_to_song = sort_songs_by_emotion(zipped_analysis)
    print("-"*88+"\n")
    print("++++++++++++++++++++++++++++++++++EMOTION TO SONG LIST++++++++++++++++++++++++++++++++++\n")
    #prints out the songs that are tagged with the mood.
    for i in emotion_to_song:
        print(i)
        for j in emotion_to_song[i]:
            print(j,)
        print()
    print("+"*88)


def sort_songs_by_emotion(d_emotion):
    """This method takes in a dictionary matching the following format:
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
    returns a list with all the necessary features for the song to be fitted in the SVM model. The list includes [mean & standard deviation of zero crossing rate,spectral centroid,contrast,bandwidth,rolloff, mfcc]
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