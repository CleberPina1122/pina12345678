#!/bin/bash
# Este script inicializa o servidor Uvicorn para FastAPI

# Verifica se o script está sendo executado como root e não faz nada se estiver
if [ "$(id -u)" = "0" ]; then
    echo "Não execute como root!" 1>&2
    exit 1
fi

# Inicializando o servidor Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
