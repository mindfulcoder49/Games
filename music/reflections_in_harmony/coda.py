from music21 import stream, chord

def create_coda():
    coda = stream.Part()

    # Create a final, calming section with repeating arpeggios
    arpeggio = [chord.Chord(["C4", "E4", "G4"], quarterLength=0.5),
                chord.Chord(["A4", "C5", "E5"], quarterLength=0.5)]
    
    for i in range(8):
        for c in arpeggio:
            coda.append(c)

    # End with a final chord
    coda.append(chord.Chord(["C4", "E4", "G4"], quarterLength=4))

    return coda
