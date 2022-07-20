message = "Rafael"
print(message)
id(message)

texto = "Let's Code"
print(f'{texto.upper()}, {texto.lower()}, {texto.title()}')

print(f'{texto.upper().replace(" ", "_")}')

valor_1 = 10
valor_2 = 2

print(f'{valor_1 ** valor_2}')
print(f'{valor_1 ** (1/valor_2)}')

v_complex = 1+3j
v_int = 5
v_decimal = 4.3

print(v_complex - v_int)
print(v_int - v_complex)
print(v_complex ** v_int)
print(v_int - v_decimal)
print(v_int ** v_complex)
# print(v_decimal % v_complex) ## erro: can't mod complex numbers
print(v_int % v_decimal)
print(v_decimal // v_int)
