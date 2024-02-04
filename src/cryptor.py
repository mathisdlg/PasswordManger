import hashlib as hl


class Cryptor:
    @staticmethod
    def cryptPass(password: str, key: str) -> str:
        ...
    
    @staticmethod
    def decryptPass(cryptedPassword: str, key: str) -> str:
        ...
    
    
    


if __name__ == "__main__":
    print(Cryptor.hash_string_256("test"))