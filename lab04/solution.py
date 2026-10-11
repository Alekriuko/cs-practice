def winner(names: list[str], scores: list[float]) -> str:
    if not names or not scores:
        return ""
    
    max_id = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[max_id]:
            max_id = i
    return names[max_id]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    d = f'{(sum(scores) / len(scores)):.2f}'
    return float(d)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    paired = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    return [name for name, score in paired]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    a = []
    sr = float(average(scores)) 
    for i in range(len(scores)):
        if scores[i] > sr:
            a.append(names[i])
    return a