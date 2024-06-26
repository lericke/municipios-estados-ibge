# Atividade Python com a API do IBGE

Atividade realizada com intuito de consumo e tratamento de dados referente a estados e cidades vindos da API do IBGE.

## Passos iniciais

Utilize o seguinte comando para criar o seu ambiente virtual.

```bash
python -m venv venv
```
Utilize o seguinte comando para iniciar o seu ambiente virtual

Windows
```bash
.\venv\Scripts\Activate.ps1
```
Linux
```bash
source venv/bin/activate
```

Utilize o seguinte comando para instalar as bibliotecas necessárias

```bash
pip install -r requirements.txt
```

## Execute o arquivo main (dentro do diretório onde o arquivo está) utilizando:

```bash
python main.py
```

## Resumo da execução do projeto

Para o arquivo ser gerado, o projeto passa por algumas etapas (Descritas no arquivo main.py). 

1º Faz uma requisição na API do IBGE para trazer a listagem dos estados.

2º Executa uma função que organiza os dados atrelando a lista de municípios de cada estados a sua UF.

3º Plota um gráfico a partir dos dados.

4º Gera um dataframe a partir dos dados.

5º Gera o arquivo em xlsx separando o dataframe em uma sheet e o gráfico em outra sheet.

## Considerações

Projeto desenvolvido por Erick Araujo, como exercício de teste para o processo seletivo da vaga de desenvolvedor python da empresa Mont Capital Asset. 

Estou a disposição para eventuais dúvidas.