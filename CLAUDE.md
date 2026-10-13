Você vai me ajudar a desenvolver um projeto acadêmico de Inteligência Artificial para a segunda unidade da disciplina.

Quero que você atue como um assistente técnico de desenvolvimento, organização experimental e documentação.

==================================================
1. CONTEXTO DO TRABALHO
==================================================

O professor solicitou um estudo comparativo envolvendo obrigatoriamente 3 técnicas vistas em sala de aula.

Requisitos da avaliação:

- Selecionar obrigatoriamente 3 técnicas abordadas em sala;
- Comparar a performance em 2 cenários:
  Técnica A + Técnica B + Técnica C
  VS
  Técnica A + Técnica B + Técnica C em uma configuração alternativa;
- Realizar 30 simulações;
- Inferir qual das duas abordagens é mais eficaz por meio de teste de hipótese:
  Hipótese Nula (H0)
  ou
  Hipótese Alternativa (H1);
- Entregar:
  - código do caso de uso;
  - apresentação;
  - relatório em formato IEEE de coluna dupla;
  - gráficos e análise dos resultados.

Os temas vistos em sala incluem:

1. Fundamentos de Inteligência Artificial e Aprendizagem Profunda;
2. Redes Neurais Profundas e Otimização;
3. Redes Neurais Convolucionais (CNNs) para Visão Computacional;
4. Modelos Sequenciais e RNNs;
5. Processamento de Linguagem Natural, Transformers e Atenção;
6. GANs e Autoencoders;
7. LLMs;
8. Prompt Engineering, Transfer Learning e Few-shot Learning;
9. Interpretabilidade, Explicabilidade (XAI) e Ética em IA;
10. IA e Ética.

Na primeira unidade, nosso grupo apresentou Transfer Learning, então queremos aproveitar esse conhecimento no projeto.

==================================================
2. TEMA DO PROJETO
==================================================

Tema:

"Estudo Comparativo entre Feature Extraction e Fine-Tuning em Redes Neurais Convolucionais utilizando Transfer Learning e Grad-CAM para Classificação de Resíduos Recicláveis"

Caso de uso:

Classificação automática de imagens de resíduos recicláveis.

Possíveis classes:

- papel;
- papelão;
- plástico;
- vidro;
- metal;
- lixo geral/trash.

A quantidade e os nomes exatos das classes devem ser definidos com base no dataset escolhido.

As 3 técnicas principais do trabalho serão:

Técnica A:
CNN - Redes Neurais Convolucionais

Técnica B:
Transfer Learning

Técnica C:
XAI / Explainable AI utilizando Grad-CAM

==================================================
3. PERGUNTA DE PESQUISA
==================================================

Pergunta principal:

"O fine-tuning melhora significativamente o desempenho de uma CNN com Transfer Learning na classificação de resíduos recicláveis em comparação ao uso da rede apenas como extratora de características?"

==================================================
4. HIPÓTESES
==================================================

H0 - Hipótese Nula:

Não existe diferença estatisticamente significativa entre o desempenho da abordagem de Feature Extraction e da abordagem de Fine-Tuning.

H1 - Hipótese Alternativa:

A abordagem de Fine-Tuning apresenta desempenho estatisticamente superior à abordagem de Feature Extraction.

Utilizar nível de significância:

alpha = 0.05

A conclusão NÃO deve ser feita apenas comparando médias.

Deve ser utilizado teste estatístico apropriado.

Preferencialmente:

- verificar normalidade das diferenças entre os pares de resultados;
- se apropriado, utilizar teste t pareado;
- caso contrário, utilizar Wilcoxon Signed-Rank Test.

As duas estratégias devem ser comparadas sobre execuções correspondentes para permitir análise pareada.

==================================================
5. CENÁRIOS EXPERIMENTAIS
==================================================

Os dois cenários devem utilizar:

- mesmo dataset;
- mesmo pré-processamento;
- mesmo backbone;
- mesmas divisões de dados;
- mesmas métricas;
- configurações equivalentes sempre que possível.

A principal diferença deve ser a estratégia de Transfer Learning.

----------------------------------------------
CENÁRIO A - FEATURE EXTRACTION
----------------------------------------------

CNN pré-treinada + Transfer Learning + Grad-CAM.

Utilizar uma CNN pré-treinada no ImageNet.

Sugestão inicial:

MobileNetV2.

Motivo:
é relativamente leve e adequada para realizar várias execuções.

Neste cenário:

- carregar pesos pré-treinados;
- remover/substituir a camada classificadora original;
- congelar o backbone convolucional;
- treinar apenas a nova cabeça classificadora;
- avaliar o modelo;
- aplicar Grad-CAM.

