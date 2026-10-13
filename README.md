# Garbage Classification — Estudo Comparativo de Transfer Learning

Estudo comparativo entre **Feature Extraction** e **Fine-Tuning** em Redes Neurais Convolucionais utilizando Transfer Learning e Grad-CAM para classificação automática de resíduos recicláveis.

---

## Contexto acadêmico

Projeto da segunda unidade da disciplina de Inteligência Artificial. Requisitos da avaliação:

- 3 técnicas vistas em sala: **CNN**, **Transfer Learning** e **XAI/Grad-CAM**
- Comparação de dois cenários em 30 simulações pareadas
- Teste de hipótese estatístico para conclusão
- Entregáveis: código, apresentação e relatório IEEE de coluna dupla

---

## Pergunta de pesquisa

> O fine-tuning melhora significativamente o desempenho de uma CNN com Transfer Learning na classificação de resíduos recicláveis em comparação ao uso da rede apenas como extratora de características?

---

## Hipóteses

- **H0:** Não existe diferença estatisticamente significativa entre Feature Extraction e Fine-Tuning.
- **H1:** Fine-Tuning apresenta desempenho estatisticamente superior ao Feature Extraction.
- **Nível de significância:** α = 0,05

---

## Técnicas utilizadas

| # | Técnica | Papel no projeto |
|---|---|---|
| A | CNN (MobileNetV2) | Backbone compartilhado nos dois cenários |
| B | Transfer Learning | Feature Extraction (Cenário A) e Fine-Tuning (Cenário B) |
| C | XAI — Grad-CAM | Interpretabilidade das predições em ambos os cenários |

---

## Dataset

**Fonte:** imagens de resíduos recicláveis em `data/raw/` (não versionadas).

| Classe | Imagens |
|---|---|
| clothes | 1.892 |
| glass | 1.736 |
| plastic | 1.597 |
| shoes | 1.449 |
| cardboard | 1.411 |
| paper | 1.336 |
| metal | 930 |
| battery | 756 |
| biological | 699 |
| trash | 453 |
| **Total** | **12.259** |

Desbalanceamento: razão máx/mín de 4,18× (clothes vs trash). Métrica principal: **Macro F1-score**.

---

## Estrutura do projeto

```
Garbage-Classification/
│
├── data/
│   ├── raw/          ← imagens brutas por classe (não versionadas)
│   ├── processed/    ← imagens pré-processadas (não versionadas)
│   └── splits/       ← índices treino/val/teste por seed
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_extraction.ipynb
│   ├── 03_fine_tuning.ipynb
│   └── 04_resultados.ipynb
│
├── src/
│   ├── data/             load_data · preprocessing · augmentation
│   ├── models/           backbone · feature_extraction · fine_tuning
│   ├── training/         train · evaluate · metrics
│   ├── explainability/   gradcam
│   ├── statistics/       hypothesis_test
│   └── utils/            config · seed · plots
│
├── experiments/
│   ├── run_feature_extraction.py
│   ├── run_fine_tuning.py
│   └── run_30_experiments.py
│
├── results/
│   ├── metrics/           all_results.csv
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
├── requirements.txt
└── .gitignore
```

---

## Instalação

```bash
git clone <repo>
cd Garbage-Classification
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> Adicione as dependências do framework escolhido (PyTorch ou TensorFlow/Keras) conforme as linhas comentadas em `requirements.txt`.

---

## Execução

### 1. EDA

```bash
jupyter notebook notebooks/01_eda.ipynb
```

### 2. Teste de uma execução — Feature Extraction

```bash
python experiments/run_feature_extraction.py --seed 1
```

### 3. Teste de uma execução — Fine-Tuning

```bash
python experiments/run_fine_tuning.py --seed 1
```

### 4. Validação do pipeline completo (dry-run — seed 1 apenas)

```bash
python experiments/run_30_experiments.py --dry-run
```

### 5. 30 simulações definitivas

```bash
python experiments/run_30_experiments.py
```

### 6. Análise estatística e gráficos

```bash
jupyter notebook notebooks/04_resultados.ipynb
```

### 7. Grad-CAM

Os exemplos são gerados automaticamente ao final de cada execução e salvos em `results/gradcam/`.

---

## Resultados

Todas as métricas são consolidadas em `results/metrics/all_results.csv` com a estrutura:

```
seed, scenario, accuracy, precision, recall, f1, macro_f1, train_time
```

Os gráficos (boxplots, curvas de treino, matrizes de confusão) são salvos em `results/figures/` e `results/confusion_matrices/`.

---

## Configuração central

Todos os hiperparâmetros estão em [`src/utils/config.py`](src/utils/config.py). Altere lá antes de rodar os experimentos.

---

## Reprodutibilidade

Cada execução recebe uma seed (1–30) aplicada a Python, NumPy e ao framework de deep learning via `src/utils/seed.py`. Os índices de divisão treino/val/teste são salvos em `data/splits/` para garantir que os dois cenários usem exatamente os mesmos dados.
