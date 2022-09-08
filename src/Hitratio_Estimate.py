
import numpy as np

def hitratio_estimate(fname):

    hitratio_o = []

    with open(fname+"-hitratio.txt") as inputfile:
        for line in inputfile:
            hitratio_o.append(float(line.strip('\n')))

    hitratio_o=np.flip(hitratio_o,0)

    data=[]
    with open(fname+'-data.txt') as inputfile:
        for line in inputfile:
            data.append(float(line.strip('\n')))

    hitratio_esti = []

    realPrecision = []
    for i in range(0,9):
        realPrecision.apped((max(data) - min(data))*error[i])

    count = 0
    miss = 0
    prediction_esti = np.zeros(len(data))
    prediction_esti[0] = data[0]
    prediction_esti[1] = data[1]
    prederror_esti = np.zeros(len(data))

    for j in range(2,len(data)):
        prediction_esti[j] = 2*data[j-1]-data[j-2]
        prederror_esti[j] = data[j] - prediction_esti[j]

        if (abs(prederror_esti[j]) < checkRadius): # Hit
            count = count+1

        hitratio_esti.append(count/len(data))

    return hitratio_esti, hitratio_o
