from music21 import stream, note, chord, meter, key, tempo, instrument
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (e.g., 120 BPM)
score.insert(0, tempo.MetronomeMark(number=120))

# Define instruments
piano = instrument.Piano()

# Create a main part for the piano
main_part = stream.Part()
main_part.insert(0, piano)

# Define chord progressions (e.g., I, IV, V, I in C major)
chord_progressions = [
    ['C4', 'E4', 'G4'],  # C major (I)
    ['F4', 'A4', 'C5'],  # F major (IV)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['C4', 'E4', 'G4'],  # C major (I)
]

# Define arpeggio patterns for the chords
def create_arpeggio(chord_notes, length=4):
    """Create an arpeggio pattern from the given chord notes."""
    arpeggio = []
    for _ in range(length):
        for note_name in chord_notes:
            arpeggio.append(note.Note(note_name, quarterLength=0.5))
    return arpeggio

# Define a melody pattern using scale notes
def create_melody(scale, length=8):
    """Create a melodic pattern using notes from the given scale."""
    melody = []
    for _ in range(length):
        note_name = random.choice(scale)
        melody.append(note.Note(note_name, quarterLength=0.5))
    return melody

# Major scale in C
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Generate the main melody and harmony with variations
for _ in range(8):  # Repeat 8 phrases to create a long piece
    for chord_notes in chord_progressions:
        # Create arpeggios for the harmony part
        arpeggio_pattern = create_arpeggio(chord_notes)
        main_part.append(arpeggio_pattern)

        # Create a corresponding melody line using scale notes
        melody_pattern = create_melody(c_major_scale)
        main_part.append(melody_pattern)

        # Add some rests to create breathing space in the melody
        main_part.append(note.Rest(quarterLength=1))

# Add the piano part to the score
score.insert(0, main_part)

# Save the score as a MIDI file
score.write('midi', fp='long_melodious_song.mid')

print("MIDI file 'long_melodious_song.mid' has been created successfully!")
