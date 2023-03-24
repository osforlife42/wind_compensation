import pytest
import numpy as np
from wind_compensation_calcs import get_desired_speed_coefficient

@pytest.mark.parametrize("desired_dir_vector_tuple, orthogonal_vector_tuple, final_vector_size, expected_coeff" , 
                        [((4,0), (0,3), 5, 1), 
                        ((3,0), (0,4), 5, 1),
                        ((4,0), (0,6), 10, 2),
                        ((8,0), (0,3), 5, 0.5)])

def test_get_coeffient(desired_dir_vector_tuple, orthogonal_vector_tuple, final_vector_size, expected_coeff): 
    desired_dir_vector = np.array(desired_dir_vector_tuple)
    orthogonal_vector_tuple = np.array(orthogonal_vector_tuple)
    assert np.isclose(get_desired_speed_coefficient(desired_dir_vector, orthogonal_vector_tuple, final_vector_size), expected_coeff)



# testing shit: 
# request_speed_angle = np.arccos(np.linalg.norm(wind_orthogonal) / VECTOR_RADIUS)

# def get_rot_mat(theta): 
#     rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
#     return rot


# rotate_mat = get_rot_mat(request_speed_angle)
# request_speed_not_normalized = np.dot(rotate_mat, -wind_orthogonal)
# request_speed = VECTOR_RADIUS * request_speed_not_normalized / np.linalg.norm(request_speed_not_normalized)