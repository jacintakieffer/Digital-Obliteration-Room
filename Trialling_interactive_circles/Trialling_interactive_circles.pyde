
# 1. Define 6 specific colours using RGB values
COLOURS = [
    (255,70, 181),    # Pink
    (255, 3, 7),      # Red
    (255, 129, 3),    # Orange
    (255, 230, 3),    # Yellow
    (0, 234, 80),     # Green
    (0, 168, 255)     # Blue
]

def setup():
    size(1300, 800)
    background(255)
    noStroke()

def draw():
    pass

def mousePressed():
    # 2. Pick a random colour from the list
    # int(random(6)) picks a whole number index from 0 to 5
    random_index = int(random(len(COLOURS)))
    chosen_colour = COLOURS[random_index]
    
    # 3. Apply the chosen RGB colour
    fill(chosen_colour[0], chosen_colour[1], chosen_colour[2])
    
    # 4. Keep the random size element (between 10 and 150 pixels)
    d = random(10, 150)
    
    # 5. Draw the circle
    circle(mouseX, mouseY, d)
    

    
      
