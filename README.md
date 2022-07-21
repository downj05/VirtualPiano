# VirtualPiano
Virtual piano desktop application that uses the keyboard layout present in virtualpiano.net, ROBLOX and GMOD.
Uses soundfont (.sf2) files for its instruments allowing for a wide range of sounds.

![CMD line window](https://cdn.discordapp.com/attachments/588629635420520454/999546178398081085/unknown.png)

## Installation

### Installing via releases (easy way)

Go to the releases section
![Release Button](https://cdn.discordapp.com/attachments/588629635420520454/999543324501356646/unknown.png)
Download the 'release' zip folder
![Zip folder](https://cdn.discordapp.com/attachments/588629635420520454/999543688025866360/unknown.png)
Extract folder and run 'main.exe'
![Extracted zip file](https://cdn.discordapp.com/attachments/588629635420520454/999544006503575562/unknown.png)

### Installing via Python (hard way)

```bash
  git clone https://github.com/downj05/VirtualPiano.git
  cd VirtualPiano
  pip install -r requirements.txt
  python main.py
```
    
## Updating Soundfonts

Go to a soundfont repository such as https://sites.google.com/site/soundfonts4u/

Download a .sf2 file
![Downloaded sf2](https://cdn.discordapp.com/attachments/588629635420520454/999544745871294524/unknown.png)
Change path in settings file in the 'instrument' field (ensure there are no quotes on either end)
![Instrument field changed](https://cdn.discordapp.com/attachments/588629635420520454/999545599231807569/unknown.png)
Run program!
(Some .sf2 files may not work with the program)