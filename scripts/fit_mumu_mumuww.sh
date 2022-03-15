#bash

for P in M0 M2 M4 M5 M7 T0 T1 T2 T5 T6 T7 S1
do
    ./bin/eftfun.py -m scan -a -p $P -c all -i configs/mumu_vbs/mumu_vbs_mumu.cfg
done