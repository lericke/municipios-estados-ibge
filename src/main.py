import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import xlsxwriter

# Função que realiza agrupamento de Municipios para UF
def dict_uf_municipios(lista_ufs):

    lista_municipio_uf = {}

    for uf in lista_ufs:
        url_municipios = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf['id']}/municipios"
        lista_municipio = requests.get(url_municipios).json()
        for municipio in lista_municipio:
            if uf['sigla'] not in lista_municipio_uf:
                lista_municipio_uf[uf['sigla']] = [municipio['nome']]
            else:
                lista_municipio_uf[uf['sigla']].append(municipio['nome'])

    return lista_municipio_uf

# Função que gera dataframe sendo organizado em Coluna: UF e Linha: Municipio
def gera_dataframe(lista_munipios):
    max_length = max(len(v) for v in lista_munipios.values())

    for k, v in lista_munipios.items():
        lista_munipios[k] = v + [''] * (max_length - len(v))

    

    df = pd.DataFrame(lista_munipios)

    return df

# Função que plota um gráfico apresentando a quantidade de municipios por estado.
def plota_grafico(lista_municipios_uf):
   
   # Calcular o número de municípios por estado
    num_municipios_por_estado = {estado: len(municipios) for estado, municipios in lista_municipios_uf.items()}

    # Plotar o gráfico
    plt.figure(figsize=(10, 6))
    bars = plt.bar(num_municipios_por_estado.keys(), num_municipios_por_estado.values(), color='blue')

    # Adicionar o número de municípios em cima de cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

    plt.title('Número de Municípios por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Número de Municípios')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico.png')
    plt.close()

    return True


# Cria arquivo   
url_ufs = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

# Realizando requisição no IBGE
lista_ufs = requests.get(url_ufs).json()

# Criando dicionario com uf e municipios
lista_uf_municipios = dict_uf_municipios(lista_ufs)

# Gerando Gráfico
grafico = plota_grafico(lista_uf_municipios)

# Gerando data Frame
dataframe = gera_dataframe(lista_uf_municipios)



# Criando arquivo com dataframe e imagem
excel_filename = 'dados.xlsx'

with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
    dataframe.to_excel(writer, index=False, sheet_name='Dados')
    
    workbook = writer.book
    worksheet = workbook.add_worksheet('Gráfico')
    worksheet.insert_image('A1', 'grafico.png')