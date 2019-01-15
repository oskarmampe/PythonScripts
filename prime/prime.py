import math
def median(seq):
  oList = sorted(seq)
  lenList = len(oList)
  med = int(((math.ceil(lenList/2)) - 1))
  print(med)
  if lenList % 2 == 1:
    return oList[med]
  else:
    return (oList[med + 1] + oList[med]) / 2.0

print(median([6, 8, 12, 2, 23]))