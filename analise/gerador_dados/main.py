import pandas as pd
import random


# Função para gerar dados aleatórios
def gerar_dados_aleatorios():
    return {
        "Glicose_Jejum": random.uniform(70, 127),
        "Hemoglobina_A1c": random.uniform(4.0, 9),
        "Tolerancia_Glicose": random.uniform(80, 220),
        "Glicose_Aleatoria": random.uniform(80, 220),
    }


# Criar DataFrame com 100 linhas de dados aleatórios
dados_aleatorios = [gerar_dados_aleatorios() for _ in range(100)]
df = pd.DataFrame(dados_aleatorios)


# Função para classificar os níveis de diabetes
def classificar_diabetes(
    glicose_jejum, hemoglobina_a1c, tolerancia_glicose, glicose_aleatoria
):
    if (
        glicose_jejum < 100
        and hemoglobina_a1c < 5.7
        and tolerancia_glicose < 140
        and glicose_aleatoria < 140
    ):
        return "Normal"
    elif (
        100 <= glicose_jejum < 126
        or 5.7 <= hemoglobina_a1c < 6.4
        or 140 <= tolerancia_glicose < 200
        or 140 <= glicose_aleatoria < 200
    ):
        return "Pré-DM"
    else:
        return "DM2"


# Aplicar a função de classificação
df["Interpretacao"] = df.apply(
    lambda row: classificar_diabetes(
        row["Glicose_Jejum"],
        row["Hemoglobina_A1c"],
        row["Tolerancia_Glicose"],
        row["Glicose_Aleatoria"],
    ),
    axis=1,
)

# Salvar o DataFrame em um arquivo Excel
df.to_excel("resultados_diabetes_100_linhas.xlsx", index=False)

print("Arquivo 'resultados_diabetes_100_linhas.xlsx' gerado com sucesso.")
