from random import shuffle

def generateCards():
  cards = []
  for i in range(13):
    cards.append(["spade", i+1])
  for i in range(13):
    cards.append(["heart", i+1])
  for i in range(13):
    cards.append(["diamond", i+1])
  for i in range(13):
    cards.append(["club", i+1])
  return cards

def shuffleCards(cards):
  shuffle(cards)
  return cards
  
def pickTop4Cards(cards):
  pickedCards = []
  pickedCards.append(cards[0])
  pickedCards.append(cards[1])
  pickedCards.append(cards[2])
  pickedCards.append(cards[3])
  return pickedCards
  
def removeTop4Cards(cards):
  for i in range(4):
    cards.pop(0)
  return cards

def find24OperatorsSolution(a, b, c, d):
  operators = ["+", "-", "*", "/"]
  usedOperators = []
  difference = abs(24 - eval('a ' + operators[0] + ' b'))
  usedOperators.append("+")
  for i in range(1, 4):
    if difference > abs(24 - eval('a ' + operators[i] + ' b')):
      usedOperators.pop(0)
      usedOperators.append(operators[i])
      difference = abs(24 - eval('a ' + operators[i] + ' b'))
  difference = abs(24 - eval('a ' + usedOperators[0] + ' b ' + operators[0] + ' c'))
  usedOperators.append("+")
  for i in range(1, 4):
    if difference > abs(24 - eval('a ' + usedOperators[0] + ' b ' + operators[i] + ' c')):
      usedOperators.pop(1)
      usedOperators.append(operators[i])
      difference = abs(24 - eval('a ' + usedOperators[0] + ' b ' + operators[i] + ' c'))
  difference = abs(24 - eval('a ' + usedOperators[0] + ' b ' + usedOperators[1] + ' c ' + operators[0] + ' d'))
  usedOperators.append("+")
  for i in range(1, 4):
    if difference > abs(24 - eval('a ' + usedOperators[0] + ' b ' + usedOperators[1] + ' c ' + operators[i] + ' d')):
      usedOperators.pop(2)
      usedOperators.append(operators[i])
      difference = abs(24 - eval('a ' + usedOperators[0] + ' b ' + usedOperators[1] + ' c ' + operators[i] + ' d'))
  
  return usedOperators

#just for testing purposes
def main():
  a = list(map(int, input('number : ').split()))
  a.sort(reverse=True)
  solution = find24OperatorsSolution(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
  print(a[0], solution[0], a[1], solution[1], a[2], solution[2], a[3])
  
main()