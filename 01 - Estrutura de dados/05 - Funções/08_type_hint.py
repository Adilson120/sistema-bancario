def soma(a: int, b: int) -> int:
    return a + b

resultado = soma(3, 5)  # Retorna 8
print(resultado)

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

mensagem = saudacao("João")  # Retorna "Olá, João!"
print(mensagem)


def eh_par(numero: int) -> bool:
    return numero % 2 == 0

print(eh_par(4))  # Retorna True
print(eh_par(7))  # Retorna False
