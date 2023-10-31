#!/bin/bash

docker build . -t ai-chatbot:1.01 -f Dockerfile-local

docker run -dt --net=host --rm --volume $(pwd):/app --name ai-chatbot-local ai-chatbot:1.01 
docker exec -it ai-chatbot-local pip install -r /app/server/requirements.txt
docker exec -it ai-chatbot-local npm i
docker exec -it ai-chatbot-local bash

