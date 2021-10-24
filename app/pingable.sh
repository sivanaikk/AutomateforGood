ping $1 -c 2 
a=$?
#echo $a
if [ $a == 0 ]

then
#echo "Failed"
touch /app/decision/pingable

fi
