# Etapa de construcción
FROM node:18-alpine AS build

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Etapa de producción: servidor web estático
FROM nginx:stable-alpine

# Copiar los archivos compilados al directorio de Nginx
COPY --from=build /usr/src/app/build /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto
CMD ["nginx", "-g", "daemon off;"]
