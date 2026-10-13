"""
Executa uma rodada de Feature Extraction com a seed fornecida.

Uso:
    python experiments/run_feature_extraction.py --seed 1
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# TODO: implementar após os módulos src/ estarem completos
#
# Passos:
#   1. Receber seed via argparse
#   2. Chamar set_seed(seed)
#   3. Carregar splits de data/splits/
#   4. Construir modelo Feature Extraction
#   5. Treinar
#   6. Avaliar no conjunto de teste
#   7. Salvar métricas em METRICS_CSV
#   8. Salvar modelo em MODELS_DIR (opcional)


def main():
    parser = argparse.ArgumentParser(description="Feature Extraction — uma execução")
    parser.add_argument("--seed", type=int, required=True, help="Seed do experimento")
    args = parser.parse_args()

    print(f"[Feature Extraction] seed={args.seed}")
    # TODO: implementar pipeline aqui


if __name__ == "__main__":
    main()
