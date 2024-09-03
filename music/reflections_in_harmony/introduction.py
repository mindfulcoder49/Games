from music21 import stream, note, chord

def create_introduction():
    introduction = stream.Part()
    
    # Define harmonic structure for the introduction
    harmony = ['C4', 'E4', 'G4', 'A4', 'C5']
    durations = [0.5, 0.5, 1, 1, 2]

    # Use loops to create an arpeggiated introduction
    for pitch in harmony:
        introduction.append(note.Note(pitch, quarterLength=0.5))

    # Adding chords to make it more interesting
    intro_chords = [chord.Chord(["C4", "E4", "G4"]), chord.Chord(["A4", "C5", "E5"])]
    for c in intro_chords:
        introduction.append(c)

    # Add final held chord for resolution
    introduction.append(chord.Chord(["F4", "A4", "C5"], quarterLength=4))

    return introduction
