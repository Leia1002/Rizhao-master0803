# -*- coding: utf-8 -*-
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.externals import joblib

from Util.InsertDataBase import InsertDataBase


class Region1(object):
    def __init__(
            self,
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount=None,
            actualAmount=None):
        self.actualAmount = actualAmount
        self.X_NextHour = np.hstack(
            (lastWeekAmount, lastDayAmount, lastHourAmount))  # 下一小时的用此方法
        self.X_SameDay = np.hstack(
            (lastWeekAmount, lastDayAmount))  # 一小时后的用此方法
        self.X_AfterDay = lastWeekAmount  # 一天后的用此方法

    def train(self):
        clf = MLPRegressor(
            solver='lbfgs',
            alpha=1e-5,
            hidden_layer_sizes=10,
            random_state=1)  # 根据测试，中间层数选用10层

        clf.fit(self.X_NextHour, self.actualAmount)
        joblib.dump(clf, "../Resource/Region1_NextHour.m")

        clf.fit(self.X_SameDay, self.actualAmount)  # 数据训练
        joblib.dump(clf, "../Resource/Region1.m")

        # clf.fit(self.X_AfterDay, self.actualAmount.ravel())
        # joblib.dump(clf, "../Resource/Region1_NextWeek.m")
        pass

    def predict(self, type):
        insertDataBase = InsertDataBase()
        if type == 'Hour':
            clf = joblib.load("../Resource/Region1_NextHour.m")
            # 新数据导入到数据库中
            result_NextHour = clf.predict(self.X_NextHour)
            insertDataBase.insertDataBaseNextHour(result_NextHour)
        if type == 'Day':
            clf = joblib.load("../model/Region1.m")
            result_SameDay = clf.predict(self.X_SameDay)
            insertDataBase.insertDataBaseSameDay(result_SameDay)

        # clf = joblib.load("../Resource/Region1_NextWeek.m")
        # result_AfterDay = clf.predict(self.X_AfterDay)
        # insertDataBase.insertDataBaseAfterDay()
