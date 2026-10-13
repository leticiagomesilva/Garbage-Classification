# Garbage-Classification
O projeto investiga como diferentes estratégias de Transfer Learning afetam a classificação automática de resíduos recicláveis.
 
---

## Introdução do projeto

O projeto investiga como diferentes estratégias de Transfer Learning afetam a classificação automática de resíduos recicláveis.
A ideia é utilizar uma CNN pré-treinada, por exemplo uma ResNet50 ou MobileNetV2, e comparar duas formas de reaproveitar esse conhecimento:
- Feature Extraction: congelar a maior parte da rede e treinar apenas a camada classificadora.
- Fine-Tuning: descongelar parte das camadas da rede e continuar o treinamento no novo conjunto de dados.

Em ambos os casos, vocês podem utilizar Grad-CAM para visualizar quais regiões da imagem influenciaram a decisão do modelo.
A pergunta de pesquisa será:

> O fine-tuning melhora significativamente o desempenho de uma CNN com Transfer Learning na classificação de resíduos recicláveis em comparação ao uso da rede apenas como extratora de características?

E as hipóteses:

> H0: não existe diferença estatisticamente significativa entre as duas estratégias

> H1: o fine-tuning apresenta desempenho estatisticamente superior ao feature extraction
