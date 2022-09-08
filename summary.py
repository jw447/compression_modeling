#!/usr/bin/bash

import numpy as np
import pandas as pd

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat"]

relError = ["1E-9", "1E-8", "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]

log_dir="log"

data_ = []
errBoundRatio_ = []
input_size_ = []
max_quant_intl_  = []
check_radius_ = []
hit_ = []
missed_ = []
hit_ratio_ = []
node_count_ = []
node_count_esti_ = []
tree_size_ = []
encode_size_ = []
outlier_size_ = []
output_size_ = []
compression_ratio_ = []

for d_ in data:
    print(d_)
    for eb_ in relError:
        data_.append(d_)
        errBoundRatio_.append(eb_)
        
        with open(str(log_dir+"/sz/"+d_+"-"+eb_+".log"),"r") as log:
            for line in log.readlines():
                if "Num of elements:" in line:
                    line = line.replace("\n","")
                    num_elements_.append(line.split("\t",2)[1])
                if "Input file size:" in line:
                    line = line.replace("\n","")
                    input_size_.append(line.split(":",2)[1])
                if "(max)intvCapacity=" in line:
                    line = line.replace("\n","")
                    max_quant_intl_.append(line.split("=",2)[1])
                if "checkradius" in line:
                    line = line.replace("\n","")
                    check_radius_.append(line.split("=",2)[1])
                if "count_hit" in line:
                    line = line.replace("\n","")
                    hit_.append(line.split("=",2)[1])
                if "count_missed" in line:
                    line = line.replace("\n","")
                    missed_.append(line.split("=",2)[1])
                    hit_ratio_.append(np.float(hit_[-1])/(np.float(hit_[-1])+np.float(missed_[-1])))
                if "nodeCount=" in line:
                    line = line.replace("\n","")
                    node_count_.append(line.split("=",2)[1])
                    node_count_esti_.append(int(line.split("=",2)[1]) -1)
                if "encodeSize=" in line:
                    line = line.replace("\n","")
                    encode_size_.append(line.split("=",2)[1])
                if "treeByteSize=" in line:
                    line = line.replace("\n","")
                    tree_size_.append(line.split("=",2)[1])
                if "outlierSize=" in line:
                    line = line.replace("\n","")
                    outlier_size_.append(line.split("=",2)[1])
                if "Output file size:" in line:
                    line = line.replace("\n","")
                    output_size_.append(line.split(":",2)[1])
                if "sz compression ratio:" in line:
                    line = line.replace("\n","")
                    compression_ratio_.append(line.split(":",2)[1])
            print([len(errBoundRatio_ ),len(input_size_ ),len(max_quant_intl_  ),len(check_radius_),
                len(node_count_ ),len(hit_ratio_ ),len(tree_size_ ),len(encode_size_ ),len(outlier_size_),
                len(output_size_),len(compression_ratio_),len(data_)])

# print(len(qf))
df = pd.DataFrame({"data": data_,
    "errBoundRatio": errBoundRatio_,
    "input_size": input_size_,
    "max_quant_intl": max_quant_intl_,
    "check_radius": check_radius_,
    "node_count": node_count_,
    "node_count_esti": node_count_esti_,
    "curve_hit": hit_,
    "curve_missed": missed_,
    "hit_ratio": hit_ratio_,
    "tree_size": tree_size_,
    "encode_size": encode_size_,
    "outlier_size": outlier_size_,
    "output_size": output_size_,
    "compression_ratio": compression_ratio_
    })

print(df.head())
df.to_csv(str("sz_results.csv"), sep=",", encoding='utf-8')
