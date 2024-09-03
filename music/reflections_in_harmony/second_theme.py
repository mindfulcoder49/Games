from music21 import stream, note

def create_second_theme():
    second_theme = stream.Part()

    # Create a theme in a different key for contrast
    theme_notes = ["D5", "B4", "A4", "G4", "F#4", "E4", "D4"]
    for pitch in theme_notes:
        second_theme.append(note.Note(pitch, quarterLength=1))

    # Add a repeating motif to create continuity
    for i in range(3):
        for pitch in theme_notes:
            second_theme.append(note.Note(pitch, quarterLength=0.5))

    return second_theme
