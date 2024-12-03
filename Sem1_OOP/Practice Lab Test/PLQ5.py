class Publication:
    def __init__(self):
        self.title = input("Please enter a title: ")
        self.price = float(input("Please enter a price: "))


class Book(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.page_count = int(input("Please enter the page count: "))

    def __str__(self):
        return "Title: {}\nPrice: {}\nPage count: {}".format(self.title, self.price,self.page_count)

    def __add__(self, param2):
        title_combined = str(input("Please enter the title : "))
        total_price = self.price + param2.price
        total_pages = self.page_count + param2.page_count
        return "Title: {}\nPrice: {}\nPage count combined : {}".format(title_combined, total_price, total_pages)



#main scope
book1 = Book()
print(book1)
print()

book2 = Book()
print(book2)
print()

print(book1 + book2)