import math


def reflection(node, dimensions_, distance):
    mirrored_points = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance // dimensions_[i]) - 1, (distance // dimensions_[i] + 2)):
            points.append(get_mirror(j, node[i], dimensions_[i]))
        mirrored_points.append(points)
    return mirrored_points


def get_mirror(mirror, coordinates, dimensions_):
    result = coordinates
    mirror_rotation = [2 * coordinates, 2 * (dimensions_ - coordinates)]
    if mirror < 0:
        for i in range(mirror, 0):
            result -= mirror_rotation[(i + 1) % 2]
    else:
        for i in range(mirror, 0, -1):
            result += mirror_rotation[i % 2]
    return result


def solution(dimensions, your_position, guard_position, distance):
    mirrored_points = [reflection(your_position, dimensions,
                                  distance), reflection(guard_position, dimensions, distance)]
    result = set()
    angles_dist = {}
    for i in range(0, len(mirrored_points)):
        for j in mirrored_points[i][0]:
            for k in mirrored_points[i][1]:
                angle = math.atan2((your_position[1] - k), (your_position[0] - j))
                traveled = math.hypot(your_position[0] - j, your_position[1] - k)
                if [j, k] != your_position and distance >= traveled:
                    if (angle in angles_dist and angles_dist[angle] > traveled) or angle not in angles_dist:
                        if i == 0:
                            angles_dist[angle] = traveled
                        else:
                            angles_dist[angle] = traveled
                            result.add(angle)
    return len(result)
