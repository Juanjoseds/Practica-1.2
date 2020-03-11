# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ac = search.GPSProblem('A', 'C', search.romania)
ad = search.GPSProblem('A', 'D', search.romania)
fa = search.GPSProblem('F', 'A', search.romania)

print("----- Anchura -----")
print("A > B")
print(search.breadth_first_graph_search(ab).path())
print("A > C")
print(search.breadth_first_graph_search(ac).path())
print("A > D")
print(search.breadth_first_graph_search(ad).path())
print("F > A")
print(search.breadth_first_graph_search(fa).path())
print("")

print("----- Profundidad -----")
print("A > B")
print(search.depth_first_graph_search(ab).path())
print("A > C")
print(search.depth_first_graph_search(ac).path())
print("A > D")
print(search.depth_first_graph_search(ad).path())
print("F > A")
print(search.depth_first_graph_search(fa).path())

print("")
print("----- Ramificación -----")
print("A > B")
print(search.ramificacion_first_graph_search(ab).path())
print("A > C")
print(search.ramificacion_first_graph_search(ac).path())
print("A > D")
print(search.ramificacion_first_graph_search(ad).path())
print("F > A")
print(search.ramificacion_first_graph_search(fa).path())
print("")

print("----- Subestimación -----")
print("A > B")
print(search.subestimacion_first_graph_search(ab).path())
print("A > C")
print(search.subestimacion_first_graph_search(ac).path())
print("A > D")
print(search.subestimacion_first_graph_search(ad).path())
print("F > A")
print(search.subestimacion_first_graph_search(fa).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
