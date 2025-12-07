import csv
import json

path = "../data/raw/vendas.csv"
path_prod = "../data/raw/produtos.csv"
path_client = "../data/raw/clientes.jsonl"
# Ler um CSV simples (sem aspas) e gerar dicionários por linha.

with open(path,encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    csv_list = list(reader)

with open(path_prod,encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    csv_prod_list = list(reader)

with open(path_client) as jsonfile:
    json_clients_list = json.load(jsonfile)
print(json_clients_list)
    
# Filtrar CSV por valor > 0 e gravar o resultado em JSONL; 
# retornar o total de registros escritos.

csv_filtered_list = []
json_file_name = "sales.json"

for i in csv_list:
    try:
        valor_string = i["valor"]
        valor = float(valor_string)
        if valor > 0:
            csv_filtered_list.append(i)
    except ValueError:
        pass
        # print(f"Value {valor_string} cannot be converted to float.")

with open(json_file_name,"w") as f:
    json.dump(csv_filtered_list,f,indent=4)

# print(f"Data saved to {json_file_name}")

# Normalizar tipos: converter campos numéricos inválidos para None

for i in csv_list:
    valor_string = i["valor"]
    try:
        valor = float(valor_string)
    except ValueError:
        valor = None

# Fazer “join” entre vendas.csv (CSV) e clientes.jsonl (JSONL) 
# por cliente_id e escrever JSONL combinado.

# Dividir CSV por mês (data_iso) em vários JSONL: um arquivo por YYYY-MM.

# Agregar total de valor por cliente_id em dicionário (sem pandas) 
# e salvar em JSON (não JSONL).

# Converter JSONL para CSV mantendo a ordem das chaves do primeiro registro.

# Validar schema mínimo: garantir a presença de chaves obrigatórias; 
# contar e reportar linhas inválidas.

# Remover duplicatas por id mantendo o primeiro registro
# (entrada CSV, saída JSONL).

# Implementar leitura “streaming”: iterar linha a linha 
# sem carregar o arquivo inteiro (arquivos grandes).