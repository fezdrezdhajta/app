### GUI imports
from guizero import *
from mares_main_appka import *

### GUI functions
def cml():
   try:
        weight = float(txtbox_weight.value)
        af = float(txtbox_af.value)
        cml = cml1(weight, af)
        text_welcome.value = f"Tvoje cml je {cml} kcal"
   except ValueError:
        text_welcome.value = "Zadej platná čísla"  

### GUI App
app = App(title="My App", width=775, height=650)


   

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Please enter your activity factor for today:"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

button = PushButton(window1, command = cml, text ="vypocitej")
app.display()

