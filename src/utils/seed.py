"""
Controle de seeds para reprodutibilidade.
Deve ser chamado no início de cada execução experimental.
"""

import os
import random
import numpy as np


def set_seed(seed: int) -> None:
    """Define a seed em todos os módulos relevantes."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    # PyTorch (opcional — só importa se estiver instalado)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    # TensorFlow/Keras (opcional — só importa se estiver instalado)
    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
    except ImportError:
        pass
