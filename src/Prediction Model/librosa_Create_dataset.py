'''

This file is used for dataset creation from pre-exisitng songs. As it is, it returns a .csv file to be used later in the analytical process.

'''

import librosa
import numpy
import pandas
import os
import sklearn
import config


def main():
'''
Main() imports and creates the .csv dataset.
This function does not have any parameter and returns a .csv file.
'''
    #Sets up the deaulted parameters in config for dataset creation.
    samp_rate = config.CreateDataset.SAMPLING_RATE
    frame_size = config.CreateDataset.FRAME_SIZE
    hop_size = config.CreateDataset.HOP_SIZE
    dataset_dir = config.CreateDataset.DATASET_DIRECTORY

    sub_folders = get_subdirectories(dataset_dir)
    print(dataset_dir)

    labels = []
    is_created = False

    #Extracts the features of the audio using get_sample_array and extract features function.
    print("Extracting features from audios...")
    #Iterates through every song and extracts the efeatures in that particular sub folder.
    for sub_folder in sub_folders:
        print(".....Working in folder:", sub_folder)
        sample_arrays = get_sample_arrays(dataset_dir, sub_folder, samp_rate)
        for sample_array in sample_arrays:
            row = extract_features(sample_array, samp_rate, frame_size, hop_size)
            if not is_created:
                dataset_numpy = numpy.array(row)
                is_created = True
            elif is_created:
                dataset_numpy = numpy.vstack((dataset_numpy, row))

            labels.append(sub_folder)
    #Normalising data for standardised analysis values.
    print("Normalizing the data...")
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
    dataset_numpy = scaler.fit_transform(dataset_numpy)

    Feature_Names = ['meanZCR', 'stdZCR', 'meanSpecCentroid', 'stdSpecCentroid', 'meanSpecContrast', 'stdSpecContrast',
                     'meanSpecBandwidth', 'stdSpecBandwidth', 'meanSpecRollof', 'stdSpecRollof',
                     'meanMFCC_1', 'stdMFCC_1', 'meanMFCC_2', 'stdMFCC_2', 'meanMFCC_3', 'stdMFCC_3',
                     'meanMFCC_4', 'stdMFCC_4', 'meanMFCC_5', 'stdMFCC_5', 'meanMFCC_6', 'stdMFCC_6',
                     'meanMFCC_7', 'stdMFCC_7', 'meanMFCC_8', 'stdMFCC_8', 'meanMFCC_9', 'stdMFCC_9',
                     'meanMFCC_10', 'stdMFCC_10', 'meanMFCC_11', 'stdMFCC_11', 'meanMFCC_12', 'stdMFCC_12',
                     'meanMFCC_13', 'stdMFCC_13','meanMFCC_14', 'stdMFCC_14', 'meanMFCC_15', 'stdMFCC_15', 'meanMFCC_16', 'stdMFCC_16',
                     'meanMFCC_17', 'stdMFCC_17', 'meanMFCC_18', 'stdMFCC_18', 'meanMFCC_19', 'stdMFCC_19'
                     ]
    dataset_pandas = pandas.DataFrame(dataset_numpy, columns=Feature_Names)
    #Saves to .csv file for further use.
    dataset_pandas["genre"] = labels
    dataset_pandas.to_csv("data_set.csv", index=False)
    print("Data set has been created and sent to the project folder!")

def get_subdirectories(a_dir):
'''
This function is used to get the directory of the song files while also checking if the directory exists 
'''
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def get_sample_arrays(dataset_dir, folder_name, samp_rate):
    '''
This function is used to extract the signal, and sample rate.
This function takes in the directory name, folder name and the defaulted sampling rate in the format:
    get_sample(directory, folder name, and sampling rate)
returns the signal of the song and the sampling rate in the form of a numpy array in the format
    array := numpy.array([signal and other features])

    '''
    path_of_audios = librosa.util.find_files(dataset_dir + "/" + folder_name)
    audios = []
    for audio in path_of_audios:
        x, sr = librosa.load(audio, sr=samp_rate, duration=5.0)
        audios.append(x)
    audios_numpy = numpy.array(audios)
    return audios_numpy


def extract_features(signal, sample_rate, frame_size, hop_size):
'''
Extracts Features of the song from the dataset.
This function takes in parameters signal, sample rate, frame size and hop size in the format:
    extract_features(signal, sample_rate, frame size, hop size)
returns the extracted features in a list for further processing in the format:
    features := [all features]
'''

    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=signal, frame_length=frame_size, hop_length=hop_size)
    spectral_centroid = librosa.feature.spectral_centroid(y=signal, sr=sample_rate, n_fft=frame_size,
                                                          hop_length=hop_size)
    spectral_contrast = librosa.feature.spectral_contrast(y=signal, sr=sample_rate, n_fft=frame_size,
                                                          hop_length=hop_size)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=signal, sr=sample_rate, n_fft=frame_size,
                                                            hop_length=hop_size)
    spectral_rolloff = librosa.feature.spectral_rolloff(y=signal, sr=sample_rate, n_fft=frame_size, hop_length=hop_size)
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