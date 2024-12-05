
from flask import Flask, request, jsonify
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo de regresión logística y vectorizador TFIDF
with open('logistic_tfidf_model.pkl', 'rb') as f:
    logistic_model = pickle.load(f)

# Cargar el modelo de generación basado en Keras
generator_model = load_model('modelo_codificador_decodificador.h5')

# Endpoint para la predicción de polaridad
@app.route('/polarity', methods=['POST'])
def predict_polarity():
    data = request.json
    review_text = data.get('review_text', '')
    if not review_text:
        return jsonify({"error": "No review text provided"}), 400
    
    # Procesar con el vectorizador TFIDF
    review_vectorized = logistic_model['vectorizer'].transform([review_text])
    prediction = logistic_model['model'].predict(review_vectorized)
    confidence = logistic_model['model'].predict_proba(review_vectorized).max()

    return jsonify({
        "polarity": int(prediction[0]),
        "confidence": float(confidence)
    })

# Endpoint para generar texto con polaridad invertida
@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    review_text = data.get('review_text', '')
    if not review_text:
        return jsonify({"error": "No review text provided"}), 400
    
    # Predecir polaridad original
    review_vectorized = logistic_model['vectorizer'].transform([review_text])
    original_polarity = int(logistic_model['model'].predict(review_vectorized)[0])
    
    # Generar texto con modelo de Keras (asumimos que ya está configurado para este propósito)
    generated_sequence = generator_model.predict(np.array([review_text]))
    generated_text = ''.join([chr(int(x)) for x in generated_sequence[0]])  # Ejemplo de postproceso

    return jsonify({
        "original_polarity": original_polarity,
        "generated_text": generated_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
