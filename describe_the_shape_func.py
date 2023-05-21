def describe_the_shape(angles):
    '''(replace s with number of sides and d with the measure of the interior angles).
    Angle measure should be floored to the nearest integer.
    Number of sides will be tested from 0 to 180.'''

    if angles < 3:
        return 'this will be a line segment or a dot'
    else:
        return f'This shape has {angles} sides and each angle measures {int(180 * (angles - 2) / angles)}'


assert (describe_the_shape(3)) == "This shape has 3 sides and each angle measures 60"

assert (describe_the_shape(2)) == "this will be a line segment or a dot"
assert (describe_the_shape(1)) == "this will be a line segment or a dot"
