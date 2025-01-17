# Polymorphism Challenge & Book Class System 🚀
## 1. Polymorphism Challenge: Action Classes 🎭
This Python program demonstrates polymorphism by creating different characters (Robot, Human, Alien, Superhero) that all perform the same action() method in their unique way.

## Features:
- Each class (Robot, Human, Alien, Superhero) defines the same method (action()), but each implements it differently, showcasing polymorphism.
- The demonstrate_actions() function calls the action() method on a list of various action objects to show how each class behaves.
Classes:
- Action: Base class with a generic action() method.
Robot, Human, Alien, Superhero: Derived classes that override the action() method to perform specific actions.
## 2. Book Class System 📚
This Python program defines a Book class to represent physical books with details like title, author, genre, and pages. It also includes an EBook class that extends the Book class, adding unique features like file size and download capability.

- Features:
- Book Class:
- Create a book with title, author, genre, and number of pages.
- display_info() method to display book details.
- read_pages() method to simulate reading pages from the book.
- EBook Class (extends Book):
- Inherits all functionality of the Book class.
- Adds a file_size attribute for the eBook's file size and a download() method.
- Classes:
- Book: Represents a traditional book.
- EBook: Inherits from Book and represents an electronic version of the book with additional properties and methods.
## How to Use:
- Clone or download this repository.
- Run the Python files (polymorphism.py or book.py) in your environment to explore the functionality.
- You can create objects for each class (Robot, Human, EBook, etc.), and observe how polymorphism works in action.
- Try different actions like reading pages, checking book details, or calling the action() method on various characters.
