# Book class
import uuid

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return self.title + ' - ' + self.author
    
    def getAvailability(self) -> str:
        if self.is_borrowed: 
            return 'available' 
        else:
            return 'borrowed'
    
    def getDetails(self) -> str:
        return f"Title: {self.title}, author: {self.author}, availability: {self.getAvailability()}"