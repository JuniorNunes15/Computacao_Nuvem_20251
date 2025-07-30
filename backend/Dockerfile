FROM python:3.12.3

WORKDIR /app

# Instalar versão específica do pip e limpar cache
RUN pip install --no-cache-dir --upgrade pip==25.1.1

COPY . .

# Instalar dependências com a versão do pip especificada
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]