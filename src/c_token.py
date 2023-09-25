class Token:
    def __init__(self, token_type, value, line_number, position):
        self.type = token_type 
        self.value = value           
        self.line_number = line_number   
        self.position = position     

    def __str__(self):
        return f"Token(type='{self.type}', value='{self.value}', line_number={self.line_number}, position={self.position})"


class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def __str__(self):
        return f"AST(node_type='{self.node_type}', value='{self.value}', children={self.children}, parent={self.parent})"



    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        if self.value is not None:
            node_str += f": {self.value}"
        result = [node_str]

        # Recursively add child nodes
        print(type(self.children))
        for child in self.children:
            child_str = child.to_string(level + 1)
            result.extend(child_str.split('\n'))

        
        return '\n'.join(result)

# class for Number nodes
class BinaryOperatorNode(ASTNode):
    def __init__(self, operator, left, right, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.operator = operator
        self.left = left
        self.right = right
    
    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:\n"
        
        node_str += f"\tleft: {self.left}, operator: {self.operator}, right: {self.right}\n"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.left, ASTNode):
 
                child_str = self.left.to_string(level + 1)
                result.extend(child_str.split('\n'))
        elif isinstance(self.right, ASTNode):
 
                child_str = self.right.to_string(level + 1)
                result.extend(child_str.split('\n'))

        return '\n'.join(result)

# class for Array nodes 
class ArrayNode(ASTNode):
    def __init__(self, name: str, size: int, elements, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.size = size
        self.elements = elements


    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        node_str += f"\tname: {self.name}, size: {self.size}\n"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.elements, ASTNode):
 
                child_str = self.elements.to_string(level + 1)
                result.extend(child_str.split('\n'))

        return '\n'.join(result)



# class for Struct nodes 
class StructNode(ASTNode):
    def __init__(self, name,  elements, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.elements = elements


# class for Macro nodes
class MacroNode(ASTNode):
    def __init__(self, name, macro_body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.body = macro_body


# class for nodes (character, int, float, string, ect...)
class VariableNode(ASTNode):
    def __init__(self, value, varType, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.varType = varType
        self.value = value


    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:\n"
        
        node_str += f"\ttype: {self.varType}, identifier: {self.value}\n"

        result = [node_str]

        return '\n'.join(result)



# class for Asignements
class AssignmentNode(ASTNode):
    def __init__(self, left, right, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.left = left
        self.right = right
    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        result = [node_str]

        # Recursively add child nodes
 
        if isinstance(self.left, ASTNode):
            child_str = self.left.to_string(level + 1)
            result.extend(child_str.split('\n'))
 
 
        if isinstance(self.right, ASTNode):
            child_str = self.right.to_string(level + 1)
            result.extend(child_str.split('\n'))
 

        return '\n'.join(result)


# class for Conditionals
class IfStatementNode(ASTNode):
    def __init__(self, condition, body, node_type, else_body=None):
        super().__init__(node_type)
        self.node_type = node_type
        self.condition = condition
        self.body = body
        self.else_body = else_body


# class for While loop
class WhileLoopNode(ASTNode):
    def __init__(self, condition, body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.condition = condition
        self.body = body


# class for Function declaration
class FunctionDeclarationNode(ASTNode):
    def __init__(self, return_type, name, parameters, body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body


# class for Function calls
class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.arguments = arguments

# class for For loop
class ForLoopNode(ASTNode):
    def __init__(self, initialization, condition, update, body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.initialization = initialization
        self.condition = condition
        self.update = update
        self.body = body

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        node_str += f"\tbody: {self.body}\n"
        result = [node_str]

        # Recursively add child nodes
 
        if isinstance(self.initialization, ASTNode):
            child_str = self.initialization.to_string(level + 1)
            result.extend(child_str.split('\n'))
 
        if isinstance(self.condition, ASTNode):
            child_str = self.condition.to_string(level + 1)
            result.extend(child_str.split('\n'))


 
        if isinstance(self.update, ASTNode):
            child_str = self.update.to_string(level + 1)
            result.extend(child_str.split('\n'))

        if isinstance(self.body, ASTNode):
            child_str = self.body.to_string(level + 1)
            result.extend(child_str.split('\n'))
            
        

        return '\n'.join(result)



class LoopConditionNode(ASTNode):
    def __init__(self, right, comparator, left, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.right = right
        self.comparator = comparator
        self.left = left

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:\n"
        
        node_str += f"\tleft: {self.left}, comparator: {self.comparator}, right: {self.right}\n"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.left, list)  == True:
        
            for child in self.left:
                if isinstance(child, ASTNode):
                    child_str = child.to_string(level + 1)
                    result.extend(child_str.split('\n'))

        if isinstance(self.right, list)  == True:
        
            for child in self.right:
                if isinstance(child, ASTNode):
                    child_str = child.to_string(level + 1)
                    result.extend(child_str.split('\n'))


        return '\n'.join(result)

