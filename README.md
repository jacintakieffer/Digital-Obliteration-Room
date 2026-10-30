# <ins>Digital Obliteration Room</ins> 

## Table of Contents

* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)

## General Information
* This project recreates the experience of Kusama's *Obliteration Room*, where visitors are given coloured dot stickers and gradually cover an all-white room. The purpose is to transform a blank space with colour, time and personal immersion
* My *Digital Obliteration Room* was designed to make Kusama's exhibit everlasting and more accessible. Instead of needing to travel to the physical and finite exhibit, users can now "obliterate" blank spaces with colour whenever they would like. 
* The purpose is to explore audience participation and how a space can be creatively changed through many small, repeated actions.
* My project gained even more purpose when finding out that Kusama unfortunately passed away as I was developing my sketches. The intention has now shifted to a tribute to Kusama, and her artistic joy that lives on in my *Digital Obliteration Room*.
* Multiple files have been attached to showcase the development of this project. **Trialling_rectangle_shapes_and_colours_** and **Trialling_interactive_circles** display earlier stages of the project. The correct and final file is named **Final_Digital_Obliteration_Room**.

## Technologies Used
* Processing - version 4.x using Python. 

## Features
* A background photo of the original *Obliteration Room* (pre-stickers) fills the canvas (1400 x 900).
* Six colour options to mimic the original exhibit (pink, red, orange, yellow, green, blue) are placed as rectangles in a column on the left.
* A white outline will indicate once a colour swatch has been selected.
* Once selected, the user can press anywhere on the room and a circle of that colour will appear.
* Each circle has a randomised diameter between 10 and 40 pixels.
* To clear the room and start again, press `C`. 

## Screenshots
#### Before:
<img width="740" height="489" alt="Screenshot 2026-10-29 at 9 32 07 am" src="https://github.com/user-attachments/assets/0bf7680f-8443-42f0-a834-3716591a805e" />

#### After:
<img width="739" height="489" alt="Screenshot 2026-10-29 at 9 33 39 am" src="https://github.com/user-attachments/assets/8faefd82-c82d-49f9-9fc1-c82949d2e3ac" />

## Setup
#### Requirements
* Must have [Processing](https://processing.org/download) downloaded with Python Mode installed.

#### Getting Started
1. Download image named **blank room.jpg** (located under data folder inside **Final_Digital_Obliteration_Room**)
2. Download or copy file named **Final_Digital_Obliteration_Room**
3. Open the `.pyde` file in Processing
4. Save it (Press `command` + `S`)
5. To ensure the image loads as the background: with Processing opened, on the menu bar select **Sketch**, **Add File...** and upload **blank room.jpg** . 
6. Press **Run**

## Usage
The overall idea is simple: **Select a colour, place a sticker (circle) of that colour**.

In more detail:
* Mouse click on coloured rectangle &rarr; White outline will appear to indicate that colour has been selected &rarr; Colour has been selected
* Mouse click anywhere on the blank room background &rarr; A circle of the selected colour will appear in a randomised size between a diameter of 10-40.
* Circles can be placed anywhere inside the room except for on top of the rectangle colour swatches. An endless amount of circles can be placed, and they may be layered on top of each other. (see [Screenshots](#screenshots) for reference)
* With this in mind, users can create any design they wish with circular shapes -- eg flowers, rainbows etc. 
* To clear all circles, press `C`

## Project Status
* Project is complete.

## Acknowledgements
* This project was inspired by Yayoi Kusama's exhibit *Obliteration Room*.
* **blank room.jpg**: Photographed by C Callistemon © QAGOMA <https://www.qagoma.qld.gov.au/stories/the-obliteration-room-by-yayoi-kusama-is-transformed/>
* This tutorial <https://processing.org/tutorials/interactivity> aided my project significantly. 
* Many thanks for reading and enjoy Obliterating your screen with colour!
  
