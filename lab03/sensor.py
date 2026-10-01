porog = float(input())
kol_vo_zap = int(input())
errors_count = 0 
cpicok_temp = []
prev = 0 
for i in range(kol_vo_zap):
    stroka = input().strip()
    if stroka == 'error':
        errors_count +=1
    else:
        gradus = float(stroka)
        cpicok_temp.append(gradus)
        if gradus > porog:
            prev +=1
max_temp = max(cpicok_temp)
avg_temp =sum(cpicok_temp)/len(cpicok_temp)
print(kol_vo_zap)
print(errors_count)
print(prev)
print(f"{max_temp:.1f}")  # округление до 1 знака после запятой
print(f"{avg_temp:.1f}")           