import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import dump


data = pd.read_excel("resultados_diabetes_100_linhas.xlsx")
X = data.drop("Interpretacao", axis=1)
y = data["Interpretacao"]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Padronizar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializar e treinar o modelo de Regressão
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, zero_division=1)

print(f"Acurácia do modelo: {accuracy:.2f}")
print("Matriz de Confusão:\n", conf_matrix)
print("Relatório de Classificação:\n", classification_rep)

# Salvar o modelo treinado e o scaler
dump(model, "modelo_diabetes.joblib")
dump(scaler, "scaler_diabetes.joblib")
