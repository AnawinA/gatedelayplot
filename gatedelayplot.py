class GateDelayPlot:

    def __init__(self, init_gate: dict[int], name: str="unknown") -> None:
        self._init_gate = init_gate
        self.gates = init_gate
        self.name = name
        self.length = len(list(self._init_gate.values())[0])
        self.str_space = 0
    def __getitem__(self, key) -> list:
        return self.gates[key]
    
    def get_dict(self) -> dict:
        return self.gates
    
    def get_init_dict(self) -> dict:
        return self._init_gate
    
    def print_str(self, *gate: str):
        if gate:
            for i in gate:
                print(f"{i[0]:<{self.str_space}} |{"".join(map(lambda x: '-' if x else '_', self.gates[i]))}|")
        else:
            for i in self.gates.items():
                print(f"{i[0]:<{self.str_space}} |{"".join(map(lambda x: '-' if x else '_', i[1]))}|")
    
    def get_str(self, gate: str):
        return gate + " |" + "".join(map(lambda x: '-' if x else '_', self.gates[gate])) + "|"
    
    def plot(*key):
        for i in key:
            print(i)
    
    def show_plot(self, gate_dict: dict[int], figsize=((5, 5)), delay=0):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, axs = plt.subplots(len(gate_dict), figsize=figsize, squeeze=False)
        fig.tight_layout()
        for i, (name, gate) in enumerate(gate_dict.items()):
            gate.insert(0, gate[0])
            x = range(self.length + 1)
            ax: plt.Axes = axs[i][0]
            ax.step(x, gate, linewidth=3, where='pre')
            ax.set_ylabel(name, size=15, rotation=0)
            ax.set_ylim(-0.2, 1.2)
            ax.set_xticks(x)
            ax.set_xlim(min(x), max(x))
            ax.set_yticks([1, 0])
            for i in x:
                ax.axvline(i, color='k', linestyle=':', linewidth=0.7)
        plt.show()
    
    def plot(self, *key):
        if key:
            self.show_plot({i: self.gates[i] for i in key})
        else:
            self.show_plot(self.gates)
    
    def add(self, gate_dict: dict[int]):
        self.gates.update(gate_dict)
    
    def add_delay(self, gate_dict: dict[int], delay=()):
        if not delay:
            delay = tuple([1] * len(gate_dict))
        for i, gate in enumerate(gate_dict.items()):
            for _ in range(delay[i]):
                gate[1].insert(0, -1)
                gate[1].pop()
            self.gates.update(dict([gate]))
    
    def _update_str_space(self):
        max_space = list(map(len, self.gates.keys()))
        self.str_space = max(max_space)
    
    def _name_config(self, name: str):
        new_name = ""
        if not name:
            def assign_chr(char: str):
                return chr(ord(char) + 1)
            if ":" in list(self.gates.keys())[-1]:
                new_name: str = list(self.gates.keys())[-1].split(":")[1]
                if new_name.isalpha() and len(new_name) == 1:
                    new_name = assign_chr(new_name)
            else:
                new_name = assign_chr(list(self.gates.keys())[-1])
        else:
            new_name = name
        return new_name
    
    def _find_name(self, name: str):
        no_parent = name.split(":")[1]
        # if name in self.gates.keys():
        #     return "".endswith(name)
        # else:
        #     return None
    
    def _logic_calc(self, key: tuple[str], type: str,):
        def not_null(a, b=0):
            return (a == -1 or b == -1)
        match type:
            case "and":
                return f"{key[0]}&{key[1]}", [int(a and b) 
                        if not not_null(a, b) else -1 
                        for a, b in zip(self.gates[key[0]], self.gates[key[1]])]
            case "or":
                return f"{key[0]}+{key[1]}", [int(a or b) 
                        if not not_null(a, b) else -1 
                        for a, b in zip(self.gates[key[0]], self.gates[key[1]])],
            case "not":
                return f"!{key[0]}", [int(not i) if not i == -1 else -1 for i in self.gates[key[0]]]
            case "nand":
                return f"!({key[0]}&{key[1]})", [int(not (a and b)) 
                        if not not_null(a, b) else -1 
                        for a, b in zip(self.gates[key[0]], self.gates[key[1]])]
            case "nor":
                return f"!({key[0]}+{key[1]})", [int(not (a or b)) 
                        if not not_null(a, b) else -1 
                        for a, b in zip(self.gates[key[0]], self.gates[key[1]])]
            case "xor":
                return f"{key[0]}^{key[1]}", [int(a ^ b) 
                        if not not_null(a, b) else -1 
                        for a, b in zip(self.gates[key[0]], self.gates[key[1]])]
            case _:
                return None
    
    def _add_config(self, *keys: tuple[str], type: str, name="", delay=1, parent=False):
        key_name = self._name_config(name)
        parent_name, gate_config = self._logic_calc(keys, type=type)
        if parent:
            key_name = parent_name + ":" + key_name
        self.add_delay({key_name: gate_config}, delay=(delay,))
        self._update_str_space()
    
    def add_not(self, key: str, name="", delay=1, parent=False):
        self._add_config(key, type="not", name=name, delay=delay, parent=parent)
    
    def add_and(self, key1: str, key2: str, name="", delay=1, parent=False):
        self._add_config(key1, key2, type="and", name=name, delay=delay, parent=parent)
    
    def add_or(self, key1: str, key2: str, name="", delay=1, parent=False):
        self._add_config(key1, key2, type="or", name=name, delay=delay, parent=parent)
    
    def add_nand(self, key1: str, key2: str, name="", delay=1, parent=False):
        self._add_config(key1, key2, type="nand", name=name, delay=delay, parent=parent)
    
    def add_nor(self, key1: str, key2: str, name="", delay=1, parent=False):
        self._add_config(key1, key2, type="nor", name=name, delay=delay, parent=parent)
    
    def add_xor(self, key1: str, key2: str, name="", delay=1, parent=False):
        self._add_config(key1, key2, type="xor", name=name, delay=delay, parent=parent)



# delay = GateDelayPlot({
#     "A": [0, 1, 1, 0, 1],
#     "B": [1, 0, 1, 1, 1]
# })
# # delay.print_str('A')
# # print(delay.get_str("A"))
# # print(delay["A"])
# # delay.add({"C": [1, 1, 0, 0, 1]})
# # delay.add_delay({"D": [1, 1, 0, 0, 1]}, delay=(3,))
# # print(delay.gates, delay._init_gate)
# delay.add_not("A", delay=1, parent=True)
# delay.add_not("B", delay=1, name="dk")
# delay.print_str()
# delay.plot()
# delay.plot()
