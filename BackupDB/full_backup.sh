#!/bin/bash
# database details
DB_NAME="pgblacklistdb"
DB_USER="postgres"
DB_PASS="PgBlackList202314"
DB_HOST="localhost"
DB_PORT="5432"

# create a backup file name
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_FILE="db_backup_${TIMESTAMP}.sql"

# connect to the database and create a backup
PGPASSWORD=$DB_PASS pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -F p -f $BACKUP_FILE -n public -W $DB_NAME

# compress the backup file
gzip -f $BACKUP_FILE

# remove original backup file
rm -f $BACKUP_FILE

echo "Backup file: $BACKUP_FILE.gz created successfully"