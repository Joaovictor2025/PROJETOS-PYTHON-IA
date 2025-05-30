'''3 - Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
* Instale o modulo requests - pip install requests *
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
        else:
            print("CEP inválido. Tente novamente.")
    else:
        print("Erro ao consultar o CEP. Tente novamente mais tarde.")

# Solicita o CEP ao usuário
cep = input("Digite o CEP: ").strip()
consultar_cep(cep)