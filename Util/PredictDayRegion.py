# -*- coding: utf-8 -*-
import configparser
import jaydebeapi

'''
当天预测数据
'''


class PredictDayRegion(object):
    def __init__(self):
        Config = configparser.ConfigParser()
        Config.read('../Resource/dbconfig.conf')
        self.dirver = Config.get('DATABASE', 'dirver')
        self.url = Config.get('DATABASE', 'url')
        self.user = Config.get('DATABASE', 'user')
        self.password = Config.get('DATABASE', 'password')
        self.jarFile = '../Resource/ojdbc6.jar'
        self.result = []
        self.length = 0

    # 将数据读取
    def getFromDB(self, region, inOrOut):
        db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
        try:
            curs = db.cursor()
            sqlx = 'SELECT JZDATE,SUM (' + inOrOut + ') FROM JZ_AREAPSGFLOW WHERE JZTYPE = 1 AND AREAID = \'' + region + '\' AND TO_CHAR (JZDATE, \'yyyy-mm-dd\') >= TO_CHAR (SYSDATE - 22, \'yyyy-mm-dd\') AND TO_CHAR (JZDATE, \'yyyy-mm-dd\') < TO_CHAR (SYSDATE, \'yyyy-mm-dd\') GROUP BY AREAID, JZDATE ORDER BY JZDATE DESC'
            curs.execute(sqlx)
            self.result = curs.fetchall()
        finally:
            db.close()
        self.length = len(self.result)

    # 预测当前天所使用的前天的数据
    def predictSameDay_Day(self):
        actualAmount = []
        for i in range(24):
            temp = [self.result[24 - i][1], self.result[48 - i][1], self.result[72 - i][1]]
            actualAmount.append(temp)
        return actualAmount

    # 预测当前天所需要的前三周数据
    def predictSameDay_Week(self):
        actualAmount = []
        for i in range(24):
            # todo:此处明天再检查一下。
            temp = [self.result[7 * 24 - i][1], self.result[14 * 24 - i][1], self.result[21 * 24 - i][1]]
            actualAmount.append(temp)
        return actualAmount

    # 预测当前周需要的谴三周数据
    # 因为预测时不需要未来一周的数据，因此下面程序先作废
    # def predictSameWeek(self):
    #     actualAmount = []
    #     for i in range(168):
    #         temp = [self.result[169 - i][1], self.result[336 - i][1], self.result[504 - i][1]]
    #         actualAmount.append(temp)
    #     return actualAmount
