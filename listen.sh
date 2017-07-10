#!/bin/bash 

conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"

bin_dir="./bin/"
crash_dir="./crash"

normal_bull_low_nu=10
grab_bull_low_nu=10


process_info=`ps -Af`
output_dev="crash/run.csh"


while true 
do 
	ps -Af  >temp.txt
	echo `date` start listening 

	#normal bull  low 
	for ((i=0; i<$normal_bull_low_nu; i++)) 
	do 
		name="${bin_dir}normal_bull -f ${conf_dir}normal_bull_low${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 

	#grab bull low 
	for ((i=0; i<$grab_bull_low_nu; i++)) 
	do 
		name="${bin_dir}grab_bull -f ${conf_dir}grab_bull_low${i}.conf" 
		#echo $name
		cat temp.txt | grep "$name" >${output_dev}
		if [[  $? -ne "0" ]]
		then 
			echo `date` $name [[Crach]] Restart
			$name>>${output_dev} &
		fi
	done 



	sleep 30
done 


