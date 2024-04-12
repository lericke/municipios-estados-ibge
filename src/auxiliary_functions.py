
import requests
import pandas as pd
import matplotlib.pyplot as plt


# Função que realiza agrupamento de Municipios para UF em um Dicionário.
def dict_uf_municipios(uf_list):

    uf_city_list = {}

    for uf in uf_list:
        url_cities = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf['id']}/municipios"
        city_list = requests.get(url_cities).json()
        for municipio in city_list:
            if uf['sigla'] not in uf_city_list:
                uf_city_list[uf['sigla']] = [municipio['nome']]
            else:
                uf_city_list[uf['sigla']].append(municipio['nome'])

    return uf_city_list

# Função que gera dataframe sendo organizado em Coluna: UF e Linha: Municipio
def create_dataframe(lista_munipios):
    max_length = max(len(v) for v in lista_munipios.values())

    for k, v in lista_munipios.items():
        lista_munipios[k] = v + [''] * (max_length - len(v))

    df = pd.DataFrame(lista_munipios)

    return df

# Função que plota um gráfico apresentando a quantidade de municipios por estado.
def graph_plot(uf_city_list):
   
   # Calcular o número de municípios por estado
    num_city_uf = {estado: len(municipios) for estado, municipios in uf_city_list.items()}

    # Plotar o gráfico
    plt.figure(figsize=(10, 6))
    bars = plt.bar(num_city_uf.keys(), num_city_uf.values(), color='blue')

    # Adicionar o número de municípios em cima de cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

    # Gera gráfico e salva em formato png dentro do projeto
    plt.title('Número de Municípios por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Número de Municípios')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico.png')
    plt.close()

    return True

# Gera arquivo xlsx com dataframe e imagem do gráfico
def create_archive(dataframe):
    
    excel_filename = 'estados_municipios_ibge.xlsx'

    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Dados')
        
        workbook = writer.book
        worksheet = workbook.add_worksheet('Gráfico')
        worksheet.insert_image('A1', 'grafico.png')

    return {"message": "Arquivo gerado com sucesso." }
