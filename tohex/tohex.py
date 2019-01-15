def rgb_colours(red, green, blue):
  redF = toHex(red / 16)
  redS = toHex(red % 16)
  greenF = toHex(green / 16)
  greenS = toHex(green % 16)
  blueF = toHex(blue / 16)
  blueS = toHex(blue % 16)
  print('#',redF,redS,greenF,greenS,blueF,blueS,sep='');

def toHex(num):
  if(int(num) == 10):
    return 'A'
  if(int(num) == 11):
    return 'B'
  if(int(num) == 12):
    return 'C'
  if(int(num) == 13):
    return 'D'
  if(int(num) == 14):
    return 'E'
  if(int(num) == 15):
    return 'F'
  if(int(num) == 16):
    return '0'
  return int(num)

rgb_colours(65, 244, 244)