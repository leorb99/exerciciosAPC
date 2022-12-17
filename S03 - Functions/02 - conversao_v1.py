#CONVERSAO V1
fahrenheit = float(input())
def converte(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    print(f'{celsius:.1f}')
converte(fahrenheit)