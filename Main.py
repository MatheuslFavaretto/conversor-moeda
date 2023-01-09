import httpx

MoedaBase = input('Digite a moeda de base: ').upper()
MoedaDesejada = input('Digite a moeda desejada: ').upper()

# Busca valores de moedas na Api pública
response = httpx.get (
url=f'https://api.exchangerate.host/latest?base={MoedaBase}'
).json()
MoedaData = response['rates']
print(f'1 {MoedaBase} vale {MoedaData.get(MoedaDesejada)} {MoedaDesejada}')
