n = 2
queries = ["desktop1 request", "desktop2 request", "desktop1 release", "desktop2 release", "desktop3 request", "desktop3 release", "desktop2 request", "desktop1 request"]

def solution(n, queries):
    answer = []
    desktop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    prev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(queries)):
        suc = 0
        suc2 = 0
        if queries[i][8] == '0':
            if queries[i][-1] == 't':
                if prev[10] != 0 and prev[10] not in desktop:
                    desktop[10] = prev[10]
                    suc2 = 1
                else:
                    for j in range(1, n + 1):
                        if j not in desktop:
                            desktop[10] = j
                            suc = 1
                            break
                if suc == 1 or suc2 == 1:
                    answer.append(queries[i][:9] + " 192.168.0." + str(desktop[10]))
                else:
                    answer.append(queries[i][:9] + " reject")
            else:
                prev[10] = desktop[10]
                desktop[10] = 0;
        else:
            num = int(queries[i][7])
            if queries[i][-1] == 't':
                if prev[num] != 0 and prev[num] not in desktop:
                    desktop[num] = prev[num]
                    suc2 = 1
                else:
                    for j in range(1, n + 1):
                        if j not in desktop:
                            desktop[num] = j
                            suc = 1
                            break
                if suc == 1 or suc2 == 1:
                    answer.append(queries[i][:8] + " 192.168.0." + str(desktop[num]))
                else:
                    answer.append(queries[i][:8] + " reject")
            else:
                prev[num] = desktop[num]
                desktop[num] = 0;
    return answer

print(solution(n, queries))