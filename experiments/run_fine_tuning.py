"""
Executa uma rodada de Fine-Tuning com a seed fornecida.

Uso:
    python experiments/run_fine_tuning.py --seed 1
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
#   4. Construir modelo Fine-Tuning (mesma cabeça do Cenário A)
#   5. Treinar em duas etapas (cabeça → descongelar backbone)
#   6. Avaliar no conjunto de teste
#   7. Salvar métricas em METRICS_CSV
#   8. Salvar modelo em MODELS_DIR (opcional)


def main():
    parser = argparse.ArgumentParser(description="Fine-Tuning — uma execução")
    parser.add_argument("--seed", type=int, required=True, help="Seed do experimento")
    args = parser.parse_args()

    print(f"[Fine-Tuning] seed={args.seed}")
    # TODO: implementar pipeline aqui


if __name__ == "__main__":
    main()
