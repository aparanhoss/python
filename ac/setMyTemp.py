from ac import Ac
import sys
data=sys.argv[1]
Arc=Ac("192.168.0.201",4998)
Arc.open()
#if data.isnumeric():
print("Temperatura: ",data)
Arc.setTemp(int(data))
Arc.close()