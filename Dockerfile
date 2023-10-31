FROM node:17

RUN apt update
RUN apt install -y g++ make python python-dev

WORKDIR /app

COPY . .
RUN pip install -r /app/server/requirements.txt
RUN npm i

CMD node main.js > /tmp/discord-log.txt