#!/usr/bin/python3
# coding=utf-8
import random


# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall verdier i generert instans.
n_lower = 3
# Høyest mulig antall verdier i generert instans.
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0
# Kontrollerer om resultatet av tester som feiler skal skrives ut i kompakt
# eller detaljert format.
compact_print = False


def sort(stack1, stack2, stack3):
	
	control = [[], [], []]
	solutions = []
	running_cash = []
	sort_faze = 0
	
	def start(stack1, stack2, stack3, control, solutions):
		while not stack1.empty():
			a = stack1.pop()
			stack2.push(a)
		while not stack3.empty() and not stack2.empty():
			a = stack2.pop()
			b = stack3.pop()
			if a > b:
				control[0].append(a)
				solutions.append(a)
				stack1.push(a)
				control[0].append(b)
				solutions.append(a)
				stack1.push(b)
			else:
				control[0].append(b)
				solutions.append(a)
				stack1.push(b)
				control[0].append(a)
				solutions.append(a)
				stack1.push(a)
		while not stack3.empty() or not stack2.empty():
			if stack3.empty():
				a = stack2.pop()
				control[0].append(a)
				solutions.append(a)
				stack1.push(a)
			else:
				a = stack3.pop()
				control[0].append(a)
				stack1.push(a)
		solutions.sort()
		solutions.reverse()
		return control, solutions


	def sort0(stack1, stack2, stack3, control, solutions):
		while len(control[0]) > 0:
			a = stack1.pop()
			if a == solutions[-1]:
				stack3.push(a)
				solutions.pop(-1)
				control[0].pop(-1)
			else:
				stack2.push(a)
				control[1].append(control[0].pop(-1))
		print(control)
		return control, solutions

	def sort4(stack1, stack2, stack3, control, solutions, p):
		while len(control[0]) > 0:
			a = stack1.pop()
			if a == solutions[p]:
				p += 1
				stack2.push(a)
				solutions.pop(0)
				control[0].pop(-1)
			else:
				stack3.push(a)
				control[2].append(control[0].pop(-1))
		print(control)
		return control, solutions
    
                        
    
	def sort3(stack1, stack2, stack3, control, solutions):
		L1 = True
		L3 = True
		while len(control[1]) > 0:
			a = stack2.pop()
			if a == solutions[-1]:
				stack3.push(a)
				solutions.pop(-1)
				control[1].pop(-1)   
			else: # a == solutions[0]:
				stack1.push(a)
				control[0].append(control[1].pop(-1))
		print(control)
		return control, solutions
	
	def sort1(stack1, stack2, stack3, control, solutions):
		while len(control[0]) > 0:
			a = stack2.pop()
			if a == solutions[0]:
				stack1.push(a)
				solutions.pop(-1)
				control[1].pop(-1)
			else:
				stack3.push(a)
				control[2].append(control[1].pop(-1))
		print(control)
		return control, solutions

                        
	def finish(stack1, stack2, stack3):
		while not stack3.empty():
			a = stack3.pop()
			stack1.push(a)    


	def sort4(stack1, stack2, stack3):
		L1 = True
		L3 = True
		while not stack1.empty() and not stack2.empty():
			a = stack2.pop()
			if a == solutions[-1]:
				stack3.push(a)
				solutions.pop(-1)
			elif a == solutions[0]:
				stack1.push(a)
		print()
		pass
    
    
        
	control, solutions = start(stack1, stack2, stack3, control, solutions)
	while True:
		p = 0
		if p == 0:
			for i in control[0]:
				
				control, solutions = sort0(stack1, stack2, stack3, control, solutions)
		if len(solutions) == 0:
			break
		control, solutions = sort3(stack1, stack2, stack3, control, solutions)
		if len(solutions) == 0:
			break
	finish(stack1, stack2, stack3)
    # Skriv koden din her


# Hardkodetetester, høyre side blir toppen av stakken
tests = [
    [4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 2, 1, 7],
    [1, 1, 1, 1],
    [7, 3, 9, 2, 0, 1, 3, 4],
    [7, 3, 0, 13, 48, 49, 233, 9, 2, 0, 1, 3, 4],
]

# Genererer k tilfeldige tester, hver med et tilfeldig antall elementer plukket
# uniformt fra intervallet [nl, nu].
def gen_examples(k, nl, nu):
    for _ in range(k):
        yield [random.randint(-99, 99) for _ in range(random.randint(nl, nu))]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(random_tests, n_lower, n_upper))


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, operation_counter, element_counter, initial=None):
        self.stack = []
        if initial is not None:
            self.stack = initial

        self.element_counter = element_counter
        self.operation_counter = operation_counter

    def push(self, value):
        if self.element_counter.get_value() <= 0:
            raise RuntimeError(
                "Du kan ikke ta vare på flere elementer på "
                "stakkene enn det fantes originalt."
            )
        self.stack.append(value)
        self.element_counter.decrement()
        self.operation_counter.increment()

    def pop(self):
        if self.element_counter.get_value() >= 2:
            raise RuntimeError(
                "Du kan ikke ha mer enn 2 elementer i minnet " "av gangen."
            )
        self.element_counter.increment()
        self.operation_counter.increment()
        return self.stack.pop()

    def peek(self):
        self.operation_counter.increment()
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

failed = False
first = True

for test in tests:
    counter1 = Counter()
    counter2 = Counter()
    stack1 = Stack(counter1, counter2, initial=test[:])
    stack2, stack3 = Stack(counter1, counter2), Stack(counter1, counter2)

    sort(stack1, stack2, stack3)

    result = []
    counter2.value = float("-inf")
    while not stack1.empty():
        result.append(stack1.pop())

    if not first:
        print("-"*50)

    if result != sorted(test) and compact_print:
        print(f"""
Koden feilet for følgende instans:
Start (stack1, fra topp til bunn): {test[::-1]}

Ditt svar (stack1, fra topp til bunn): {result}
Forventet svar: {sorted(test)}
""")
        failed = True
    elif result != sorted(test):
        result2 = []
        while not stack2.empty():
            result2.append(stack2.pop())

        result3 = []
        while not stack3.empty():
            result3.append(stack3.pop())
        print(f"""
Koden feilet for følgende instans.
---------------
 Starttilstand
---------------

--------
Stack 1:
--------
{chr(10).join(map(str, test[::-1])) or "ingen elementer i stakken"}

--------------
 Sluttilstand
--------------

--------
Stack 1:
--------
{chr(10).join(map(str, result)) or "ingen elementer i stakken"}

--------
Stack 2:
--------
{chr(10).join(map(str, result2)) or "ingen elementer i stakken"}

--------
Stack 3:
--------
{chr(10).join(map(str, result3)) or "ingen elementer i stakken"}
""")
        failed = True
    else:
        print(f"""
Koden brukte {counter1.get_value() - len(result)} operasjoner på sortering av
{test[::-1]}
""")

    first = False

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")