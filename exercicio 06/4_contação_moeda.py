
import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"
        
        if chave in dados:
            cotacao = dados[chave]
            print(f"Cotação atual do {moeda}: {cotacao.get('bid', 'N/A')} BRL")
            print(f"Valor máximo do dia: {cotacao.get('high', 'N/A')} BRL")
            print(f"Valor mínimo do dia: {cotacao.get('low', 'N/A')} BRL")
            print(f"Última atualização: {cotacao.get('create_date', 'N/A')}")
        else:
            print("Código da moeda inválido. Tente novamente.")
    else:
        print("Erro ao consultar a cotação. Tente novamente mais tarde.")

# Solicita a moeda ao usuário
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
consultar_cotacao(moeda)