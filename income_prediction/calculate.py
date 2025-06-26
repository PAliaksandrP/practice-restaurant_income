import os
from django.conf import settings
from xgboost import XGBRegressor
import numpy as np
import pandas as pd


class ModelPredict:
    def __init__(self):
        self.model = XGBRegressor()
        model_path = os.path.join(settings.BASE_DIR, 'income_prediction', 'xgboost_model.json')
        self.model.load_model(model_path)

    def predict_result(self, params: dict):
        feature_order = [
            "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P11", "P12", "P14", "P15", "P17", "P18", "P19", "P20", "P21",
            "P22", "P23", "P25", "P27", "P28", "P29", "P33", "P37", "Days Open", "City Group_Big Cities",
            "City Group_Other", "Type_FC", "Type_IL"
        ]

        # Упорядочиваем параметры согласно ожидаемому порядку
        ordered_params = {feature: params[feature] for feature in feature_order}

        # Создаем DataFrame
        data = pd.DataFrame([ordered_params])
        result = np.expm1(self.model.predict(data))
        pd.set_option('display.float_format', '{:.2f}'.format)

        return result


model = ModelPredict()