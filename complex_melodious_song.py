from music21 import stream, note, chord, meter, key, tempo, instrument
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (e.g., 120 BPM)
score.insert(0, tempo.MetronomeMark(number=120))

# Define instruments
piano1 = instrument.Piano()
piano2 = instrument.Piano()
bass = instrument.Bass()
violin = instrument.Violin()
voice = instrument.Soprano()

# Define chord progressions (e.g., I, IV, V, I in C major)
chord_progressions = [
    ['C4', 'E4', 'G4'],  # C major (I)
    ['F4', 'A4', 'C5'],  # F major (IV)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['C4', 'E4', 'G4'],  # C major (I)
]

# Major scale in C
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Define function to create arpeggio patterns
def create_arpeggio(chord_notes, length=4):
    arpeggio = []
    for _ in range(length):
        for note_name in chord_notes:
            arpeggio.append(note.Note(note_name, quarterLength=0.5))
    return arpeggio

# Define function to create melody patterns
def create_melody(scale, length=8):
    melody = []
    for _ in range(length):
        note_name = random.choice(scale)
        melody.append(note.Note(note_name, quarterLength=0.5))
    return melody

# Define function to create bassline
def create_bassline(chord_progression, length=2):
    bassline = []
    for chord_notes in chord_progression:
        root_note = note.Note(chord_notes[0] + '2', quarterLength=length)
        bassline.append(root_note)
    return bassline

# Define function to create vocal melody
def create_vocal_melody(scale, length=8):
    melody = []
    for _ in range(length):
        note_name = random.choice(scale)
        melody.append(note.Note(note_name, quarterLength=1))
        melody.append(note.Rest(quarterLength=0.5))  # Add rests for variation
    return melody

# Create parts for different instruments
piano1_part = stream.Part()
piano1_part.insert(0, piano1)

piano2_part = stream.Part()
piano2_part.insert(0, piano2)

bass_part = stream.Part()
bass_part.insert(0, bass)

violin_part = stream.Part()
violin_part.insert(0, violin)

voice_part = stream.Part()
voice_part.insert(0, voice)

# Generate music parts with variations
for _ in range(8):  # Repeat 8 phrases to create a long piece
    for chord_notes in chord_progressions:
        # Piano 1: Arpeggios
        arpeggio_pattern = create_arpeggio(chord_notes)
        piano1_part.append(arpeggio_pattern)

        # Piano 2: Melody using scale notes
        melody_pattern = create_melody(c_major_scale)
        piano2_part.append(melody_pattern)

        # Violin: Harmonized melody
        violin_melody = create_melody(c_major_scale)
        violin_part.append(violin_melody)

        # Bass: Bassline following the chord roots
        bassline = create_bassline(chord_progressions)
        bass_part.append(bassline)

        # Voice: Simple vocal melody with rests for phrasing
        vocal_melody = create_vocal_melody(c_major_scale)
        voice_part.append(vocal_melody)

        # Add rests to each part for natural phrasing and dynamics
        piano1_part.append(note.Rest(quarterLength=2))
        piano2_part.append(note.Rest(quarterLength=2))
        violin_part.append(note.Rest(quarterLength=2))
        bass_part.append(note.Rest(quarterLength=2))
        voice_part.append(note.Rest(quarterLength=4))

# Add all parts to the score
score.insert(0, piano1_part)
score.insert(0, piano2_part)
score.insert(0, bass_part)
score.insert(0, violin_part)
score.insert(0, voice_part)

# Save the score as a MIDI file
score.write('midi', fp='complex_melodious_song.mid')

print("MIDI file 'complex_melodious_song.mid' has been created successfully!")
