# Fase de build - Node.js
FROM node:18 AS builder

# Diretório de trabalho
WORKDIR /app


# 2. Limpar cache e instalar dependências
RUN npm cache clean --force && npm install

# 3. Copiar o restante do código
COPY . .

# 4. Build da aplicação
RUN npm run build

# Fase de execução - Nginx
FROM nginx:stable-alpine

# Remover configuração padrão do Nginx
RUN rm -rf /etc/nginx/conf.d/default.conf

# Copiar arquivos de build
COPY --from=builder /app/build /usr/share/nginx/html

# Copiar configuração customizada do Nginx
COPY nginx.conf /etc/nginx/conf.d

# Expor a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]