----------------------------------------------
CENÁRIO B - FINE-TUNING
----------------------------------------------

CNN pré-treinada + Transfer Learning + Grad-CAM.

Utilizar exatamente o mesmo backbone.

Neste cenário:

- iniciar com a rede pré-treinada;
- utilizar a mesma cabeça classificadora;
- inicialmente manter o backbone congelado, caso faça sentido;
- posteriormente descongelar parte das últimas camadas;
- continuar o treinamento com learning rate menor;
- avaliar;
- aplicar Grad-CAM.

Evitar comparar arquiteturas diferentes.

O objetivo principal é comparar estratégias diferentes de Transfer Learning, e não MobileNet vs ResNet.

==================================================
6. DATASET
==================================================

Pretendemos utilizar um dataset de imagens de resíduos recicláveis.

Possíveis fontes:

- TrashNet;
- Kaggle;
- Roboflow Universe;
- Mendeley Data;
- Zenodo.

Termos para busca:

- garbage classification dataset;
- recyclable waste classification;
- trash classification;
- waste classification;
- recycling dataset.

Preferência:

dataset com aproximadamente 2.000 a 10.000 imagens.

Antes de implementar definitivamente o pipeline, analisar:

- quantidade total de imagens;
- quantidade por classe;
- possíveis classes desbalanceadas;
- resolução das imagens;
- imagens corrompidas;
- duplicatas, caso possível;
- distribuição por classe.

NÃO assuma ainda a estrutura final do dataset enquanto ele não estiver presente no repositório.

Caso o dataset ainda não esteja disponível, prepare a estrutura do código para recebê-lo, mas não invente caminhos ou classes definitivas.

==================================================
7. EDA - ANÁLISE EXPLORATÓRIA
==================================================

Criar uma etapa de EDA contendo:

- número total de imagens;
- quantidade por classe;
- distribuição das classes;
- exemplos visuais de cada classe;
- dimensões/resoluções;
- identificação de possível desbalanceamento;
- identificação de imagens inválidas/corrompidas, se possível.

Gerar gráficos úteis para o relatório.

Exemplos:

- gráfico de barras por classe;
- amostras de imagens;
- distribuição das dimensões.

==================================================
8. PRÉ-PROCESSAMENTO
==================================================

Pipeline inicial sugerido:

- redimensionar para 224x224;
- normalizar de acordo com o backbone utilizado;
- gerar datasets de treino, validação e teste;
- usar divisão estratificada quando aplicável.

Divisão sugerida inicialmente:

70% treino
15% validação
15% teste

A divisão exata pode ser ajustada após análise do dataset.

IMPORTANTE:

O conjunto de teste deve ser preservado para avaliação final.

A comparação entre os dois cenários deve usar exatamente os mesmos dados de teste.

Caso seja utilizado Data Augmentation:

- aplicar apenas nos dados de treinamento;
- documentar exatamente quais transformações são utilizadas.

Possíveis transformações:

- pequenas rotações;
- flip horizontal;
- zoom leve;
- pequenas alterações de brilho.

Evitar augmentations que alterem semanticamente a classe.

==================================================
9. 30 SIMULAÇÕES
==================================================

O professor exige 30 simulações.

Precisamos de um protocolo experimental claro e reproduzível.

Executar:

30 rodadas para Feature Extraction
30 rodadas para Fine-Tuning

As execuções devem ser pareadas.

Exemplo:

seed 1:
feature extraction
fine-tuning

seed 2:
feature extraction
fine-tuning

...

seed 30:
feature extraction
fine-tuning

Registrar a seed de cada experimento.

Não alterar hiperparâmetros arbitrariamente entre execuções.

O objetivo é observar a variabilidade do treinamento e comparar as duas estratégias de forma justa.

==================================================
10. MÉTRICAS
==================================================

Registrar no mínimo:

- accuracy;
- precision;
- recall;
- F1-score;
- macro F1-score;
- training loss;
- validation loss;
- tempo de treinamento.

Se houver desbalanceamento entre as classes, priorizar Macro F1 como uma das métricas principais.

Também gerar:

- matriz de confusão;
- classification report por classe.

==================================================
11. RESULTADOS
==================================================

Gerar um arquivo consolidado, preferencialmente CSV, com estrutura semelhante:

seed
scenario
accuracy
precision
recall
f1
macro_f1
train_time

Exemplo:

1,feature_extraction,...
1,fine_tuning,...
2,feature_extraction,...
2,fine_tuning,...
...

==================================================
12. ANÁLISE ESTATÍSTICA
==================================================

Após as 30 execuções, calcular:

- média;
- mediana;
- desvio padrão;
- mínimo;
- máximo;
- intervalo de confiança, se adequado.

Gerar gráficos como:

