class Book:
    def __init__(self, title, author, genre, price, num_pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.__num_pages = num_pages  # Encapsulated attribute
    
    # Method to display book details
    def display_details(self):
        return f"'{self.title}' by {self.author} - Genre: {self.genre}, Price: {self.price} Ksh"
    
    # Method to calculate reading time based on average reading speed
    def estimated_reading_time(self, avg_speed=50):  # avg_speed is pages per hour
        return f"Estimated reading time: {self.__num_pages / avg_speed:.2f} hours"
    
    # Getter for num_pages
    def get_num_pages(self):
        return self.__num_pages
    
    # Setter for num_pages
    def set_num_pages(self, new_num_pages):
        if new_num_pages > 0:
            self.__num_pages = new_num_pages
        else:
            print("Number of pages must be greater than zero.")

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, genre, price, num_pages, file_size):
        super().__init__(title, author, genre, price, num_pages)
        self.file_size = file_size  # in MB
    
    # Overriding display_details to include file size
    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, File Size: {self.file_size}MB"
    
    # Unique method for EBook
    def download(self):
        return f"Downloading '{self.title}'... ({self.file_size}MB)"

# Derived class: Audiobook
class Audiobook(Book):
    def __init__(self, title, author, genre, price, num_pages, audio_length):
        super().__init__(title, author, genre, price, num_pages)
        self.audio_length = audio_length  # in hours
    
    # Overriding estimated_reading_time to reflect listening time
    def estimated_reading_time(self, avg_speed=None):
        return f"Listening time: {self.audio_length} hours"
    
    # Unique method for Audiobook
    def play_sample(self):
        return f"Playing sample of '{self.title}' by {self.author}..."

# Create a physical book
physical_book = Book("1984", "George Orwell", "Dystopian", 1500, 328)
print(physical_book.display_details())
print(physical_book.estimated_reading_time())

# Create an eBook
ebook = EBook("Digital Minimalism", "Cal Newport", "Self-help", 800, 256, 2.5)
print(ebook.display_details())
print(ebook.download())

# Create an audiobook
audiobook = Audiobook("Atomic Habits", "James Clear", "Self-help", 2000, 320, 5.5)
print(audiobook.display_details())
print(audiobook.estimated_reading_time())
print(audiobook.play_sample())
