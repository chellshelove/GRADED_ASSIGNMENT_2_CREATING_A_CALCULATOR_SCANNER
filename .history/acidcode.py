# Token types
TOKEN_NUMBER = "NUMBER"
TOKEN_INT = "INT"
TOKEN_PLUS = "PLUS"
TOKEN_MINUS = "MINUS"
TOKEN_MULTIPLY = "MULTIPLY"
TOKEN_DIVIDE = "DIVIDE"
TOKEN_LPAREN = "LPAREN"
TOKEN_RPAREN = "RPAREN"
TOKEN_EQUALS = "EQUALS"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NEWLINE = "NEWLINE"

# Define the DFA transitions
TRANSITIONS = {
    "START": {
        "digit": ("INT", "INT"),
        "+": ("PLUS", "START"),
        "-": ("MINUS", "START"),
        "*": ("MULTIPLY", "START"),
        "/": ("DIVIDE", "START"),
        "(": ("LPAREN", "START"),
        ")": ("RPAREN", "START"),
        "=": ("EQUALS", "START"),
        "\n": ("NEWLINE", "START"),
        "letter": ("IDENTIFIER", "IDENTIFIER"),
    },
    "INT": {
        "digit": ("INT", "INT"),
        "+": ("PLUS", "START"),
        "-": ("MINUS", "START"),
        "*": ("MULTIPLY", "START"),
        "/": ("DIVIDE", "START"),
        "(": ("LPAREN", "START"),
        ")": ("RPAREN", "START"),
        "=": ("EQUALS", "START"),
        "\n": ("NEWLINE", "START"),
    },
    "IDENTIFIER": {
        "letter": ("IDENTIFIER", "IDENTIFIER"),
        "digit": ("IDENTIFIER", "IDENTIFIER"),
        "=": ("EQUALS", "START"),
        "\n": ("NEWLINE", "START"),
    },
}

# Tokenization function using DFA
def tokenize(expression):
    tokens = []
    state = "START"
    current_token = ""

    for char in expression:
        if char.isdigit():
            input_type = "digit"
        elif char.isalpha():
            input_type = "letter"
        else:
            input_type = char

        if input_type in TRANSITIONS[state]:
            token_type, new_state = TRANSITIONS[state][input_type]
            if token_type == "INT":  # Change to "INT" for digits
                current_token += char
            elif token_type == "IDENTIFIER":
                current_token += char
            else:
                if current_token:
                    tokens.append((TOKEN_INT, current_token))  # Change to "INT" for digits
                    current_token = ""
                tokens.append((token_type, char))
            state = new_state
        else:
            # Skip invalid characters
            continue

    if current_token:
        tokens.append((TOKEN_INT, current_token))  # Change to "INT" for digits

    return tokens

# Test the lexer with the provided expression
expression = "Celcius = 98 * Celcius = 50\nFahrenheit = (7/4)"
tokens = tokenize(expression)
print("The expression :")
print(expression)
for token in tokens:
    print(token)
