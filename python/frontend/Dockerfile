FROM node:18-bullseye AS build

WORKDIR /app
RUN chmod -R 777 /app
COPY package.json package-lock.json* ./
RUN npm config set cache /tmp --global
RUN npm install

# Copy remaining files and build
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
