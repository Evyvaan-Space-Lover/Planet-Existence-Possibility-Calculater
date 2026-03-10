# Planet Existence Possibility Simulator

## Overview

The **Planet Existence Possibility Simulator** is a small scientific tool written in Python that estimates whether a planet can realistically exist based on several physical parameters. The program evaluates planetary characteristics such as **mass, radius, temperature, and atmosphere type**, and computes derived properties like **surface gravity**.

The goal of the simulator is **educational**: it helps users explore how different planetary properties influence whether a planet could form and remain stable. Rather than giving a definitive answer, the simulator provides **calculated values and scientific indicators** that help users reason about planetary conditions.

---

## Purpose

This project was created to demonstrate how **basic planetary physics** can be applied in a simple computational model. It allows users to experiment with different planetary parameters and observe how those values affect gravitational strength and atmospheric retention.

The simulator is intended for:

* students learning basic astronomy or physics
* experimentation with planetary parameters
* educational demonstrations of planetary properties

---

## Features

* Graphical User Interface (GUI) built with **Tkinter**
* Input fields for planetary properties
* Calculation of **surface gravity**
* Atmospheric condition options (Trace, Thin, Thick, etc.)
* Scientific feedback based on provided parameters
* Simple and easy-to-use interface

---

## Parameters Used

### Planet Mass

The total mass of the planet. Larger mass increases gravitational attraction.

### Planet Radius

The distance from the planet’s center to its surface. Larger radius decreases surface gravity.

### Surface Temperature

Used to estimate whether atmospheric gases could remain bound to the planet.

### Atmosphere Type

A qualitative description of the planet’s atmospheric density.

---

## Physics Used

The simulator uses the standard **surface gravity equation**:

g = GM / R²

Where:

* **G** = gravitational constant
* **M** = planetary mass
* **R** = planetary radius

This value determines how strongly the planet pulls objects toward its surface.

---

## Limitations

This simulator is **not a full planetary formation model**. It uses simplified assumptions and does not simulate:

* planetary formation processes
* orbital dynamics
* stellar radiation models
* atmospheric chemistry
* geological evolution

The tool is intended for **conceptual exploration**, not precise scientific prediction.

---

## How to Run

1. Ensure Python 3 is installed.
2. Download or clone the project files.
3. Navigate to the project directory.
4. Run the program:

python planet_existence_possibility_calculator.py

The GUI window will open and allow you to enter planetary parameters.

---

## Example Use Cases

Users can test questions such as:

* What happens if a planet has **high mass but small radius**?
* How does **surface gravity change with size**?
* Why do some planets struggle to retain atmospheres?

---

## Future Improvements

Possible improvements include:

* atmospheric escape calculations
* star distance and habitable zone modeling
* graphical data visualization
* support for additional planetary parameters

---

## Author

Created by **Evyvaan Singh** as a learning project exploring planetary physics and computational modeling.

---

## License

This project is intended for **educational use** and experimentation.
