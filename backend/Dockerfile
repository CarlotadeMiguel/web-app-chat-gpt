# 1. Imagen base: Python ligero
FROM python:3.11-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar sólo requirements y aislar la capa de dependencias
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código de la aplicación
COPY . .

# 6. Variables de entorno
#    Ajusta según tu .env.example
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
# Si usas Redis, MAIL, etc. añade aquí
# ENV REDIS_URL=redis://redis:6379/0

# 7. Exponer el puerto de Flask
EXPOSE 5000

# 8. Comando por defecto
CMD ["flask", "run", "--host=0.0.0.0"]
