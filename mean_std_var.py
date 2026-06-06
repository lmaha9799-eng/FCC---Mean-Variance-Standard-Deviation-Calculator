import numpy as np

def calculate(list_input):
    # Check if the list contains exactly 9 elements
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 Numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Calculate statistics
    # axis=0 refers to columns (Axis 1 in the description)
    # axis=1 refers to rows (Axis 2 in the description)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations

    import numpy as np

def calculate(list_input):
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list_input).reshape(3, 3)
    
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]
    }

    return calculations

# --- ADD THIS CODE AT THE BOTTOM TO TEST IT ---
if __name__ == "__main__":
    test_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(test_data)
    
    # Using pprint (pretty print) makes the dictionary look nice in the terminal
    import pprint
    pprint.pprint(result)