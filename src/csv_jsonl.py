import csv
import json

# Ler um CSV simples (sem aspas) e gerar dicionários por linha.

def read_csv_file(path: str) -> list:
    with open(path,encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        csv_list = list(reader)
        return csv_list

def read_json_file(path: str) -> list:
    json_clients_list = []

    with open(path_client,"r",encoding="utf-8") as jsonfile:
        for i in jsonfile:
            json_client = json.loads(i)
            json_clients_list.append(json_client)

    return json_clients_list

    
# Filtrar CSV por valor > 0 e gravar o resultado em JSONL; 
# retornar o total de registros escritos.

def filter_csv_value_and_save_json(values_list: list) -> list:
    csv_filtered_list = []
    json_file_name = "sales.json"

    for i in values_list:
        try:
            valor_string = i["valor"]
            valor = float(valor_string)
            if valor > 0:
                csv_filtered_list.append(i)
        except ValueError:
            pass

    with open(json_file_name,"w") as f:
        json.dump(csv_filtered_list,f,indent=4)

    return csv_filtered_list

# print(f"Data saved to {json_file_name}")

# Normalizar tipos: converter campos numéricos inválidos para None

def normalize_list_values(values_list: list):
    normalized_list = []
    for i in values_list:
        temp_dict = i
        valor_string = i["valor"]
        try:
            valor = float(valor_string)
        except ValueError:
            valor = None

        temp_dict.update({"valor":valor})
        normalized_list.append(temp_dict)

    return normalized_list

# Fazer “join” entre vendas.csv (CSV) e clientes.jsonl (JSONL) 
# por cliente_id e escrever JSONL combinado.

def joining_dicts_lists_by_keys(sales_list: list, clients_list: list) -> list:

    clients_dict = {}
    merged_list = []

    for c in clients_list:
        clients_dict[c["cliente_id"]] = c
    print(clients_dict)


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

if __name__ == "__main__":
    
    path_sales = "../data/raw/vendas.csv"
    path_prod = "../data/raw/produtos.csv"
    path_client = "../data/raw/clientes.jsonl"

    values_list = read_csv_file(path_sales)
    normalized_list = normalize_list_values(values_list)

    json_values_list = read_json_file(path_client)

    joining_dicts_lists_by_keys(values_list,json_values_list)
