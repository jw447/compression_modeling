import numpy as np
import pandas as pd

fname = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat", "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat"]
error = ["1E-9","1E-8","1E-7","1E-6","1E-5","1E-4","1E-3","1E-2","1E-1"]

import struct
def read_dat_d(d_):
    with open(d_,"rb") as dfile:
        data = dfile.read()
        fmat_string = "="+str(int(len(data)/8))+"d"
        d_data = struct.unpack(fmat_string, data) # decoded double data
    return d_data

def read_dat_f(d_):
    with open(d_,"rb") as dfile:
        data = dfile.read()
        fmat_string = "="+str(int(len(data)/4))+"f"
        d_data = struct.unpack(fmat_string, data) # decoded float data
    return d_data


def hitratio_estimate(fname):
    print(fname) 
    results = pd.read_csv("sz_results.csv",delimiter=",", index_col=0 ,dtype=str)
    data=read_dat_d(str("inputdata/"+fname))
    hitratio_esti = []

    for i in range(0,9):
        count = 0
        prediction_esti = np.zeros(len(data))
        prediction_esti[0] = data[0]
        prediction_esti[1] = data[1]

        prederror_esti = np.zeros(len(data))
        
        checkRadius = results.check_radius[(results.data.values == fname) & (results.errBoundRatio.values == error[i])]
        print(results.data.values == fname)
        print(results.errBoundRatio.values == error[i])
        print(checkRadius)

        for j in range(2,len(data)):
            prediction_esti[j] = 2*data[j-1]-data[j-2]
            prederror_esti[j] = data[j] - prediction_esti[j]

            if (abs(prederror_esti[j]) <= np.float(checkRadius)): # Hit
                count = count+1

        hitratio_esti.append(count/len(data))

    return hitratio_esti
