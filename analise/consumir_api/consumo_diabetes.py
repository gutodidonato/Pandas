import requests


def fazer_previsao_diabetes(
    glicose_jejum, hemoglobina_a1c, tolerancia_glicose, glicose_aleatoria
):
    base_url = "http://127.0.0.1:5000"
    url_diabetes = f"{base_url}/predict_diabetes"

    data_diabetes = {
        "Glicose_Jejum": glicose_jejum,
        "Hemoglobina_A1c": hemoglobina_a1c,
        "Tolerancia_Glicose": tolerancia_glicose,
        "Glicose_Aleatoria": glicose_aleatoria,
    }

    response_diabetes = requests.post(url_diabetes, json=data_diabetes)
    return response_diabetes.json()


def fazer_previsao_hipertensao(
    glicose_jejum, hemoglobina_a1c, tolerancia_glicose, glicose_aleatoria
):
    base_url = "http://127.0.0.1:5000"
    url_hipertensao = f"{base_url}/predict_hipertensao"

    data_hipertensao = {
        "Glicose_Jejum": glicose_jejum,
        "Hemoglobina_A1c": hemoglobina_a1c,
        "Tolerancia_Glicose": tolerancia_glicose,
        "Glicose_Aleatoria": glicose_aleatoria,
    }

    response_hipertensao = requests.post(url_hipertensao, json=data_hipertensao)
    return response_hipertensao.json()


# Exemplo de uso da função
resultado_diabetes = fazer_previsao_diabetes(100, 5.0, 120, 110)
resultado_hipertensao = fazer_previsao_hipertensao(120, 6.0, 140, 130)

print("Resultado da previsão para Diabetes:", resultado_diabetes)
print("Resultado da previsão para Hipertensão:", resultado_hipertensao)
