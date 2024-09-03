from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, articulations
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (e.g., 120 BPM)
score.insert(0, tempo.MetronomeMark(number=60))

# Define instruments
piano1 = instrument.Piano()
piano2 = instrument.Piano()
bass = instrument.Bass()
violin = instrument.Violin()
voice = instrument.Soprano()

# Define chord progressions for sections (I-IV-V-I in C major, ii-V-I in G major)
chord_progressions = [
    ['C4', 'E4', 'G4'],  # C major (I)
    ['F4', 'A4', 'C5'],  # F major (IV)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['C4', 'E4', 'G4'],  # C major (I)
    ['A4', 'C5', 'E5'],  # A minor (vi)
    ['D4', 'F#4', 'A4'], # D major (V of G major)
]

# Define major and minor scales for melodic lines
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
a_minor_scale = ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4']

# Motifs for melodic development
melody_motif_1 = ['E4', 'G4', 'A4', 'G4']
melody_motif_2 = ['C5', 'B4', 'A4', 'G4']

# Define function to create arpeggio patterns
def create_arpeggio(chord_notes, length=4):
    arpeggio = []
    for _ in range(length):
        for note_name in chord_notes:
            arpeggio_note = note.Note(note_name, quarterLength=0.5)
            arpeggio_note.articulations.append(articulations.Staccato())  # Add staccato articulation
            arpeggio.append(arpeggio_note)
    return arpeggio

# Define function to create melody patterns based on motifs
def create_melody(scale, motif, length=8):
    melody = []
    for i in range(length):
        note_name = motif[i % len(motif)]
        melody_note = note.Note(note_name, quarterLength=0.5)
        volume = random.uniform(0.5, 1.0)  # Randomize volume for dynamics
        melody_note.volume = volume
        melody.append(melody_note)
    return melody

# Define function to create a more sophisticated bassline
def create_bassline(chord_progression, length=2):
    bassline = []
    for chord_notes in chord_progression:
        root_note = note.Note(chord_notes[0] + '2', quarterLength=length)
        root_note.articulations.append(articulations.Accent())  # Add accents for emphasis
        bassline.append(root_note)
    return bassline

# Define function to create vocal melody with a structured rhythm
def create_vocal_melody(scale, motif, length=8):
    melody = []
    for i in range(length):
        note_name = motif[i % len(motif)]
        vocal_note = note.Note(note_name, quarterLength=1 if i % 2 == 0 else 0.5)
        vocal_note.expressions.append(dynamics.Crescendo())  # Add expression for dynamics
        melody.append(vocal_note)
        if i % 2 == 0:
            melody.append(note.Rest(quarterLength=0.5))  # Add rests for phrasing
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

# Generate music parts with structured variations
section_length = 4  # Number of measures per section
sections = 3  # Number of sections (e.g., A-B-A form)

for section in range(sections):
    # Determine key and scale for the section (e.g., modulate for variety)
    if section == 1:  # Modulate for middle section (B section)
        score.insert(0, key.Key('G'))  # Change key to G major
        current_scale = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
        motif = melody_motif_2  # Use second motif in middle section
    else:
        score.insert(0, key.Key('C'))  # Return to C major for A sections
        current_scale = c_major_scale
        motif = melody_motif_1  # Use first motif in A sections

    for i in range(section_length):
        chord_notes = chord_progressions[i % len(chord_progressions)]

        # Piano 1: Arpeggios
        arpeggio_pattern = create_arpeggio(chord_notes)
        piano1_part.append(arpeggio_pattern)

        # Piano 2: Melody based on motif
        melody_pattern = create_melody(current_scale, motif)
        piano2_part.append(melody_pattern)

        # Violin: Harmonized melody
        violin_melody = create_melody(current_scale, motif)
        violin_part.append(violin_melody)

        # Bass: Sophisticated bassline
        bassline = create_bassline(chord_progressions)
        bass_part.append(bassline)

        # Voice: Melodic and rhythmic variation
        vocal_melody = create_vocal_melody(current_scale, motif)
        voice_part.append(vocal_melody)

        # Add strategic rests to each part for natural phrasing and dynamics
        if i % 2 == 0:  # Introduce rests every other measure
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
score.write('midi', fp='enhanced_melodious_song.mid')

print("MIDI file 'enhanced_melodious_song.mid' has been created successfully!")
