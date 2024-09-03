from music21 import stream, note, chord, instrument

def create_second_theme():
    # Initialize the section score
    second_theme = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Create melody part for Piano 1
    melody_part = stream.Part()
    melody_part.insert(0, piano1)

    # Rhythmic and energetic theme in A minor
    melody_notes = [
        note.Rest(quarterLength=1),  # Rest for a dramatic start
        note.Note('A4', quarterLength=1, style='staccato'),  # Staccato articulation
        note.Note('C5', quarterLength=0.5, style='staccato'),
        note.Note('E5', quarterLength=0.5),
        note.Note('A4', quarterLength=1),  # Return to A
        note.Rest(quarterLength=0.5),  # Short rest
        note.Note('G4', quarterLength=0.5),
        note.Note('F4', quarterLength=1),
        note.Rest(quarterLength=1),  # Dramatic pause
        note.Note('E4', quarterLength=0.5, style='staccato'),
        note.Note('C4', quarterLength=0.5, style='staccato'),
        note.Note('A4', quarterLength=1),
        note.Rest(quarterLength=0.5),
        note.Note('G4', quarterLength=0.5),
        note.Note('A4', quarterLength=1),
        note.Note('C5', quarterLength=1),
        note.Note('E5', quarterLength=1),
        note.Note('A5', quarterLength=1),
        note.Rest(quarterLength=1),
    ]

    melody_part.append(melody_notes)

    # Accompaniment part for Piano 2
    accompaniment_part = stream.Part()
    accompaniment_part.insert(0, piano2)

    # Cross-rhythms and off-beat accents
    accompaniment_notes = [
        chord.Chord(['A2', 'E3', 'A3'], quarterLength=2, style='staccato'),
        chord.Chord(['C3', 'G3', 'E4'], quarterLength=2),
        chord.Chord(['E3', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['F2', 'A3', 'D4'], quarterLength=2, style='staccato'),
        chord.Chord(['G2', 'B3', 'D4'], quarterLength=2),
        chord.Chord(['A2', 'C3', 'E4'], quarterLength=2),
        chord.Chord(['E2', 'G3', 'C4'], quarterLength=2, style='staccato'),
        chord.Chord(['A2', 'C4', 'E4'], quarterLength=2),
    ]

    accompaniment_part.append(accompaniment_notes)

    # Add melody and accompaniment to the section score
    second_theme.insert(0, melody_part)
    second_theme.insert(0, accompaniment_part)

    return second_theme
