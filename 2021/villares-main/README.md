<!--**username/username** is a āØ _special_ āØ repository because its `README.md` (this file) appears on your GitHub profile.-->
### Hi there š

<img src="https://abav.lugaralgum.com/sketch-a-day/2020/sketch_2020_09_17deque/sketch_2020_09_17deque.gif">

> This animation is made with points in a Python collections.deque data structure, added by dragging the mouse in Processing Python mode (code shown bellow)
- š­ I'm currently working on a PhD at Unicamp
- š± Iām currently learning how not to talk too much and concentrate
- šÆ Iām looking to collaborate on open resources to teach programming in a visual context
- š¬ Ask me about drawing with Python!
- š« How to reach me: [twitter.com/villares](https://twitter.com/villares)
- š Pronouns: he/him
- ā” Fun fact: I think I actually need a repo named *villares* to store some [code](https://github.com/villares/villares).

```python
from collections import deque

h = deque([(0, 0)], 300) # mouse drag position history

def setup():
    size(500, 500)
    noStroke()
    colorMode(HSB)

def draw():
    background(51)
    for i, (x, y) in enumerate(h):
        fill(i, 255, 255, 255 / 2)
        circle(x, y, i / 5)
    h.append(h.popleft())

def mouseDragged():
    h.append((mouseX, mouseY))
```
