#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import math

relError = [["9.9e-10","9.9e-9", "9.9e-8", "9.9e-7", "9.9e-6", "9.9e-5", "9.9e-4", "9.9e-3", "9.9e-2"],
            ["4.3e-7", "4.3e-6", "4.3e-5", "4.3e-4", "4.3e-3", "4.3e-2", "4.3e-1", "4.3e0", "4.3e1"],
            ["4.7e-11", "4.7e-10", "4.7e-9", "4.7e-8", "4.7e-7", "4.7e-6", "4.7e-5", "4.7e-4", "4.7e-3"],
            ["1.4e-8", "1.4e-7", "1.4e-6", "1.4e-5", "1.4e-4", "1.4e-3", "1.4e-2", "1.4e-1", "1.4e0"],
            ["8.8e-3", "8.8e-2", "8.8e-1", "8.8e0", "8.8e1", "8.8e2", "8.8e3", "8.8e4", "8.8e5"],
            ["4.4e-8", "4.4e-7", "4.4e-6", "4.4e-5", "4.4e-4", "4.4e-3", "4.4e-2", "4.4e-1", "4.4e0"],
            ["4.7e-11", "4.7e-10", "4.7e-9", "4.7e-8", "4.7e-7", "4.7e-6", "4.7e-5", "4.7e-4", "4.7e-3"],
            ["1e-4", "1e-3", "1e-2", "1e-1", "1e0", "1e1", "1e2", "1e3", "1e4"],
            ["3e-7", "3e-6", "3e-5", "3e-4", "3e-3", "3e-2", "3e-1", "3e0", "3e1"],
            ["6e-12", "6e-11", "6e-10", "6e-9", "6e-8", "6e-7", "6e-6", "6e-5", "6e-4"],
            ["3.6e-15", "3.6e-14", "3.6e-13", "3.6e-12", "3.6e-11", "3.6e-10", "3.6e-9", "3.6e-8", "3.6e-7"],
            ["5e-14", "5e-13", "5e-12", "5e-11", "5e-10", "5e-9", "5e-8", "5e-7", "5e-6"],
            ["7.5e-10", "7.5e-9", "7.5e-8", "7.5e-7", "7.5e-6", "7.5e-5", "7.5e-4", "7.5e-3", "7.5e-2"],
            ["2e-8", "2e-7", "2e-6", "2e-5", "2e-4", "2e-3", "2e-2", "2e-1", "2e0"],
            ["5e-5", "5e-4", "5e-3", "5e-2", "5e-1", "5e0", "5e1", "5e2", "5e3"],
            ["6.5e-3", "6.5e-2", "6.5e-1", "6.5e0", "6.5e1", "6.5e2", "6.5e3", "6.5e4", "6.5e5"],
            ["2e-7", "2e-6", "2e-5", "2e-4", "2e-3", "2e-2", "2e-1", "2e0", "2e1"],
            ["3e-7", "3e-6", "3e-5", "3e-4", "3e-3", "3e-2", "3e-1", "3e0", "3e1"],
            ["1.4e-8", "1.4e-7", "1.4e-6", "1.4e-5", "1.4e-4", "1.4e-3", "1.4e-2", "1.4e-1", "1.4e0"],
            ["3.6e-9", "3.6e-8", "3.6e-7", "3.6e-6", "3.6e-5", "3.6e-4", "3.6e-3", "3.6e-2", "3.6e-1"]]

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
        "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]

df = pd.read_csv("zfp_results.csv",delimiter=",", index_col=0 ,dtype=str)
df.num_elements = df.num_elements.astype(int)
df.compression_ratio = df.compression_ratio.astype(float)
df.min_exp = df.min_exp.astype(int)
df.input_byte_size = df.input_byte_size.astype(float)
df.emax = df.emax.astype(int)

df_bp = pd.read_csv("bpbp_dist.csv",delimiter=",", index_col=0,dtype=str)
df_bp.aver = df_bp.aver.astype(float)

def zfp_cr_estimation(df,d_,relError):
    min_exp_ = df.min_exp[df.data == d_].values[0]
    dim_ = 1
    emax = df.emax[df.data == d_].values[0] 
    num_blocks_ = np.ceil(df.num_elements[df.data == d_].values[0]/4)
    input_size_ = df.input_byte_size[df.data == d_].values[0]
    cr_esti_ = []
    
    bpbp = df_bp.aver[df_bp.name == d_+"-"+relError[0]+".log"].values[0]
    
    if df.data_type[df.data == d_].values[0] == "double":
        coef_size = 12
    else:
        coef_size = 8
        
    for i in range(0,len(relError)):
        max_prec_ = emax - np.log2(np.float(relError[i])) + 2*(1+dim_)
        block_size_ = max_prec_ * bpbp + coef_size
        output_size_ = num_blocks_ * block_size_ /8
        cr_esti_.append(input_size_/output_size_)
            
    
    return cr_esti_

if __name__ == "__main__":
    for i in range(0,len(data)):
        orig = df.compression_ratio[df.data==data[i]].values[[0,2,4,6,8]]
        esti = np.array(zfp_cr_estimation(df,data[i],relError[i]))[[0,2,4,6,8]]
        print(data[i])
        print(df.compression_ratio[df.data==data[i]].values)
        print(np.array(zfp_cr_estimation(df,data[i],relError[i])))
        


