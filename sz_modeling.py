#!/usr/bin/env python
# coding: utf-8

import os
import math
import struct
import numpy as np
import pandas as pd

# read double-precision floating data
def read_dat_d(dname):
    with open(dname,"rb") as dfile:
        data = dfile.read()
        fmat_string = "="+str(int(len(data)/8))+"d"
        d_data = struct.unpack(fmat_string, data) # decoded double data
    return d_data

# read single-precision floating data
def read_dat_f(dname):
    with open(dname,"rb") as dfile:
        data = dfile.read()
        fmat_string = "="+str(int(len(data)/4))+"f"
        d_data = struct.unpack(fmat_string, data) # decoded float data
    return d_data

# hitratio estimation
def hitratio_estimate(dname):
    results = pd.read_csv("sz_results.csv",index_col=0 ,dtype=str)
    data=read_dat_d(str("inputdata/"+dname))
    hitratio_esti = []
    
    for i in range(0,9): # 9 is the number of error bounds.
        count = 0
        prediction_esti = np.zeros(len(data))
        prediction_esti[0] = data[0]
        prediction_esti[1] = data[1]
        prederror_esti = np.zeros(len(data))

        checkRadius = results.check_radius[(results.data.values == dname) &
                                            (results.errBoundRatio.values == relError[i])]

        for j in range(2,len(data)):
            prediction_esti[j] = 2*data[j-1]-data[j-2]
            prederror_esti[j] = data[j] - prediction_esti[j]
            if (abs(prederror_esti[j]) < np.float(checkRadius)): # Hit
                count = count+1
                
        hitratio_esti.append(count/len(data))
        
    return hitratio_esti

def cr_estimate(df, dname):
    input_size = df.input_size[df.data==dname].values[0]
    nc_esti = df.node_count_esti[df.data == dname].values
    hr_esti = hitratio_estimate(dname)
    
    # at base error bound (relErrpr[0])
    ts_esti = [df.tree_size[(df['data'] == dname) & (df['errBoundRatio']==relError[0])].values[0]]
    es_esti = [df.encode_size[(df['data'] == dname) & (df['errBoundRatio']==relError[0])].values[0]]
    os_esti = [df.outlier_size[(df['data'] == dname) & (df['errBoundRatio']==relError[0])].values[0]]
    oc_esti = [df.curve_missed[(df['data'] == dname) & (df['errBoundRatio']==relError[0])].values[0]]
    total_esti = [df.output_size[(df['data'] == dname) & (df['errBoundRatio']==relError[0])].values[0]]
    cr_esti = [df.compression_ratio[(df['data'] == dname) & (df['errBoundRatio'] == relError[0])].values[0]]

    num_elements = df.curve_missed[df.data==dname].values[0] + df.curve_hit[df.data==dname].values[0]
    
    for i in range(1,len(relError)):
        ts_e = ts_esti[0]*(nc_esti[i]/nc_esti[0])
        es_e = es_esti[0]*(np.log2(nc_esti[i])/np.log2(nc_esti[0]))
        oc_e = num_elements*(1-hr_esti[i])
        
        os_e = oc_e * os_esti[0]/oc_esti[0]
        total_e = ts_e + es_e + os_e
        cr_e = input_size/total_e

        ts_esti.append(ts_e)
        es_esti.append(es_e)
        os_esti.append(os_e)
        oc_esti.append(oc_e)
        total_esti.append(total_e)
        cr_esti.append(cr_e)
    
    return cr_esti

if __name__ == "__main__":

    relError = ["1E-9", "1E-8", "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]

    data = ["astro.dat", "blast2_p.dat", "bump.dat",
            "dpot.dat", "eddy.dat", "fish.dat",
            "sedov_p.dat", "yf17_p.dat","yf17_t.dat"]

    df = pd.read_csv("sz_results.csv", index_col=0 ,dtype=str)

    df.input_size = df.input_size.astype(float)
    df.max_quant_intl = df.max_quant_intl.astype(float)
    df.check_radius =  df.check_radius.astype(float)
    df.node_count = df.node_count.astype(float)
    df.node_count_esti = df.node_count_esti.astype(float)
    df.curve_hit = df.curve_hit.astype(float)
    df.curve_missed = df.curve_missed.astype(float)
    df.hit_ratio = df.hit_ratio.astype(float)
    df.tree_size = df.tree_size.astype(float)
    df.encode_size = df.encode_size.astype(float)
    df.outlier_size = df.outlier_size.astype(float)
    df.output_size = df.output_size.astype(float)
    df.compression_ratio = df.compression_ratio.astype(float)

    for dname in data:
        cr_orig = df.compression_ratio[df.data == dname].values
        cr_esti = cr_estimate(df, dname)
        
        print( dname, cr_orig, cr_esti)
