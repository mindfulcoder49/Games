from music21 import stream, chord

def create_climax():
    climax = stream.Part()

    # Series of powerful chords to build tension
    for i in range(6):
        c = chord.Chord(["C4", "E4", "G4", "C5"], quarterLength=1)
        c.transpose(i)
        climax.append(c)

    # Final resolving chord
    climax.append(chord.Chord(["F4", "A4", "C5"], quarterLength=4))

    return climax
