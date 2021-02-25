# Convert a certain expression like 2+3 to expression in a postfix notation.
#
# The given expression can have one of the following tokens:
#
# a number;
# a parenthesis;
# arithmetic operator:
# subtraction (-);
# addition (+);
# multiplication (*);
# division (/);
# modulo operation (%).
# Example:
#
# For expression = ["2","+","3"] the output should be ["2","3","+"].


def toPostFixExpression(e):
    polish_notation = []
    out = []
    for i in e:
        if i.isnumeric():
            out.append(i)
        elif i == '(':
            polish_notation.append(i)
        elif i == ')':
            while polish_notation[-1] != '(':
                out.append(polish_notation.pop())
            polish_notation.pop()
        elif i in ['*', '/', '+', '-', '%']:
            if (i in ['+', '-']) and polish_notation and (polish_notation[-1] in ['*', '/', '%', '+', '-']):
                out.append(polish_notation.pop())
                polish_notation.append(i)
            else:
                polish_notation.append(i)
    while polish_notation:
        out.append(polish_notation.pop())
    return out
