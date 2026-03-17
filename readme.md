# 🧮 Calculadora em Python (Terminal)

Uma **calculadora simples feita em Python** que roda no terminal.  
Ela permite realizar operações matemáticas básicas e mantém um **histórico das operações realizadas** durante a execução do programa.

---

## 🚀 Funcionalidades

- Operações matemáticas básicas:
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- Histórico das operações realizadas
- Tratamento de erros para:
  - Entrada inválida
  - Operador inválido
  - Divisão por zero
- Execução contínua até o usuário digitar `sair`

---

## 📋 Como funciona

1. O programa solicita o **primeiro número**.
2. Depois solicita o **operador matemático**.
3. Em seguida pede o **segundo número**.
4. O resultado é calculado e exibido na tela.
5. A operação é salva no **histórico**.

Também existem dois comandos especiais:

| Comando | Função |
|--------|------|
| `historico` | Mostra todas as operações realizadas |
| `sair` | Encerra o programa |

## 😁 Final

Enfim isso é tudo pessoal :D

## ✅ Versões

### Versão Calc-v1

Nesta versão voce consegue fazer as operações mais basicas de uma calculadora somar, subtrair, dividir e multiplicar.

Exemplo:

Digite o primeiro número: 10
Digite o Operador ( +, -, x, /): +
Digite o segundo número: 10

Resultado: 20

#### Funções - Sair & Historico

##### Sair

A função sair ela encerra o programa da Calculadora

##### Historico

Ela exibe o último calculo exibido na tela exemplo:

Digite a função ou primeiro número (Sair - encerra o programa - Historico - exibe o historico de calculos): 

Se Historico:
Exibir Historico
Historico.append[] = {Num1} {Num2} "=" {Resultado} 
10 + 10 = 20

### Versão Calc-v2

Nesta versão além dos calculos básicos voce consegue fazer raiz quadrada, cubica, exponenciação, porcentagem, entre outros calculos de sin, con, tan, log. Nesta calculadora você tambem consegue fazer calculos com expressão númerica inteira exemplo:

10 + 10 + 10 = 30 | 10 + 10 * 2 = 30

Lembrando que ele faz em ordem de acordo com as regras matematicas primeiro parenteses, multiplicação e divisão.

Esse código também armazena o resultado da conta anterior podendo utilizar o resultado da última conta na próxima conta exemplo:

Digite a operação: 10 + 10 + 10
Deseja utilizar o resultado da conta anterior (s/n):

se sim:
resultado = 60

se não:
resultado = 30

As funções sair e historico não mudaram isso é tudo 😁

#### ‼️OBS

Essa calculadora não suporta expressões sem espaço: 
❌ 5+5
✔️ 5 + 5

Nao suporta:
múltiplas operações customizadas (tipo r2 r3 etc.)
parênteses complexos com parsing manual

### Versão Calc-v3

Projeto em andamento ainda
