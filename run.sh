conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"
bin_dir="./bin/"
crash_dir="./crash"

hlddz_low_num=1
hlddz_middle_num=1
hlddz_high_num=1
hlddz_master_num=1
lzddz_low_num=1
bsddz_low_num=1

output_dev="crash/run.csh"

#check dir exist 
for dir in $conf_dir $pid_dir $log_dir $crash_dir;
do
	if [ ! -d "$dir" ]
	then 
		echo "Create Dir $dir"
		mkdir $dir 
	fi
done 

#start  hlddz low 
for ((i=0; i<$hlddz_low_num; i++)) 
do 
	echo "Start ${bin_dir}hlddz -f  ${conf_dir}hlddz_low${i}.conf"
	${bin_dir}hlddz -f ${conf_dir}hlddz_low${i}.conf>>${output_dev} &
done 

#start  hlddz middle 
for ((i=0; i<$hlddz_middle_num; i++)) 
do 
	echo "Start ${bin_dir}hlddz -f  ${conf_dir}hlddz_middle${i}.conf"
	${bin_dir}hlddz -f ${conf_dir}hlddz_middle${i}.conf>>${output_dev} &
done 

#start  hlddz high 
for ((i=0; i<$hlddz_high_num; i++)) 
do 
	echo "Start ${bin_dir}hlddz -f  ${conf_dir}hlddz_high${i}.conf"
	${bin_dir}hlddz -f ${conf_dir}hlddz_high${i}.conf>>${output_dev} &
done 

#start  hlddz master 
for ((i=0; i<$hlddz_master_num; i++)) 
do 
	echo "Start ${bin_dir}hlddz -f  ${conf_dir}hlddz_master${i}.conf"
	${bin_dir}hlddz -f ${conf_dir}hlddz_master${i}.conf>>${output_dev} &
done 

#start  lzddz low 
for ((i=0; i<$lzddz_low_num; i++))
do
    echo "Start ${bin_dir}lzddz -f  ${conf_dir}lzddz_low${i}.conf"
    ${bin_dir}lzddz -f ${conf_dir}lzddz_low${i}.conf>>${output_dev} &
done
      
#start  bsddz low 
for ((i=0; i<$bsddz_low_num; i++))
do
    echo "Start ${bin_dir}bsddz -f  ${conf_dir}bsddz_low${i}.conf"
    ${bin_dir}bsddz -f ${conf_dir}bsddz_low${i}.conf>>${output_dev} &
done
