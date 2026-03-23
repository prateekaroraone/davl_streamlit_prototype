def compute_score(validation_results):
    scores = {}
    for source, metrics in validation_results.items():
        score = (float(metrics['fresh_pass']) + float(metrics['completeness_pass'])) / 2
        scores[source] = score
    return scores
