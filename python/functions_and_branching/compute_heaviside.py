import math

def compute_heaviside(position):

    if position < 0:
        return 0.0

    elif position ==0:
        return 0.5 
    else:
        return 1.0

def test_heaviside():

    tests = [(-10, 0), (-10 - 15, 0), (0, 0.5), (10 - 15, 0), (10, 1)]

    for input_value, expected_output_value in tests:
        output = compute_heaviside(input_value)
        correct = math.isclose(output, expected_output_value)
        print(f"Input Value: {input_value}\n Result: {output}, Expect Output: {expected_output_value}, Test: {correct}\n")

if __name__ == "__main__":
    test_heaviside()