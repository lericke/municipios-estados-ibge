
import requests
from auxiliary_functions import dict_uf_municipios, graph_plot, create_dataframe, create_archive


# Url da API do IBGE
url_ufs = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

# Realizando requisição no IBGE
uf_list = requests.get(url_ufs).json()

# Criando dicionario com uf e municipios
uf_city_list = dict_uf_municipios(uf_list)

# Gerando Gráfico
grafico = graph_plot(uf_city_list)

# Gerando data Frame
dataframe = create_dataframe(uf_city_list)

# Gerando arquivo com o dataframe e gráfico inseridos.
create_archive(dataframe)