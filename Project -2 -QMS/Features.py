from Connections import CONNECTIONS


class Features(CONNECTIONS):

    def fetch_questions(self):
        ques_dict = {}
        query = 'Select QuesNo,Questions,Options from tbl_quizquestions'
        fetched_data = self.fetch_data(query)
        for data in fetched_data:
            ques_no, question, options = data
            ques_dict.update({ques_no: {question: options.split(',')}})
        return ques_dict

    def start_quiz(self,name):
        print('============ QUIZ STARTED ============')
        questions = self.fetch_questions()
        no_of_questions = len(questions)
        print('NO OF QUESTIONS: ', no_of_questions)
        response = {}
        for ques_no, question in questions.items():
            print('Question No:', ques_no)
            ques = list(question.keys())[0]
            options = list(question.values())[0]
            print(ques)
            for i, option in enumerate(options):
                print('%s. %s'%(str(i+1), option))
            answer = ','.join(input('Answer:').split())
            response.update({ques_no: answer})
        result = {name: response}
        print(result)
        self.submit_quiz(result)

    def fetch_answer(self):
        query = ' select QuesNo,Answer from tbl_quizquestions;'
        answers = self.fetch_data(query)
        answer_dict = {}
        for ques,answer in answers:
            answer_dict.update({ques:answer})
        return answer_dict

    def store_results(self, name, correct_attempts, wrong_attempts, total_ques):
        query = "insert into tbl_results values('%s',%s,%s,%s)"%(name,int(correct_attempts),int(wrong_attempts),int(total_ques))
        # print(query)
        self.execute_query(query)
        print('Results are stored!!')

    def submit_quiz(self, result):
        correct_attempts = 0
        wrong_attempts = 0
        all_answers = self.fetch_answer()
        for name, response in result.items():
            for q_no, user_ans in response.items():
                if all_answers[q_no] == user_ans:
                    correct_attempts += 1
                else:
                    wrong_attempts += 1
            self.store_results(name, correct_attempts, wrong_attempts, len(response))
            self.display_result(name)

    def add_questions(self):
        print('============ ENTER QUESTIONS ============')
        no_ques = eval(input('Enter the Number of Questions that is need to be added:'))
        for _ in range(no_ques):
            question = input('Enter the Question:')
            no_options = eval(input('Enter the no of Options:'))
            options = []

            for i in range(no_options):
                option = input('Enter option no %s: '%(i+1))
                options.append(option)

            options_ = ','.join(options)
            answer = input('Enter the Answer: ')
            difficulty_level = input('Enter the difficulty_level: ')

            query = """insert into tbl_quizquestions(Questions,DifficultyLevel,Options,Answer) 
                       values('{0}','{1}','{2}','{3}')""".format(question, difficulty_level, options_, answer)
            # print(query)
            self.execute_query(query)
            print('1 Row Inserted!! ')

    def display_instructions(self):
        instructions = """1. Each round consists of 10 random questions. To answer, you must press 1/2/3/4. 
2. Each question consists of 1 point.
3. Your final score will be given at the end."""
        print(instructions)

    def display_result(self, name):
        query = 'select * from tbl_results where UserName like "%s"'%name
        result = self.fetch_data(query)
        print('Correct/Total - %s/%s'%(result[0][1],result[0][3]))
        print('Wrong/Total - %s/%s'%(result[0][2],result[0][3]))