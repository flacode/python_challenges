import sys
S='SOSSOT'
S=S.strip()
def save_the_ship(received_message):
  expected_message='SOS'*int(len(received_message)/3.0)
  count=0
  if expected_message!=received_message:
    for i in xrange(len(received_message)):
      if expected_message[i]!=received_message[i]:
        count+=1
  return count
print save_the_ship(S)
