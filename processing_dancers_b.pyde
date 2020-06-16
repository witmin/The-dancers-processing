canvas_width = 640
canvas_height = 800


def setup():
    size(canvas_width, canvas_height)
    background(255, 255, 255)


def draw():
    random_color_counter = random(1, 10)
    ellipse_size = random(2, 50)
    fill_translucent = random(10, 50)
    stroke_translucent = random(1, 100)
    
    # Toggle color by round
    colorMode(RGB)
    if (random_color_counter < 5 ):
        # fill in ellipse color
        fill(255, random(100, 120), random(145, 155), fill_translucent)
    else:
        # fill in bezier line color
        fill(255, random(10, 40), random(100, 120), fill_translucent)

         
    if mousePressed:
        # draw a ellipse
        strokeWeight(random(3))
        stroke(255, 255, 255, random(1, 100))
        ellipse(mouseX, mouseY, 10, 10)
        # draw a bezier shape
        noStroke()
        bezier(mouseX, mouseY, mouseX+random(-ellipse_size*2,ellipse_size*2), mouseY+random(-ellipse_size*2,ellipse_size*2), mouseX + random(-ellipse_size*2, ellipse_size*2), mouseY+random(-ellipse_size*2, ellipse_size*2), mouseX + random(-ellipse_size*2, ellipse_size*2), mouseY+random(-ellipse_size*2, ellipse_size*2))
        # draw a bezier line
        noFill()
        strokeWeight(random(0, 2))
        stroke(random(171, 182), random(170, 179), random(201, 211), stroke_translucent)
        bezier(mouseX, mouseY, mouseX+random(-ellipse_size-80,ellipse_size+80), mouseY+random(-ellipse_size-10,30), mouseX + random(10), mouseY+random(ellipse_size, ellipse_size*2), mouseX + random(-10, 0), mouseY+random(ellipse_size, ellipse_size*3))
        #change cursor mode 
        cursor(HAND)
    else: 
        cursor(ARROW)
    
            
def keyPressed():
    save("dancers.png")
    print("saved")
    
