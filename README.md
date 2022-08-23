# machine-learning-algoritmos

No primeiro exemplo (plot3.py) mostramos a função sigmóide e sua derivada, muito usada 
como função de ativação nas Redes Neurais Artificiais

Através dos gráficos observamos como a função tende a 1 e sua derivada
tende a 0, o que explica seu uso para maximizar o acerto quando treinamos
um conjunto de dados e minimizamos o erro usando a derivada da função.


No segundo exemplo (pycaret_churn.ipynb) utilização do pycaret para previsão de Churn

No terceiro exemplo (classes_desbalanceadas.ipynb) sobre classes desbalanceadas vale dizer que 
é umerro muito comum ao trabalhar com problemas de classificação.
A maioria dos conjuntos de dados em tarefas de classificação tem um problema de desequilíbrio de classe.
Uma maneira de resolver o desequilíbrio de classe é fazer oversampling, ou seja, adicionando aleatoriamente
amostras de classes minoritárias ao conjunto de dados para equilibrar o número de amostras para cada rótulo.

Considere que você está trabalhando em um conjunto de dados de detecção de fraude.
Você observa que há um desequilíbrio de classe extremo nesse problema e decide resolver
esse problema primeiro. Para resolver o problema, você decide fazer oversampling. Depois disso,
você opta por fazer a validação cruzada. Agora, seus conjuntos de dados de treinamento e validação
formados por validação cruzada k-fold terão várias amostras comuns que levarão à superestimação
do desempenho do modelo. Portanto, evite fazer oversampling seguido de validação cruzada.

