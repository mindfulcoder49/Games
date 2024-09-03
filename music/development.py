from music21 import stream, note, chord, instrument

def create_development():
    # Initialize the section score
    development = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Development section: combines motifs from A2 and B2 with modulation
    development_part1 = stream.Part()
    development_part1.insert(0, piano1)

    development_melody = [
        # Modulate through different keys with thematic development
        note.Note('E4', quarterLength=1),  # Motif from A2
        note.Note('G4', quarterLength=1.5),  # Augmentation of motif
        note.Note('B4', quarterLength=0.5),
        note.Note('D5', quarterLength=1, style='staccato'),
        note.Note('E5', quarterLength=0.5, style='staccato'),
        note.Note('C5', quarterLength=0.5),
        note.Rest(quarterLength=1),
        note.Note('A4', quarterLength=1),
        note.Note('C5', quarterLength=1.5, style='staccato'),
        note.Note('E5', quarterLength=0.5),
        note.Note('D5', quarterLength=1),
        note.Rest(quarterLength=0.5),
        note.Note('F4', quarterLength=0.5, style='staccato'),
        note.Note('A4', quarterLength=1),
        note.Note('G4', quarterLength=1),
        note.Rest(quarterLength=1),
        note.Note('B4', quarterLength=1),
        note.Note('D5', quarterLength=1, style='staccato'),
        note.Note('E5', quarterLength=1, style='staccato'),
        note.Note('F5', quarterLength=1, style='staccato'),
        note.Rest(quarterLength=1),
    ]

    development_part1.append(development_melody)

    development_part2 = stream.Part()
    development_part2.insert(0, piano2)

    # Chords supporting the modulation and dynamic shifts
    development_harmony = [
        chord.Chord(['E3', 'G3', 'B3'], quarterLength=2),
        chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['A2', 'C3', 'E3'], quarterLength=2),
        chord.Chord(['D3', 'F3', 'A3'], quarterLength=2),
        chord.Chord(['Bb2', 'D3', 'F3'], quarterLength=2),
        chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),
        chord.Chord(['Eb3', 'G3', 'Bb3'], quarterLength=2),
        chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),
    ]

    development_part2.append(development_harmony)

    # Add melody and accompaniment to the section score
    development.insert(0, development_part1)
    development.insert(0, development_part2)

    return development
