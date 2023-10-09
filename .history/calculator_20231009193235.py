import re

# Define token types and their regular expressions
TOKEN_TYPES = [
    ('id', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
    ('assign', r':='),                 # Assignment :=
    ('number', r'\d+(\.\d*)?'),        # Numbers
    ('lparen', r'\('),                 # Left Parenthesis (
    ('rparen', r'\)'),                 # Right Parenthesis )
    ('plus', r'\+'),                   # Addition +
    ('minus', r'-'),                  # Subtraction -
    ('times', r'\*'),                  # Multiplication *
    ('div', r'/'),                     # Division /
]

# Combine the regular expressions into a single pattern
PATTERN = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKEN_TYPES)

# Function to tokenize input source code
def lexer(source_code):
    tokens = []
    while source_code:
        match = re.match(PATTERN, source_code)
        if match:
            token_type = match.lastgroup
            lexeme = match.group()
            tokens.append((token_type, lexeme))
            source_code = source_code[len(lexeme):].strip()
        else:
            raise SyntaxError(f"Invalid character in source code: {source_code[0]}")
    return tokens

# Example usage
if __name__ == '__main__':
    source_code = """Celcius := 100.00
                    Fahrenheit := (9/5)*Celcius + 32"""

    tokens = lexer(source_code)
    for token_type, lexeme in tokens:
        print(f'{token_type}: {lexeme}')