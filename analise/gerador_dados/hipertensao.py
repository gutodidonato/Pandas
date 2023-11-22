import pandas as pd
import random


# Função para gerar dados aleatórios de hipertensão
def gerar_dados_aleatorios_hipertensao():
    return {
        "Pressao_Sistolica": random.uniform(90, 180),
        "Pressao_Diastolica": random.uniform(60, 120),
        "Pulso": random.uniform(60, 100),
        "Idade": random.randint(20, 80),
    }


# Criar DataFrame com 100 linhas de dados aleatórios de hipertensão
dados_aleatorios_hipertensao = [
    gerar_dados_aleatorios_hipertensao() for _ in range(100)
]
df_hipertensao = pd.DataFrame(dados_aleatorios_hipertensao)


# Função para classificar os níveis de hipertensão
def classificar_hipertensao(pressao_sistolica, pressao_diastolica, pulso, idade):
    if (
        pressao_sistolica < 120
        and pressao_diastolica < 80
        and pulso < 100
        and idade <= 40
    ):
        return "Normal"
    elif (
        120 <= pressao_sistolica <= 129
        and pressao_diastolica < 80
        and pulso < 100
        and idade <= 40
    ):
        return "Elevada"
    elif (
        130 <= pressao_sistolica <= 139
        or 80 <= pressao_diastolica <= 89
        or 100 <= pulso <= 109
        or idade > 40
    ):
        return "Estágio 1"
    elif (
        140 <= pressao_sistolica <= 159
        or 90 <= pressao_diastolica <= 99
        or 110 <= pulso <= 119
    ):
        return "Estágio 2"
    elif pressao_sistolica >= 160 or pressao_diastolica >= 100 or pulso >= 120:
        return "Estágio 3"
    else:
        return "Não Classificado"


# Aplicar a função de classificação
df_hipertensao["Interpretacao"] = df_hipertensao.apply(
    lambda row: classificar_hipertensao(
        row["Pressao_Sistolica"],
        row["Pressao_Diastolica"],
        row["Pulso"],
        row["Idade"],
    ),
    axis=1,
)

# Salvar o DataFrame em um arquivo Excel
df_hipertensao.to_excel("resultados_hipertensao_100_linhas.xlsx", index=False)

print("Arquivo 'resultados_hipertensao_100_linhas.xlsx' gerado com sucesso.")
