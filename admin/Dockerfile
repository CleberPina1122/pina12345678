# Use uma imagem base do Node.js
FROM node:16-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos package.json e package-lock.json para o container
COPY package.json package-lock.json ./

# Instala as dependências do projeto
RUN npm install

# Copia todo o conteúdo da pasta do projeto para o container
COPY . .

# Expondo a porta 5173 para a aplicação frontend
EXPOSE 5173

# Comando para iniciar a aplicação
CMD ["npm", "run", "dev"]