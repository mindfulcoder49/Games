from music21 import stream, note

def create_first_theme():
    first_theme = stream.Part()

    # Create a repeating melodic motif with variations
    motif = [note.Note("G4", quarterLength=1), note.Rest(quarterLength=0.5), note.Note("E4", quarterLength=0.5)]

    for i in range(4):
        # Transpose motif each iteration to create a theme
        for n in motif:
            new_note = n.transpose(i)
            first_theme.append(new_note)

    return first_theme