- boxplot Feature Extraction vs Fine-Tuning;
- distribuição das métricas;
- gráfico das 30 execuções;
- comparação de médias;
- curvas de treino e validação representativas;
- matrizes de confusão;
- Grad-CAM.

Realizar teste de hipótese.

Não interpretar p-value incorretamente.

A análise final deve considerar:

- significância estatística;
- tamanho da diferença;
- estabilidade das execuções;
- custo computacional;
- desempenho por classe.

==================================================
13. GRAD-CAM / XAI
==================================================

Utilizar Grad-CAM para interpretar previsões dos dois cenários.

Gerar exemplos para:

- classificações corretas;
- classificações incorretas;
- casos ambíguos, se existirem.

Comparar visualmente:

Feature Extraction
VS
Fine-Tuning

Objetivo:

investigar se o modelo está utilizando regiões visualmente coerentes da imagem para realizar a classificação.

Grad-CAM NÃO deve ser usado como métrica quantitativa principal de desempenho.

Ele será utilizado como ferramenta de interpretabilidade.

==================================================
14. ESTRUTURA DO PROJETO
==================================================

Utilizar aproximadamente esta estrutura:

transfer-learning-waste/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── splits/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_extraction.ipynb
│   ├── 03_fine_tuning.ipynb
│   └── 04_resultados.ipynb
│
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   ├── preprocessing.py
│   │   └── augmentation.py
│   │
│   ├── models/
│   │   ├── backbone.py
│   │   ├── feature_extraction.py
│   │   └── fine_tuning.py
│   │
│   ├── training/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── metrics.py
│   │
│   ├── explainability/
│   │   └── gradcam.py
│   │
│   ├── statistics/
│   │   └── hypothesis_test.py
│   │
│   └── utils/
│       ├── seed.py
│       ├── config.py
│       └── plots.py
│
├── experiments/
│   ├── run_feature_extraction.py
│   ├── run_fine_tuning.py
│   └── run_30_experiments.py
│
├── results/
│   ├── metrics/
│   ├── figures/
│   ├── confusion_matrices/
│   ├── gradcam/
│   └── models/
│
├── reports/
│   ├── artigo_ieee/
│   └── apresentacao/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore

A estrutura pode ser simplificada se o repositório atual já possuir outra organização.

Antes de criar muitos arquivos, examine primeiro a estrutura existente do repositório.

==================================================
15. CONFIGURAÇÃO CENTRAL
==================================================

Centralizar hiperparâmetros.

Exemplos:

IMAGE_SIZE = 224
BATCH_SIZE = 32
BACKBONE = "MobileNetV2"
NUM_RUNS = 30
RANDOM_SEEDS = 1..30

Separar parâmetros de:

Feature Extraction

e

Fine-Tuning.

Exemplo:

FEATURE_EXTRACTION_LR
FINE_TUNING_LR
FEATURE_EXTRACTION_EPOCHS
FINE_TUNING_EPOCHS
NUM_UNFROZEN_LAYERS

Não fixar valores definitivos sem antes avaliar recursos computacionais e dataset.

==================================================
16. REPRODUTIBILIDADE
==================================================

Implementar controle de seeds para:

- Python;
- NumPy;
- framework de Deep Learning;
- divisão dos dados, quando aplicável.

Registrar:

- versão das bibliotecas;
- hiperparâmetros;
- seed;
- data do experimento;
- hardware quando possível.

==================================================
17. FRAMEWORK
==================================================

Antes de começar, verifique qual framework já existe no repositório.

Preferência:

TensorFlow/Keras ou PyTorch.

Não misturar frameworks sem necessidade.

Se nenhum framework estiver definido, apresente brevemente as vantagens e desvantagens de:

- TensorFlow/Keras;
- PyTorch;

e aguarde decisão antes de implementar toda a solução.

==================================================
18. README
==================================================

O README deve documentar:

- objetivo do projeto;
- contexto acadêmico;
- pergunta de pesquisa;
- hipóteses;
- técnicas utilizadas;
- dataset;
- estrutura do projeto;
- instalação;
- execução da EDA;
- execução de Feature Extraction;
- execução de Fine-Tuning;
- execução das 30 simulações;
- geração da análise estatística;
- geração do Grad-CAM;
- localização dos resultados.

==================================================
19. RELATÓRIO IEEE
==================================================

O relatório será em formato IEEE de coluna dupla.

Estrutura inicial sugerida:

1. Abstract
2. Introdução
3. Fundamentação Teórica
   - CNN
   - Transfer Learning
   - Feature Extraction
   - Fine-Tuning
   - Explainable AI
   - Grad-CAM
