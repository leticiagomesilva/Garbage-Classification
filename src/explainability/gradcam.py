"""
Implementação de Grad-CAM para interpretabilidade (XAI).
Utilizado em ambos os cenários após o treinamento.
"""

# TODO: implementar após os modelos estarem treinados
#
# Responsabilidades:
#   1. Receber modelo e imagem de entrada
#   2. Identificar a última camada convolucional do backbone
#   3. Calcular gradientes em relação à classe predita
#   4. Gerar heatmap sobreposto na imagem original
#   5. Salvar em GRADCAM_DIR (ver config.py)
#
# Gerar exemplos para:
#   - classificações corretas
#   - classificações incorretas
#   - casos ambíguos (se existirem)
#
# IMPORTANTE: Grad-CAM é ferramenta de interpretabilidade,
# não deve ser usado como métrica quantitativa principal.
