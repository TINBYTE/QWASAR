def last_word(param_1):
    # Remove leading/trailing whitespace and split by whitespace
    words = param_1.strip().split()
    # Return the last word followed by '\n', or just '\n' if no words
    return (words[-1] if words else '') + '\n'

# Example usage
print(last_word("FOR PONIES"), end='')         # Output: PONIES
print(last_word("this        ...       is sparta"), end='')  # Output: sparta
print(last_word("  lorem,ipsum  "), end='')    # Output: ipsum
print(last_word(""), end='')                   # Output: (empty)