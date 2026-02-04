FROM node:18-bullseye AS build

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install

# Copy remaining files and build
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
