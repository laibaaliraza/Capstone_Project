#!/bin/sh
PGPASSWORD=$POSTGRES_PASSWORD pg_dump -U $POSTGRES_USER -h db -d $POSTGRES_DB > /scripts/db_backup.sql
