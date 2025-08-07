FROM alpine:latest

# Install necessary packages (replace 'cron' with 'dcron')
RUN apk update && apk add --no-cache bash curl git tzdata postgresql-client dcron

# Set working directory
WORKDIR /backup

# Copy backup script
COPY backup.sh /backup/backup.sh

# Make the script executable
RUN chmod +x /backup/backup.sh

# Copy crontab file
COPY crontab.txt /etc/crontabs/root

# Start the cron daemon
CMD ["sh", "-c", "crond -f"]
