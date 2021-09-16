from forex_python.converter import CurrencyRates

c = CurrencyRates()

v1 = float(input("\nQual o valor em dolar que deseja converter para real?"))
r = round(c.convert("USD", "BRL", v1), 2)

print (f"{v1} = R$ {r}")