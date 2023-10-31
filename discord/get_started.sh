#!/bin/bash

docker build . -t ai-chatbot:1.0

docker run -it --rm --net=host ai-chatbot:1.0 bash

