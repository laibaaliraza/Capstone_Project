#!/bin/bash
set -e

while getopts ":d:ir" opt; do
    case $opt in
    d) DATA="$OPTARG" ;;       # If -d is passed, store the argument in $DATA
    i) INCREMENTAL=1 ;;        # If -i is passed, set a flag to enable incremental
    r) ROTATE=1 ;;             # If -r is passed, set a flag to enable rotation
    *) echo "Invalid option"; exit 1 ;;  # Any unknown option -> error
  esac
done

DATE=$(date +%Y%m%d)
DEST="$DATA/incremental-$DATE"
mkdir -p "$DEST"
#Connects to PostgreSQL.
cp -r /var/lib/postgresql/data/* "$DEST"
#Saves output as a .sql file inside /backups and return backup complete msg
echo "Backup completed at $DEST"




