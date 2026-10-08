def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i]>scores[best_index]:
            best_index = i
    return names[best_index]
def average(scores: list[float])-> float:
    if not scores:
        return 0.0
    return round(sum(scores)/len(scores),2)
def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    indices.sort(key=lambda i: scores[i], reverse=True)
    return [names[i] for i in indices]
def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])
    return result

тестовые_имена = ["Аня", "Борис", "Влад", "Даша"]
тестовые_баллы = [4.5, 5.0, 3.8, 5.0]

# Проверяем работу функций
print("Победитель:", winner(тестовые_имена, тестовые_баллы))
print("Средний балл:", average(тестовые_баллы))
print("Рейтинг:", ranking(тестовые_имена, тестовые_баллы))
print("Выше среднего:", above_average(тестовые_имена, тестовые_баллы))
