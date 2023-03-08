class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

prompts = ["who plays John Wick? /n/ta.Keanu Reeves/n/tb.Hugh Jackman /n/tc.none",
           "What color is sky? /n/ta.green /n/tb.white /n/tc.blue"]	

questions = [Question(prompts[0], 'a'), Question(prompts[1], 'c')]  

score = 0

for q in questions:
    answer = input(q.prompt)  
    if answer == q.answer:
        score += 1

print(f"you did {score}/2 right")               	
