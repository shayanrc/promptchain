from promptchain import Node, Chain

class Message(Node):
    def __init__(self, role, content):
        if role not in ["system", "user", "assistant"]:
            raise ValueError("Role must be 'system', 'user' or 'assistant'")
        self.role = role
        self.content = content

    @property
    def value(self):
        return {'role': self.role, 'content': self.content}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.role!r}, {self.content!r})"

    def __add__(self, other):
        if isinstance(other, Node):
            return Chain([self, other])
        elif isinstance(other, Chain): 
            return Chain([self] + other.nodes)  
        else:
            raise TypeError("Unsupported operand type(s) for +")