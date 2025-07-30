# Etapa 1: Build da aplicação React
FROM node:18 as builder


RUN npm install
RUN npm run build

# Etapa 2: Servir os arquivos com Nginx
FROM nginx:alpine

# Copia o build do React para o diretório padrão do Nginx
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
