Very basic image editing program in python.

How to download/install:
1) Click on the "<> Code" button and select "Download ZIP".
2) Extract the downloaded archive.
3) Open a terminal in the extracted folder and execute:
   (on Windows:) "python -m venv venv", followed by: "venv/Scripts/activate", followed by: "pip install -r requirements.txt".
   (on MacOS:) "python3 -m venv venv", followed by: "source venv/bin/activate", followed by: "pip install -r requirements.txt".
   (on Linux:) "python3 -m venv venv", followed by: "source venv/bin/activate", followed by: "pip install -r requirements.txt".

How to use:
1) copy-paste the pic you want to change into the same directory as "Edpic.sh"
2) execute Edpic.sh in a terminal
3) type the picture name (extension included)
4) select the editing mode:
   "shift": moves the picture's color components (warning! incomplete: it can go out-of-bounds)
   "scale": resizes the picture's color components (warning! incomplete: it can go out-of-bounds)
   "level": inverte le componenti dell'immagine
   "switch r g": switches red and green values
   "switch r b": switches red and blue values
   "switch g b": switches green and blue values
   "posterize": reduces colors
   "glasses": stained-glass effect
   "threshold": reduces colors to just black and white
5) select the name of the resulting image file (extension included)
The resulting file will be created in the same directory.

("trialpic.jpg" was only used for testing; you can remove it)
