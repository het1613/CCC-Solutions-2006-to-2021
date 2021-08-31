num_of_antennas=int(input('How many antennas?: '))
num_of_eyes=int(input('How many eyes?: '))

if ((num_of_antennas>=3) and (num_of_eyes<=4)):
    print('TroyMartian')

if ((num_of_antennas<=6) and (num_of_eyes>=2)):
    print('VladSaturnian')
    
if ((num_of_antennas<=2) and (num_of_eyes<=3)):
    print('GraemeMercurian')
