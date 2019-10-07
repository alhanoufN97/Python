class Library :
    def __init__(self , book , shelf ):
        self.book = book
        self.shelf=shelf

class science_section(Library):
    def __init__(self ,name , book =300 ,shelf =45 ) :
        super().__init__(book,shelf)
        self.name = name

    def Fun(self):
        print("Book name : ",self.name,"\nNumber of Book in Library : ",self.book,"\nNumber of Shelf in Library : ",self.shelf)



P1 = science_section(name ="Physics books")
P1.Fun()

P1.book=20
P1.shelf=40
P1.Fun()
