from typing import overload

class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False

    def __add__(self, other):
        if isinstance(other, Node):
            return Chain([self, other])
        elif isinstance(other, Chain): 
            return Chain([self] + other.nodes)  
        else:
            raise TypeError("Unsupported operand type(s) for +")



class Chain(Node):
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes is not None else []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nodes!r})"
    
    
    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.nodes == other.nodes
        return False

    def __add__(self, other):
        if isinstance(other, Node):
            new_nodes = self.nodes + [other]  
            return Chain(new_nodes)
        elif isinstance(other, Chain):
            new_nodes = self.nodes + other.nodes  
            return Chain(new_nodes)
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __call__(self):
        updated_nodes = []
        for node in self.nodes:
            if isinstance(node, Transform):
                ret_val = node(Chain(updated_nodes))

                if isinstance(ret_val, Chain):
                    updated_nodes = ret_val.nodes
                
                elif isinstance(ret_val, Node):
                    updated_nodes.append(ret_val)
            else:
                updated_nodes.append(node)
        
        return Chain(updated_nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, index):
        return self.nodes[index]


    def map(self, function):
        new_nodes = []
        for node in self.nodes:
            new_nodes.append(function(node))
        return Chain(new_nodes)


    def agg(self, function):
        ...

           

        # for transform in self.transformations:
        #     input_data = transform(input_data).execute()


    


class Transform(Node):
    def __init__(self, value=None):
        if value is None:
            super().__init__(self.__class__.__name__)
        else:
            
            super().__init__(value)

    def __call__(self, obj):
        if isinstance(obj, (Node, Chain)):
            raise NotImplementedError
        else:
            return obj
            # raise TypeError("Unsupported operand type(s) for transformation")