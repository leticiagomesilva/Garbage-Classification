"""
Cenário A — Feature Extraction.
Backbone congelado + nova cabeça classificadora treinada do zero.
"""

# TODO: implementar após backbone.py estar completo
#
# Passos:
#   1. Carregar backbone com backbone.trainable = False
#   2. Adicionar nova cabeça classificadora (GlobalAveragePooling + Dense + Softmax)
#   3. Compilar com FE_LR de config.py
#   4. Retornar modelo pronto para treinamento
