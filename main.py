from bst import BST
from graph import Graph
from hash_set import HashSet
from hash_table import HashTable
from linked_list import LinkedList
from linked_queue import Queue, board_passengers
from linked_stack import Stack, is_balanced
from min_heap import MinHeap

def create_metro_graph():
    graph = Graph()
    stations = ["Airport", "Beach", "Campus", "Downtown", "Eastside", "Factory", "Garden"]
    connections = [
        ("Airport", "Downtown"),
        ("Airport", "Eastside"),
        ("Beach", "Campus"),
        ("Beach", "Garden"),
        ("Campus", "Downtown"),
        ("Downtown", "Eastside"),
        ("Downtown", "Factory"),
        ("Eastside", "Factory"),
        ("Factory", "Garden")
    ]

    for station in stations:
        graph.add_vertex(station)

    for u, v in connections:
        graph.add_edge(u, v)

    return graph

def main():
    stations = ["Airport", "Beach", "Campus", "Downtown", "Eastside", "Factory", "Garden"]
    print("=" * 40)
    print("     METRO CITY NAVIGATION SYSTEM")
    print("=" * 40)
    
    print("\n1. METRO CITY GRAPH")
    graph = create_metro_graph()
    print(graph)
    print("Total stations:", graph.vertex_count())
    print("Total connections:", graph.edge_count())
    
    print("\n2. STATION DIRECTORY - BINARY SEARCH TREE")
    tree = BST()
    for station in stations:
        tree.insert(station)

    print("Alphabetical inorder traversal:")
    print(tree.inorder())
    print("Level-order traversal:")
    print(tree.level_order())
    print("Tree height:", tree.height())
    print("Number of leaf nodes:", tree.count_leaves())
    
    print("\n3. FARE ZONE DIRECTORY - HASH TABLE")
    fares = HashTable()
    fare_zones = {
        "Airport": 1,
        "Beach": 3,
        "Campus": 2,
        "Downtown": 1,
        "Eastside": 2,
        "Factory": 2,
        "Garden": 3
    }

    for station, zone in fare_zones.items():
        fares.put(station, zone)

    for station in stations:
        print(f"{station}: Zone {fares.get(station)}")

    print("Total fare records:", len(fares))
    print("\n4. TRIP LOG - LINKED LIST")
    trip = LinkedList()
    trip_stations = ["Airport", "Downtown", "Campus", "Beach"]
    for station in trip_stations:
        trip.append(station)

    print("Original trip:")
    print(trip)
    trip.reverse()
    print("Reversed trip:")
    print(trip)
    
    print("\n5. MAINTENANCE TASKS - MIN HEAP")
    heap = MinHeap()
    tasks = [
        (3, "Inspect Beach-Campus sign"),
        (1, "Repair Eastside crossing"),
        (2, "Replace Downtown display")
    ]

    for priority, task in tasks:
        heap.push(priority, task)

    print("Tasks removed by ascending numeric task priority:")
    while not heap.is_empty():
        priority, task = heap.pop()
        print(f"Task Priority {priority}: {task}")

    print("\n6. RIDER BACK BUTTON - STACK")
    stack = Stack()
    pages = ["Airport", "Downtown", "Campus", "Beach"]
    for page in pages:
        stack.push(page)

    print("Browser history:", stack.to_list())
    print("Back button:", stack.pop())
    print("Back button:", stack.pop())
    print("Current page:", stack.peek())
    print("Remaining history:", stack.to_list())

    print("\n7. SERVICE LINE - QUEUE")
    queue = Queue()
    passengers = ["Ana", "Ben", "Cy"]
    for passenger in passengers:
        queue.enqueue(passenger)

    print("Initial service line:", queue.to_list())
    print("Passenger served:", queue.dequeue())
    print("Next passenger:", queue.peek())
    print("Remaining passengers:", queue.to_list())
    print("Passengers waiting:", len(queue))

    print("\n8. COMMON STOPS - HASH SET")
    airport_neighbors = HashSet()
    factory_neighbors = HashSet()
    beach_neighbors = HashSet()
    for station in graph.neighbors("Airport"):
        airport_neighbors.add(station)

    for station in graph.neighbors("Factory"):
        factory_neighbors.add(station)

    for station in graph.neighbors("Beach"):
        beach_neighbors.add(station)

    common_stops = airport_neighbors.intersection(
        factory_neighbors
    )

    combined_stops = airport_neighbors.union(
        beach_neighbors
    )

    print(
        "Airport neighbors:",
        sorted(airport_neighbors.to_list())
    )

    print(
        "Factory neighbors:",
        sorted(factory_neighbors.to_list())
    )

    print(
        "Common stops between Airport and Factory:",
        sorted(common_stops.to_list())
    )

    print(
        "Union of Airport and Beach neighbors:",
        sorted(combined_stops.to_list())
    )

    print(
        "Intersection of Airport and Beach neighbors:",
        sorted(
            airport_neighbors.intersection(
                beach_neighbors
            ).to_list()
        )
    )

    print("\n9. ADDITIONAL APPLICATION FUNCTIONS")
    examples = [
        "{[()]}",
        "{[(])}"
    ]

    for example in examples:
        print(
            f"Is {example} balanced? {is_balanced(example)}"
        )

    print("\nPassenger boarding simulation:")
    boarding_examples = [
        (["Ana", "Ben", "Cy", "Dan"], 2),
        (["Alice", "Bob", "Charlie", "David", "Eve"], 3)
    ]

    for names, k in boarding_examples:
        elimination_order, winner = board_passengers(
            names, k
        )

        print("Passengers:", names)
        print("Elimination order:", elimination_order)
        print("Last passenger:", winner)

    print("\n" + "=" * 40)
    print("   METRO CITY DEMONSTRATION COMPLETE")
    print("=" * 40)

if __name__ == "__main__":
    main()

