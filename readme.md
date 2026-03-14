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

## ‼️OBS

Exixtem duas versões dessa Calculadora 1 código versão 1 e outro versão 2
Qual a diferença do código 2 para o código 1 ?

Simples o código 2 suporta expressões matematicas mais completas exemplo:
10 + 10 + 10 = 30
ja o código 1 nao suporta, o código 2 tambem te pergunta se deja utilizar o resultado da conta anterior para fazer a conta nova.
Exemplo:
10 + 10 + 10 = 30
Conta nova: 
10 + 10
Deseja utilizar o resultado da conta anteriro ? (s/n) 
se sim: 30 + 10 + 10 = 50
se nao: + 10 + 10 = 20