#DOCKERFILE--
FROM node:14-alpine
#copiar archivos de la aplicación
COPY . /app/
#establecer el directorio de trabajo
WORKDIR /app
#instalar express y mongoose
RUN npm install express@4.19.2 mongoose@5.13.2
#comando para iniciar la aplicación
CMD [ "node", "server.js" ]