# Library info
The library that was selected for this assignment was Python's wave library.
This library allows for .wav files to be written to and read from frame by frame. Each frame is written as a binary value that represents the sound to be played during said frame.

The github repository supplied for the library dates the first commit as being February 15th 1994 by the user gvanrossum, the creator of python [[ref]](https://github.com/python/cpython/commits/3.12?after=ef4bd1b57ff2b0a908149d178b0b1fbdf9f7e247+34&branch=3.12&path%5B%5D=Lib&path%5B%5D=wave.py&qualified_name=refs%2Fheads%2F3.12)

# Library Functionalities
The wave library can be split into two pieces, one portion for reading from files and one for writing to them. The most important function being the `open()`, which opens the file stream.
Open takes two arguments, the name of the file, and the mode that the file is being opened in.
```
f_in = wave.open("input.wav", "rb")
f_out = wave.open("output.wav", "wb")
```
`f_in` becomes the read only file object for `input.wav`, if it exists, as it was opened in read only mode. `f_out` becomes the write only file object for a newly created file `output.wav`. If the file already exists, it will be replaced by `f_out`. [[ref]](https://docs.python.org/3/library/wave.html)

Some other functions we can do on the files are:
```
f_in.getnchannels()
f_out.setnchannels(n)
```
These get and set the number of channels for the track, 1 for mono and 2 for stereo. [[ref]](https://docs.python.org/3/library/wave.html)
```
f_in.getsamplewidth()
f_out.setsamplewidth(n)
```
These get and set the sample width, which is how many bytes will make up one frame. [[ref]](https://docs.python.org/3/library/wave.html)
```
f_in.getnframes()
f_out.setnframes(n)
```
These get and set the number total frames in the file. For output files, this can be overwritten if a different number of frames are written to the file than specified. [[ref]](https://docs.python.org/3/library/wave.html)
```
f_in.getframerate()
f_out.setframerate(n)
```
These get and set the framerate of the file, or the number of frames per second to be played by the file. [[ref]](https://docs.python.org/3/library/wave.html) This is also known as the sampling rate, and the rate used by audio CD's is 44100. [[ref]](https://manual.audacityteam.org/man/sample_rates.html)

All of these function calls can be replaced by one, `setparams()`, which takes the number of channels, the sample width, the framerate, the number of frames, the compression type and a string descibing the compression type, as a tuple. For the compression type, the only one that is supported right now is NONE [[ref]](https://docs.python.org/3/library/wave.html), and the description is unimportant as a result so any string will do. The version of this function for the read only file objects is `getparams()`, which returns a tuple with all the parameters. This means that if you were looking to create a file with the same parameters as the input, you could simply use `f_out.setparams(f_in.getparams())`.

The two most important functions in the library are `readframes(n)` and `writeframes(n)`. readframes reads the specified number of frames and returns them as a bytes object. Passing a -1 to readframes will cause it to read in all available frames from the file [[ref]](https://docs.python.org/3/library/wave.html). writeframes takes in any bytes-like object and writes it to the output file as frames based on the sample size of the file.

# Personal Reflection
I selected this library for the exploration activity as I have worked with acessing text files and raw data through programming, but that was all text-based. I thought it was very interesting to work with a library that can create files that we can hear rather than just read. I had initially planned to create music or something similar with the library, however it is less messy to use files that already exist as a starting point.

Learning this library has influenced my learning of python as it has taught me to fully read the documentation to decide which functions are best for whatever operation I want to do, as many have similar results but differ in some key aspects. Originally, when reading through the library, I thought that using setparams() would be perfect for what I planned on doing. However, that would have caused me to repeat multiple statements as each output file had the same sample width, number of channels and number of frames. With an all in one function like setparams(), it made the code look better but it impacted readability and refactoring. In this scenario it was better for me to have a custom function that set the values that were the same between both files, and then I could put in the unique values like framerate without repetition of code.

My experience with the wave library overall was good, it was easy to use once I had read through the documentation, and the documentation itself was easy to follow. I would only reccomend this library to someone doing something similar to me or to check out because it was neat, as I cannot think of any other real world applications for something like this other than what I explored and possibly creating music if someone where looking to put in a fair amount of work to figure it out. Additionally, I do not see myself using this language again. While I did enjoy working with it and I was excited to get my program working, the library is quite specialized and again I cannot see another scenario that it would be benificial for me to use this language. 
