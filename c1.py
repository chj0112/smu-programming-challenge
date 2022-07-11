h = 10
k = 1
boxes = [9, 8, 7, 6, 5, 4, 3, 2, 1]	

def solution(h, k, boxes):
    answer = -1
    prev = 0
    box = 0
    boxes.sort()
    for i in boxes:
        if i - box == k:
            answer += 1
            box = i
        elif i - box > k:
            if prev - i > k:
                answer = -1
                break
            else:
                answer += 1
                box = prev
        if h - box <= k:
            box = h
            answer += 1
            break
        prev = i
    if box != h:
        answer = -1
    return answer


print(solution(h, k, boxes))