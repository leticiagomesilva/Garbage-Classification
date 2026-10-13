"""
Teste de hipótese pareado entre Feature Extraction e Fine-Tuning.
"""

# TODO: implementar após as 30 execuções estarem concluídas
#
# Protocolo:
#   1. Carregar METRICS_CSV (ver config.py)
#   2. Para cada seed, calcular a diferença (FT - FE) na métrica principal (macro_f1)
#   3. Verificar normalidade das diferenças (Shapiro-Wilk)
#   4. Se normal: aplicar teste t pareado (scipy.stats.ttest_rel)
#      Senão:      aplicar Wilcoxon Signed-Rank (scipy.stats.wilcoxon)
#   5. Interpretar p-value com alpha = 0.05
#   6. NÃO concluir H1 apenas com base na média — exigir significância estatística
#
# Saída esperada:
#   - estatística do teste
#   - p-value
#   - decisão (rejeitar H0 ou não rejeitar H0)
#   - resumo das métricas (média, mediana, dp, min, max, IC)
