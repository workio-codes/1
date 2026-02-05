# ---- Build stage ----
FROM node:18-alpine AS build
WORKDIR /app

# Install deps
COPY frontend/package*.json ./
RUN npm ci

# Copy source and build (Vite)
COPY frontend/ ./
RUN npm run build

# ---- Serve stage (Nginx with API proxy) ----
FROM nginx:alpine

# Copy compiled app to Nginx web root
COPY --from=build /app/dist /usr/share/nginx/html

# Copy our proxy config so /api goes to the backend container
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
