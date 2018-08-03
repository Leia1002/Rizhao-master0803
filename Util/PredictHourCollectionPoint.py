# -*- coding: utf-8 -*-
import configparser
import jaydebeapi

'''
小时预测数据
'''


class PredictHourCollectionPoint(object):
    def __init__(self):
        Config = configparser.ConfigParser()
        Config.read('../Resource/dbconfig.conf')
        self.dirver = Config.get('DATABASE2', 'dirver')
        self.url = Config.get('DATABASE2', 'url')
        self.user = Config.get('DATABASE2', 'user')
        self.password = Config.get('DATABASE2', 'password')
        self.jarFile = '../Resource/ojdbc6.jar'
        self.result = []
        self.length = 0
        self.lengthActual = 0

    def getFromDB(self, region):
        db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
        try:
            curs = db.cursor()
            sqlx = 'SELECT JZDATE,SUM (PSGINCOUNT) FROM JZ_AREAPSGFLOW WHERE JZTYPE = 1 AND AREAID = \'' + region + '\' AND JZDATE >= SYSDATE - 21 GROUP BY AREAID, JZDATE ORDER BY JZDATE DESC'
            curs.execute(sqlx)
            self.result = curs.fetchall()
        finally:
            db.close()
        self.length = len(self.result)
        self.lengthActual = self.length - 504

    def predictSameDay_Hour(self):
        actualAmount = []
        if self.lengthActual <= 0:
            return [[0, 0, 0]]
        else:
            for i in range(24):
                temp = [self.result[0][1], self.result[1][1], self.result[2][1]]
                actualAmount.append(temp)
        return actualAmount

    def predictSameDay_Day(self):
        actualAmount = []
        if self.lengthActual <= 0:
            return [[0, 0, 0]]
        else:
            for i in range(24):
                temp = [self.result[24][1], self.result[48][1], self.result[72][1]]
                actualAmount.append(temp)

        return actualAmount

    # 预测当前天所需要的前三周数据
    def predictSameDay_Week(self):
        actualAmount = []
        if self.lengthActual <= 0:
            return [[0, 0, 0]]
        else:
            for i in range(24):
                # todo:此处明天再检查一下。
                temp = [self.result[7 * 24][1], self.result[14 * 24][1], self.result[21 * 24][1]]
                actualAmount.append(temp)
        return actualAmount
