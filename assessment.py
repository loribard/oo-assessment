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

    def __init__(self, student_dictionary):
        

        self.first_name = student_dictionary["first_name"]
        self.last_name = student_dictionary["last_name"]
        self.address = student_dictionary['address']
        print self.first_name,self.last_name,self.address




class Question(object):
	def __init__(self,type_of_test):
		self.test_type = type_of_test["name"]
		print self.test_type
		self.questions = type_of_test["questions"]
		print self.questions
		#self.questions = type_of_test["questions"]
		
		#self.question_list = break_into_questions()
		#self.question = question_dictionary["question"]
		#self.correct_answer = question_dictionary["correct_answer"]
		#print self.question, self.correct_answer
	# def ask_question(self):
	# 	first_question = radom.choice(self.questions.keys())
	# 	print first_question
	#def break_into_questions(self):
		print len(self.questions), "Length"

	def separate_out_questions(self):
		dictionary_of_questions = {}
		i = 0
		# for question in range(len(self.questions)):
		# 	self.dictionary_of_questions[i] = self.questions[i]
		# 	i+=1
		# print self.dictionary_of_questions
		individual_questions_and_answers = {}
		# for list_of_questions in self.list_of_questions.keys():
		# 	self.individual_questions_and_answers["question"] = "correct_answer"
		# print self.individual_questions_and_answers
		
	#return self.individual_questions_and_answers

	def get_individual_and_answers(self):
		answer = 0
		question1 = random.choice(individual_questions_and_answers.keys())
		self.answer = raw_input(str(question1))
		if self.individual_questions_and_answers[question1] == self.answer:
			print "RIGHT"
			answer += 1




# question1 = Question({'question': 'What is the capital of Alberta?',
#  'correct_answer': 'Edmonton'})
# question2 = Question({'question': 'Who is the author of Python?',
#  'correct_answer': 'Guido Van Rossum'})

class Exam(Question):

	def __init__(self,type_of_test):
		#self.test_type = type_of_test["name"]
		#self.questions = type_of_test["questions"]
		super(Exam,self).__init__(type_of_test)
		print self.test_type,self.questions
	def exam_add_question(self,question,answer):
		new_question = {"question":question,"correct_answer":answer}
		print new_question
		self.questions.append(new_question)
		print self.questions
		return self.questions
		

midterm = {'name':'Midterm',
 'questions': [

    {'question':'What is the capital of Alberta?',
     'correct_answer': 'Edmonton'},

    {'question': 'Who is the author of Python?',
     'correct_answer': 'Guido Van Rossum' }]
     }

  


final = {'name':'Final',
 'questions': [

    {'question':"Who is Ubermelon's competition?",
     'correct_answer': 'Sqysh'},

    {'question': "What is Balloonicorn's favorite color?",
     'correct_answer': 'Sparkles'}]

}


jasmine = Student({'first_name': 'Jasmine',
 'last_name': 'Debugger',
 'address': '0101 Computer Street'})

jaqui = Student({'first_name': 'Jaqui',
 'last_name': 'Console',
 'address': '888 Binary Ave'})

exam = Exam(midterm)
exam.exam_add_question("What is the method for adding an element to a set?",".add()")
exam.separate_out_questions()



