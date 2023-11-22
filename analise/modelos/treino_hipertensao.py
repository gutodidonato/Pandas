import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import dump

# Leitura do CSV gerado
data_hipertensao = pd.read_excel(
    r"C:\Users\guto\Desktop\Python\GS\Pandas\analise\modelos\resultados_hipertensao_100_linhas.xlsx"
)
X_hipertensao = data_hipertensao.drop("Interpretacao", axis=1)
y_hipertensao = data_hipertensao["Interpretacao"]

# Dividir os dados em conjuntos de treino e teste
(
    X_train_hipertensao,
    X_test_hipertensao,
    y_train_hipertensao,
    y_test_hipertensao,
) = train_test_split(X_hipertensao, y_hipertensao, test_size=0.2, random_state=42)

scaler_hipertensao = StandardScaler()
X_train_scaled_hipertensao = scaler_hipertensao.fit_transform(X_train_hipertensao)
X_test_scaled_hipertensao = scaler_hipertensao.transform(X_test_hipertensao)

# Inicializar e treinar o modelo de Regressão
model_hipertensao = LogisticRegression()
model_hipertensao.fit(X_train_scaled_hipertensao, y_train_hipertensao)

# Fazer previsões no conjunto de teste
y_pred_hipertensao = model_hipertensao.predict(X_test_scaled_hipertensao)
accuracy_hipertensao = accuracy_score(y_test_hipertensao, y_pred_hipertensao)
conf_matrix_hipertensao = confusion_matrix(y_test_hipertensao, y_pred_hipertensao)
classification_rep_hipertensao = classification_report(
    y_test_hipertensao, y_pred_hipertensao, zero_division=1
)

print(f"Acurácia do modelo de hipertensão: {accuracy_hipertensao:.2f}")
print("Matriz de Confusão para hipertensão:\n", conf_matrix_hipertensao)
print("Relatório de Classificação para hipertensão:\n", classification_rep_hipertensao)

# Salvar o modelo treinado e o scaler
dump(model_hipertensao, "modelo_hipertensao.joblib")
dump(scaler_hipertensao, "scaler_hipertensao.joblib")
