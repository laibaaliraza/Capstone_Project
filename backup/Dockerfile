
#Builds a minimal Alpine container
FROM alpine
RUN apk add bash git
# Copies backup.sh 
COPY search_backup.sh /scripts/search_backup.sh
# Sets it to run on container start.
RUN chmod +x /scripts/search_backup.sh
CMD ["tail", "-f", "/dev/null"]


