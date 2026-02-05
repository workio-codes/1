# ---- build stage ----
FROM node:18-alpine AS build
WORKDIR /app

# Install dependencies
COPY frontend/package*.json ./
RUN npm ci

# Copy source and build
COPY . .
RUN npm run build

# ---- run stage (nginx) ----
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
