#!/bin/sh

source .venv/bin/activate

# Wait for the database server to be ready
until nc -z -v -w30 db 3306
do
  echo "Waiting for database server to start..."
  # Wait for 5 seconds before checking again
  sleep 5
done

# Run the database upgrade
while true; do
    flask db upgrade 2>&1

    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "Upgrade command failed, retrying in 5 secs..."
    sleep 5
done

# Start the Gunicorn server and listen on port 5000
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
