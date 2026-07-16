from collector.nodes import get_nodes

nodes = get_nodes()

print(f"Nodes : {len(nodes)}")

for node in nodes:
    print(node)
