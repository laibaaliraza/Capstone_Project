# Use Alpine base image
FROM alpine

# Install necessary packages
RUN apk update && apk add --no-cache bash curl git tzdata postgresql-client cron

# Set working directory
WORKDIR /scripts

# Copy backup script and cron job from local context
COPY backup/search_backup.sh .
COPY backup/cronjob /etc/crontabs/root

# Make the script executable
RUN chmod +x /scripts/search_backup.sh

# Set timezone (optional)
ENV TZ=Asia/Karachi

# Start cron in the foreground
CMD ["crond", "-f"]
