import random

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
word = ''
word_shown = []
count_attempts = 4


def getNewWord():
	return random.choice(words)

def showWord():
	print(''.join(word_shown))

def getAllPositions(ch):
	return [i for i, letter in enumerate(word) if letter == ch]

def makeChoice():
	showWord()
	let = input('Enter a letter: ')
	return checkChoice(let)
	
def checkChoice(let):
	if let in word and len(let)==1:
		arr_pos=getAllPositions(let)
		for pos in arr_pos:
			word_shown[pos]=let
		return True
	return False

def checkWin():
	if not '_' in word_shown:
		print('You win')
		return True
	return False

def startGame():
	global word, word_shown
	word=getNewWord()
	word_shown=['_']*len(word)
	count_attempts=4
	while count_attempts>0:
		if not makeChoice():
			count_attempts-=1
			print('You have {} attempts'.format(count_attempts))
		else:
			showWord()
			if checkWin():
				break

if __name__ == '__main__':
	startGame()
		

