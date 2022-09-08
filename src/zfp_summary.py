#!/home/jon/anaconda3/bin/python
import numpy as np
import pandas as pd

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
        "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]

#data = ["vx.dat2"]

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

#relError = [["2e-7","2e-6","2e-5","2e-4","2e-3","2e-2","2e-1","2e0","2e1"]]
# log_dir="../../log"

data_ = []
errBoundMode_ = []
num_elements_ = []
data_type_ = []
errBoundRatio_ = []
input_byte_size_ = []
output_byte_size_ = []
compression_ratio_ = []
total_block_bit_size_ = []
min_exp_ = []

for i in range(0,len(data)):
    print(data[i])
    for j in range(0,len(relError[i])):
        print("error bound: ",relError[i][j])
        data_.append(data[i])
        errBoundMode_.append("Accuracy")
        errBoundRatio_.append(relError[i][j])
        block_size_ = 0
        with open("../../log/Accuracy/"+str(data[i]+"-"+str(relError[i][j])+".log"),"r") as log:
            for line in log.readlines():
                if "nx=" in line:
                    num_elements_.append(line.split("=")[1].replace("\n",""))
                if "raw=" in line:
                    input_byte_size_.append(line.split("=")[1].replace("\n",""))
                if "zfp=" in line:
                    output_byte_size_.append(line.split("=")[1].replace("\n",""))
                if "type=" in line:
                    data_type_.append(line.split("=")[1].replace("\n",""))
                if "ratio=" in line:
                    compression_ratio_.append(line.split("=")[1].replace("\n",""))
                #if "totalsize" in line:
                #    total_block_bit_size_.append(np.int(line.split(":")[1].replace("\n","")))
                if "minexp" in line:
                    min_exp_.append(line.split(":")[1].replace("\n",""))
                if "block_size = " in line:
                    block_size_ = block_size_ + np.int(line.split(" = ")[1])
        total_block_bit_size_.append(block_size_)
    print(len(data_),len(errBoundMode_),len(num_elements_),
            len(data_type_),len(errBoundRatio_),len(input_byte_size_),
            len(output_byte_size_),len(compression_ratio_),len(min_exp_),len(total_block_bit_size_))

df = pd.DataFrame({"data": data_,
    "errBoundMode": errBoundMode_,
    "num_elements": num_elements_,
    "data_type": data_type_,
    "errBoundRatio": errBoundRatio_,
    "input_byte_size": input_byte_size_,
    "output_byte_size": output_byte_size_,
    "compression_ratio": compression_ratio_,
    "block_size_bit": total_block_bit_size_,
    "min_exp": min_exp_})

print(df)
df.to_csv("zfp_summary.csv", sep=",", encoding='utf-8')
