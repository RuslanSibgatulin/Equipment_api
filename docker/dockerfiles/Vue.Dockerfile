FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY ./frontend/vue-app/package*.json ./

RUN npm install

COPY ./frontend/vue-app .

RUN npm run build

CMD [ "http-server", "dist" ]