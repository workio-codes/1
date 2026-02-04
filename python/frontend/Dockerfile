FROM node:18-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install

# Fix permission issues:
RUN chmod -R +x node_modules/.bin

# Copy remaining files and build
COPY . .
RUN chmod -R +x node_modules/.bin && npm run build
RUN ls -l node_modules/.bin/vite
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
