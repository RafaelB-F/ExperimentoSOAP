from zeep import Client


wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'


client = Client(wsdl_url)


resultado = client.service.Add(10, 20)
print("Resultado da soma:", resultado)


resultado = client.service.Multiply(5, 4)
print("Resultado da multiplicação:", resultado)