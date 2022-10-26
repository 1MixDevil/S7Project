import pickle
import sqlite3
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from pycaret.anomaly import *
from sklearn.preprocessing import OneHotEncoder
from pathlib import Path
import pathlib
from S7Project.settings import FLOAT_CHOICE_CONST
path = Path(pathlib.Path.cwd())

with open(str(Path(path, 'data.pickle')), 'rb') as f:
    cols_null_persent = pickle.load(f)

def preprocess(keys, value):
    # value = list(value)
    # keys = list(keys)
    data_plane_full1 = pd.DataFrame(value, keys)
    print(data_plane_full1)
    data = pd.read_csv(str(Path(path, "X_test.csv")))
    data_plane_full = data.join(data_plane_full1)
    ser = pd.DataFrame(data_plane_full.loc[data_plane_full.shape[0] - 1]).T
    print(ser["aircraft_type"])
    data_plane_full.drop(0, axis=1, inplace=True)
    arr = ['IAI', 'IVS12', 'IBP', 'IAIE']
    columns_to = []
    for col in data_plane_full.columns:
        if cols_null_persent[col] != 0.0:
            if col in arr:
                data_plane_full[col + '_was_null'] = data_plane_full[col].isnull().astype('int')
                data_plane_full.fillna({col: data_plane_full[col].mode()[0]}, inplace=True)
            else:
                data_plane_full[col + '_was_null'] = data_plane_full[col].isnull().astype('int')
                columns_to.append(col)

    data_p = data_plane_full.copy()

    imp_mean = IterativeImputer(random_state=0)
    imp_mean = imp_mean.fit_transform(data_p[columns_to])
    data_full = pd.DataFrame(imp_mean, columns=columns_to)
    data_p = pd.concat([
        data_p.drop(columns_to, axis=1),
        data_full
    ], axis=1)

    data_p.drop('engine_id', axis=1, inplace=True)
    data_p.drop('flight_datetime', axis=1, inplace=True)
    data_p.drop('aircraft_id', axis=1, inplace=True)

    columns_to_change = ['engine_type', 'flight_phase', 'aircraft_grp', 'engine_family', 'manufacturer',
                         'aircraft_family', 'aircraft_type', 'ac_manufacturer']
    b = OneHotEncoder(sparse=False)
    data_onehot = b.fit_transform(data_p[columns_to_change])
    column_names = b.get_feature_names_out(columns_to_change)
    data_onehot = pd.DataFrame(data_onehot, columns=column_names)
    data_p = pd.concat([
        data_p.drop(columns_to_change, axis=1),
        data_onehot
    ], axis=1)

    columns_to_change = ['n1_modifier', 'IBP', 'IAIE', 'IBE']
    b = OneHotEncoder(sparse=False)
    data_onehot = b.fit_transform(data_p[columns_to_change])
    column_names = b.get_feature_names_out(columns_to_change)
    data_onehot = pd.DataFrame(data_onehot, columns=column_names)
    data_p = pd.concat([
        data_p.drop(columns_to_change, axis=1),
        data_onehot
    ], axis=1)

    return pd.DataFrame(data_p.loc[data_p.shape[0] - 1]).T


