# csv : comma separated value(콤마로 구분된 값(들))

# .csv 파일 열기 (import csv)
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫기

import csv

# csv 읽기
f = open('sspy1.csv','r',encoding="utf-8")
sspy1 = csv.reader(f,delimiter=' ')
# for row in sspy1:
#     for d in row:
#         print(d)
# f.close()

for row in sspy1:
    print(row)
f.close()

# csv 쓰기
# f = open('sspy1.csv','w',encoding="utf-8")
# sspy1 = csv.writer(f)
# sspy1.writerow(["john","john@hphk.kr","010-1234-1234","sspy1","CS"])  #실제 리스트는 아닌, 리스트와 비슷한 형태의 구조(리스트라고 생각해도 무방)
# f.close()

# csv 수정(추가)
# f = open('sspy1.csv','a',encoding="utf-8")
# sspy1 = csv.writer(f)
# sspy1.writerow(["seung","seung@hphk.kr","010-2587-4568","sspy1","LIS"])
# f.close()