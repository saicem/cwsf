import cv2
import os
import json
# im_gray = cv2.imread('./Chars/0.jpg',cv2.IMREAD_GRAYSCALE)
# print(im_gray)

charSet = {}
for c in '0123456789':
  charSet[c] = [[0 for i in range(9)] for i in range(12)]
fileLs = os.listdir('./Chars')

for file in fileLs:
  c = file[0]
  im_gray = cv2.imread('./Chars/'+file, cv2.IMREAD_GRAYSCALE)
  for i in range(12):
    for j in range(9):
      if(im_gray[i][j]>200):
        charSet[c][i][j] += 1

ks = charSet.keys()
for k in ks:
  for i in range(12):
    for j in range(9):
      charSet[k][i][j] = 1 if charSet[k][i][j] > 3 else 0

f = open('a.json','w')
f.write(json.dumps(charSet))
f.close()