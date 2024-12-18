# Amazon-Review-System
Proyecto de Modelos Generativos y Clasificación de Reseñas
Este proyecto aborda la construcción de modelos de clasificación y generación de texto enfocados en el análisis y transformación de reseñas con polaridad positiva y negativa. El repositorio contiene notebooks y scripts que implementan estos modelos y técnicas relacionadas.

Descripción General del Proyecto
Clasificación de Reseñas
Preprocesamiento: Limpieza y preparación de datos para el entrenamiento del modelo clasificador.
Modelo de Clasificación:
Construcción de un clasificador utilizando vectorización TF-IDF y regresión logística.
Implementación en una clase que encapsula la lógica de vectorización, entrenamiento y predicción.
Validación Cruzada:
Uso de K-Folds para evaluar el rendimiento del modelo.
Generación de informes de clasificación con métricas como precisión, recall y F1-score.
Resultados:
Análisis de las métricas de evaluación y comparación con el sistema generativo.
Modelo Generativo para Invertir Polaridad
Transformación de Polaridad:
Desarrollo de un modelo generativo para convertir reseñas positivas en negativas y viceversa.
Generación de un conjunto de datos adecuado para entrenar este modelo.
Construcción del Modelo:
Implementación de un modelo de codificador-decodificador basado en redes neuronales.
Proceso:
Codificación de la secuencia de entrada en vectores de estado.
Generación iterativa de caracteres de salida hasta completar la secuencia transformada.
Validación:
Evaluación de la calidad de las transformaciones mediante ejemplos generados.
Puntos Finales en la Nube
El proyecto incluye la implementación de dos puntos finales públicos desplegados en un proveedor de nube:

Debido a limitaciones de tamaño en GitHub, algunos recursos como datasets y configuraciones específicas no están incluidos en este repositorio. Se recomienda consultar las fuentes indicadas en la documentación para obtener los datos y configuraciones necesarias.

tire paro profe.
