#!/usr/bin/bash

import numpy as np
import pandas as pd

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
        "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]

relError = ["1E-9", "1E-8", "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]
#relError = ["1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]
# data=["sample_r_B_0.5_26.dat"]
# relError=["1E-9", "1E-8"]

mode="REL"

log_dir="../log"

data_ = []
num_elements_ = []
data_type_ = []
errBoundMode_ = []
errBoundRatio_ = []
input_size_ = []
max_quant_intl_  = []
act_quant_intl_ = []
check_radius_ = []
realPrecision_ = []
hit_ = []
missed_ = []
hit_ratio_ = []
# qf = []
node_count_ = []
tree_size_ = []
encode_size_ = []
leadNumaArray_size_ = []
exactMidBytes_size_ = []
residualMidBitsLength_ = []
outlier_size_ = []
output_size_ = []
compression_ratio_ = []

for d_ in data:
    print(d_)
    for eb_ in relError:
        # print(str(log_dir+mode+"/"+d_+"-"+mode+"-"+eb_+".log"))
        data_.append(d_)
        errBoundMode_.append(mode)
        errBoundRatio_.append(eb_)
        # qf_ = []
        with open(str(log_dir+"/"+mode+"/"+d_+"-"+eb_+".log"),"r") as log:
            for line in log.readlines():
                if "Num of elements:" in line:
                    line = line.replace("\n","")
                    num_elements_.append(line.split("\t",2)[1])
                if "Data type:" in line:
                    line = line.replace("\n","")
                    data_type_.append(line.split("\t",2)[1])
                if "Input file size:" in line:
                    line = line.replace("\n","")
                    input_size_.append(line.split(":",2)[1])
                if "max_quant_intervals" in line:
                    line = line.replace("\n","")
                    max_quant_intl_.append(line.split("\t",2)[1])
                if "checkradius" in line:
                    line = line.replace("\n","")
                    check_radius_.append(line.split("=",2)[1])
                if "realPrecision" in line:
                    line = line.replace("\n","")
                    realPrecision_.append(line.split(":",2)[1])
                if "actual used # intervals:" in line:
                    line = line.replace("\n","")
                    act_quant_intl_.append(line.split("\t",2)[1])
                if "count_hit" in line:
                    line = line.replace("\n","")
                    hit_.append(line.split("=",2)[1])
                if "count_missed" in line:
                    line = line.replace("\n","")
                    missed_.append(line.split("=",2)[1])
                    hit_ratio_.append(np.float(hit_[-1])/(np.float(hit_[-1])+np.float(missed_[-1])))
                    #print(hit_ratio_[-1])
               # if "*" in line:
                #     line = line.replace("\n","")
                #     qf_.append(line.split("*",2)[1])
                if "nodeCount=" in line:
                    line = line.replace("\n","")
                    node_count_.append(line.split("=",2)[1])
                if "encodeSize=" in line:
                    line = line.replace("\n","")
                    encode_size_.append(line.split("=",2)[1])
                if "treeByteSize=" in line:
                    line = line.replace("\n","")
                    tree_size_.append(line.split("=",2)[1])
                if "tdps->leadNumArray_size=" in line:
                    line = line.replace("\n","")
                    leadNumaArray_size_.append(line.split("=",2)[1])
                if "tdps->exactMidBytes_size=" in line:
                    line = line.replace("\n","")
                    exactMidBytes_size_.append(line.split("=",2)[1])
                if "residualMidBitsLength=" in line:
                    line = line.replace("\n","")
                    residualMidBitsLength_.append(line.split("=",2)[1])
                if "outlierSize=" in line:
                    line = line.replace("\n","")
                    outlier_size_.append(line.split("=",2)[1])
                if "Output file size:" in line:
                    line = line.replace("\n","")
                    output_size_.append(line.split(":",2)[1])
                if "sz compression ratio:" in line:
                    line = line.replace("\n","")
                    compression_ratio_.append(line.split(":",2)[1])
        # qf.append(qf_)
            print([len(num_elements_ ),len(data_type_ ),len(errBoundMode_ ),
                len(errBoundRatio_ ),len(input_size_ ),len(max_quant_intl_  ),
                len(act_quant_intl_ ),len(check_radius_),len(node_count_ ),len(hit_ratio_ ),
                len(tree_size_ ),len(encode_size_ ),len(leadNumaArray_size_ ),
                len(exactMidBytes_size_ ),len(residualMidBitsLength_ ),len(outlier_size_),
                len(output_size_),len(compression_ratio_),len(data_)])

# print(len(qf))
df = pd.DataFrame({"data": data_,
    "num_elements": num_elements_,
    "data_type": data_type_,
    "errBoundMode": errBoundMode_,
    "errBoundRatio": errBoundRatio_,
    "input_size": input_size_,
    "max_quant_intl": max_quant_intl_,
    "act_quant_intl": act_quant_intl_,
    "check_radius": check_radius_,
    "realPrecision": realPrecision_,
    "node_count": node_count_,
    "curve_hit": hit_,
    "curve_missed": missed_,
    "hit_ratio": hit_ratio_,
    # "qf": qf,
    "tree_size": tree_size_,
    "encode_size": encode_size_,
    "leadNumaArray_size": leadNumaArray_size_,
    "exactMidBytes_size": exactMidBytes_size_,
    "residualMidBitsLength": residualMidBitsLength_,
    "outlier_size": outlier_size_,
    "output_size": output_size_,
    "compression_ratio": compression_ratio_
    })

print(df.head())
df.to_csv(str(mode+".csv"), sep=",", encoding='utf-8')
