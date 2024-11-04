def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

texto = input("Digite uma string para inverter: ")
print("String invertida:", reverse_string(texto))
