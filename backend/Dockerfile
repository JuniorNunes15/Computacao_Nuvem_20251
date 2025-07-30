FROM python:3.12.3

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos do backend
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt --break-system

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar a API
CMD ["python", "app.py"]
