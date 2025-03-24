
# Algoritmo MaxMin Select

## Descrição do Projeto
Este projeto implementa o algoritmo **MaxMin Select**, que encontra simultaneamente o maior e o menor elemento de um array utilizando a técnica de **Divisão e Conquista**.

### Explicação do Algoritmo
O algoritmo segue os seguintes passos:
1. **Caso base**:
   - Se houver apenas um elemento, ele é retornado como o máximo e o mínimo.
   - Se houver dois elementos, eles são comparados diretamente.
2. **Divisão**:
   - O array é dividido ao meio recursivamente.
3. **Conquista**:
   - O menor e o maior de cada metade são encontrados recursivamente.
4. **Combinação**:
   - Os resultados das metades são combinados para encontrar o menor e o maior do array inteiro.

## Como Executar o Projeto
Para rodar o projeto em seu ambiente local, siga os passos:
1. Instale o **Python 3.10+**.
2. Clone este repositório:
   ```bash
   git clone https://github.com/Druitti/trabalho_individual_2_FPAA.git

   cd trabalho_individual_2_FPAA
   ```
3. Execute o código Python:
   ```bash
   python src/app.py
   ```

## Relatório Técnico
### Análise da Complexidade Assintótica por Contagem de Operações

O algoritmo realiza **n-1** comparações no pior caso, e **cerca de 3n/2** comparações em média, reduzindo o número de operações em comparação com a abordagem ingêna, que requer 2(n-1) comparações.

1. Cada chamada recursiva divide o array em duas metades.
2. O número total de comparações é aproximadamente **3n/2**.
3. Portanto, a complexidade é **O(n)**.

### Análise da Complexidade pelo Teorema Mestre
A recorrência do algoritmo é:
```
T(n) = 2T(n/2) + O(1)
```

1. Identificação dos valores:
   - **a = 2** (duas chamadas recursivas)
   - **b = 2** (problema dividido ao meio)
   - **f(n) = O(1)** (operação de combinação)

2. Calculando ** n ^log_b a**:
   ```
   n^log_2(2) = n^1 = n
   ```

3. Os três casos do Teorema Mestre são:

#### Caso 1:  
Se **( f(n) < n log_b a ), então ( T(n) = O(n^p) ).**   
#### Caso 2:   
Se **( f(n) = n log_b a ), então ( T(n) = O(n^p \log n) ).**  
#### Caso 3:  
Se **( f(n) > n log_b a ), então  T(n) = O(f(n)  ).**

 O Teorema Mestre se encaixa no **Caso 1** (*O(1) < T(n^**log_b a**)*).


4. Solução assintótica:
   ```
   T(n) = Θ(n^log_2(2)) = Θ(n)
   ```

O algoritmo possui complexidade **Θ(n)**, o que é eficiente para este problema.

5. Diagrama Visual da Divisão e Conquista:

O diagrama abaixo ilustra a divisão e combinação do algoritmo MaxMin Select:



## Fluxo de Ida do Algorítmo
![Diagrama MaxMin](imgs/Diagram_maxmin2.png)

## Fluxo de Retorno do Algorítmo
![Diagrama MaxMin](imgs/Diagram_maxmin_return.png)

