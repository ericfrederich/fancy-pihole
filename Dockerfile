FROM pihole/pihole:latest

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
RUN apt-get update && apt-get install -y \
    python3 \
    python3-bottle \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8080

ADD s6/debian-root /
