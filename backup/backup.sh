#!/bin/sh
set -e

STAMP=$(date +"%Y%m%d_%H%M%S")
OUT="/backup/${POSTGRES_DB}_${STAMP}.sql"

echo "📦  Starting pg_dump → $OUT"
PGPASSWORD="$POSTGRES_PASSWORD" \
  pg_dump -U "$POSTGRES_USER" -h "$POSTGRES_HOST" -d "$POSTGRES_DB" > "$OUT"
echo "✅  Backup complete"