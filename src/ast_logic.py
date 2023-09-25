import json
from c_token import *
from c_utils import get_comparator_index

def parser(tokens: [Token]):
    length = len(tokens)

    ast = ASTNode("Entry", "Program")
    i = 0

    # only valid for 'for' loop currently
    while i < length:
        if tokens[i].value == "for":
            i += 1
            buffer = []
            while i < length and tokens[i].value != ")":
                buffer.append(tokens[i].value)
                i += 1

            if i < length and tokens[i].value == ")":
                i += 1

            body = []
            # Check bounds and put the body of the for loop in a separate place
            while tokens[i].value != "}":
                body.append(tokens[i].value)
                i += 1

            if tokens[i].value == "}":
                body.append(tokens[i].value)

                # Create an AST node for the loop, AST class is not implemented yet, so will only print tokens
                ast.add_child(parse_for_loop(buffer, body))
                
        else:
            i += 1

    # Return AST after processing all tokens
    print(ast.to_string())
    return ast


def split_array_by_delimiter(arr, delimiter):
    subarrays = []
    subarray = []

    for item in arr:
        if item == delimiter:
            subarrays.append(subarray)
            subarray = []
        else:
            subarray.append(item)

    if subarray:
        subarrays.append(subarray)

    return subarrays


def parse_for_loop(init: [str], loop_token: [str]) -> ForLoopNode:
    init = init[1:]
    arr_loop = split_array_by_delimiter(init, ';')
    assign = arr_loop[0]
    condition = arr_loop[1]
    operation = arr_loop[2]
    parse_assign(assign_tokens=assign)
    parse_condition(condition)
    parse_operation(operation)
    return ForLoopNode( node_type="For Loop", initialization=parse_assign(assign_tokens=assign), condition=parse_condition(condition), update=parse_operation(operation), body=loop_token)


# add abilitty to parse operations


def parse_condition(condition_tokens: [str]):
    comp_index = get_comparator_index(condition_tokens)
    left = condition_tokens[0:comp_index]
    right = condition_tokens[comp_index+1:len(condition_tokens)]
    comp = condition_tokens[comp_index]
    
    return LoopConditionNode( node_type="Loop Condition", right=right, comparator=comp, left=left) # Later, should parse both parts of conditions, in case they are Expressions
    

def parse_operation(operation_tokens: [str]):
    if len(operation_tokens) == 1:
        print(operation_tokens[0][0], operation_tokens[0][1:len(operation_tokens[0])])
        operator = ""
        if(operation_tokens[0][1:len(operation_tokens[0])] == "++"):
            operator = "+"
        elif(operation_tokens[0][1:len(operation_tokens[0])] == "--"):
            operator = "-"

        return AssignmentNode( node_type="Assignement", left=operation_tokens[0][0], right=BinaryOperatorNode( node_type="Binary Expression", operator=operator, left=operation_tokens[0][0], right="1"))
    elif len(operation_tokens) == 3:
        operator = operation_tokens[1][0] # (ex: if +=, operator will be set to +, ect...)
        return AssignmentNode( node_type="Assignement", left=operation_tokens[0], right=BinaryOperatorNode( node_type="Binary Expression", operator=operator, left=operation_tokens[0], right=operation_tokens[2]))





def parse_assign(assign_tokens: [str]):
    right = assign_tokens[-1:len(assign_tokens)]
    left = assign_tokens[0:-2]
    return AssignmentNode(node_type="Assignement", right=right, left=parse_var(left))


def parse_var(var_tokens: [str]):
    var_type = None

    if (len(var_tokens) == 2):
        return VariableNode(node_type="Variable",value=var_tokens[1], varType=var_tokens[0])

    else:  # it means that the loop variable was allready initialized
        return VariableNode(node_type="Variable", value=var_tokens[0], varType=var_type)
