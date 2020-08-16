#if 
nilai_ujian = 100

def doCheckValue(nilai_ujian):  
    if nilai_ujian >= 80 and nilai_ujian <= 100:
        return 'A'
    elif nilai_ujian >= 70 and nilai_ujian < 80:
        return 'B'
    elif nilai_ujian >= 60 and nilai_ujian < 70:
        return 'C'
    elif nilai_ujian >= 50 and nilai_ujian < 60:
        return 'D'
    elif nilai_ujian < 50:
        return 'E'
    else:
        return 'Please insert value from 1 to 100'

print('nilai anda adalah:', doCheckValue(nilai_ujian))