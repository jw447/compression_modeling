#!/bin/bash

###############################
##### Run SZ-1.4.9 ############
#####  Sep-05-2019 ############
###############################

# SZ parameters:
cfg="sz.config"

# env
input_dir="inputdata"
log_dir="log"

#sz=/home/jon/local_build/sz-1.4.9/install/bin/sz

relError=(1E-9)
# eb_=1E-9
data=("astro.dat" "blast2_p.dat" "bump.dat" "dpot.dat" "eddy.dat" "fish.dat" "sedov_p.dat" "yf17_p.dat" "yf17_t.dat")

for eb_ in "${relError[@]}";do

  # ===============================================================================================================================
  for d in "${data[@]}"; do
    echo $d
    log_="$log_dir/sz/$d-$eb_.log"
    /home/jon/local_build/LossyCompressStudy/SZ/example/testdouble_compress sz.config $input_dir/$d `expr $(stat -c%s "$input_dir/$d") / 8` &> $log_

    #$sz -z -d -c $cfg -i $input_dir/$d -1 `expr $(stat -c%s "$input_dir/$d") / 8` &> $log_
    inputFILESIZE=$(stat -c%s $input_dir/$d)
    outputFILESIZE=$(stat -c%s $input_dir/$d".sz")
    echo "Input file size: $inputFILESIZE" &>> $log_
    echo "Output file size: $outputFILESIZE" &>> $log_
    echo "$inputFILESIZE $outputFILESIZE" | awk '{printf "sz compression ratio: %.5f\n", $1/$2}' &>> $log_
  done
done


# echo "Brown"
# d_=sample_r_B_0.5_26.dat
# output_="$output_dir/$mode/$d_-$eb_.sz"
# log_="$log_dir/$mode/$d_-$eb_.log"
#
# echo "relative error bound at $eb_" &> $log_
# $sz -d -c $cfg -M $mode -R $eb_ -i $input_dir/$d_ -1 8388609 -z $output_ &>> $log_ 2> "$log_dir/$mode/$d_-$eb_-qf.txt"
# $sz -p -s $output_ &>> $log_
#
# inputFILESIZE=$(stat -c%s $input_dir/$d_)
# outputFILESIZE=$(stat -c%s $output_)
# echo "Input file size: $inputFILESIZE" &>> $log_
# echo "Output file size: $outputFILESIZE" &>> $log_
# echo "$inputFILESIZE $outputFILESIZE" | awk '{printf "sz compression ratio: %.5f\n", $1/$2}' &>> $log_
#
#
# echo "EXAALT"
# d_=vx.dat2
# output_="$output_dir/$mode/$d_-$eb_.sz"
# log_="$log_dir/$mode/$d_-$eb_.log"
#
# echo "relative error bound at $eb_" &> $log_
# $sz -f -c $cfg -M $mode -R $eb_ -i $input_dir/$d_ -1 2869440 -z $output_ &>> $log_ 2> "$log_dir/$mode/$d_-$eb_-qf.txt"
# $sz -p -s $output_ &>> $log_
#
# inputFILESIZE=$(stat -c%s $input_dir/$d_)
# outputFILESIZE=$(stat -c%s $output_)
# echo "Input file size: $inputFILESIZE" &>> $log_
# echo "Output file size: $outputFILESIZE" &>> $log_
# echo "$inputFILESIZE $outputFILESIZE" | awk '{printf "sz compression ratio: %.5f\n", $1/$2}' &>> $log_
#
# echo "NYX"
# d_=velocity_x.dat
# output_="$output_dir/$mode/$d_-$eb_.sz"
# log_="$log_dir/$mode/$d_-$eb_.log"
#
# echo "relative error bound at $eb_" &> $log_
# $sz -f -c $cfg -M $mode -R $eb_ -i $input_dir/$d_ -1 134217728 -z $output_ &>> $log_ 2> "$log_dir/$mode/$d_-$eb_-qf.txt"
# $sz -p -s $output_ &>> $log_
#
# inputFILESIZE=$(stat -c%s $input_dir/$d_)
# outputFILESIZE=$(stat -c%s $output_)
# echo "Input file size: $inputFILESIZE" &>> $log_
# echo "Output file size: $outputFILESIZE" &>> $log_
# echo "$inputFILESIZE $outputFILESIZE" | awk '{printf "sz compression ratio: %.5f\n", $1/$2}' &>> $log_
