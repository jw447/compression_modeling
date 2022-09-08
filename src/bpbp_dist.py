#!/gpfs/alpine/proj-shared/csc143/jwang/python-tf/bin/python

import numpy as np
import os

#data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
#        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
#        "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
#        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]

data = ["stat_planar.2.9950E-03.field.mpi"]
def bpbp_h(fname):
    flist = os.listdir("../../log/Accuracy_bpbp/")

    for f in flist:
        if(f.startswith(fname)):
            print(f)
            with open("../../log/Accuracy_bpbp/"+f,"r") as fdata:
                bpbp_ = []
                for line in fdata.readlines():
                    if "#" in line:
                        bpbp_.append(np.int(line.split("#")[1].replace("\n","")))
                print(np.histogram(bpbp_,[0,1.5,2.5,3.5,4.5,5.5,6.5,7.5]))

for d in data:
    bpbp_h(d)
