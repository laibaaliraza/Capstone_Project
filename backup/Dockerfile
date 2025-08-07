FROM alpine:3.20

# Only the tools you really need
RUN apk add --no-cache bash tzdata postgresql-client dcron

WORKDIR /backup

# Backup script
COPY backup.sh /backup/backup.sh
RUN chmod +x /backup/backup.sh

# Root’s crontab – one full dump every night at 03:00
COPY crontab.txt /etc/crontabs/root

# Run cron in foreground (PID 1)
ENTRYPOINT ["crond","-f","-l","8"]