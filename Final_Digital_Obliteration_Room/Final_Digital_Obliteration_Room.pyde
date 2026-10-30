#variables to remember the photo, the circles and the chosen colour
img = None
circles = []
chosenR = 0
chosenG = 0
chosenB = 0
hasColour = False
selected = -1   #which rectangle is chosen (-1 means none yet) and all colours are 0-5 (pink to blue)

def setup():
    global img

    #set the size of the canvas
    size(1400, 900)

    #input background image (photo of blank room)
    img = loadImage("blank room.jpg")
    img.resize(1400, 900)

def draw():
    #paint the background
    image(img, 0, 0)

    #draw every circle that has been placed
    for c in circles:
        fill(c[2], c[3], c[4])
        noStroke()
        ellipse(c[0], c[1], c[5], c[5])

    #create a pink rectangle
    fill(255, 70, 181)
    if selected == 0:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 20, 150, 100)

    #create a red rectangle
    fill(255, 3, 7)
    if selected == 1:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 170, 150, 100)

    #create an orange rectangle
    fill(255, 129, 3)
    if selected == 2:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 320, 150, 100)

    #create a yellow rectangle
    fill(255, 230, 3)
    if selected == 3:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 470, 150, 100)

    #create a green rectangle
    fill(0, 234, 80)
    if selected == 4:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 620, 150, 100)

    #create a blue rectangle
    fill(0, 168, 255)
    if selected == 5:
        stroke(255)
        strokeWeight(4)
    else:
        noStroke()
    rect(20, 770, 150, 100)

def mousePressed():
    global chosenR, chosenG, chosenB, hasColour, selected

    #only check the rectangles if the click is in the column
    if mouseX >= 20 and mouseX <= 170:

        #clicked the pink rectangle
        if mouseY >= 20 and mouseY <= 120:
            chosenR, chosenG, chosenB = 255, 70, 181
            hasColour = True
            selected = 0
            return

        #clicked the red rectangle
        if mouseY >= 170 and mouseY <= 270:
            chosenR, chosenG, chosenB = 255, 3, 7
            hasColour = True
            selected = 1
            return

        #clicked the orange rectangle
        if mouseY >= 320 and mouseY <= 420:
            chosenR, chosenG, chosenB = 255, 129, 3
            hasColour = True
            selected = 2
            return

        #clicked the yellow rectangle
        if mouseY >= 470 and mouseY <= 570:
            chosenR, chosenG, chosenB = 255, 230, 3
            hasColour = True
            selected = 3
            return

        #clicked the green rectangle
        if mouseY >= 620 and mouseY <= 720:
            chosenR, chosenG, chosenB = 0, 234, 80
            hasColour = True
            selected = 4
            return

        #clicked the blue rectangle
        if mouseY >= 770 and mouseY <= 870:
            chosenR, chosenG, chosenB = 0, 168, 255
            hasColour = True
            selected = 5
            return

    #otherwise, place a circle in the chosen colour
    if hasColour:
        #pick a random size for this circle
        diameter = random(10, 40)
        circles.append((mouseX, mouseY, chosenR, chosenG, chosenB, diameter))

def keyPressed():
    #press 'c' to clear the room and start again
    if key == 'c':
        del circles[:]
