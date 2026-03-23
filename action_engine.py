def take_action(decision_name, scores, thresholds={'critical':0.5,'warning':0.8}):
    for source, score in scores.items():
        if score < thresholds['critical']:
            print(f"[CRITICAL] {decision_name} failed validation for {source}. Trigger fallback!")
        elif score < thresholds['warning']:
            print(f"[WARNING] {decision_name} below expected quality for {source}. Notify team.")
        else:
            print(f"[OK] {decision_name} passed validation for {source}.")
