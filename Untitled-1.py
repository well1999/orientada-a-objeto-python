## atividade 1
class ArquivoCSV(object):
def __init__(self, arquivo: str):
self.arquivo = arquivo
self.conteudo = self._extrair_conteudo()
self.colunas = self._extrair_nome_colunas()
def _extrair_conteudo(self):
conteudo = None
with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
conteudo = arquivo.readlines()
return conteudo
def _extrair_nome_colunas(self):
return self.conteudo[0].strip().split(sep=',')
def extrair_coluna(self, indice_coluna: str):
coluna = list()
for linha in self.conteudo:
conteudo_linha = linha.strip().split(sep=',')
coluna.append(conteudo_linha[indice_coluna])
coluna.pop(0)
return coluna
## atividade 2
class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str):

self.colunas = 
def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):
arquivo_csv = ArquivoCSV(arquivo='carros.csv')
numero_linha = 1
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))
# id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
print(arquivo_csv.colunas)
 [
 'id',
 'valor_venda',
 'valor_manutencao',
 'portas',
 'pessoas',
# 'porta_malas'
]
numero_linha = 10
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))
9,low,med,2,2,small
numero_linha = 10
numero_coluna = 2
