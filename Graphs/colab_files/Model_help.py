import pickle

import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from pathlib import Path
import pathlib
path = Path(pathlib.Path.cwd(), 'final_models')


def model(data_p):
    np.random.seed(0)
    res_ans = []
    labels = []
    np.random.seed(0)

    data_f = ['BRAT', 'DELFN', 'DELN1', 'DPOIL', 'EGTC', 'EGTHDM', 'GEGTMC', 'GN2MC',
           'GPCN25', 'PCN12', 'PCN12I', 'PCN1AR', 'PCN1K', 'PCN2C', 'SLOATL',
           'WBI', 'WFMP', 'ZTLA_D', 'DEGT', 'DELVSV', 'EGTHDM_D', 'GWFM', 'PCN1BR', 'SLOATL_D',
            'WBE', 'ZPCN25_D', 'ZT49_D', 'ZTNAC_D', 'ZWF36_D']

    for col in data_f:

        X = data_p
        paths = str(Path(path, "final_model", 'final_model', f'model_{col}_scaled'))
        with open(paths, 'rb') as f:
            scaler = pickle.load(f)
        X = scaler.transform(X)

        with open(str(Path(path, "final_model", 'final_model', f'model_{col}_scaled')), 'rb') as f:
            select = pickle.load(f)
        X = select.transform(X)

        model = CatBoostRegressor()

        model = model.load_model(str(Path(path, "final_model", 'final_model', f'model_{col}')))
        catboost_predicted = model.predict(X)
        res_ans.append(catboost_predicted)
        labels.append(f'{col}')
    model_answers = pd.DataFrame(res_ans, labels).T
    return (labels, res_ans)