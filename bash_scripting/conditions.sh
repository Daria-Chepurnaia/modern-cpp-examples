FIRST_PARAM=$1
if [[ $# -lt 1 ]]; then 
    echo "command should contain at least one parameter"
    exit 1
else 
    echo "First parameter is $FIRST_PARAM"
fi    

# -eq	(equal)
# -ne	(not equal)
# -lt	(less than)
# -le	(less than or equal)
# -gt	(greater than)
# -ge	(greater than or equal)