#!/bin/sh

source .venv/bin/activate

# Default DB host will be used if DATABASE_HOST is not set
# DB_HOST=${DATABASE_HOST:-default_db_host}

# # Wait for the database server to be ready
# until nc -z -v -w30 $DB_HOST 3306
# do
#   echo "Waiting for database server to start..."
#   # Wait for 5 seconds before checking again
#   sleep 5
# done

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
exec gunicorn -b :5000 --access-logfile - --error-logfile - -c gunicorn_config.py microblog:app
