"""
Configuração central do projeto.
Altere os valores aqui antes de executar os experimentos.
"""

# -------------------------------------------------------------------
# Dados
# -------------------------------------------------------------------
DATA_RAW_DIR = "data/raw"
DATA_PROCESSED_DIR = "data/processed"
DATA_SPLITS_DIR = "data/splits"

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

# -------------------------------------------------------------------
# Pré-processamento
# -------------------------------------------------------------------
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

# Normalização ImageNet (usada pelo MobileNetV2)
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

# -------------------------------------------------------------------
# Backbone
# -------------------------------------------------------------------
BACKBONE = "MobileNetV2"   # deve ser o mesmo nos dois cenários

# -------------------------------------------------------------------
# Feature Extraction
# -------------------------------------------------------------------
FE_EPOCHS = 20
FE_LR = 1e-3

# -------------------------------------------------------------------
# Fine-Tuning
# -------------------------------------------------------------------
FT_EPOCHS_HEAD = 10        # etapa 1: cabeça congelada
FT_EPOCHS_UNFREEZE = 20    # etapa 2: últimas camadas descongeladas
FT_LR_HEAD = 1e-3
FT_LR_UNFREEZE = 1e-5
FT_NUM_UNFROZEN_LAYERS = 30  # número de camadas descongeladas no backbone

# -------------------------------------------------------------------
# Simulações
# -------------------------------------------------------------------
NUM_RUNS = 30
RANDOM_SEEDS = list(range(1, NUM_RUNS + 1))

# -------------------------------------------------------------------
# Resultados
# -------------------------------------------------------------------
RESULTS_DIR = "results"
METRICS_DIR = "results/metrics"
FIGURES_DIR = "results/figures"
CONFUSION_DIR = "results/confusion_matrices"
GRADCAM_DIR = "results/gradcam"
MODELS_DIR = "results/models"

METRICS_CSV = "results/metrics/all_results.csv"
