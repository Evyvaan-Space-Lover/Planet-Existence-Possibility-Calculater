import math
import tkinter as tink 

#Variables
mass = 0
radius = 0
G = float(6.67430e-11)  # gravitational constant in m^3 kg^-1 s^-2
g = 0 # Surface Gravity

root = tink.Tk()
root.title("Planet Maker")
root.geometry("830x650")

#heading
heading=tink.Label(root, text="Make your own Planet and Get scientific Data!", font=("Arial", 30))

frame1 = tink.Frame(root, width=400, height=300) # Input Frame
frame2 = tink.Frame(root, width=400, height=300) # Output Frame

# Input Labels and Entries
massLabel=tink.Label(frame1, text="Mass :", font=("Times New Roman", 20))
radiusLabel=tink.Label(frame1, text="Radius :", font=("Times New Roman", 20))
AvTempLabel=tink.Label(frame1, text="Average Temperature :", font=("Times New Roman", 20))

massEntry=tink.Entry(frame1,bg="lightgray", font=("Times New Roman", 20))
radiusEntry=tink.Entry(frame1,bg="lightblue", font=("Times New Roman", 20))
AvTempEntry=tink.Entry(frame1,bg="lightyellow", font=("Times New Roman", 20))

unitLabel1=tink.Label(frame1, text="x Earth's Mass", font=("Times New Roman", 8))
unitLabel2=tink.Label(frame1, text="x Earth's Radius", font=("Times New Roman", 8))
unitLabel3=tink.Label(frame1, text="K", font=("Times New Roman", 8))


# Output Labels
escapeVelocityLabel = tink.Label(frame2,bg="lightgray", text="Escape Velocity:", font=("Times New Roman", 20))
surfaceGravityLabel = tink.Label(frame2, bg="lightblue", text="Surface Gravity:", font=("Times New Roman", 20))
atmosphereLabel = tink.Label(frame2, bg="lightyellow", text="Type of Atmosphere:", font=("Times New Roman", 20))
# verdictLabel = tink.Label(frame2, bg="lightgreen", text="Verdict:", font=("Times New Roman", 24))
tempLabel = tink.Label(frame2, bg="lightpink", text="Temperature Classification:", font=("Times New Roman", 20))
massLabel1 = tink.Label(frame2, bg="lightgreen", text="Mass Classification:", font=("Times New Roman", 20))  

def EVcalc(massc, radiusc):
    escape_velocity= (math.sqrt((2 * G * massc) / radiusc))/1000
    return escape_velocity

def SGcalc(massc, radiusc):
    surface_gravity = (G * massc) / (radiusc ** 2)
    return surface_gravity 

def AtmosClassifier(escapevelocity, AvTemp):
    if escapevelocity <= 2:
        return "No Atmosphere"
    elif escapevelocity <= 5.5:
        if AvTemp>1000:
            return "Trace Amounts of Atmosphere"  
        return "Very Thin Atmosphere"
    elif escapevelocity <= 15.5:
        if AvTemp>1000:
            return "Thin Atmosphere"
        return "Earth Like Atmosphere"
    elif escapevelocity >= 15.5:
        if AvTemp>1000:
            return "Moderate Atmosphere"
        return "Thick Atmosphere"


def massClassifier(mass):
    if mass < (9.38*10**20):
        return "Asteroid like Object"
    elif mass < (1.66*10**22):
        return "Dwarf Planet"
    elif mass < (17*5.972e24):
        return "Terrestrial Planet"
    elif mass < (36*5.972e24):
        return "Super Earth"
    elif mass < (40*5.972e24):
        return "Ice Giant"
    else:
        return "Gas Giant like mass planet"
    
def tempClassifier(temp):
    if temp > 800:
        return "Hot"
    elif temp < 800 and temp >= 400:
        return "Not suitable for life"
    elif temp < 400 and temp >= 200:
        return "Temperate"
    elif temp < 200:
        return "Cold"

def Analyze():
    mass = float(massEntry.get()) * 5.972e24  # Convert Earth masses to kg
    radius = float(radiusEntry.get()) * 6.371e6  # Convert Earth radii to meters
    AvTemp = float(AvTempEntry.get())  # Average Temperature in Kelvin 
    escapevelocity = round(EVcalc(mass, radius), 2)
    surfacegravity = SGcalc(mass, radius)
    escapeVelocityLabel.config(text=f"Escape Velocity: {escapevelocity} km/s")
    surfaceGravityLabel.config(text=f"Surface Gravity: {round((surfacegravity/9.81), 2)} x Earth's Gravity or {round(surfacegravity, 3)} m/s²")
    atmosphereLabel.config(text=f"Atmosphere: {AtmosClassifier(escapevelocity, AvTemp)}")
    massClassification = massClassifier(mass)
    tempClassification = tempClassifier(AvTemp)
    tempLabel.config(text=f"Temperature Classification: {tempClassification}")
    massLabel1.config(text=f"Mass Classification: {massClassification}")
    # verdictLabel.config(text=f"Verdict: {tempClassification} {massClassification} with {AtmosClassifier(escapevelocity, AvTemp)}")

AnalyzeButton=tink.Button(root, text="Analyze Planet", font=("Comic Sans MS", 16), bg="red", command=Analyze)#i would have put it up with the other variables but the analyze function needs to be defined first

def InputGUIDraw():
    heading.grid()
    frame1.grid(row=1, column=0, pady=20)
    frame2.grid(row=3, column=0, pady=20)

    massLabel.grid(row=0, column=0, padx=10, pady=10)
    radiusLabel.grid(row=1, column=0, padx=10, pady=10)
    AvTempLabel.grid(row=2, column=0, padx=10, pady=10)

    massEntry.grid(row=0, column=1, padx=10, pady=10)
    radiusEntry.grid(row=1, column=1, padx=10, pady=10)
    AvTempEntry.grid(row=2, column=1, padx=10, pady=10)

    unitLabel1.grid(row=0, column=2, padx=10, pady=10)
    unitLabel2.grid(row=1, column=2, padx=10, pady=10)
    unitLabel3.grid(row=2, column=2, padx=10, pady=10)

    AnalyzeButton.grid(row=2, column=0, columnspan=2, pady=20)

def OutputGUIDraw():
    escapeVelocityLabel.grid(row=0, column=0, padx=10, pady=10)
    surfaceGravityLabel.grid(row=1, column=0, padx=10, pady=10)
    # verdictLabel.grid(row=3, column=0, padx=10, pady=10)
    atmosphereLabel.grid(row=2, column=0, padx=10, pady=10)
    tempLabel.grid(row=4, column=0, padx=10, pady=10)
    massLabel1.grid(row=5, column=0, padx=10, pady=10)

def main():
    InputGUIDraw()
    OutputGUIDraw()
    root.mainloop()


main()