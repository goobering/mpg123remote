# This thing is dumb as a box of rocks. It just flings pretty much anything
# at mpg123 and lets it raise whatever errors it likes. It does seem to work, however. 

import pipes
import tempfile
import os
    
__fifo = tempfile.NamedTemporaryFile()
fifo = __fifo.name
__fifo.close()

# LOAD/L <trackname>: load and start playing resource <trackname>
def load(pathtofile):
    runcommand('echo load ' + pathtofile)

# LOADPAUSED/LP <trackname>: load but do not start playing resource <trackname>
def loadPaused(pathtofile):
    runcommand('echo loadpaused ' + pathtofile)
        
# LOADLIST <entry> <url>: load a playlist from given <url>, and display its entries, 
# optionally load and play one of these specificed by the integer <entry> 
# (<0: just list, 0: play last track, >0:play track with that position in list)
# Defaults to 1/play list from track in position 1
def loadList(pathtofile, entry = 1):  
    runcommand('echo loadlist ' + str(entry) + ' ' + pathtofile)
        
# PAUSE/P: pause playback
def pause():
    runcommand('echo pause')  

# STOP/S: stop playback (closes file)
def stop():
    runcommand('echo stop')
        
# JUMP/J <frame>|<+offset>|<-offset>|<[+|-]seconds>s: 
# jump to mpeg frame <frame> or change position by offset,
# same in seconds if number followed by "s"
def jump(jumpvalue):
    runcommand('echo jump ' + str(jumpvalue))
        
# VOLUME/V <percent>: set volume in % (0..100...); float value
def volume(volumevalue):
    runcommand('echo volume ' + str(volumevalue))
        
# RVA (Relative Volume Adjustment) off|(mix|radio)|(album|audiophile): set rva mode
def rva(rvavalue):
    runcommand('echo rva ' + rvavalue)
        
# EQ/E <channel> <band> <value>: set equalizer value for frequency band 0 to 31
# on channel 1 (left) or 2 (right) or 3 (both). Function defaults to 3/both.
def eq(band, value, channel = 3):
    runcommand('echo ' + str(channel) + ' ' + str(band) + ' ' + str(value))
        
# EQFILE <filename>: load EQ settings from a file
def eqfile(pathtofile):
    runcommand('echo eqfile ' + pathtofile)

# SHOWEQ: show all equalizer settings (as <channel> <band> <value> lines in a SHOWEQ block (like TAG))
def showeq():
    runcommand('echo showeq')
        
# SEEK/K <sample>|<+offset>|<-offset>: jump to output sample position <samples> or change position by offset
def seek(seekvalue):        
    runcommand('echo seek ' + seekvalue)
        
# SCAN: scan through the file, building seek index        
def scan():
    runcommand('echo scan')
    
# SAMPLE: print out the sample position and total number of samples
def sample():
    runcommand('echo scan')

# SEQ <bass> <mid> <treble>: simple eq setting...   
def seq(seqvalue):
    runcommand('echo ' + seqvalue)

# PITCH <[+|-]value>: adjust playback speed (+0.01 is 1 % faster)
def pitch(pitchvalue):
    runcommand('echo ' + pitchvalue)
        
# SILENCE: be silent during playback (meaning silence in text form)
def silence():
    runcommand('echo silence')

# STATE: Print auxiliary state info in several lines (just try it to see what info is there).
def state():
    runcommand('echo state')
    
# TAG/T: Print all available (ID3) tag info, for ID3v2 that gives output of all collected text fields, 
# using the ID3v2.3/4 4-character names.    
def tag():    
    runcommand('echo tag')
    
def quit():
    runcommand('echo quit')
    
def runcommand(command):
    t = pipes.Template()
    t.append(command, '--')
    f = t.open(fifo, 'w')
    f.close()
