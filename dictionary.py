class Diccionario():
    def __init__(self):
        self.elementos = {}
    
    def _add(self, key, val):
        hash_key = hash(key)
        self.elementos[hash_key] = val
       # print(self.elementos)

    def _find(self, key):
        if hash(key) in self.elementos:
            val = self.elementos[hash(key)]
            return val
        return False

    def _del(self, key):
        self.elementos[hash(key)] = ""

    def _clean(self, key):
        self.elementos = {}

dicc = Diccionario()
dicc._add("pais", "peru")
dicc._add("ciudad", "lima")
dicc._del("ciudad")


print(dicc._find("ciudad"))