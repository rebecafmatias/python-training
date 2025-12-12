import csv
import json
from datetime import datetime

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

    for s in sales_list:
        id_client = int(s["cliente_id"])
        s_temp = s.copy()

        client_info = clients_dict.get(id_client)

        s_temp["nome_cliente"] = client_info["nome"]
        s_temp["cidade_cliente"] = client_info["cidade"]

        merged_list.append(s_temp)

    return merged_list

# Dividir CSV por mês (data_iso) em vários JSONL: um arquivo por YYYY-MM.

def split_csv_into_jsonl_by_month(csv_path:str, json_file_name:str):
    csv_list = read_csv_file(csv_path)

    dates_list = []
    dates_dicts = {}

    for i in csv_list:
        split_date = i["data_iso"]
        split_date = split_date[0:10]
        
        if split_date not in dates_list:
            dates_list.append(split_date)
        
    for i in dates_list:
        dates_dicts[i] = []
    
    for i in csv_list:
        split_date = i["data_iso"]
        split_date = split_date[0:10]

        dates_dicts.get(split_date).append(i)
    
    for key, value in dates_dicts.items():
        print(f"\n{key}")
        print(value)

        with open(f"{json_file_name}_{key}.jsonl","w") as f:
            json.dump(value,f,indent=4)


# Agregar total de valor por cliente_id em dicionário (sem pandas) 
# e salvar em JSON (não JSONL).

def sum_total_sales_by_client(merged_list: list[dict], json_path: str):
    client_total_sales_dict = {}
    clients_listed = []

    for i in merged_list:
        client_id = i["cliente_id"]
        sale_value = i["valor"]
        if client_id in clients_listed:
            client_total_sales_dict[client_id] += sale_value
        else:
            client_total_sales_dict[client_id] = sale_value
            clients_listed.append(client_id)
    
    with open(f"{json_path}.json","w") as f:
        json.dump(client_total_sales_dict,f,indent=4)

# Converter JSONL para CSV mantendo a ordem das chaves do primeiro registro.

def convert_jsonl_to_csv(jsonl_path:str,csv_path:str):
    with open(jsonl_path,"r",encoding="utf-8") as jsonlfile:
        final_list = []
        for jsonl_list in jsonlfile:
            jsonl_list = str(jsonl_list).replace("[","").replace("]","")
            
            jsonl_row = json.load(jsonl_list)
            
            #     # jsonl_list.append(jsonl_row)

            #     print(f"{i}")
            #     # print(jsonl_row)
            #     # print(jsonl_list)


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
    json_file_path = "../data/processed/sales"
    json_path_sales_client = "../data/processed/sales_clients"

    values_list = read_csv_file(path_sales)
    normalized_list = normalize_list_values(values_list)

    json_values_list = read_json_file(path_client)

    merged_list = joining_dicts_lists_by_keys(values_list,json_values_list)

    convert_jsonl_to_csv("../data/processed/sales_2025-06-02.jsonl",None)
    
    # sum_total_sales_by_client(merged_list,json_path_sales_client)

    # split_csv_into_jsonl_by_month(path_sales,json_file_path)