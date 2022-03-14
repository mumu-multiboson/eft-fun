#bash

for P in T0 T1 T2 S0 S1 M7 M1 M0
do
    ./bin/eftfun.py -m scan -a -p $P -c all -i configs/mumu_vbs/mumu_vbs_nunu.cfg
done