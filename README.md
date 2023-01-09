## conversor-moeda

# Descrição
Conversor de Moeda em tempo real utlizando a biblioteca httpx e uma api pública em python. 

- checar de maneira eficiente conversao de moedas pela sigla exemplo:USD,TZS,EUR entre outras.


# instalação
- pip install httpx

#### para realizar a conversão :
- execute Main.py
suejestão de comando: python3 Main.py

![image](https://user-images.githubusercontent.com/116848225/211287397-1964f87e-5f98-4a14-a49e-4fc166ceb818.png)

#### codigo em python:

```
import httpx

MoedaBase = input('Digite a moeda de base: ').upper()
MoedaDesejada = input('Digite a moeda desejada: ').upper()

# Busca valores de moedas na Api pública
response = httpx.get (
url=f'https://api.exchangerate.host/latest?base={MoedaBase}'
).json()
MoedaData = response['rates']
print(f'1 {MoedaBase} vale {MoedaData.get(MoedaDesejada)} {MoedaDesejada}')
```


## imagens de demonstração:
![image](https://user-images.githubusercontent.com/116848225/211288291-23bc757d-ed00-454b-98d5-d87c420d810f.png)

![image](https://user-images.githubusercontent.com/116848225/211288003-9cda5c0e-ab83-4a87-b83a-abdae731a4ac.png)

