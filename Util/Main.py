# -*- coding: utf-8 -*-
from Region.Region1 import Region1
from Util.Dispatch import Dispatch
from Util.SocketServer import SocketServer
from Util.TrainDataRegion import TrainDataRegion

if __name__ == '__main__':
    # socketServer = SocketServer()
    # socketServer.startProject()

    # temp = TrainData()
    # temp.getFromDB('1177017f-6fe6-472c-a183-8b2d9b09d4ca')
    # aaa = temp.getLastHour()
    # print(aaa)

    dispatch = Dispatch()
    dispatch.Region1PredictHour()

    # region = Region1([0, 0, 0], [0, 0, 0], [0, 0, 0])
    # region.predict('Hour')
