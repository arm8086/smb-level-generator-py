# smb-level-generator-py
Automatically generates SMB games and plays them in Mesen.

This python script comes with both the Mesen emulator and Level-Headed built in to both generate the games, and run them.
The GitHub links for both projects will be below:

Level-Headed: https://github.com/Coolcord/Level-Headed

Mesen: https://github.com/SourMesen/Mesen

# Build Instructions
Requisities:
1. Python 3+
2. PyInstaller (optional)

1. Download all the files (smbgen.py, names.json, namegen.py)
2. Download the preconfigured Mesen and Level-Headed.
3. Move them to the same folder as you stored the 3 files.
4. (a) if you just want to run it via python, then run smbgen.py.
   (b) if you wanted to build it to an exe, follow the next steps
5. Build the smbgen.py file in PyInstaller as one file
6. Move the names.json into the same folder as the new EXE file.
7. Move the preconfigured Mesen and Level-Headed to the same directory as the EXE file.
8. Now you can double click the EXE file to launch it. Windows may give you a little virus warning, but ignore it.
END OPTIONAL INSTRUCTIONS
5. Mesen should launch with the game.

Sorry if the build instructions are confusing, I'm not good with these things.
