'''

This file is the necessary configurations for data training, model creation, and model prediction to save time in deciding the default parameters, file type and directory path for analysis.
This file does not return anything and is importable.

'''




# --- CONFIGURATIONS FOR Convert_to_mp3 --- #
class ConvertWav:
    # Path of the song folder which will be used for wav converting
    CONVERT_DIRECTORY = "E:\\ALP\\Training_set"

    # File extension in song folder
    FILE_TYPE = "mp3"


# --- CONFIGURATIONS FOR Create_Dataset_as_csv --- #
class CreateDataset:
    # Path of GTZAN dataset
    DATASET_DIRECTORY = "E:\\ALP\\Training_set"

    # Sampling rate (Hz)
    SAMPLING_RATE = 22050

    # Frame size (Samples)
    FRAME_SIZE = 2048

    # Hop Size (Samples)
    HOP_SIZE = 512


class Test:
    # Path for test data
    TEST_DATA_PATH = "E:\\ALP\\Test_Data\\"