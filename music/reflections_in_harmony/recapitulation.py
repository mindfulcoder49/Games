from music21 import stream, note

def create_recapitulation():
    recapitulation = stream.Part()

    # Return to the first theme with some variation
    motif = [note.Note("G4", quarterLength=1), note.Rest(quarterLength=0.5), note.Note("E4", quarterLength=0.5)]

    for i in range(4):
        for n in motif:
            new_note = n.transpose(-i)
            recapitulation.append(new_note)

    # Modulate back to the original key
    for i in range(4, 0, -1):
        for n in motif:
            new_note = n.transpose(i)
            recapitulation.append(new_note)

    return recapitulation
