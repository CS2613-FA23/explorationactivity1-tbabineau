[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1

## Package Information
The sample program Distortions.py demonstates the functionality of the [Pyhton wave library](https://docs.python.org/3/library/wave.html), which allows us to read, write and create .wav files.
## How to run the Distortions.py
To run the program, all you need is a .wav file you would like to distort. When the program starts, it will prompt the user to input the name of the file to distort (excluding the .wav extension). Once a file name that exists has been given, the user will be promped to distort the file by either reversing it, speeding it up or slowing it down by a factor given by the user. The new file will be written to with the users specifications and the user will select whether they would like to distort another file.
## What does Distortions.py do?
This program is a tool to speed up, slow down, and reverse WAV files without the need to download bulky audio software to do a simple operation. 
## Sample Input and Output
If I wanted to take a file called **Talking.wav**, reverse it and then speed it up by a multiple of 3, this is how I would interact with the program:

```
Enter the name of the WAV file you want to edit, excluding the .wav: Talking

re - reverse the input file
sl - slow down the input file
sp - speed up the input file
re

Done!
Would you like to edit another file? (y/n): y
Enter the name of the WAV file you want to edit, excluding the .wav: Talking_reversed

re - reverse the input file
sl - slow down the input file
sp - speed up the input file
sp
Enter the factor that the file should be sped up by: 3

Done!
Would you like to edit another file? (y/n): n
```

This would result in two files being added to the directory, Talking_reversed.wav, which is just the original file in reverse, and Talking_reversed_sped_up_3.0x.wav, which is the original file reversed and with a framerate 3 times higher than the original.
