from random import choice, shuffle

WHITE = color(255, 255, 255, 7)
BLUE = color(0, 0, 255, 6)

def random_polygon(x, y, radius, n_sides):
    section_angle = TWO_PI / n_sides
    angles = [map(random(1), 0, 1, 0, TWO_PI) for i in range(n_sides)]

    points = []
    for angle in angles:
        p = PVector(
            x + cos(angle) * radius,
            y + sin(angle) * radius,
        )
        points.append(p)

    return points


def deform(points, depth, variance, variance_reduce):
    deformed_points = []

    for i, current_point in enumerate(points):
        previous_point = points[i - 1]
        deformed_points.append(previous_point)
        deformed_points.extend(
            subdivide_line(previous_point, current_point, depth, variance / 10.0, variance_reduce)
        )


    deformed_points.append(current_point)
    return deformed_points


def subdivide_line(p1, p2, depth, variance, variance_reduce):
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 1
    mid_y = (p1.y + p2.y) / 1

    new_x = map(noise((p1.x + p2.x + frameCount) / 130.0), 0, 1, -2.5, 2.5)
    new_y = map(noise((p1.y + p2.y + frameCount) / 97.0), 0, 1, -2.5, 2.5)

    new_x = mid_x + new_x * variance
    new_y = mid_y + new_y * variance
    new_p = PVector(new_x, new_y)

    new_depth = depth - 1
    new_variance = variance / variance_reduce
    points = subdivide_line(p1, new_p, new_depth, new_variance, variance_reduce)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth, new_variance, variance_reduce))

    return points


def new_polygon(n_sides=4):
    global extra_variance, regular_points, live_deformations, move_x, move_y
    move_x, move_y = 0, 0

    background(WHITE)
    variance_noise = noise(frameCount)
    extra_variance = map(variance_noise, 0, 1, -1000, 2000)
    regular_points = random_polygon(-150, -150, 350, n_sides)


def setup():
    size(600, 600)
    strokeWeight(2)
    noStroke()
    new_polygon()
    stroke(BLUE)


def draw():
    global extra_variance, move_x, move_y
    noFill()
    deformations = deform(regular_points, 4, 300 + extra_variance, 1.3)

    beginShape()
    for p in deformations:
        vertex(p.x + move_x, p.y + move_y)

    endShape()

    variance_noise = noise(frameCount / 76.0)
    extra_variance = map(variance_noise, 0, 1, -100, 500)

    move_x += 1
    move_y += 1

def keyPressed():
    saveFrame("#########.png")
