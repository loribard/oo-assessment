

def break_into_questions(question_dictionary_in_a_list):
		dictionary_of_questions = {}
		i = 0
		for question in range(len(questions)):
			dictionary_of_questions[i] = questions[i]
			i+=1
			print dictionary_of_questions
		individual_questions_and_answers = {}
		for list_of_questions in self.list_of_questions.keys():
			individual_questions_and_answers["question"] = "correct_answer"
		print individual_questions_and_answers
		return individual_questions_and_answers




questions =  [

    {'question':'What is the capital of Alberta?',
     'correct_answer': 'Edmonton'},

    {'question': 'Who is the author of Python?',
     'correct_answer': 'Guido Van Rossum' }]
     

break_into_questions(questions)








