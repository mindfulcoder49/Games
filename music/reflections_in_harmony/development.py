from music21 import stream, note

def create_development():
    development = stream.Part()

    # Take motifs from the first and second themes and develop them
    motif1 = [note.Note("G4", quarterLength=1), note.Rest(quarterLength=0.5), note.Note("E4", quarterLength=0.5)]
    motif2 = [note.Note("D5", quarterLength=1), note.Rest(quarterLength=0.5), note.Note("B4", quarterLength=0.5)]

    # Develop motifs by varying dynamics and tempo
    for i in range(4):
        for n in motif1:
            n.quarterLength += 0.25
            development.append(n)

        for n in motif2:
            n.quarterLength -= 0.25
            development.append(n)

    return development
