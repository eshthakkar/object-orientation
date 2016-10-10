"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Object orientation provides the following 3 design benefits:
   1. Abstraction - The ability for us to use functions without worrying what is inside it. Hides the details
                    from user
   2. Encapsulation - Keeping everything related in one place, together. Variables and functions related.
   3. Polymorphism - Sub classes can add functionality on top of parent class , can override functionality
                     without having to use conditionals in parent class methods. Method with same name from parent class 
                     can be overwritten by the same method with little tweaking defined in subclass.                   

2. What is a class?

Class is a type of datastructure that can have attributes(data) and methods(functions) that operate
on the date defined in it together at the same place. This helps to keep everything related together without 
having to keep track of it. 


3. What is an instance attribute?

An attribute related to particular instance of the class is called as an instance attribute.

4. What is a method?

Method is a function defined inside a class. Any object of that particular class can access it using <.method_name>.

5. What is an instance in object orientation?

An object of the class is called as an instance. we instantiate a class to make an instance.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute is defined inside the class. Mainly used for immutable properties that are going to be same 
   for all objects of that class. E.g : color of all objects of class red wine will be "red". 
   Instance attribute is unique to each instance. For e.g name of each student can be different. Denoted as
   self.name or <instance_name>.name.



"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    """ Creates a student with first name, last name and address as parameters"""

    def __init__(self,first_name,last_name,address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):

    """ Creates a Question with question and its correct answer as parameters"""

    def __init__(self,question,correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):

        """ Prints question to console. Takes answer from user and compares it to 
        the expected answer"""

        print "{}".format(self.question)
        user_answer = raw_input("> ")
        return (user_answer == self.correct_answer)    

class Exam(object):

    """ Creates an exam with a name"""

    def __init__(self,name):
        self.name = name
        self.questions = [] 

    def add_question(self,question,correct_answer):

        """ Adds questions to the list of questions in the exam """

        self.questions.append(Question(question,correct_answer)) 

    def administer(self):

        """ Computes and returns the score percentage based on user responses 
        for all questions in the exam """

        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        return ((float(score)/len(self.questions)) * 100)

class Quiz(Exam):

    """ Creates a quiz which inherits the exam class"""

    def administer(self):

        """ Returns quiz pass or fail result """

        passed = False
        score = super(Quiz,self).administer()
        passed = score > 50
        return passed


        
# Functions to create an example and take test for a student.

def take_test(exam,student):

    """ Gives back result of exam/quiz of a student """

    student.score = exam.administer()
      


def example():

    """ Creates an exam, quiz and a student.
    Takes the exam and quiz for the student and prints out the student's performance in those
    on the console"""

    exam = Exam("Midterms 2")
    print exam.name
    exam.add_question("What is the method for adding an element to the list?",".append()")
    exam.add_question("Are tuples ordered?","Yes")
    exam.add_question("Which is the fastest datastructure for searching an item in it?","dictionary")
    student1 = Student("Anika","Garg","Santa Clara")
    take_test(exam,student1)
    print "{} {} scored {:.2f}% in {} exams.".format(student1.first_name,student1.last_name,
                                                 student1.score, exam.name)
    print ""

    quiz = Quiz("HB Quiz")
    print quiz.name
    quiz.add_question("The property of being able to use methods and attributes from parent class is called?",
                      "Inheritance")
    quiz.add_question("How can you delete elements from a list end?",".pop()")
    quiz.add_question("method to strip whitespaces at the end of a string?",".rstrip()")
    take_test(quiz,student1)


    if student1.score:
        print "{} {} passed in {}.".format(student1.first_name,student1.last_name,
                                             quiz.name)
    else:
        print "{} {} failed in {}.".format(student1.first_name,student1.last_name,
                                             quiz.name)    

# Call the example function
example()    



