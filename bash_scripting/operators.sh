FIRST_PARAM=$1

#-z check if string is emtpy
if [[ -z $FIRST_PARAM ]]; then 
    echo "First parameter is an empty string"
#-n check if string is not emtpy
elif [[ -n $FIRST_PARAM ]]; then 
    echo "First parameter is not an empty string: $FIRST_PARAM"
fi

#-f check if file exists 
if [[ -f conditions.sh ]]; then 
    echo "file conditions.sh exists"
fi

#-d check if directory exists 
if [[ -d ../bash_scriptin ]]; then 
    echo "directory bash_scripting exists"
else
    echo "directory bash_scripting doesn't exist"
fi 

#return code of the previous command 
echo $?
