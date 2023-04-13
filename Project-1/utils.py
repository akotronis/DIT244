import keras
import pandas as pd
import numpy as np

def load_csv(filepath):
    dataframe = pd.read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values


def load_and_stack(filenames, prefix=''):
    loaded = list()
    for name in filenames:
        data = load_csv(prefix + name)
        loaded.append(data)
        # stack group so that features are the 3rd dimension
    loaded = np.dstack(loaded)
    return loaded


def load_inertial_signals(group, prefix=''):
    filepath = prefix + group + '/Inertial Signals/'
    # load all 9 files as a single array
    filenames = list()
    # total acceleration
    filenames += ['total_acc_x_'+group+'.txt', 'total_acc_y_'+group+'.txt', 'total_acc_z_'+group+'.txt']
    # body acceleration
    filenames += ['body_acc_x_'+group+'.txt', 'body_acc_y_'+group+'.txt', 'body_acc_z_'+group+'.txt']
    # body gyroscope
    filenames += ['body_gyro_x_'+group+'.txt', 'body_gyro_y_'+group+'.txt', 'body_gyro_z_'+group+'.txt']
    # load input data
    X = load_and_stack(filenames, filepath)

    # load class output
    y = load_csv(prefix + group + '/y_' + group + '.txt')
    return X, y


def load_dataset(prefix=''):
    # load all train dataset signals
    trainX, trainy = load_inertial_signals('train', prefix + 'UCI HAR Dataset/')

    # load all test dataset signals
    testX, testy = load_inertial_signals('test', prefix + 'UCI HAR Dataset/')

    # zero-offset class values
    trainy = trainy - 1
    testy = testy - 1

    trainy = trainy.squeeze()
    testy = testy.squeeze()

    # one hot encode y
    # trainy = keras.utils.to_categorical(trainy)
    # testy = keras.utils.to_categorical(testy)
    return trainX, trainy, testX, testy


def int_to_one_hot(y, n_classes):
    return np.eye(n_classes)[y]


def one_hot_to_int(y):
    return np.argmax(y, axis=1)


def flatten_X(X):
    return X.reshape(X.shape[0], X.shape[1] * X.shape[2])