from music21 import stream, note, chord, instrument

def create_climax():
    # Initialize the section score
    climax = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Climax section: intense, powerful, using unison and octave doubling
    climax_part1 = stream.Part()
    climax_part1.insert(0, piano1)

    climax_melody = [
        note.Note('C5', quarterLength=1),  # Unison with octave doubling
        note.Note('E5', quarterLength=1),
        note.Note('G5', quarterLength=1),
        note.Note('C6', quarterLength=1),
        note.Rest(quarterLength=0.5),
        note.Note('G5', quarterLength=0.5),
        note.Note('F5', quarterLength=1),
        note.Note('E5', quarterLength=0.5),
        note.Note('D5', quarterLength=0.5),
        note.Rest(quarterLength=0.5),
        note.Note('C5', quarterLength=0.5),
        note.Note('B4', quarterLength=1),
        note.Note('A4', quarterLength=1, style='staccato'),
        note.Note('G4', quarterLength=1, style='staccato'),
        note.Rest(quarterLength=0.5),
        note.Note('F4', quarterLength=0.5),
        note.Note('E4', quarterLength=1),
    ]

    climax_part1.append(climax_melody)

    climax_part2 = stream.Part()
    climax_part2.insert(0, piano2)

    # Full chords and octave runs
    climax_harmony = [
        chord.Chord(['C3', 'G3', 'C4', 'E4'], quarterLength=2),
        chord.Chord(['F3', 'A3', 'C4', 'F4'], quarterLength=2),
        chord.Chord(['G3', 'B3', 'D4', 'G4'], quarterLength=2),
        chord.Chord(['C4', 'E4', 'G4', 'C5'], quarterLength=2),
        chord.Chord(['A3', 'C4', 'E4', 'A4'], quarterLength=2),
        chord.Chord(['D3', 'F4', 'A4', 'D5'], quarterLength=2),
        chord.Chord(['G3', 'B4', 'D5', 'G5'], quarterLength=2),
    ]

    climax_part2.append(climax_harmony)

    # Add melody and accompaniment to the section score
    climax.insert(0, climax_part1)
    climax.insert(0, climax_part2)

    return climax
