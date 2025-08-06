# Use Alpine base image
FROM alpine

# Install necessary packages
RUN apk update && apk add --no-cache bash curl git tzdata postgresql-client cron

# Set working directory
WORKDIR /scripts

# Copy backup script and cron job
COPY ../scripts/search_backup.sh .
COPY ../scripts/cronjob /etc/crontabs/root

# Make script executable
RUN chmod +x /scripts/search_backup.sh

# Set timezone if needed (optional)
ENV TZ=Asia/Karachi

# Start cron in foreground (this is important!)
CMD [ "crond", "-1", "2", "-f" ]
