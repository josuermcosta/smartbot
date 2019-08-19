# smartbot

### Observações:
Para esse programa assumi que apenas as bibliotecas padrões do python poderiam ser usadas. Sendo assim utilizei apenas 3 delas json,urllib e argparse.

Para utilizar o programa basta rodar o app.py:

```console
# Para rodar o programa e entender as variaveis.
python app.py -h

# Para decidir a velocidade de multiplos personagens.
python app.py 'pessoa 1' 'pessoa 2'

# Para decidir o vencedor de uma corrida entre os persogens baseado na velocidade maxima
python app.py 'pessoa 1' 'pessoa 2' --race

```

### Desenvolvimento:

Eu decidi criar uma biblioteca que extrai os dados nescessarios da API utilizando requisições e trata o json recebido. E um arquivo principal que cuida do CLI e recolhe os dados.

### Testes: 
Em desenvolvimento.
