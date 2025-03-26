# front/Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

# Serve app with lightweight server
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]