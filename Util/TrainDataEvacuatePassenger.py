# -*- coding: utf-8 -*-
'''
获取训练
'''
import configparser
import jaydebeapi


class TrainDataEvacuatePassenger(object):
    def __init__(self):
        Config = configparser.ConfigParser()
        Config.read('../Resource/dbconfig.conf')
        self.dirver = Config.get('DATABASE2', 'dirver')
        self.url = Config.get('DATABASE2', 'url')
        self.user = Config.get('DATABASE2', 'user')
        self.password = Config.get('DATABASE2', 'password')
        self.jarFile = '../Resource/ojdbc6.jar'
        self.length = 0
        self.result = []
        # todo:如果是刚好有504个小时，也就是三周的数据，应该也可以
        self.lengthActual = 0

    def getFromDB(self, region):
        db = jaydebeapi.connect(
            self.dirver, [
                self.url, self.user, self.password], self.jarFile)
        try:
            curs = db.cursor()
            sqlx = 'select JZDATE, PSGOUTCOUNT from JZ_TRANRUNDATA where JZTYPE = 1  and TRANSTYPE = ' + region + 'and TO_CHAR(JZDATE, \'yyyy-mm-dd\') >= TO_CHAR(SYSDATE - 90, \'yyyy-mm-dd\')  and TO_CHAR(JZDATE, \'yyyy-mm-dd\') < TO_CHAR(SYSDATE, \'yyyy-mm-dd\')ORDER BY JZDATE DESC '
            curs.execute(sqlx)
            self.result = curs.fetchall()
        finally:
            db.close()
        self.length = len(self.result)
        self.lengthActual = self.length - 504

    def getLastWeek(self):
        actualAmount = []
        for i in range(self.lengthActual):
            temp = [self.result[i + 169][1],
                    self.result[i + 336][1],
                    self.result[i + 504][1]]
            actualAmount.append(temp)
        if self.lengthActual <= 0:
            return [[0, 0, 0], [0, 0, 0]]
        return actualAmount

    def getLastDay(self):
        actualAmount = []
        for i in range(self.lengthActual):
            temp = [self.result[i + 24][1],
                    self.result[i + 48][1],
                    self.result[i + 72][1]]
            actualAmount.append(temp)
        if self.lengthActual <= 0:
            return [[0, 0, 0], [0, 0, 0]]
        return actualAmount

    def getLastHour(self):
        actualAmount = []
        for i in range(self.lengthActual):
            temp = [self.result[i + 1][1],
                    self.result[i + 2][1],
                    self.result[i + 3][1]]
            actualAmount.append(temp)
        if self.lengthActual <= 0:
            return [[0, 0, 0], [0, 0, 0]]
        return actualAmount

    def getActualAmount(self):
        actualAmount = []
        for i in range(self.lengthActual):
            actualAmount.append(self.result[i][1])
        if self.lengthActual <= 0:
            return [0, 0]
        return actualAmount
