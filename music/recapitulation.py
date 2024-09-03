from music21 import stream, note, chord, instrument

def create_recapitulation():
    # Initialize the section score
    recapitulation = stream.Score()
    piano1 = instrument.Piano()
    piano2 = instrument.Piano()

    # Recapitulation: return to the main theme with embellishments
    recap_part1 = stream.Part()
    recap_part1.insert(0, piano1)

    recap_melody = [
        note.Note('E4', quarterLength=1),  # Main theme
        note.Note('G4', quarterLength=1.5, ornaments=['trill']),  # Trill for embellishment
        note.Note('A4', quarterLength=0.5),
        note.Rest(quarterLength=1),
        note.Note('C5', quarterLength=1),
        note.Note('B4', quarterLength=1),
        note.Note('A4', quarterLength=1),
        note.Rest(quarterLength=1),
        note.Note('G4', quarterLength=0.5, ornaments=['grace']),  # Grace note
        note.Note('F4', quarterLength=0.5),
        note.Note('E4', quarterLength=1),
        note.Note('D4', quarterLength=1),
        note.Rest(quarterLength=0.5),
        note.Note('C4', quarterLength=0.5),
        note.Note('B3', quarterLength=1),
        note.Note('A3', quarterLength=1),
        note.Rest(quarterLength=1),
    ]

    recap_part1.append(recap_melody)

    recap_part2 = stream.Part()
    recap_part2.insert(0, piano2)

    # Fuller harmonic background
    recap_harmony = [
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
        chord.Chord(['A2', 'C3', 'E3'], quarterLength=2),
        chord.Chord(['F2', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['G2', 'B3', 'D4'], quarterLength=2),
        chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
        chord.Chord(['A2', 'C4', 'E4'], quarterLength=2),
        chord.Chord(['F2', 'A3', 'C4'], quarterLength=2),
        chord.Chord(['G2', 'B3', 'D4'], quarterLength=2),
    ]

    recap_part2.append(recap_harmony)

    # Add melody and accompaniment to the section score
    recapitulation.insert(0, recap_part1)
    recapitulation.insert(0, recap_part2)

    return recapitulation
