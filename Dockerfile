FROM node:latest

# Create app directory
WORKDIR /d/Documents/GitHub/basic-banking-system

COPY package*.json ./

RUN npm install

EXPOSE 3000

COPY . .

CMD [ "node", "app.js" ]
