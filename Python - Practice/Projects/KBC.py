"""
Kaun Banega Crorepati Game
Author: VKrishna04
Date: August 26th, 2023
"""


def KBC() -> None:
	"""
	This function represents the game 'Kaun Banega Crorepati' (Who Wants to Be a Millionaire).
	It contains a list of questions from various categories such as General Knowledge, Indian History and Politics,
	World Geography, and Science and Technology. The player is presented with multiple-choice questions and must
	select the correct answer to progress to the next question. The game ends when the player answers a question
	incorrectly or completes all the questions.
	"""
	questions = [
		# 1st level questions
		[# General Knowledge
			["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3],
			["Who painted the famous artwork 'The Starry Night'?", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet", 2],
			["What is the chemical symbol for iron?", "I", "Fe", "Ir", "In", 2],
			["Which river is the longest in the world?", "Nile", "Amazon", "Mississippi", "Yangtze", 1],
			["In which country can you find the ancient city of Machu Picchu?", "Peru", "Mexico", "Brazil", "Chile", 1],
			["Which English physicist defined the three laws of motion?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla", 1],
			["What is the largest planet in our solar system?", "Mars", "Jupiter", "Saturn", "Venus", 2],
			["Which famous playwright wrote 'Hamlet'?", "William Shakespeare", "George Bernard Shaw", "Anton Chekhov", "Oscar Wilde", 1],
			["What is the currency of Brazil?", "Real", "Peso", "Rupiah", "Rand", 1],
			["Which is the tallest mammal on Earth?", "Giraffe", "Elephant", "Blue Whale", "Kangaroo", 1],

			# Indian History and Politics
			["Who was the first Prime Minister of India?", "Indira Gandhi", "Jawaharlal Nehru", "Rajiv Gandhi", "Lal Bahadur Shastri", 2],
			["In which year did India gain independence from British rule?", "1945", "1947", "1950", "1955", 2],
			["Who is known as the 'Father of the Indian Constitution'?", "B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", 1],
			["What is the national emblem of India?", "Lion", "Tiger", "Elephant", "Ashoka Chakra", 4],
			["Which Indian state is known as the 'Land of Five Rivers'?", "Punjab", "Haryana", "Rajasthan", "Uttar Pradesh", 1],
			["Who is the current President of India?", "Ram Nath Kovind", "Narendra Modi", "Amit Shah", "Sonia Gandhi", 1],
			["Which Indian leader is often referred to as the 'Iron Man of India'?", "Indira Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "B.R. Ambedkar", 3],
			["What is the national animal of India?", "Tiger", "Lion", "Elephant", "Leopard", 1],
			["Which political party is currently in power in India?", "Indian National Congress (INC)", "Bharatiya Janata Party (BJP)", "Aam Aadmi Party (AAP)", "Bahujan Samaj Party (BSP)", 2],
			["Who led the 'Dandi March' as part of the Indian independence movement?", "Subhas Chandra Bose", "Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", 3],

			# World Geography
			["Which mountain range is located in South America?", "Rocky Mountains", "Andes", "Himalayas", "Alps", 2],
			["What is the smallest continent by land area?", "North America", "South America", "Australia", "Europe", 3],
			["Which river flows through Egypt?", "Nile", "Amazon", "Mississippi", "Yangtze", 1],
			["Which African country is known as the 'Rainbow Nation'?", "Egypt", "Nigeria", "South Africa", "Kenya", 3],
			["Which ocean surrounds the Maldives?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", 1],
			["Which is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Arabian Desert", "Kalahari Desert", 1],
			["Which city is known as the 'Eternal City'?", "Rome", "Athens", "Paris", "Cairo", 1],
			["Which country is known as the 'Land of the Rising Sun'?", "China", "Japan", "South Korea", "Thailand", 2],
			["Which canal connects the Mediterranean Sea to the Red Sea?", "Panama Canal", "Suez Canal", "Kiel Canal", "Erie Canal", 2],
			["Which famous river flows through London?", "Seine", "Danube", "Thames", "Volga", 3],

			# Science and Technology
			["What is the chemical symbol for oxygen?", "O", "Ox", "Oi", "Og", 1],
			["Which planet is known as the 'Red Planet'?", "Mars", "Jupiter", "Venus", "Saturn", 1],
			["What is the process by which plants make their own food?", "Respiration", "Photosynthesis", "Fermentation", "Transpiration", 2],
			["Which instrument is used to measure atmospheric pressure?", "Thermometer", "Hygrometer", "Barometer", "Anemometer", 3],
			["What is the unit of electric current?", "Volt", "Ohm", "Ampere", "Watt", 3],
			["Who is considered the 'Father of Computer Science'?", "Alan Turing", "Bill Gates", "Steve Jobs", "Tim Berners-Lee", 1],
			["What is the largest cell in the human body?", "Nerve cell", "Red blood cell", "Muscle cell", "Ovum (egg cell)", 4],
			["What type of energy is stored in a battery?", "Chemical energy", "Nuclear energy", "Solar energy", "Kinetic energy", 1],
			["What is the chemical formula for water?", "Wo", "Wa", "Wt", "H2O", 4],
			["What is the process by which plants lose water through their leaves?", "Transpiration", "Respiration", "Photosynthesis", "Evaporation", 1]
		],
		# 2nd Level - next level questions after 5th question
		[
			# General Knowledge
			["Which scientist is known for his theory of general relativity?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Marie Curie", 2],
			["What is the largest species of shark?", "Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark", 3],
			["Which famous scientist developed the laws of motion and universal gravitation?", "Isaac Newton", "Galileo Galilei", "Charles Darwin", "Nikola Tesla", 1],
			["What is the smallest bone in the human body?", "Stapes", "Femur", "Tibia", "Radius", 1],
			["Which planet has the most moons?", "Jupiter", "Saturn", "Uranus", "Neptune", 1],

			# History and Politics
			["Who was the first woman Prime Minister of a country?", "Margaret Thatcher", "Angela Merkel", "Golda Meir", "Indira Gandhi", 4],
			["Which war is often referred to as the 'Great War'?", "World War I", "American Civil War", "World War II", "Vietnam War", 1],
			["Who was the first President of the United States?", "Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams", 2],
			["Which leader was known as 'The Iron Lady'?", "Indira Gandhi", "Angela Merkel", "Golda Meir", "Margaret Thatcher", 4],
			["Which historical figure wrote the book 'The Art of War'?", "Sun Tzu", "Confucius", "Laozi", "Mao Zedong", 1],

			# World Geography
			["Which mountain is the tallest in North America?", "Mount Kilimanjaro", "Mount McKinley", "Mount Everest", "Mount Fuji", 2],
			["Which sea is the largest in the world?", "Arabian Sea", "Caspian Sea", "Mediterranean Sea", "Philippine Sea", 2],
			["Which country is known as the 'Land of the Midnight Sun'?", "Canada", "Norway", "Sweden", "Russia", 2],
			["Which river is the longest in Asia?", "Yangtze", "Ganges", "Indus", "Mekong", 1],
			["What is the capital of South Korea?", "Tokyo", "Beijing", "Seoul", "Bangkok", 3],

			# Science and Technology
			["Which element has the chemical symbol 'K'?", "Potassium", "Krypton", "Phosphorus", "Calcium", 1],
			["What is the phenomenon where light waves change direction as they pass through different mediums?", "Refraction", "Reflection", "Diffraction", "Dispersion", 1],
			["Which gas is responsible for the Earth's ozone layer?", "Oxygen", "Carbon Dioxide", "Methane", "Ozone", 4],
			["What is the study of fossils called?", "Archaeology", "Anthropology", "Paleontology", "Geology", 3],
			["Which scientist is known for the theory of evolution by natural selection?", "Charles Darwin", "Isaac Newton", "Gregor Mendel", "Albert Einstein", 1]
		],

		# 3rd Level - next level questions after 10th question
		[
			# General Knowledge
			["What is the smallest planet in our solar system?", "Mercury", "Venus", "Mars", "Pluto", 1],
			["Which famous scientist developed the theory of special relativity?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Marie Curie", 2],
			["What is the largest species of penguin?", "Emperor Penguin", "King Penguin", "Adélie Penguin", "Chinstrap Penguin", 1],
			["What is the name of the process by which plants convert light energy into chemical energy?", "Photosynthesis", "Respiration", "Transpiration", "Fermentation", 1],
			["In which year did the Chernobyl nuclear disaster occur?", "1986", "1979", "1991", "1999", 1],

			# History and Politics
			["Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart", "Sally Ride", "Bessie Coleman", "Valentina Tereshkova", 1],
			["Which country was the first to recognize the United States as an independent nation?", "France", "Russia", "Spain", "United Kingdom", 1],
			["Who led the Indian National Army (Azad Hind Fauj) during World War II?", "Subhas Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", 1],
			["Which war led to the division of Korea into North and South Korea?", "Vietnam War", "Korean War", "World War I", "Iraq War", 2],
			["What is the significance of the Magna Carta?", "It established the principle of habeas corpus", "It guaranteed religious freedom", "It outlined the rights of women", "It limited the power of the monarchy", 4],

			# World Geography
			["Which country is known as the 'Land of a Thousand Lakes'?", "Canada", "Finland", "Sweden", "Russia", 2],
			["Which is the only sea without any coastline?", "Sargasso Sea", "Caspian Sea", "Dead Sea", "Red Sea", 1],
			["Which mountain range separates Europe from Asia?", "Himalayas", "Andes", "Rocky Mountains", "Ural Mountains", 4],
			["What is the highest mountain in Africa?", "Mount Kilimanjaro", "Mount Everest", "Mount Elbrus", "Mount McKinley", 1],
			["Which country is known as the 'Land of Fire and Ice'?", "Iceland", "Greenland", "Norway", "Japan", 1],

			# Science and Technology
			["What is the process of converting sugar into alcohol called?", "Photosynthesis", "Fermentation", "Respiration", "Oxidation", 2],
			["What is the study of the Earth's atmosphere and weather patterns called?", "Geology", "Meteorology", "Astronomy", "Botany", 2],
			["What is the chemical formula for table salt?", "NaCl", "H2O", "CO2", "C6H12O6", 1],
			["Which particle is responsible for carrying an electric charge?", "Neutron", "Proton", "Electron", "Photon", 3],
			["What is the process of converting a solid directly into vapor called?", "Evaporation", "Sublimation", "Condensation", "Melting", 2]
		]
	]

	# index or the prize levels
	index = ("1,000","2,000","3,000","5,000","10,000","20,000","40,000","80,000","1,60,000","3,20,000","6,40,000","12,50,000","25,00,000","50,00,000","75,00,000","1,00,00,000","7,50,00,000")

	#timer for various levels used with variable level
	timer=(30,120)
	# after 15th questions there is no timer

	# money in safe in game
	money=0

	# the game starts with the introduction
	print("Welcome to Kaun Banega Crorepati!")
	print("You will be asked 17 questions and you will have 4 options for each question.\n")
	print("You will get 30 seconds to answer each question till 5th question of Rs. 10,000\n")
	print("You will win the amount mentioned for each question you answer correctly and quit by just simply clicking on enter without any answer.\n")
	print("If you answer a question incorrectly, you will lose all the money you have won so far after the milestone question and the game will end.\n")
	print("If you quit the game, you will win the amount you have won so far.\n")
	print("Good Luck!\n")
	print("Now, for the four options just type a,b,c,d to lock-in the option within the time otherwise it will be taken as if you have given the wrong answer and the amount won will be \n")

	import random
	import time

	# randomizer part for selecting the questions
	def querand(i):
		# the randomizer selects the question from the list of questions
		if i==3:
			return random.choice(random.choice(questions))
		else:
			return random.choice(questions[i])

	# Set of all questions that have appeared once already
	pastque=set()

	# time given to read the rules and then press enter
	input()

	# the game starts
	for i in range(0,17):

		# level is just a variable holding this value used in various places for operations related to level
		# it can have the values of 0,1,2
		level=int(i/5)

		# to make sure unique questions are coming
		# okay so let me explain my thinking process and what is each term
		# 1. querand(level) ----> this is a user defined function to generate questions no problem in this and
		# 2. level ----> is the price of the question like 1000 2000 ... till 75000000
		# 3. pastque ----> is the list of questions once generated it will be stored here
		# so my thinking is that first a question will be generated next in a for loop it
		# will check with every question that has occurred in the past and if it has occurred
		# then it will continue to next iteration of while loop and try everything again from
		# generating new question and again comparing and if it does not match with any only
		# then will it come out of the loop and continue with the question

		while True:
			que=querand(level)
			if tuple(que) in pastque :
				continue
			pastque.add(tuple(que))
			break

		print("Let's Start with question no.",i+1,"worth",index[i])
		# the question is printed after determining it is
		print(que[0],que[5],"\n1.",que[1],"\n2.",que[2],"\n3.",que[3],"\n4.",que[4])
		answer=0
				
		# timer is checked here
		if level<2:
			# the timer starts
			start=time.time()
			# the user enters the answer
			answer=int(input("\nYour answer: "))
			# the timer stops
			stop=time.time()
			# the time taken is calculated
			time_taken=stop-start

			# the time taken is checked
			if time_taken > timer[level]:
			# if it is less than 30 seconds for first level and 120 seconds for second level
				print("You took too long to answer the question and so you are out of the game")
				break
				#why is answer here possibly unbound
		# the answer is checked
		if answer == que[5] or answer == 5 :
			print("Correct Answer")
			# if the user has won 5th question the timer is changed to 120 seconds 10th question then it becomes timeless question
			if i==0:
				print("You have won Rs.",index[i],"and the timer is set to 30 seconds\n")
			elif i==1 :
				money=index[i]
				print("You have won Rs.",index[i],"and the timer is changed to 60 seconds\n")
			elif level==2:
				# this is valid only if the 17th questions is answered correctly thus the loop will end naturally after this
				print("You have won Rs.",index[i],"and timer is removed from now on.\n")
			elif level==3:
				print("You have won Rs.",index[i],"\n")
		# if the answer is wrong
		else:
			print("Your answer is Wrong the correct answer is:",que[5],que[que[5]],"\n")
			# the game ends
			break
		
  		# the current money won is printed
		print("The correct answer is",que[5],que[que[5]],"\nCurrent Total amount earned Rs.",money,"\n")
		# print ("\n...",flush=True)
	
	if i==16:
		money=75000000
		print("Congratulations on conquering the game and hope you have not cheated here you have earned Rs.",money)
	else:
		print("\n\nYou have lost in question no.",i+1,"by wrong answer or by running out of time")

	print("Thank You for playing with us hope to see you again")
	input()
if __name__=="__main__":
	KBC()
 
 
r = input("Do you want to play again? (yes/no): ")