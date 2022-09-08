#!/gpfs/alpine/proj-shared/csc143/jwang/python-tf/bin/python

import numpy as np

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
         "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
         "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
         "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]
#data = ["einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
#        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]
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

for i in range(0,len(data)):
    for j in range(0,len(relError[i])):
        print(data[i]+"-"+str(relError[i][j])+".log")
        with open("../../log/Accuracy/"+data[i]+"-"+str(relError[i][j])+".log") as log:
            l_data = log.readlines()
        
        block_size_ = []
        for line in l_data:
            if "block_size = " in line:
                #print(line)
                if len(line.split("block_size = ")) == 2:
                    block_size_.append(np.int(line.split("block_size = ",2)[1].replace("\n","")))
        print(np.histogram(block_size_))

