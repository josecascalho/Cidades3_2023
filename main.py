import json
import random

import nodes

# Example of Search using cities
def read_file(cities:str) -> list:
	with open(cities) as config_file:
		# Reading the configuration file
		lst = json.load(config_file)
		# Test: printing config file
		#print("Configuração:",lst)
	return lst

def convert_to_dict(places:list,cities)->dict:
	cities_dict = {}
	for p in places:
		cities_dict[p] = []
	for p in places:
		for cn in cities["connections"]:
			if cn["from"] == p:
				cities_dict[p].append([cn["to"],cn["cost"]])
	# Test
	print("Cities dict:", cities_dict)
	return cities_dict

def cost_value(state: list, cities_dict: dict)->int:
	i = 0
	cost = 0
	_from = state[i]
	i+=1
	_to = state[i]
	end = False
	while end == False:
		connected = cities_dict[_from]
		for c in connected:
			if c[0] == _to:
				cost = cost + c[1]
				# Test
				print("Cost ", c[1],"added after adding connection ",_from,"->",_to)

		if i < len(state) - 1:
			_from = _to
			i+=1
			_to = state[i]
		else:
			end = True
	#Last connection between first city and last city
	_from = state[-1]
	_to = state[0]
	connected = cities_dict[_from]
	for c in connected:
		if c[0] == _to:
			cost += c[1]
			# Test
			print("Cost ", c[1],"added after adding connection ",_from,"->",_to)
	# Test
	#print("Total cost is:", cost)
	return cost

def main():
	random.seed()
	cities = read_file("./cities.conf")
	# Initial state: A random selection
	state = ["Lisboa","Evora","Beja","Setubal"]
	cities_dict = convert_to_dict(state,cities)
	random.shuffle(state)
	cost = cost_value(state,cities_dict)
	# Costs for the first example:
	print("For the initial state ", state,"the total cost is ",cost)
	end = False
	state_selected = state
	cost_selected = cost
	max_step = 10
	step = 0
	while end== False:
		# Find a neighbour, for example, exchange two positions in the state
		pos_1 = random.randint(0,len(state) - 1 )
		pos_2 = pos_1 + 1 if pos_1 + 1 < len(state) else -1
		#pos_2 = random.randint(0,len(state) - 1 )
		# Test
		print("Changing values between ", pos_1," and ",pos_2)
		# Swap: a[i], a[n] = a[n], a[i]
		state[pos_1], state[pos_2] = state[pos_2], state[pos_1]

		cost = cost_value(state,cities_dict)
		# Test
		print("State after swap is:", state," with the cost ",cost)
		# Keep the smaller cost
		if cost < cost_selected:
			cost_selected = cost
			state_selected = state
			# Test
			print("A new minimum cost or state ",state," is ", cost)
		step +=1
		# End the program
		if step >= max_step:
			end = True
		input()

	print("The state selected is ", state_selected," with the total cost is ",cost_selected)
	input()

main()





