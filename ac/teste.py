"""
from ac import Ac
Arc=Ac("192.168.0.201",4998)
Arc.open()
Arc.setTemp(17)
Arc.close()
"""
from myserv import MyServer
ms=MyServer()
ms.listen()