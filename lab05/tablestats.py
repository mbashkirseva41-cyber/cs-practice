def read_rows(lines): ##читаем строки из файла, из каждой строчки делаем словарь
    rows = []
    headers = None #для хранения заголовка файла
    
    for line in lines:
        line = line.strip() ##удаляем пробелы
        if not line:
            continue  # Пропускаем пустые строки
            
        # Разбираем строку по запятым и убираем пробелы вокруг значений
        fields = [f.strip() for f in line.split(',')]
        
        # Находим первый непустой заголовок
        if headers is None:
            headers = fields
            continue
            
        # Если полей не столько же, сколько в заголовке — пропускаем
        if len(fields) != len(headers):
            continue
            
        # Собираем словарь {колонка: значение}
        row_dict = {headers[i]: fields[i] for i in range(len(headers))}
        rows.append(row_dict)
        
    return rows


def count_types(rows): ##посчитать, сколько раз в таблице встречается каждый тип события
    counts = {}##словарь
    for row in rows:
        # Предполагаем, что тип события лежит в колонке 'тип' или 'type'
        kind = row.get('тип') or row.get('type')
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind): ##найти все строчки с нужным типом события 
    total = 0.0
    has_kind = False
    
    for row in rows: ##проходим по всем прочитанным ранее строкам-словарям.
        current_kind = row.get('тип') or row.get('type')
        if current_kind == kind: ## совпадает ли тип текущей строки с тем, что мы ищем
            has_kind = True
            # Ищем колонку с минутами (длительностью)
            duration_str = row.get('минуты') or row.get('minutes') or row.get('длительность')
            if duration_str:
                # Меняем запятую на точку для правильной конвертации в float
                duration_str = duration_str.replace(',', '.')
                try:
                    total += float(duration_str)
                except ValueError:
                    continue  # Нечисловое значение пропускается
                    
    if not has_kind:
        return 0.0
        
    return round(total, 1)##возвращает итоговую сумму минут, округленную до одного знака после запятой


def to_csv(counts):##превращает её обратно в красивый текст формата CSV, чтобы записать в итоговый файл.
    # Заголовок
    csv_lines = ["тип,количество"]
    
    # Сортируем типы по алфавиту и добавляем строки
    for kind in sorted(counts.keys()):
        csv_lines.append(f"{kind},{counts[kind]}")
        
    # В конце обязателен перевод строки
    return "\n".join(csv_lines) + "\n"
## склеивает все элементы списка в один большой текст, вставляя между ними перенос строки 
