#!/bin/bash

# Replace these variables with your actual values
HOST=localhost
USER=postgres
DATABASE=films
CSV_DIR=/Users/pythagoras/Desktop/Jigsaw_Labs_Bootcamp/flask_setup_lab/flask-setup-lab/backend/data

# load environment variables
if command -v dotenv &> /dev/null; then
  dotenv
else
  set -a
  [ -f .env ] && . .env
  set +a
fi

# Check if the directory exists
if [ ! -d "$CSV_DIR" ]; then
    echo "Directory not found: $CSV_DIR"
    exit 1
fi

# Check if the directory exists
if [ ! -d "$CSV_DIR" ]; then
    echo "Directory not found: $CSV_DIR"
    exit 1
fi

# Loop through all CSV files in the directory
for CSV_FILE in "$CSV_DIR"/*.csv; do
    
    # extract everything before .csv
    TABLE=$(basename "$CSV_FILE" .csv)

    echo "RUNNING: psql -h $HOST -U $USER -d $DATABASE -c \"\\COPY $TABLE FROM '$CSV_FILE' WITH CSV HEADER;\""
    # Construct the psql command
    PSQL_CMD="psql -h $HOST -U $USER -d $DATABASE -c \"\\COPY $TABLE FROM '$CSV_FILE' WITH CSV HEADER;\""

    # Execute the psql command
    eval "$PSQL_CMD"

    # Check the exit status of the psql command
    if [ $? -eq 0 ]; then
        echo "Data from $CSV_FILE copied successfully."
    else
        echo "Error copying data from $CSV_FILE."
    fi
done
