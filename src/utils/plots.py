"""
Funções de plotagem reutilizáveis.
Salva automaticamente as figuras em FIGURES_DIR.
"""

import os
import matplotlib.pyplot as plt
import numpy as np
from src.utils.config import FIGURES_DIR, CONFUSION_DIR


def save_fig(fig: plt.Figure, filename: str, subdir: str = FIGURES_DIR) -> None:
    os.makedirs(subdir, exist_ok=True)
    path = os.path.join(subdir, filename)
    fig.savefig(path, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(f"Figura salva em: {path}")


def plot_class_distribution(class_counts: dict, title: str = "Distribuição por Classe") -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(class_counts.keys(), class_counts.values())
    ax.set_title(title)
    ax.set_xlabel("Classe")
    ax.set_ylabel("Número de imagens")
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    return fig


def plot_boxplot(fe_scores: list, ft_scores: list, metric: str = "macro_f1") -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.boxplot(
        [fe_scores, ft_scores],
        labels=["Feature Extraction", "Fine-Tuning"],
        patch_artist=True,
    )
    ax.set_title(f"Comparação — {metric}")
    ax.set_ylabel(metric)
    return fig


def plot_training_curves(history: dict, title: str = "Curvas de Treinamento") -> plt.Figure:
    """history deve conter chaves 'train_loss' e 'val_loss' (listas)."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(history["train_loss"], label="Train Loss")
    ax.plot(history["val_loss"], label="Val Loss")
    ax.set_title(title)
    ax.set_xlabel("Época")
    ax.set_ylabel("Loss")
    ax.legend()
    fig.tight_layout()
    return fig
