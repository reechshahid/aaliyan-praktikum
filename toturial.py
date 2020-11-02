from time import sleep

x = 10
print('Hallo')
sleep (1)
x = input ("Wie heißt du?")
print ('Hallo' + x + 'Schön dich kennenzulernen!')
x = int(x)
if x == 0:
  print('Null!')
elif x < 0:
  print('Kleiner als Null!')
elif x > 0:
  print('Größer als Null!')
else:
  print('???')
#############################
if x == 0 or x == 1:
  print( ' x ist 0 oder 1 ' )