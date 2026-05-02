# core/optimizer.py

from collections import defaultdict

def greedy_set_cover_safe(cases, min_ratio=0.7):

    universe = set()
    for c in cases:
        universe |= set(c.features)

    selected = []
    covered = set()

    remaining = cases.copy()

    target = int(len(cases) * min_ratio)

    while remaining and len(selected) < target:

        best = None
        best_gain = -1

        for c in remaining:
            gain = len(set(c.features) - covered)

            if gain > best_gain:
                best_gain = gain
                best = c

        if not best:
            break

        selected.append(best)
        covered |= set(best.features)
        remaining.remove(best)

    return selected