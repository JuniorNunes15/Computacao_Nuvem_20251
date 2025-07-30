# Substitua o Dockerfile atual por este:
FROM node:18

# Diretório de trabalho
WORKDIR /app

# 1. Copiar apenas arquivos de dependência
COPY package*.json ./

# 2. Limpar cache e instalar dependências
RUN npm cache clean --force && npm install

# 3. Copiar o restante do código
COPY . .

# 4. Build da aplicação (se necessário)
RUN npm run build

# Expor a porta
EXPOSE 80

CMD ["npm", "run", "start"]