4. Trabalhos Relacionados
5. Metodologia
6. Dataset
7. Configuração Experimental
8. Resultados
9. Análise Estatística
10. Discussão
11. Ameaças à Validade / Limitações
12. Conclusão
13. Referências

Não inventar resultados antes dos experimentos.

==================================================
20. APRESENTAÇÃO
==================================================

A apresentação deve posteriormente explicar:

- problema;
- motivação;
- dataset;
- técnicas escolhidas;
- arquitetura;
- Cenário A;
- Cenário B;
- protocolo das 30 execuções;
- métricas;
- resultados;
- teste estatístico;
- Grad-CAM;
- conclusão.

==================================================
21. BOAS PRÁTICAS
==================================================

O código deve:

- ser modular;
- evitar duplicação;
- possuir nomes claros;
- separar treino, avaliação e análise;
- salvar resultados automaticamente;
- permitir reprodução dos experimentos;
- evitar hardcode desnecessário;
- conter comentários apenas onde agregarem entendimento;
- possuir tratamento de erros essencial;
- não esconder decisões metodológicas.

==================================================
22. O QUE NÃO DEVE SER FEITO
==================================================

Não:

- criar resultados fictícios;
- inventar métricas;
- assumir classes do dataset antes de verificá-lo;
- usar o conjunto de teste durante treinamento ou seleção de hiperparâmetros;
- mudar múltiplas variáveis ao mesmo tempo entre os cenários;
- usar arquiteturas diferentes entre Feature Extraction e Fine-Tuning sem justificativa;
- executar fine-tuning com todos os parâmetros aleatoriamente definidos sem uma estratégia;
- tratar Grad-CAM como prova de causalidade;
- concluir H1 apenas porque a média é maior;
- executar teste estatístico inadequado sem verificar suas premissas;
- versionar datasets ou modelos gigantes sem necessidade;
- criar uma arquitetura excessivamente complexa antes de validar o pipeline mínimo.

==================================================
23. ORDEM DE IMPLEMENTAÇÃO
==================================================

Quero seguir esta sequência:

ETAPA 1
Inspecionar o repositório existente.

ETAPA 2
Definir framework e dependências.

ETAPA 3
Adicionar estrutura mínima de pastas.

ETAPA 4
Adicionar e validar o dataset.

ETAPA 5
Realizar EDA.

ETAPA 6
Criar preprocessing e DataLoader.

ETAPA 7
Criar backbone compartilhado.

ETAPA 8
Implementar Feature Extraction.

ETAPA 9
Executar uma execução de teste.

ETAPA 10
Implementar Fine-Tuning.

ETAPA 11
Executar uma execução de teste.

ETAPA 12
Implementar avaliação e métricas.

ETAPA 13
Implementar Grad-CAM.

ETAPA 14
Validar todo o pipeline com poucas execuções.

ETAPA 15
Implementar execução automatizada das 30 simulações.

ETAPA 16
Executar os experimentos definitivos.

ETAPA 17
Analisar resultados.

ETAPA 18
Executar testes estatísticos.

ETAPA 19
Gerar gráficos e tabelas.

ETAPA 20
Atualizar README e documentação.

ETAPA 21
Produzir conteúdo para relatório IEEE e apresentação.

==================================================
24. COMO QUERO QUE VOCÊ TRABALHE
==================================================

Não implemente tudo de uma vez.

Primeiro:

1. examine a estrutura atual do repositório;
2. identifique o que já existe;
3. diga quais arquivos precisam ser criados ou modificados;
4. proponha o primeiro pequeno passo;
5. aguarde confirmação quando existir uma decisão relevante ainda não definida.

Quando uma informação essencial estiver faltando, como:

- dataset;
- framework;
- hardware;
- estrutura atual do repositório;
- quantidade de classes;

não faça suposições desnecessárias.

Informe claramente o que está faltando.

Durante a implementação, explique de forma curta:

- o que está sendo feito;
- por que é necessário;
- qual arquivo está sendo alterado;
- como testar.

Priorize uma implementação incremental e executável.

==================================================
25. OBJETIVO FINAL
==================================================

Ao final, o projeto deve permitir responder de maneira experimental e estatisticamente fundamentada:

"Na classificação de resíduos recicláveis utilizando uma CNN pré-treinada, o Fine-Tuning oferece ganho significativo de desempenho em relação ao uso do modelo apenas como Feature Extractor?"

Os resultados devem permitir avaliar simultaneamente:

- desempenho;
- estabilidade;
- custo computacional;
- interpretabilidade.

Agora, antes de implementar qualquer coisa, examine o estado atual do repositório e me entregue:

1. resumo da estrutura existente;
2. o que já pode ser reutilizado;
3. o que está faltando;
4. a estrutura mínima recomendada;
5. o primeiro passo que devemos implementar.