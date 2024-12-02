# tokenizer goes here

import re

def tokenize_cpp(code):
    # Define token patterns
    patterns = [
        ('KEYWORD', r'\b(int|float|double|char|void|for|while|if|else|return|class|public|private|protected)\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
        ('NUMBER', r'\b\d+(\.\d+)?\b'),
        ('STRING', r'"[^"]*"'),
        ('OPERATOR', r'[+\-*/=<>!&|^~]'),
        ('PUNCTUATION', r'[{}()\[\];,.]'),
        ('WHITESPACE', r'\s+'),
    ]

    # Combine patterns
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns)

    # Tokenize
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':
            yield (kind, value)

# Example usage
cpp_code = """
int main() {
    int x = 5;
    double y = 3.14;
    if (x > 0) {
        return y * 2;
    }
    return 0;
}
"""

tokens = list(tokenize_cpp(cpp_code))
for token in tokens:
    print(token)
