from kasutaja import *

class Privileegid():
    def __init__(self, privileegid = "lubatud lisada kasutajaid, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"):
        self.privileegid = privileegid
    def naita_privileegid(self):
        print(self.privileegid)


class Admin(Kasutajad, Privileegid):


    def privileegid(self, privileegid):
        self.privileegid = privileegid
