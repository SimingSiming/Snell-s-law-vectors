from snells_law import calculate_exit_point
import pytest
import numpy as np

# Define test cases for 2D and 3D
test_cases = [
    {
        "entry_point": [0, 0],
        "incident_vector": [1, -1],
        "thickness": 2,
        "normal": [0, 1],
        "n1": 1.0,
        "n2": 1.5
    },
    {
        "entry_point": [0, 0, 0],
        "incident_vector": [1, -1, -1],
        "thickness": 2,
        "normal": [0, 0, 1],
        "n1": 1.0,
        "n2": 1.5
    },
    {
        "entry_point": [0, 0],
        "incident_vector": [1, 0],
        "thickness": 3,
        "normal": [0, 1],
        "n1": 1.0,
        "n2": 2.0
    },
    {
        "entry_point": [0, 0, 0],
        "incident_vector": [1, 0, -1],
        "thickness": 3,
        "normal": [0, 0, 1],
        "n1": 1.0,
        "n2": 2.0
    },
    {
        "entry_point": [1, 1],
        "incident_vector": [0, -1],
        "thickness": 1,
        "normal": [0, 1],
        "n1": 1.0,
        "n2": 1.33
    },
    {
        "entry_point": [1, 1, 1],
        "incident_vector": [0, -1, -1],
        "thickness": 1,
        "normal": [0, 0, 1],
        "n1": 1.0,
        "n2": 1.33
    },
    {
        "entry_point": [2, 2],
        "incident_vector": [1, -1],
        "thickness": 4,
        "normal": [0, 1],
        "n1": 1.0,
        "n2": 1.5
    },
    {
        "entry_point": [2, 2, 2],
        "incident_vector": [1, -1, 1],
        "thickness": 4,
        "normal": [0, 0, 1],
        "n1": 1.0,
        "n2": 1.5
    },
    {
        "entry_point": [0, 0],
        "incident_vector": [1, 1],
        "thickness": 5,
        "normal": [0, 1],  
        "n1": 1.0,   
        "n2": 1.33
    },
    {
        "entry_point": [0, 0, 0],
        "incident_vector": [1, 1, 1],
        "thickness": 5,
        "normal": [0, 0, 1],
        "n1": 1.0,
        "n2": 1.33
    }
]

@pytest.mark.parametrize("case", test_cases)
def test_calculate_exit_point(case):
    entry_point = case["entry_point"]
    incident_vector = case["incident_vector"]
    thickness = case["thickness"]
    normal = case["normal"]
    n1 = case["n1"]
    n2 = case["n2"]

    exit_point, transmitted_vector = calculate_exit_point(entry_point, incident_vector, thickness, normal, n1, n2)

    ## test snell' s law expected formula
    snell_left = n1 * np.sin(np.arccos(np.dot(incident_vector, normal)/ np.linalg.norm(incident_vector))) 
    snell_right = n2 * np.sin(np.arccos(np.dot(transmitted_vector, normal)))
    assert np.allclose(snell_left, snell_right, atol=0.001), f"Expected {snell_left} but got {snell_right}"

    ## height test
    height = abs(np.dot(exit_point - entry_point, normal))
    expected_height = thickness
    assert np.allclose(expected_height, height, atol = 0.001), f"expected height {expected_height}, but got {height}"

    ## exit point test
    excpted_exit_point = transmitted_vector * thickness / np.dot(transmitted_vector, normal) + entry_point
    assert np.allclose(exit_point, excpted_exit_point , atol=0.001), f"Expected exit point {excpted_exit_point} but got {exit_point}"


if __name__ == "__main__":
    pytest.main()