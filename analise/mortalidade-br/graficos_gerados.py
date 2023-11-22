import pandas as pd
import matplotlib.pyplot as plt
import statistics

data = pd.read_csv(
    r"C:\Users\guto\Desktop\Python\GS\Pandas\analise\mortalidade-2019.csv", sep=";"
)


"""Este arquivo é um arquivo do sus sobre mortalidade"""
# data.info()


data["IDADE"] = pd.to_numeric(data["IDADE"], errors="coerce")

# Filtrar valores não nulos na coluna "IDADE"
idade_numerica = data["IDADE"].dropna()
# Filtrar as idades no intervalo de 1 a 99 anos
idade = idade_numerica[(idade_numerica >= 401) & (idade_numerica <= 499)]
# Calcular o desvio padrão amostral
idade_desvio = statistics.stdev(idade)
# Calcular a soma total das idades
total_idade = idade.sum()
# Calcular a média das idades
media_idade = total_idade / len(idade)

print(
    f"Média de idade de pessoas que morreram no intervalo de 1 a 99 anos: {(media_idade - 400):.2f}"
)
print(f"O desvio amostral é de {idade_desvio}")
print(
    f"Então é uma faixa média de morte entre: {(media_idade - 400 + idade_desvio):.2f} e {(media_idade - 400 - idade_desvio):.2f} anos de idade"
)
media_esc_0 = data[data["ESC"] == 1.0]
media_esc_8 = data[(data["ESC"] == 4.0) | (data["ESC"] == 5.0)]
print(
    f"Podemos comparar se em 2019 morreram mais pessoas com 0 anos de estudo: {len(media_esc_0)} vs pessoas com mais de 8 anos de estudo: {len(media_esc_8)} "
)
# Este arquivo possui mais de 88 colunas, é um patrimonio do sistema público de saúde brasileiro, serão utilizadas menos de 10 colunas neste momento, para induzirmos nosso projeto
# além desses experimentos que mostrei agora, existe muito dado interpretável como este aqui

gravidez_escolaridade_alta = data[
    ((data["ESC"] == 5.0) | (data["ESC"] == 4.0)) & (data["OBITOGRAV"] == 1.0)
]

gravidez_escolaridade_baixa = data[
    (
        ((data["ESC"] == 2.0) | (data["ESC"] == 1.0) | (data["ESC"] == 3.0))
        & (data["OBITOGRAV"] == 1.0)
    )
]

contagem_escolaridade_menor_gravidez = len(gravidez_escolaridade_baixa)
contagem_escolaridade_alta_gravidez = len(gravidez_escolaridade_alta)
total = contagem_escolaridade_menor_gravidez + contagem_escolaridade_alta_gravidez
print(
    f"Total de óbitos durante a gravidez no qual mãe escolaridade < 7 anos : {contagem_escolaridade_menor_gravidez} \nTotal de óbitos durante a gravidez no qual escolaridade mãe > 7 anos : {contagem_escolaridade_alta_gravidez}"
)

# que podemos abordar até a questão do aborto por mulheres de maior nível de instrução não quererem interromper seus estudos


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""comparativo AVC"""
# utilizei %100, porque por padrão as idades com anos, iniciam com 4, daria 400 e algo
data["IDADE"] = data["IDADE"] % 100
avc = data[data["CAUSABAS"] == "E149"]["IDADE"]
idade_que_mais_matou_avc = avc.value_counts()
idade_que_mais_matou_rank_avc = idade_que_mais_matou_avc.nlargest(10)


plt.bar(idade_que_mais_matou_rank_avc.index, idade_que_mais_matou_rank_avc.values)


plt.xlabel("Idade")
plt.ylabel("Número de AVCs")
plt.title("Top 10 Idades que Morreram de AVCs")
plt.show()


"""comparativo qual idade mais mata a diabetes"""
diabetes = data[(data["CAUSABAS"] == "E149")]["IDADE"]
idade_que_mais_matou_diabetes = diabetes.value_counts()
idade_que_mais_matou_rank_diabetes = idade_que_mais_matou_diabetes.nlargest(10)
print(idade_que_mais_matou_rank_diabetes)


plt.bar(
    idade_que_mais_matou_rank_diabetes.index, idade_que_mais_matou_rank_diabetes.values
)


plt.xlabel("Idade")
plt.ylabel("Número de diabetes mellitus")
plt.title("Top 10 Idades que Morreram de diabetes mellitus")
plt.show()


"""comparativo qual idade mais mata a leucemia"""
leucemia_idade = data[(data["CAUSABAS"] == "C910")]["IDADE"]
idade_que_mais_matou = leucemia_idade.value_counts()
idade_que_mais_matou_rank = idade_que_mais_matou.nlargest(10)
print(idade_que_mais_matou_rank)

plt.bar(idade_que_mais_matou_rank.index, idade_que_mais_matou_rank.values)


plt.xlabel("Idade")
plt.ylabel("Número de leucemias")
plt.title("Top 10 Idades que Morreram de Leucemia")
plt.show()

""" comparativo escolaridade media"""

escolaridade = data[data["ESC"] != 9.0]["ESC"]
contagem_escola = escolaridade.value_counts().nlargest(5)


plt.bar(contagem_escola.index, contagem_escola.values)
plt.xlabel("Escolaridade")
plt.ylabel("Número de mortes por escolaridade")
plt.title("Avaliar por anos de escolaridade")
plt.show()
print(
    "Neste gráfico a escolaridade equivale a =  1: Nenhuma, 2: de 1 a 3 anos, 3: de 4 a 7 anos, 4: de 8 a 11 anos, 5: 12 anos e mais"
)
"""causas que mais mataram"""
doenca = data["CAUSABAS"].value_counts()
doenca_rank = doenca.nlargest(10)
print(doenca_rank)

plt.bar(doenca_rank.index, doenca_rank.values)


plt.xlabel("Idade")
plt.ylabel("Número de mortes pelas causas que mais mataram")
plt.title("Avaliar pelas causas que mais mataram")
plt.show()
print("As causas pelo código estão disponível pelo CID-10")

""""""
