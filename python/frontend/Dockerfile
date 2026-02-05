# ---- build stage ----
FROM node:18-alpine AS build
WORKDIR /app

# Because build context is the project root (.), copy from frontend/
COPY frontend/package*.json ./
RUN npm ci

# Copy the rest of the frontend source into /app
COPY frontend/ ./
# Optional: verify files are indeed here (helps debug)
RUN echo "== Listing /app after COPY ==" && ls -la && \
    echo "== Show top of index.html ==" && head -n 5 index.html || true

# Build (Vite will look for /app/index.html by default)
RUN npm run build

# ---- run stage (nginx) ----
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
