from read_shield_class import Shield

shield=Shield()
for i in range(10):
  adcv=shield.read_shield()
  print(adcv)

exit()