import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis (self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")
    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        return trenutna_godina - self.godina_proizvodnje
    
auto_1 = Automobil("Seat", "Leon", 2024, 10000)
auto_1.ispis()
auto_2 = Automobil("Seat", "Leon", 2024, 10000)
print(f"Starost automobila -> {auto_2.starost()} godina")
print("-----------")

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno"
    
    def potenciranje(self):
        return self.a ** self.b 
    
    def korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Nije moguće izračunati korijen negativnog broja"

kalkulator = Kalkulator(7, 2)
print(f"Zbroj {kalkulator.a} i {kalkulator.b} iznosi: {kalkulator.zbroj()}")
print(f"Oduzimanje {kalkulator.a} i {kalkulator.b} iznosi: {kalkulator.oduzimanje()}")
print(f"Množenje {kalkulator.a} i {kalkulator.b} iznosi: {kalkulator.mnozenje()}")
print(f"Dijeljenje {kalkulator.a} i {kalkulator.b} iznosi: {kalkulator.dijeljenje()}")
print(f"{kalkulator.a} na potenciju {kalkulator.b} iznosi: {kalkulator.potenciranje()}")
print(f"Korijen broja {kalkulator.a} iznosi: {kalkulator.korijen()}")
print("-----------")

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene  
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
    ]    
    
studenti_objekti = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]
najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime} s prosjekom {najbolji_student.prosjek()}")
print("-----------")

class Krug:
    def __init__(self, r):
        self.r = r
        
    def opseg(self):
        return 2 * 3.14 * self.r
    
    def povrsina(self):
        return 3.14 * (self.r ** 2)

krug = Krug(7)    
print(f"Opseg kruga s radijskom {krug.r} iznosi: {krug.opseg()}")
print(f"Površina kruga s radijskom {krug.r} iznosi: {krug.povrsina()}")
print("-----------")

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji: {self.pozicija}")   

class Manager(Radnik):    
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Radnik {radnik.ime} je dobio povišicu. Nova plaća je {radnik.placa} €")

radnik = Radnik("Lovre", "Developer", 6000)     
radnik.work()
manager = Manager("Lucija", "Manager", 8000, "Sales") 
manager.work()
manager.give_raise(radnik, 500)   