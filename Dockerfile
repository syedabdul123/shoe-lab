#!/bin/bash
set -euo pipefail

REMOTE="ec2-user@16.171.133.106"
IMAGE="flask-web:${BUILD_NUMBER}"
ARCHIVE="flask-web-${BUILD_NUMBER}.tar.gz"

trap 'rm -f "$ARCHIVE"' EXIT

echo "Building Docker image..."
docker build -t "$IMAGE" .

echo "Saving Docker image..."
docker save "$IMAGE" | gzip > "$ARCHIVE"

echo "Transferring image to EC2..."
scp -o BatchMode=yes -o StrictHostKeyChecking=yes \
    "$ARCHIVE" "${REMOTE}:/home/ec2-user/${ARCHIVE}"

echo "Starting deployment..."
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes \
    "$REMOTE" bash -s -- "$IMAGE" "$ARCHIVE" <<'REMOTE_SCRIPT'
set -euo pipefail

IMAGE="$1"
ARCHIVE="$2"
CONTAINER="flask-web"

docker load -i "/home/ec2-user/$ARCHIVE"
rm -f "/home/ec2-user/$ARCHIVE"

if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
    docker rm -f "$CONTAINER"
fi

docker run -d \
    --name "$CONTAINER" \
    --restart unless-stopped \
    -p 80:5000 \
    "$IMAGE"

for attempt in $(seq 1 15); do
    if curl --fail --silent --output /dev/null \
        --max-time 2 http://127.0.0.1/; then
        echo "AWS deployment successful"
        docker ps --filter "name=$CONTAINER"
        exit 0
    fi
    sleep 2
done

echo "Application did not respond"
docker logs "$CONTAINER"
exit 1
REMOTE_SCRIPT