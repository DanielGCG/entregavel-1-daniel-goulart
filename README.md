# ENTREGÁVEL 1 — Verificação de Autonomia de Bateria

## 1. Informações

**Nome:** Daniel Goulart Camacho Gonçalves

**Objetivo:**
Desenvolver um programa para verificar se a bateria disponível em um robô é suficiente para realizar uma determinada missão, considerando a duração prevista e o consumo de bateria por minuto.

---

## 2. Requisitos

Para executar o programa, é necessário ter o Python 3 instalado no sistema.

---

## 3. Execução

A partir da raiz do projeto, execute o seguinte comando:

```bash
python3 src/missao.py
```

---

## 4. Funcionamento

O programa deve receber:

* **Bateria atual**;
* **Duração prevista da missão**;
* **Consumo por minuto**.

O programa deve verificar se a bateria disponível é suficiente para completar a missão.

---

## 5. Exemplo de execução

### Entrada

```
Bateria atual: 80
Duração prevista da missão: 10
Consumo por minuto: 3
```

### Saída

```
Bateria suficiente para a missão, sobrando: 50% de carga.
```

---

## 6. Validação de entradas

O programa deve realizar a validação dos valores de entrada.

### 6.1

**Entrada:**

```
Bateria atual: 100
Duração prevista da missão: 10
Consumo por minuto: 10
```

**Saída:**

```
Bateria suficiente para a missão, sobrando: 0% de carga.
```

---

### 6.2

**Entrada:**

```
Bateria atual: 100
Duração prevista da missão: 100
Consumo por minuto: 10
```

**Saída:**

```
Bateria insuficiente para a missão, faltaria: 900% de carga.
```

---

### 6.3

**Entrada:**

```
Bateria atual: 101
```

**Saída:**

```
Valor inválido
```

---

### 6.4

**Entrada:**

```
Bateria atual: -1
```

**Saída:**

```
Valor inválido
```

---

### 6.5

**Entrada:**

```
Bateria atual: 100
Duração prevista da missão: 0
```

**Saída:**

```
Valor inválido
```

---

### 6.6

**Entrada:**

```
Bateria atual: 100
Duração prevista da missão: 10
Consumo por minuto: 0
```

**Saída:**

```
Valor inválido
```