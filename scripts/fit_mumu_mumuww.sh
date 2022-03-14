#bash

for P in T1
do
    ./bin/eftfun.py -m scan -a -p $P -c all -i configs/mumu_vbs/mumu_vbs_mumu.cfg
done