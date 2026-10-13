"""
Cenário B — Fine-Tuning.
Backbone parcialmente descongelado + treinamento em duas etapas.
"""

# TODO: implementar após feature_extraction.py estar completo
#
# Passos:
#   Etapa 1 — aquecer a cabeça:
#     1. Carregar backbone congelado
#     2. Treinar somente a cabeça por FT_EPOCHS_HEAD épocas com FT_LR_HEAD
#
#   Etapa 2 — fine-tuning:
#     3. Descongelar as últimas FT_NUM_UNFROZEN_LAYERS camadas do backbone
#     4. Continuar treinamento por FT_EPOCHS_UNFREEZE épocas com FT_LR_UNFREEZE
#
# IMPORTANTE: usar o mesmo backbone e cabeça do Cenário A.
