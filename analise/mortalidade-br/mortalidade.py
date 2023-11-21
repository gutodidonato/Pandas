import pandas as pd

data = pd.read_csv(
    r"C:\Users\guto\Desktop\Python\GS\Pandas\analise\mortalidade-2019.csv", sep=";"
)

doenca_refere = "CAUSABAS"
se_morte_gravidez = "OBITOGRAV"
se_morte_parto = "OBITOPARTO"
se_morte_pos_parto = "OBITOPUERP"
anos_de_escolaridade = "ESC"

doencas = data[doenca_refere]

"""obitos na gravidez"""
obitos_gravidez = data[data[se_morte_gravidez] == 1.0]
nao_obitos_gravidez = data[data[se_morte_gravidez] == 2.0]
total_gravidez = len(obitos_gravidez) + len(nao_obitos_gravidez)

print("Total de óbitos: ", obitos_gravidez, "\n")
print(
    f"Porcentagem de óbitos durante gravidez: {len(obitos_gravidez)/total_gravidez:.2%}\n"
)

"""Óbito pos parto"""
obito_parto = data[se_morte_pos_parto].value_counts()
contagem = obito_parto.nlargest(4)
print(contagem)
obitos_pos_1 = data[data[se_morte_pos_parto] == 1.0]
obitos_pos_2 = data[data[se_morte_pos_parto] == 2.0]
obitos_pos_nao = data[data[se_morte_pos_parto] == 3.0]
total_pos_parto = len(obitos_pos_1) + len(obitos_pos_2) + len(obitos_pos_nao)

print("Total de óbitos pós gravidez: ", len(obitos_pos_1) + len(obitos_pos_2), "\n")
print(
    f"Porcentagem de óbitos pós gravidez: {(len(obitos_pos_1) + len(obitos_pos_2))/total_pos_parto:.2%}\n"
)

obito_pos_parto = data[se_morte_pos_parto].value_counts()
contagem = obito_pos_parto.nlargest(5)
print(contagem)

""""""


"""escolaridade media"""

escolaridade = data["ESC"].value_counts()
contagem_escola = escolaridade.nlargest(6)
print(f"A contagem de mortalidade por escolaridade é:\n{contagem_escola}")

"""escolaridade """


"""comparitivo de doenças entre 5 e 20 anos de idade"""
""""""
filtro_causabas_idade_05_20 = data[(data["IDADE"] >= 405) & (data["IDADE"] <= 420)]

maiores_causas = filtro_causabas_idade_05_20["LINHAA"].value_counts()
contagem_mortes_05_20 = maiores_causas.head(10)

print(
    f"O que mais matou jovens entre 05 e 20 anos de idade : \n", contagem_mortes_05_20
)

""""""

filtro_causabas_idade_05_20_leucemia = data[
    (data["IDADE"] >= 405) & (data["IDADE"] <= 420) & (data["CAUSABAS"] == "C910")
]

filtro_causabas_idade_05_20_pneumonia = data[
    (data["IDADE"] >= 405) & (data["IDADE"] <= 420) & (data["CAUSABAS"] == "J189")
]

filtro_causabas_idade_05_20 = data[(data["IDADE"] >= 405) & (data["IDADE"] <= 420)]

mortes_leucemia = len(filtro_causabas_idade_05_20_leucemia)
mortes_pneumonia = len(filtro_causabas_idade_05_20_pneumonia)
outras_mortes = len(filtro_causabas_idade_05_20) - (mortes_leucemia + mortes_pneumonia)
total = len(filtro_causabas_idade_05_20)

print(
    f"Mortes de 5 a 20 anos: Pneumonia {mortes_pneumonia}, Leucemia {mortes_leucemia}, outras mortes: {outras_mortes}"
)


"""comparativo escolaridade e obito durante a gravidez"""

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

"""comparativo qual idade mais mata a leucemia"""
leucemia_idade = data[(data["CAUSABAS"] == "C910")]["IDADE"]
idade_que_mais_matou = leucemia_idade.value_counts()
idade_que_mais_matou_rank = idade_que_mais_matou.nlargest(10)
print(idade_que_mais_matou_rank)

"""comparativo qual idade mais mata a pneumonia"""
pneumonia = data[(data["CAUSABAS"] == "J189")]["IDADE"]
idade_que_mais_matou_pneumo = pneumonia.value_counts()
idade_que_mais_matou_rank_pneumo = idade_que_mais_matou_pneumo.nlargest(10)
print(idade_que_mais_matou_rank_pneumo)

"""doenças que mais mataram"""
doenca = data["CAUSABAS"].value_counts()
doenca_rank = doenca.nlargest(10)
print(doenca_rank)


""""""
