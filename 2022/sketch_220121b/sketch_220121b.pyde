MIN_RADIUS = 5
MAX_RADIUS = 200
CIRCLES = []

class PackedCircle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def display(self):
        ellipse(self.x, self.y, self.r * 2, self.r * 2)

    def is_colliding(self, circles):
        if self.x + self.r >= width or self.x - self.r < 0:
            return True
        if self.y + self.r >= height or self.y - self.r < 0:
            return True

        for circle in circles:
            center_dist = self.r + circle.r
            x_diff = self.x - circle.x
            y_diff = self.y - circle.y

            if center_dist >= sqrt(x_diff ** 2 + y_diff ** 2):
                return True
        return False

    def shrink(self, rate=1):
        self.r -= rate

    @property
    def too_small(self):
        return self.r < MIN_RADIUS


def setup():
    background(245)
    noFill()
    stroke(30)
    strokeWeight(3)
    size(600, 600)

def draw():
    attempts = 500

    while attempts:
        x, y = random(width), random(height)
        new_circle = PackedCircle(x, y, MAX_RADIUS)

        while not new_circle.too_small and new_circle.is_colliding(CIRCLES):
            new_circle.shrink()

        if not new_circle.too_small:
            new_circle.display()
            CIRCLES.append(new_circle)
            attempts = 0
        else:
            attempts -= 1

def keyPressed():
    saveFrame("output.png")
