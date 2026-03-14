import math

historico = []
ultimo_resultado = None

print("=== Calculadora Python Avançada ===")

while True:

    print("\nComandos:")
    print("sair -> encerrar | historico -> ver histórico | limpar -> apagar histórico")

    print("\nExemplos:")
    print("5 + 5  |  5 - 5  |")
    print("10 * 2 |  10 / 2 |")
    print("9 ^ 2  |  r2 9   | r3 27")
    print("5 r2 9 |  5 r3 27|")
    print("sin 90 |  log 10 |")

    entrada = input("\nDigite a operação: ")

    if entrada.lower() == "sair":
        print("Calculadora encerrada.")
        break

    if entrada.lower() == "historico":
        print("\n=== Histórico ===")

        if not historico:
            print("Histórico vazio.")
        else:
            for item in historico:
                print(item)

        continue

    if entrada.lower() == "limpar":
        historico.clear()
        print("Histórico apagado.")
        continue

    try:

        partes = entrada.split()

        # Raiz quadrada
        if len(partes) == 2 and partes[0] == "r2":
            num = float(partes[1])
            resultado = math.sqrt(num)
            operacao = f"√{num} = {resultado}"

        # Raiz cúbica
        elif len(partes) == 2 and partes[0] == "r3":
            num = float(partes[1])
            resultado = math.copysign(abs(num) ** (1/3), num)
            operacao = f"∛{num} = {resultado}"

        # Número * raiz quadrada
        elif len(partes) == 3 and partes[1] == "r2":
            num1 = float(partes[0])
            num2 = float(partes[2])
            resultado = num1 * math.sqrt(num2)
            operacao = f"{num1} * √{num2} = {resultado}"

        # Número * raiz cúbica
        elif len(partes) == 3 and partes[1] == "r3":
            num1 = float(partes[0])
            num2 = float(partes[2])
            resultado = num1 * math.copysign(abs(num2) ** (1/3), num2)
            operacao = f"{num1} * ∛{num2} = {resultado}"

        # Funções matemáticas
        elif len(partes) == 2 and partes[0] in ["sin", "cos", "tan", "log"]:
            num = float(partes[1])

            if partes[0] == "sin":
                resultado = math.sin(math.radians(num))
            elif partes[0] == "cos":
                resultado = math.cos(math.radians(num))
            elif partes[0] == "tan":
                resultado = math.tan(math.radians(num))
            elif partes[0] == "log":
                resultado = math.log10(num)

            operacao = f"{partes[0]}({num}) = {resultado}"

        else:

            # Usar resultado anterior
            if ultimo_resultado is not None:
                usar = input("Usar resultado anterior? (s/n): ")

                if usar.lower() == "s":

                    operadores = ["+", "-", "*", "/", "^"]

                    # Se não começa com operador, adiciona +
                    if not any(entrada.startswith(op) for op in operadores):
                        entrada = "+ " + entrada

                    entrada = str(ultimo_resultado) + " " + entrada

            # Trocar ^ por **
            entrada = entrada.replace("^", "**")

            # Avaliação segura
            resultado = eval(
                entrada,
                {"__builtins__": None},
                {
                    "sqrt": math.sqrt,
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log10,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            operacao = f"{entrada} = {resultado}"

        resultado = round(resultado, 6)

        print("Resultado:", resultado)

        historico.append(operacao)
        ultimo_resultado = resultado

    except ZeroDivisionError:
        print("Erro: divisão por zero.")

    except Exception:
        print("Erro: expressão inválida.")