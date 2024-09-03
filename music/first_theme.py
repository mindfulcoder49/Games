from music21 import stream, note, chord, instrument

def create_first_theme():
    # Initialize the section score
    theme = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Create melody part for Piano 1
    melody_part = stream.Part()
    melody_part.insert(0, piano1)

    # First Theme melody in C major with some variations
    melody_notes = [
        note.Rest(quarterLength=1),  # Rest to give a breathing space
        note.Note('E4', quarterLength=1),  # E
        note.Note('G4', quarterLength=1),  # G
        note.Note('A4', quarterLength=1),  # A
        note.Rest(quarterLength=0.5),      # Short rest
        note.Note('E4', quarterLength=0.5),  # E
        note.Note('D4', quarterLength=1),  # D
        note.Note('C4', quarterLength=2),  # C
        # Additional melody lines
        note.Note('F4', quarterLength=1),  # F
        note.Note('G4', quarterLength=1),  # G
        note.Rest(quarterLength=1),        # Rest for variation
        note.Note('E4', quarterLength=0.5),  # E
        note.Note('F4', quarterLength=0.5),  # F
        note.Note('G4', quarterLength=1),  # G
        note.Note('C5', quarterLength=2),  # C (high)
    ]

    melody_part.append(melody_notes)

    # Create accompaniment for Piano 2
    accompaniment_part = stream.Part()
    accompaniment_part.insert(0, piano2)

    accompaniment_notes = [
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
        chord.Chord(['A2', 'E3', 'C4'], quarterLength=2),
        chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
    ]

    accompaniment_part.append(accompaniment_notes)

    # Add melody and accompaniment to the section score
    theme.insert(0, melody_part)
    theme.insert(0, accompaniment_part)

    return theme
