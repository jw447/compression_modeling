import numpy as np
import pandas as pd

relError = ["1E-9", "1E-8", "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-2", "1E-1"]

data = ["astro.dat", "blast2_p.dat", "bump.dat", "dpot.dat", "eddy.dat",
        "fish.dat", "sedov_p.dat", "yf17_p.dat", "yf17_t.dat", "631-tst.bin.d64",
        "CLDICE_1_26_1800_3600.f32", "CLOUDf48.bin.f32", "einspline_115_69_69_288.f32", "sample_r_B_0.5_26.dat", "PRES-98x1200x1200.dat",
        "velocity_x.dat", "vx.dat2", "vx.f32", "xgc.3d.08100.dat", "stat_planar.2.9950E-03.field.mpi"]

mode="REL"

df = pd.read_csv("REL.csv",delimiter=",", index_col=0 ,dtype=str)
df.num_elements = df.num_elements.astype(float)
df.input_size = df.input_size.astype(float)
df.max_quant_intl = df.max_quant_intl.astype(float)
df.act_quant_intl = df.act_quant_intl.astype(float)
df.check_radius =  df.check_radius.astype(float)
df.realPrecision = df.realPrecision.astype(float)
df.node_count = df.node_count.astype(float)
df.curve_hit = df.curve_hit.astype(float)
df.curve_missed = df.curve_missed.astype(float)
df.hit_ratio = df.hit_ratio.astype(float)
df.tree_size = df.tree_size.astype(float)
df.encode_size = df.encode_size.astype(float)
df.leadNumaArray_size = df.leadNumaArray_size.astype(float)
df.exactMidBytes_size = df.exactMidBytes_size.astype(float)
df.residualMidBitsLength = df.residualMidBitsLength.astype(float)
df.outlier_size = df.outlier_size.astype(float)
df.output_size = df.output_size.astype(float)
df.compression_ratio = df.compression_ratio.astype(float)

print(df.head())

# read binary data
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


def hr_estimate(df, d_, relError):
    
    if df.data_type[df.data == d_].values[0] == " DOUBLE":
        d_data = read_dat_d(str("../inputdata/"+d_))
    elif df.data_type[df.data == d_].values[0] == " FLOAT":
        d_data = read_dat_f(str("../inputdata/"+d_))
    hr_esti=[df.hit_ratio[(df['data'] == d_) & (df['errBoundRatio'] == relError[0])].values[0]]
    
    for i in range(1,len(relError)):
        check_radius = df.check_radius[(df['data'] == d_) & (df['errBoundRatio'] == relError[i])].values[0]
        hit = 0
        prederr_esti = np.zeros(len(d_data))
        for j in range(2,len(d_data)):
            prederr_esti = d_data[j] - (2*d_data[j-1] - d_data[j-2])
            if (abs(prederr_esti) <= check_radius): # Hit
                hit = hit+1     
        hr_esti.append(hit/len(d_data))
    del d_data
    return hr_esti


# Hit ratio estimation to file
Hr_e = []
for i in range(0,len(data)):
    print(data[i])
    Hr_e.append([hr_estimate(df,data[i],relError)])

hr_df = pd.DataFrame(data={"name":data,"value":Hr_e})
print(hr_df)
hr_df.to_csv("hit_ratio_estimation.csv",sep=",",encoding="utf-8")


