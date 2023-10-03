import wave
def create_outfile(f_in, f_out):
    f_out.setnchannels(f_in.getnchannels())
    f_out.setsampwidth(f_in.getsampwidth())
    f_out.setnframes(f_in.getnframes())
    return f_out

def reverse(file_name):
    f_in = wave.open(file_name + ".wav", "rb")
    f_out = wave.open(file_name + "_reversed.wav", "wb")

    f_out = create_outfile(f_in, f_out)
    f_out.setframerate(f_in.getframerate())

    nframes = f_in.getnframes()
    frames = [0] * nframes

    for i in range(nframes):
        frames[-i] = f_in.readframes(1)

    for i in range(nframes):
        f_out.writeframes(frames[i])

    f_in.close()
    f_out.close()

def speedup(file_name, amount):
    if(amount == 0):
        amount = 1
    f_in = f_in = wave.open(file_name + ".wav", "rb")
    f_out = wave.open(file_name + "_sped_up_x" + str(amount) + ".wav", "wb")

    f_out = create_outfile(f_in, f_out)
    f_out.setframerate(f_in.getframerate() * amount)
    f_out.writeframes(f_in.readframes(-1))

    f_in.close()
    f_out.close()

def slow(file_name, amount):
    if(amount == 0):
        amount = 1
    f_in = f_in = wave.open(file_name + ".wav", "rb")
    f_out = wave.open(file_name + "_slowed_x " + str(amount) + ".wav", "wb")

    f_out = create_outfile(f_in, f_out)
    f_out.setframerate(f_in.getframerate() / amount)
    f_out.writeframes(f_in.readframes(-1))

    f_in.close()
    f_out.close()


while(True):
    fname = input("Enter the name of the WAV file you want to edit, excluding the .wav: ")

    try:
        correct = False
        while(not correct):
            print("\nre - reverse the input file")
            print("sl - slow down the input file")
            print("sp - speed up the input file")
            choice = input("").lower()

            if(choice == "re"):
                reverse(fname)
                correct = True
            elif(choice == "sl"):
                factor = int(input("Enter the factor that the file should be slowed by: "))
                slow(fname, factor)
                correct = True
            elif(choice == "sp"):
                factor = int(input("Enter the factor that the file should be sped up by: "))
                speedup(fname, factor)
                correct = True
            else:
                print("That is not a valid option, please pick a valid option")
    except:
        print("Invalid file name.")

    choice = input("Would you like to edit another file? (y/n): ").lower()
    if(choice == "n"):
        break