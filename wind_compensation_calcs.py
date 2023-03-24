from math import cos, sin
import numpy as np
from typing import Tuple


# inputs: 
VECTOR_RADIUS = 20

# example
desired_speed = np.array([0,VECTOR_RADIUS])
wind_speed = np.array([-5, 0])


# wind 2d orthogonal and projection
def get_projection_and_orthogonal_vector(v1: np.ndarray, v2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    v_projection = v1 * np.dot(v1, v2) / np.dot(v1, v1)
    v_orthogonal = v2 - v_projection 
    return v_projection, v_orthogonal

wind_projection, wind_orthogonal = get_projection_and_orthogonal_vector(desired_speed, wind_speed)

# request speed

def get_desired_speed_coefficient(desired_dir_vector, orthogonal_vector, final_vector_size): 
    '''
    || alpha * desired_dir_vector || ^ 2 + || orthogonal_vector || ^ 2 = || final_vector_size || ^ 2 
    '''
    alpha = np.sqrt((final_vector_size ** 2 - np.linalg.norm(orthogonal_vector) ** 2 ) / np.linalg.norm(desired_dir_vector) ** 2 )
    return alpha

def get_compensated_vector_and_desired_vector_coefficient(desired_vector: np.ndarray, wind_vector: np.ndarray, final_vector_size: float) -> Tuple[np.ndarray, float]: 
    desired_vector_coeff = get_desired_speed_coefficient(desired_speed, -wind_orthogonal, VECTOR_RADIUS)
    compensated_vector = desired_vector_coeff * desired_speed - wind_orthogonal 
    return compensated_vector, desired_vector_coeff

request_speed, desired_speed_coeff = get_compensated_vector_and_desired_vector_coefficient(desired_speed, wind_speed, VECTOR_RADIUS)
 



# print results: 
print(wind_orthogonal)
print(desired_speed_coeff)
print(request_speed)
print(np.linalg.norm(request_speed))
