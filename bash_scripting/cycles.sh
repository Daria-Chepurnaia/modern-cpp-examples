for ((i=0; i<5; i++)); do 
    echo "Step $i"
done 

for i in {1..5}; do 
    echo "Step $i"
done 

count=0
while [[ $count -lt 5 ]]; do 
    echo "Loop $count"
    ((count++))
done 