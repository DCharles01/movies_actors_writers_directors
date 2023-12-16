#!/bin/bash
CSV_DIR="../data"
# check if any csv file exists
shopt -s nullglob
csv_files=("$CSV_DIR"/*.csv)
shopt -u nullglob

if [ ${#csv_files[@]} -eq 0 ]; then
    echo "No CSV files found in $CSV_DIR"
    exit 1
fi


for CSV_FILE in "$CSV_DIR"/*.csv; do 
    DB_FILE="films.db"
    OUTPUT="../data/"
    FULL_OUTPUT=$OUTPUT$CSV_FILE
    TABLE=$(basename "$CSV_FILE")
    sqlite3 "$DB_FILE" \
    -cmd ".headers on" \
    -cmd ".mode csv" \
    -cmd ".output $FULL_OUTPUT" \
    -cmd "select * from ${TABLE%.csv}"

done

# Detach the auxiliary database
sqlite3 "$DB_FILE" -cmd ".quit"
