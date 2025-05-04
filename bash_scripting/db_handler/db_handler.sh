INPUT_FILE="people.csv"
OUTPUT_FILE="filtered.csv"

head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"

tail -n +2 "$INPUT_FILE" | tr -d '\r' | while IFS=',' read -r name surname age city; do
    if (( age > 25 )); then 
        echo "$name,$surname,$age,$city" >> "$OUTPUT_FILE"
    fi
done

echo "filtration has been completed"