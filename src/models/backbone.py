"""
Backbone compartilhado (MobileNetV2 pré-treinado no ImageNet).
Utilizado por Feature Extraction e Fine-Tuning.
"""

# TODO: implementar após definir o framework (PyTorch ou TensorFlow/Keras)
#
# Responsabilidades deste módulo:
#   1. Carregar MobileNetV2 com pesos ImageNet
#   2. Remover a cabeça classificadora original
#   3. Expor o backbone como módulo reutilizável
#   4. Aceitar parâmetro `trainable` para controlar congelamento
