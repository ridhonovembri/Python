class Mahasiswa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInformation(self):
        print("this object ==> name:", self.name, "age:", self.age)

class Prodi(Mahasiswa):
    def __init__(self, name, age, fakultas, jurusan):
        #inheritance using super statement
        super().__init__(name, age)
        self.fakultas = fakultas
        self.jurusan = jurusan

    def prodiInformation(self):
        print('name',self.name, 'age:', self.age, 'fakultas:',self.fakultas,'jurusan:', self.jurusan)

class Biodata(Mahasiswa):
    def __init__(self, name, age, alamat, status):
        #inheritance using class name
        Mahasiswa.__init__(self, name, age)
        self.alamat = alamat
        self.status = status

    def bioInformation(self):
        print('name:', self.name,'age:',self.age,'alamat:',self.alamat,'status:',self.status)
 

mahasiswa1 = Mahasiswa("icha","20")
mahasiswa1.showInformation()

mahasiswa2 = Mahasiswa("ezel","25")
mahasiswa2.showInformation()

mahasiswa3 = Prodi("widya","40","ILKOM","Sistem Informasi")
mahasiswa3.prodiInformation()

mahasiswa4 = Biodata('ridho','39','TS 2','Married')
mahasiswa4.bioInformation()


