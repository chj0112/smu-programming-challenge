def solution(text):
    answer = []
    dict = ['A', 'B']
    now = ''
    count = 0
    for i in range(len(text)):
        if count != i:
            continue
        if text[i] in dict:
            now = text[i]
            if i + 1 == len(text):
                answer.append(dict.index(now))
            else:
                for j in range(i + 1, len(text)):
                    if now + text[j] not in dict:
                        answer.append(dict.index(now))
                        dict.append(now + text[j])
                        break
                    else:
                        now += text[j]
                        if j + 1 == len(text):
                            answer.append(dict.index(now))
                        count += 1
        count += 1
    return answer


print(solution("BBAAA"))