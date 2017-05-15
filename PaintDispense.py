import pygame

# This is the algorithm that determines how much each each colorant value affects the RGB values.
def convert_rgb(color):
    redshift = 0
    greenshift = 0
    blueshift = 0
    for i in range(len(color)):
        if colors_chosen[i] == 'LB':
            redshift -= (colorants[color[i]]["OZ"] * 8) - (colorants[color[i]]["32nd's"] * .25)\
            - (colorants[color[i]]["64's"] * .2) - (colorants[color[i]]["128's"] * .1)

            greenshift -= (colorants[color[i]]["OZ"] * 8) - (colorants[color[i]]["32nd's"] * .25)\
            - (colorants[color[i]]["64's"] * .2) - (colorants[color[i]]["128's"] * .1)

            blueshift -= (colorants[color[i]]["OZ"] * 8) - (colorants[color[i]]["32nd's"] * .25)\
            - (colorants[color[i]]["64's"] * .2) - (colorants[color[i]]["128's"] * .1)
        if colors_chosen[i] == 'PG':
            redshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .15)\
            - (colorants[color[i]]["64's"] * .1) - (colorants[color[i]]["128's"] * .05)

            greenshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            blueshift -= (colorants[color[i]]["OZ"] * 4) - (colorants[color[i]]["32nd's"] * .125)\
            - (colorants[color[i]]["64's"] * .05) - (colorants[color[i]]["128's"] * .025)
        if colors_chosen[i] == 'PB':
            redshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .15)\
            - (colorants[color[i]]["64's"] * .1) - (colorants[color[i]]["128's"] * .05)

            greenshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .15)\
            - (colorants[color[i]]["64's"] * .1) - (colorants[color[i]]["128's"] * .05)

            blueshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)
        if colors_chosen[i] == 'YO':
            redshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            greenshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            blueshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .1)\
            - (colorants[color[i]]["64's"] * .05) - (colorants[color[i]]["128's"] * .025)

        if colors_chosen[i] == 'TW':
            redshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            greenshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25)\
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            blueshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25) \
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)
        if colors_chosen[i] == 'RO':
            redshift += (colorants[color[i]]["OZ"] * 8) + (colorants[color[i]]["32nd's"] * .25) \
            + (colorants[color[i]]["64's"] * .2) + (colorants[color[i]]["128's"] * .1)

            greenshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .25)\
            - (colorants[color[i]]["64's"] * .2) - (colorants[color[i]]["128's"] * .1)

            blueshift -= (colorants[color[i]]["OZ"] * 6) - (colorants[color[i]]["32nd's"] * .25)\
            - (colorants[color[i]]["64's"] * .2) - (colorants[color[i]]["128's"] * .1)

    # Here we round the final shift variables so they can convert into an RGB value to make a color.
    redshift = int(round(redshift))
    greenshift = int(round(greenshift))
    blueshift = int(round(blueshift))
    total_shift = (redshift, greenshift, blueshift)
    return total_shift






# This function converts the smaller units into bigger ones in order to fit the proper formula label format.
# <------------------------------------- If you add more colorants this function needs to be updated
def format_label(color):
    if colorants[color]["128's"] > 1:
        x = divmod(colorants[color]["128's"], 2)
        colorants[color]["64's"] += x[0]
        colorants[color]["128's"] = x[1]
    if colorants[color]["64's"] > 1:
        x = divmod(colorants[color]["64's"], 2)
        colorants[color]["32nd's"] += x[0]
        colorants[color]["64's"] = x[1]
    if colorants[color]["OZ"] % 2 == 1:
        colorants[color]["OZ"] = colorants[color]["OZ"] - 1
        colorants[color]["32nd's"] += 32
    if colorants[color]["32nd's"] > 63:
        x = divmod(colorants[color]["32nd's"], 32)
        if x[0] > 1:
            colorants[color]["OZ"] += x[0]
            colorants[color]["32nd's"] = x[1]
    if colorants[color]["OZ"] %2 == 1:
        if colorants[color]["OZ"] % 2 == 1:
            colorants[color]["OZ"] = colorants[color]["OZ"] - 1
            colorants[color]["32nd's"] += 32

# This function prints the final formula label
# <------------------------------------- If you add more colorants this function needs to be updated
def total_formula():
    print('\t  OZ   32  64  128')
    print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[0]]) % colors_chosen[0])
    if len(colors_chosen) > 1:
        print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[1]]) % colors_chosen[1])
    if len(colors_chosen) > 2:
        print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[2]]) % colors_chosen[2])
    if len(colors_chosen) > 3:
        print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[3]]) % colors_chosen[3])
    if len(colors_chosen) > 4:
        print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[4]]) % colors_chosen[4])
    if len(colors_chosen) > 5:
        print("%s\t  {OZ}   {32nd's}    {64's}   {128's}".format(**colorants[colors_chosen[5]]) % colors_chosen[5])

# This function adds the input amount of colorant into the total formula
def shoot(col, oz, thirtySeconds, sixtyFourths, oneTwentyEighths):
    col["OZ"] += oz
    col["32nd's"] += thirtySeconds
    col["64's"] += sixtyFourths
    col["128's"] += oneTwentyEighths

# Initialized variables
colorants ={
'LB': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0},
'PG': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0},
'PB': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0},
'YO': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0},
'TW': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0},
'RO': {"OZ": 0, "32nd's": 0, "64's": 0, "128's": 0}
}
colors_chosen = []

r = 255
g = 255
b = 255


shoot_again = True
# While loop takes color and amount input until the user decides they are finished adding colorant.
while shoot_again == True:
    colorant_choice = input("Please choose a color: [LB, PG, PB, YO, TW, RO]")
    recent_choice = colorant_choice
    if colorant_choice not in colorants:
        continue
    oz = int(input("Please input ounces or type 0 to move on."))
    thirtySeconds = int(input("Please input 32's, or type 0 to move on."))
    sixtyFourths = int(input("please input 64's, or type 0 to move on."))
    oneTwentyEighths = int(input("Please input 128's or type 0 to move on."))
    if colorant_choice not in colors_chosen:
        colors_chosen.append(colorant_choice)
    while shoot_again == True:
        again = input("Would you like to add any more? Y/N")
        if again == 'Y':
            shoot_again = True
            break
        elif again == 'N':
            shoot_again = False
            break
        else:
            print("I did not understand that input. Try again.")
            continue

    shoot(colorants[recent_choice], oz, thirtySeconds, sixtyFourths, oneTwentyEighths)

for i in range(len(colors_chosen)):
    format_label(colors_chosen[i])

rgb = convert_rgb(colors_chosen)

r += rgb[0]
g += rgb[1]
b += rgb[2]

if r > 255:
    r = 255
elif r < 0:
    r = 0

if g > 255:
    g = 255
elif g < 0:
    g = 0

if b > 255:
    b = 255
elif b < 0:
    b = 0

match_color = (r, g, b)
total_formula()

# Screen display stuff here
screen = pygame.display.set_mode((700, 500))
screen.fill(match_color)
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

