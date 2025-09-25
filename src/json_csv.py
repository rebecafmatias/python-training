# Ler um CSV simples (sem aspas) e gerar dicionários por linha.

# Filtrar CSV por valor > 0 e gravar o resultado em JSONL; 
# retornar o total de registros escritos.

# Normalizar tipos: converter campos numéricos inválidos para 
# None e pular linhas sem header completo.

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