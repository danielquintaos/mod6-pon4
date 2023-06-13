# Criando o cliente do supabase
from supabase import create_client, Client
import os
import time

# Estas são minhas chaves de acesso ao supabase, não compartilhe com ninguém!!
# Dentro do Dashboard do Projeto, selecionar Project Settings -> API -> API Settings

# Copiar o valor de URL e colocar na variável url
url: str = "https://ujgarriilwhcfccrdlgn.supabase.co"
# Copiar a Project API Keys. IMPORTANTE: por hora, utilizar a service_role key.
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqZ2FycmlpbHdoY2ZjY3JkbGduIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjU5OTIxOCwiZXhwIjoyMDAyMTc1MjE4fQ.36o__pc0tl7EWzCTno5ztyyawJeWthQQzim0QKSH5d8"

# Cria o cliente para conectar na API do supabase
supabase: Client = create_client(url, key)

# Nome do bucket utilizado
bucket_name: str = "Artaud"

# Pega todas os arquivos do bucket
res = supabase.storage.from_(bucket_name).list()
# print(res)

# Passa por todos os arquivos de um diretório
lista_arquivos = os.listdir("./images")

# Envia os arquivos do diretório para o bucket
for arquivo in lista_arquivos:
    with open(os.path.join("./images", arquivo), 'rb+') as f:
        dados = f.read()
        res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
        print(res)