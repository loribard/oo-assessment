"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   1. Encapsulation :the data is near it's functionality. You have to call the 
   	class to access the method.
   2. Abstraction: you don't need to know all details of the methods. Name the
   	methods appropriately, and anyone call call the method in the class and get
   	the result they want. You can hide the complexity with abstraction.
   3. Polymorphism: allows for an interchangeability of components. Code can be 
   	adjusted to the type of data. Allows you to specify common methods in an abstract
   	level (like animals talking) and implement them in instances (ie dogs bark is how they talk)


2. What is a class? A description for an object that defines a set
	of attributes that characterize any object of the class. For example,
	if Animals is a class, one of the attributes for this class would be that they 
	can breathe.


3. What is an instance attribute?
	An instance attribute is a particular case. For instance, if you want
	to put people in the class, you, yourself will be an instance attribute 
	for the class. The instance attribute becomes the 'self'.

4. What is a method?
	A method is a lot like a function. It actually is a function that is a member of 
	a class. You need to call the class and instantiate the object before you call
	the method.

5. What is an instance in object orientation?
 	It is when you call make an instance...you instantiate! For instance, if you have
 	a class of Cats, if you say my cat name = Cats() then you're making an instance.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   The CLASS attribute is shared by ALL instances. The attribute on an instance is
   unique to that instance. INSTANCE attributes are owned by the
   specific instances of a class(the self).

   For example:
class Hello(object):
	print "hello"
	def __init__(self,message):
		self.message = message
		print self.message
lori = Hello("Lori")

print "hello" is a class attribute...we do it for every instance
printing "Lori" is an instance variable is it only happens in the instance of lori



"""
#Part 2: Classes and Init Methods
import random

class Student(object):
    """Melon."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = 0


class Question(object):
	def __init__(self, question_str, answer):
		self.question_str = question_str
		self.answer = answer

	def ask_and_evaluate(self):
		answer = raw_input(self.question_str + " ")
		is_correct = answer == self.answer
		return is_correct


class Exam(object):
	def __init__(self, name):
		self.name = name
		self.questions = []

	def add_question(self, question_str, answer):
		q = Question(question_str, answer)
		self.questions.append(q)

	def score(self):
		score = 0
		for q in self.questions:
			is_correct = q.ask_and_evaluate()
			if is_correct:
				score += 1
		return score

	def administer(self):
		return self.score()

class Quiz(Exam):
	def administer(self):
		score = self.score()
		num_questions = len(self.questions)
		is_passed = float(score)/num_questions >= 0.5
		return is_passed
			


def take_test(exam,student):
	student.score = exam.administer()


def example():
	exam = Quiz('midterm')
	exam.add_question("what's your name?","Lori")
	exam.add_question("Where do you live?","Burlingame")

	student = Student('Lori','Bard','30 Knightwood Lane')

	take_test(exam, student)

	return student.score


if __name__ == '__main__':
	print example()

# questions1 = Question({"question":"What is the capital of Alberta?", "correct_answer":"Edmonton"})
# questions2 = Question({"question":"Who is the author of Python?","correct_answer":"Guido Van Rossum"})
# student_1 = Student({'first_name':'Lori',
# 	'last_name':'Bard','address':'30 Knightwood Lane'})
# exam = Exam({'name':'Midterm',
#  'questions': [

#     {'question':'What is the capital of Alberta?',
#      'correct_answer': 'Edmonton'},

#     {'question': 'Who is the author of Python?',
#      'correct_answer': 'Guido Van Rossum' }

#   ]
# })

# exam.add_question('What is your name?','Lori')
# exam.administer()
	