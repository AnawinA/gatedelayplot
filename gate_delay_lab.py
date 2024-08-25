from gatedelayplot import GateDelayPlot

gate = GateDelayPlot({
    "A": [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    "B": [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
}, name="Example 1")

gate.add_not("B")
gate.add_or("A", "B")
gate.add_nand("A", "D", "F")
gate.add_nand("C", "D", "G")
print(gate.get_dict())
gate.print_str()
gate.plot()