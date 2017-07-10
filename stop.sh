for pid in `ls pid| grep pid` ;
do 
	echo "Kill "$pid
	kill -s KILL `cat pid/$pid`
done 


