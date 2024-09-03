from music21 import stream, note, chord, instrument

def create_coda():
    # Initialize the section score
    coda = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Coda: tranquil and reflective ending
    coda_part1 = stream.Part()
    coda_part1.insert(0, piano1)

    coda_melody = [
        note.Rest(quarterLength=1),
        note.Note('C4', quarterLength=2),  # Return to the introductory theme
        note.Note('E4', quarterLength=1.5),
        note.Note('G4', quarterLength=0.5, ornaments=['grace']),  # Grace note for gentle closure
        note.Note('A4', quarterLength=1),
        note.Rest(quarterLength=0.5),
        note.Note('F4', quarterLength=0.5),
        note.Note('E4', quarterLength=1),
        note.Note('D4', quarterLength=1),
        note.Note('C4', quarterLength=2),  # Gentle ending note
    ]

    coda_part1.append(coda_melody)

    coda_part2 = stream.Part()
    coda_part2.insert(0, piano2)

    # Soft, arpeggiated patterns for a reflective backdrop
    coda_harmony = [
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
        chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['G2', 'B3', 'D4'], quarterLength=2),
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
    ]

    coda_part2.append(coda_harmony)

    # Add melody and accompaniment to the section score
    coda.insert(0, coda_part1)
    coda.insert(0, coda_part2)

    return coda
