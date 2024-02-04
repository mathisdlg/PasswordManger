import cryptor as c


class Password:
    def __init__(self, site, cryptedPass, desc=""):
        self.site = site
        self.cryptedPass = cryptedPass
        self.desc = desc
        
    
    def __str__(self):
        return f"{self.site} : {self.cryptedPass} ({self.desc})"
    
    def getJson(self):
        return {
            "site": self.site,
            "password": c.Cryptor.cryptPass(self.cryptedPass, "test"),
            "desc": self.desc
        }
    
    def getPassword(self):
        return self.cryptedPass
    
    def getSite(self):
        return self.site
    
    def getDesc(self):
        return self.desc



if __name__ == "__main__":
    p = Password("facebook", "test")
    print(p.getJson())