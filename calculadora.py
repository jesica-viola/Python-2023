# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b

# Ejemplo de uso
print("Ingrese dos números:")
num1 = float(input())
num2 = float(input())

print("¿Qué operación desea realizar?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
operacion = input()

if operacion == "1":
    print(num1, "+", num2, "=", sumar(num1, num2))
elif operacion == "2":
    print(num1, "-", num2, "=", restar(num1, num2))
elif operacion == "3":
    print(num1, "*", num2, "=", multiplicar(num1, num2))
elif operacion == "4":
    print(num1, "/", num2, "=", dividir(num1, num2))
else:
    print("Operación inválida")
