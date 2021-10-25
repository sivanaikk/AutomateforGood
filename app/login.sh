#echo "/app/pem/$2" "$3@$1"
ssh -i "/app/pem/$2" "$3@$1" date
a=$?
#echo $a
if [ $a == 0 ]

then
#echo "Failed"
touch /app/decision/login

fi
