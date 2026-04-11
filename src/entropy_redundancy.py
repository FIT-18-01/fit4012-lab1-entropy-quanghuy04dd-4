import math
from collections import Counter

def calculate_entropy(text):
    if not text:
        return 0.0
    
    freq = Counter(text)
    entropy = 0.0
    for count in freq.values():
        p = count / len(text)
        entropy -= p * math.log2(p)
    
    return entropy

def calculate_redundancy(text, alphabet_size=256):
    if not text or alphabet_size <= 1:
        return 0.0
    
    entropy = calculate_entropy(text)
    max_entropy = math.log2(alphabet_size)
    redundancy = max_entropy - entropy
    
    return max(redundancy, 0.0)

def main():
    input_str = input("Enter a string of characters: ")
    
    entropy = calculate_entropy(input_str)
    redundancy = calculate_redundancy(input_str)
    
    print(f"Entropy: {entropy}")
    print(f"Redundancy: {redundancy}")

if __name__ == "__main__":
    main()