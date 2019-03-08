#!usr/bin/env python
#coding=utf-8

import pyaudio
import wave
import random
from datetime import datetime
import time
import datetime

class soundRandom:

    def randSound(self):
        fh = open("log.txt","w")

        #print('Press Ctrl-C to quit.')
        try:

            while True:
                random.seed(datetime.datetime.now())
                percentage_chance = random.uniform(0.0, 1.0)
        #print 'perc. chance =  ' + str(percentage_chance)
                chance = random.random()
                if chance < percentage_chance:
            #print 'if statement i chance = ' + str(chance)
            #define stream chunk
                    chunk = 1024

            #open a wav format music
                    f = wave.open( './smashingSound.wav', 'rb' )
            #instantiate PyAudio
                    p = pyaudio.PyAudio()
            #open stream
                    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                            channels = f.getnchannels(),
                            rate = f.getframerate(),
                            output = True)
            #read data
                    data = f.readframes(chunk)

            #play stream
                    while data:
                        stream.write(data)
                        data = f.readframes(chunk)
            #logtoafile
                    millis = int(round(time.time() * 1000))
                    t =str(millis)
                    fh.write("%s\n"%t)
                    fh.flush()
            #stop stream
                    stream.stop_stream()
                    stream.close()
            #close PyAudio
                    f.close()



                else:
                    time.sleep(random.randint(5,10)) #randomly wait to 5 to 20 seconds

            fh.close()
        except KeyboardInterrupt:
            print ('\n')
