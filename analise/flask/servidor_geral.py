from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from sklearn.preprocessing import StandardScaler
from joblib import load

app = Flask(__name__)
api = Api(app)

# Carregar modelos treinados e scalers
model_diabetes = load("modelo_diabetes.joblib")
scaler_diabetes = load("scaler_diabetes.joblib")

model_hipertensao = load("modelo_hipertensao.joblib")
scaler_hipertensao = load("scaler_hipertensao.joblib")


class DiabetesPredictor(Resource):
    def post(self):
        data = request.get_json()
        features = [
            data["Glicose_Jejum"],
            data["Hemoglobina_A1c"],
            data["Tolerancia_Glicose"],
            data["Glicose_Aleatoria"],
        ]

        # Padronizar os dados
        features_scaled = scaler_diabetes.transform([features])

        # Fazer previsão
        prediction = model_diabetes.predict(features_scaled)[0]

        return jsonify({"prediction": prediction})


class HipertensaoPredictor(Resource):
    def post(self):
        data = request.get_json()
        features = [
            data["Glicose_Jejum"],
            data["Hemoglobina_A1c"],
            data["Tolerancia_Glicose"],
            data["Glicose_Aleatoria"],
        ]

        # Padronizar os dados
        features_scaled = scaler_hipertensao.transform([features])

        # Fazer previsão
        prediction = model_hipertensao.predict(features_scaled)[0]

        return jsonify({"prediction": prediction})


# Adicionar recursos à API
api.add_resource(DiabetesPredictor, "/predict_diabetes")
api.add_resource(HipertensaoPredictor, "/predict_hipertensao")

if __name__ == "__main__":
    app.run(debug=True)
