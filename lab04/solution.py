def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i]>scores[best_index]:
            best_index = i
    return names[best_index]
def average(score: list[float])-> float:
    if not score:
        return 0.0
    return round(sum(scores)/len(scores),2)

        

