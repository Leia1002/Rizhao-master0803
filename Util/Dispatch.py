# -*- coding: utf-8 -*-
from Region.Region1 import Region1
from Util.PredictDayEvacuatePassenger import PredictDayEvacuatePassenger
from Util.PredictDayRegion import PredictDayRegion
from Util.PredictDayCollectionPoint import PredictDayCollectionPoint
from Util.PredictHourEvacuatePassenger import PredictHourEvacuatePassenger
from Util.PredictHourRegion import PredictHourRegion
from Util.PredictHourCollectionPoint import PredictHourCollectionPoint
from Util.TrainDataEvacuatePassenger import TrainDataEvacuatePassenger
from Util.TrainDataRegion import TrainDataRegion
from Util.TrainDataCollectionPoint import TrainDataCollectionPoint


class Dispatch(object):
    # 长途候车厅
    def CTHCT_InTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca', 'PSGINCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def CTHCT_InPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca', 'PSGINCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def CTHCT_InPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca', 'PSGINCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    def CTHCT_OutTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca', 'PSGOUTCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def CTHCT_OutPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca', 'PSGOUTCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def CTHCT_OutPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGOUTCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # 公交候车厅

    def GJ_InTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGINCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def GJ_InPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGINCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def GJ_InPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGINCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    def GJ_OutTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGOUTCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def GJ_OutPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGOUTCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def GJ_OutPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('5d2b5e32-d088-4dd9-9373-2a18dfb8f638', 'PSGOUTCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # 旅游集散中心

    def LYJSZX_InTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGINCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def LYJSZX_InPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGINCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def LYJSZX_InPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGINCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    def LYJSZX_OutTrain(self):
        trainData = TrainDataRegion()
        trainData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGOUTCOUNT')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def LYJSZX_OutPredictDay(self):
        predictData = PredictDayRegion()
        predictData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGOUTCOUNT')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def LYJSZX_OutPredictHour(self):
        predictData = PredictHourRegion()
        predictData.getFromDB('dba6de5f-2088-40d2-a99a-04638bcf67fe', 'PSGOUTCOUNT')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # 采集点
    # A31F南客流量西

    def A31fSouthGFWest_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('3bfa0d241e2645f6a8cda6016a36a6ec')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fSouthGFWest_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('3bfa0d241e2645f6a8cda6016a36a6ec')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fSouthGFWest_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('3bfa0d241e2645f6a8cda6016a36a6ec')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A31F南客流量东
    def A31fSouthGFEast_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('502ef3f5267245578ef116692a3d3a11')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fSouthGFEast_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('502ef3f5267245578ef116692a3d3a11')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fSouthGFEast_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('502ef3f5267245578ef116692a3d3a11')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A31F公交大厅客流量西
    def A31fLTOTWestS_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('f41c761ac6ca46f3add0e00b92873421')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fLTOTWestS_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('f41c761ac6ca46f3add0e00b92873421')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fLTOTWestS_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('f41c761ac6ca46f3add0e00b92873421')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A31F公交大厅客流量东
    def A31fLTOTEastS_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('600128075b6047ca9d8496660b938fc3')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fLTOTEastS_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('600128075b6047ca9d8496660b938fc3')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fLTOTEastS_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('600128075b6047ca9d8496660b938fc3')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A31F东南客流量西
    def A31fSoutheastPFWest_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('60385eae4a444f6c8040987aac15ef89')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fSoutheastPFWest_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('60385eae4a444f6c8040987aac15ef89')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fSoutheastPFWest_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('60385eae4a444f6c8040987aac15ef89')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A31F东南客流量东
    def A31fSoutheastPFEast_InTrain(self):
        trainData = TrainDataCollectionPoint()
        trainData.getFromDB('')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def A31fSoutheastPFEast_InPredictDay(self):
        predictData = PredictDayCollectionPoint()
        predictData.getFromDB('')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def A31fSoutheastPFEast_InPredictHour(self):
        predictData = PredictHourCollectionPoint()
        predictData.getFromDB('')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # A11F客流量01 A11FPassengerFlow01
    # A11F客流量02 A11FPassengerFlow02
    # A11F客流量03 A11FPassengerFlow03
    # A11F客流量04 A11FPassengerFlow04



    # 运营监控
    # 长途客运运行监控
    def evacuatePassengerTOLDPT_InTrain(self):
        trainData = TrainDataEvacuatePassenger()
        trainData.getFromDB('30')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def evacuatePassengerTOLDPT_InPredictDay(self):
        predictData = PredictDayEvacuatePassenger()
        predictData.getFromDB('30')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def evacuatePassengerTOLDPT_InPredictHour(self):
        predictData = PredictHourEvacuatePassenger()
        predictData.getFromDB('30')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # 公交车运营监控
    def evacuatePassengerBus_InTrain(self):
        trainData = TrainDataEvacuatePassenger()
        trainData.getFromDB('50')
        lastWeekAmount = trainData.getLastWeek()
        lastDayAmount = trainData.getLastDay()
        lastHourAmount = trainData.getLastHour()
        actualAmount = trainData.getActualAmount()
        region1Train = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount,
            actualAmount)
        region1Train.train()

    def evacuatePassengerBus_InPredictDay(self):
        predictData = PredictDayEvacuatePassenger()
        predictData.getFromDB('50')
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(lastWeekAmount, lastDayAmount)
        airportBusTrain.predict('day')

    def evacuatePassengerBus_InPredictHour(self):
        predictData = PredictHourEvacuatePassenger()
        predictData.getFromDB('50')
        lastHourAmount = predictData.predictSameDay_Hour()
        lastDayAmount = predictData.predictSameDay_Day()
        lastWeekAmount = predictData.predictSameDay_Week()
        # todo: 参数需要修改
        airportBusTrain = Region1(
            lastWeekAmount,
            lastDayAmount,
            lastHourAmount)
        airportBusTrain.predict('Hour')

    # 按时间调度
    def dispatch(self, requestType):
        if requestType == 'everyMonth':
            self.CTHCT_InTrain()
            self.CTHCT_OutTrain()
        if requestType == 'everyDay':
            self.CTHCT_InPredictDay()
            self.CTHCT_OutPredictDay()
        if requestType == 'everyHour':
            self.CTHCT_InPredictHour()
            self.CTHCT_OutPredictHour()
