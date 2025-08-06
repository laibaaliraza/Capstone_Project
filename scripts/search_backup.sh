#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M)
PGPASSWORD="password" pg_dump -U postgres -h db capstone > /data/backup_$DATE.sql
