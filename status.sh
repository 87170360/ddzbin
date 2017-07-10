#!/bin/bash 

conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"

bin_dir="./bin/"

#normal_bull_nu=10
#grab_bull_nu=10  
hlddz_low_nu=1
hlddz_middle_nu=1
hlddz_high_nu=1
hlddz_master_nu=1
lzddz_low_nu=1
bsddz_low_nu=1

process_info=`ps -Af`

ps -Af  >temp.txt


#for ((i=0; i<$normal_bull_nu; i++)) 
#do 
	#name="${bin_dir}normal_bull -f ${conf_dir}normal_bull_low${i}.conf" 
	##echo $name
	#cat temp.txt | grep "$name" >/dev/null
	#if [[  $? == "0" ]]
	#then 
		#echo $name Start [[Running]] 
	#else 
		#echo $name Start Stopped
	#fi
#done 

#for ((i=0; i<$grab_bull_nu; i++)) 
#do 
	#name="${bin_dir}grab_bull -f ${conf_dir}grab_bull_low${i}.conf" 
	##echo $name
	#cat temp.txt | grep "$name" >/dev/null
	#if [[  $? == "0" ]]
	#then 
		#echo $name Start [[Running]] 
	#else 
		#echo $name Start Stopped
	#fi
#done 

#hlddz low
for ((i=0; i<$hlddz_low_nu; i++)) 
do 
	name="${bin_dir}hlddz -f ${conf_dir}hlddz_low${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 

#hlddz middle
for ((i=0; i<$hlddz_middle_nu; i++)) 
do 
	name="${bin_dir}hlddz -f ${conf_dir}hlddz_middle${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 

#hlddz high
for ((i=0; i<$hlddz_high_nu; i++)) 
do 
	name="${bin_dir}hlddz -f ${conf_dir}hlddz_high${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 

#hlddz master
for ((i=0; i<$hlddz_master_nu; i++)) 
do 
	name="${bin_dir}hlddz -f ${conf_dir}hlddz_master${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 

#lzddz
for ((i=0; i<$lzddz_low_nu; i++)) 
do 
	name="${bin_dir}lzddz -f ${conf_dir}lzddz_low${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 

#bsddz
for ((i=0; i<$bsddz_low_nu; i++)) 
do 
	name="${bin_dir}bsddz -f ${conf_dir}bsddz_low${i}.conf" 
	#echo $name
	cat temp.txt | grep "$name" >/dev/null
	if [[  $? == "0" ]]
	then 
		echo $name Start [[Running]] 
	else 
		echo $name Start Stopped
	fi
done 


#hlddz_robot low
name="${bin_dir}hlddz_robot -f ${bin_dir}hlddz_robot_low.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi

#hlddz_robot middle
name="${bin_dir}hlddz_robot -f ${bin_dir}hlddz_robot_middle.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi

#hlddz_robot high
name="${bin_dir}hlddz_robot -f ${bin_dir}hlddz_robot_high.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi

#hlddz_robot master
name="${bin_dir}hlddz_robot -f ${bin_dir}hlddz_robot_master.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi

#lzddz_robot
name="${bin_dir}lzddz_robot -f ${bin_dir}lzddz_robot.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi

#bsddz_robot
name="${bin_dir}bsddz_robot -f ${bin_dir}bsddz_robot.conf" 
cat temp.txt | grep "$name" >/dev/null
if [[  $? == "0" ]]
then 
    echo $name Start [[Running]] 
else 
    echo $name Start Stopped
fi
