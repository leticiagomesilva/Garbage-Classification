"""
Executa as 30 simulações pareadas (Feature Extraction + Fine-Tuning).

Uso:
    python experiments/run_30_experiments.py
    python experiments/run_30_experiments.py --dry-run   # executa apenas seed 1 para validação
"""

import argparse
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.utils.config import RANDOM_SEEDS


def run_experiment(script: str, seed: int) -> int:
    cmd = [sys.executable, script, "--seed", str(seed)]
    print(f"\n{'='*60}")
    print(f"Executando: {' '.join(cmd)}")
    print(f"{'='*60}")
    result = subprocess.run(cmd)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="30 simulações pareadas")
    parser.add_argument("--dry-run", action="store_true", help="Executa apenas seed=1")
    args = parser.parse_args()

    seeds = [1] if args.dry_run else RANDOM_SEEDS
    fe_script = os.path.join(os.path.dirname(__file__), "run_feature_extraction.py")
    ft_script = os.path.join(os.path.dirname(__file__), "run_fine_tuning.py")

    failed = []
    for seed in seeds:
        for script, label in [(fe_script, "FE"), (ft_script, "FT")]:
            rc = run_experiment(script, seed)
            if rc != 0:
                failed.append((seed, label))
                print(f"ERRO na execução seed={seed} {label}")

    print(f"\n{'='*60}")
    if failed:
        print(f"Execuções com falha: {failed}")
    else:
        print("Todas as execuções concluídas com sucesso.")


if __name__ == "__main__":
    main()
