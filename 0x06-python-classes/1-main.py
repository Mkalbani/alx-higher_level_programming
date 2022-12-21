
0x06. Python - Classes and Objects
Python
OOP
 By: Guillaume
 Weight: 1
 Ongoing second chance project - started Dec 20, 2022 6:00 AM, must end by Dec 22, 2022 6:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/77 mandatory & 0.0/63 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%


Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

Resources
Read or watch:

Object Oriented Programming (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
Object-Oriented Programming (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
Properties vs. Getters and Setters
Learn to Program 9 : Object Oriented Programming
Python Classes and Objects
Object Oriented Programming
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is the __dict__ of a class and/or instance of a class and what does it contain
How does Python find the attributes of an object or class
How to use the getattr function
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
More Info
Documentation is now mandatory! Each module, class, and method must contain docstring as comments. Example Google Style Python Docstrings

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. My first square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write an empty class Square that defines a square:

You are not allowed to import any module
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x06-python-classes
File: 0-square.py
    
1. Square with size
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
