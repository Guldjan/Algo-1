
class ClosestCoffeeStore:

    # Finds the closest coffee store to a point.
    # graph - [[bool]]
    # starting_point - int
    # is_coffee_store - [bool]
   
    def find_shortest_path(self, graph, start, end, path=[]):
    	path = path + [start]
    	if (start == end):
    		return path
    	shortest = []
    	for vertex in range(len(graph)):
    		if vertex not in path:
    			new_path = self.find_shortest_path(graph, vertex, end, path)
    			if new_path:
    				if not shortest or len(new_path) < len(shortest):
    					shortest = new_path
    	return shortest


    def closestCoffeeStore(self, graph, is_coffee_store, starting_point):
    	coffee_shops = [i for i in range(len (is_coffee_store)) if is_coffee_store[i] == 1]
    	paths = [(len (self.find_shortest_path(graph, starting_point, i)), i) for i in coffee_shops]
    	if paths:
    		a = [i for i in paths if i[0] > 0]
    		return min(a)[1]
    	else:
    		return -1
