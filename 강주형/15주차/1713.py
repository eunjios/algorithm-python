# 1713
# 후보 추천하기

from collections import defaultdict

n = int(input())
total_rec = int(input())
rec_list = list(map(int, input().split()))

# 정답으로 출력할 list (계속 업데이트함)
answer_list = []

# 각 학생의 추천 수
student_n_rec = defaultdict(int)

for student in rec_list:
    min_rec = 1001

    # 현재 정답 후보 중 최솟값
    for val in answer_list:
        min_rec = min(min_rec, student_n_rec[val])
    
    
    # 사진틀 아직 다 안 참 -> 채우기
    if len(student_n_rec) < n:
        if student not in answer_list:
            answer_list.append(student)
        student_n_rec[student] +=  1
        continue
    
    student_n_rec[student] +=  1
    
	  # 사진틀이 꽉 찼을 때
    if student not in answer_list:
        for idx, val in enumerate(answer_list):
						# 처음 발견되는 것이 더 먼저 온 것 -> pop으로 제거하자
            if student_n_rec[val] == min_rec:
                answer_list.pop(idx)
                answer_list.append(student)
                student_n_rec[val] = 0
                break

for val in sorted(answer_list):
    print(val, end=' ')