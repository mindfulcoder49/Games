from music21 import *
import random

def create_ethereal_chord():
    root = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
    chord_type = random.choice(['maj7', 'm7', 'sus4', 'add9'])
    return chord.Chord(f"{root}{chord_type}")

def create_melody_note(chord):
    chord_pitches = [p.nameWithOctave for p in chord.pitches]
    return note.Note(random.choice(chord_pitches))

def create_ethereal_song():
    song = stream.Score()
    
    # Create a piano part
    piano = instrument.Piano()
    piano_part = stream.Part()
    piano_part.insert(0, piano)
    
    # Create a flute part for melody
    flute = instrument.Flute()
    flute_part = stream.Part()
    flute_part.insert(0, flute)
    
    # Set tempo
    bpm = 60
    mm = tempo.MetronomeMark(number=bpm)
    piano_part.insert(0, mm)
    
    # Generate chords and melody
    for i in range(32):
        chord = create_ethereal_chord()
        piano_part.append(chord)
        
        for _ in range(4):
            melody_note = create_melody_note(chord)
            melody_note.quarterLength = 0.5
            flute_part.append(melody_note)
    
    song.insert(0, piano_part)
    song.insert(0, flute_part)
    
    return song

# Generate the song
ethereal_song = create_ethereal_song()

# Save as MIDI file
mf = midi.translate.streamToMidiFile(ethereal_song)
mf.open("ethereal_song.mid", 'wb')
mf.write()
mf.close()

print("Ethereal song has been created and saved as 'ethereal_song.mid'")