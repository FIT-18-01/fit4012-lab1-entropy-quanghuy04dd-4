#!/usr/bin/env python3
"""Test script for Lab 1 - Entropy, Redundancy, and Modular Inverse"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from entropy_redundancy import calculate_entropy, calculate_redundancy
from mod_inverse import mod_inverse, gcd

def test_entropy_redundancy():
    print("=" * 60)
    print("Testing Entropy and Redundancy")
    print("=" * 60)
    
    test_cases = [
        ("aaaa", "All same characters - low entropy, high redundancy"),
        ("abcd", "All unique characters - higher entropy"),
        ("hello world", "Mixed characters with spaces"),
    ]
    
    results = []
    for text, description in test_cases:
        entropy = calculate_entropy(text)
        redundancy = calculate_redundancy(text)
        results.append((text, entropy, redundancy, description))
        print(f"\nInput: '{text}'")
        print(f"Description: {description}")
        print(f"Entropy: {entropy:.6f}")
        print(f"Redundancy: {redundancy:.6f}")
    
    return results

def test_mod_inverse():
    print("\n" + "=" * 60)
    print("Testing Modular Inverse")
    print("=" * 60)
    
    test_cases = [
        (3, 7, 5, "3 * 5 mod 7 = 15 mod 7 = 1"),
        (10, 17, 12, "10 * 12 mod 17 = 120 mod 17 = 1"),
        (6, 9, None, "gcd(6, 9) = 3 != 1, no inverse exists"),
    ]
    
    results = []
    for a, m, expected, description in test_cases:
        print(f"\nTest: a={a}, m={m}")
        print(f"Description: {description}")
        
        if expected is None:
            # Should not exist
            if gcd(a, m) != 1:
                print(f"Result: No inverse exists (gcd={gcd(a, m)})")
                results.append((a, m, "Không tồn tại", "Không tồn tại"))
            else:
                inv = mod_inverse(a, m)
                print(f"Result: {inv}")
                results.append((a, m, "Không tồn tại", str(inv)))
        else:
            inv = mod_inverse(a, m)
            verification = (a * inv) % m
            print(f"Result: {inv}")
            print(f"Verification: {a} * {inv} mod {m} = {verification}")
            status = "PASS" if inv == expected and verification == 1 else "FAIL"
            print(f"Status: {status}")
            results.append((a, m, str(expected), str(inv)))
    
    return results

def main():
    print("FIT4012 - Lab 1 Test Results")
    print("=" * 60)
    
    entropy_results = test_entropy_redundancy()
    mod_results = test_mod_inverse()
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    print("\nEntropy/Redundancy Results:")
    print("-" * 60)
    print(f"{'Input':<20} {'Entropy':>10} {'Redundancy':>12}")
    print("-" * 60)
    for text, entropy, redundancy, _ in entropy_results:
        print(f"'{text}'{' ' * (19-len(text))} {entropy:>10.4f} {redundancy:>12.4f}")
    
    print("\nModular Inverse Results:")
    print("-" * 60)
    print(f"{'a':>5} {'m':>5} {'Expected':>15} {'Got':>15}")
    print("-" * 60)
    for a, m, expected, got in mod_results:
        print(f"{a:>5} {m:>5} {expected:>15} {got:>15}")

if __name__ == "__main__":
    main()