from music21 import stream, note

def create_transition():
    transition = stream.Part()

    # A chromatic ascending line to create tension
    for i in range(12):
        n = note.Note()
        n.pitch.midi = 60 + i
        n.quarterLength = 0.25
        transition.append(n)

    # Add a final resolving note
    transition.append(note.Note("C5", quarterLength=2))

    return transition
