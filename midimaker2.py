from music21 import stream, note, chord, meter, key, tempo, instrument

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (e.g., 120 BPM)
score.insert(0, tempo.MetronomeMark(number=120))

# Define instruments
piano = instrument.Piano()
bass = instrument.Bass()
voice = instrument.Soprano()

# Create a melody for the song
melody_part = stream.Part()
melody_part.insert(0, piano)

# Extended melody with variations in C major
melody_notes = [
    note.Rest(quarterLength=1),  # Rest to give a breathing space
    note.Note('E4', quarterLength=1),  # E
    note.Note('G4', quarterLength=1),  # G
    note.Note('A4', quarterLength=1),  # A
    note.Rest(quarterLength=0.5),      # Short rest
    note.Note('E4', quarterLength=0.5),  # E
    note.Note('D4', quarterLength=1),  # D
    note.Note('C4', quarterLength=2),  # C
    note.Note('F4', quarterLength=1),  # F
    note.Note('G4', quarterLength=1),  # G
    note.Rest(quarterLength=1),        # Rest for variation
    note.Note('E4', quarterLength=0.5),  # E
    note.Note('F4', quarterLength=0.5),  # F
    note.Note('G4', quarterLength=1),  # G
    note.Note('C5', quarterLength=2),  # C (high)
    note.Rest(quarterLength=1),        # Another rest for pause
    # New melodic variation
    note.Note('G4', quarterLength=1),  # G
    note.Note('A4', quarterLength=1),  # A
    note.Note('B4', quarterLength=1),  # B
    note.Rest(quarterLength=0.5),      # Rest
    note.Note('C5', quarterLength=0.5),  # C
    note.Note('B4', quarterLength=1),  # B
    note.Note('A4', quarterLength=1),  # A
    note.Note('G4', quarterLength=2),  # G
    note.Rest(quarterLength=1),        # Rest for break
]

melody_part.append(melody_notes)

# Create a simple harmony using basic triads with variations
harmony_part = stream.Part()
harmony_part.insert(0, piano)

# Extended chords corresponding to the melody notes
harmony_chords = [
    chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),  # C major chord
    chord.Chord(['A2', 'E3', 'C4'], quarterLength=2),  # A minor chord
    chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),  # F major chord
    chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),  # G major chord
    chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),  # C major chord
    chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),  # F major chord
    chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),  # G major chord
    chord.Chord(['A2', 'C3', 'E3'], quarterLength=2),  # A minor chord
    chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),  # F major chord
    chord.Chord(['D3', 'F3', 'A3'], quarterLength=2),  # D minor chord
    chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),  # G major chord
    chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),  # C major chord
]

harmony_part.append(harmony_chords)

# Create a bass line
bass_part = stream.Part()
bass_part.insert(0, bass)

# Bassline that follows the harmonic structure with a rhythmic pattern
bass_notes = [
    note.Note('C2', quarterLength=2),  # C
    note.Note('A2', quarterLength=2),  # A
    note.Note('F2', quarterLength=2),  # F
    note.Note('G2', quarterLength=2),  # G
    note.Note('C2', quarterLength=2),  # C
    note.Note('F2', quarterLength=2),  # F
    note.Note('G2', quarterLength=2),  # G
    note.Note('A2', quarterLength=2),  # A
    note.Note('F2', quarterLength=2),  # F
    note.Note('D2', quarterLength=2),  # D
    note.Note('G2', quarterLength=2),  # G
    note.Note('C2', quarterLength=2),  # C
]

bass_part.append(bass_notes)

# Create a vocal melody line
vocal_part = stream.Part()
vocal_part.insert(0, voice)

# Simple vocal melody with rhythmic variation
vocal_melody = [
    note.Rest(quarterLength=2),  # Intro rest
    note.Note('E4', quarterLength=1),  # E
    note.Rest(quarterLength=0.5),  # Short rest
    note.Note('G4', quarterLength=0.5),  # G
    note.Note('A4', quarterLength=1),  # A
    note.Rest(quarterLength=0.5),  # Short rest
    note.Note('C5', quarterLength=0.5),  # C
    note.Note('B4', quarterLength=1),  # B
    note.Note('A4', quarterLength=1),  # A
    note.Rest(quarterLength=0.5),  # Rest
    note.Note('G4', quarterLength=0.5),  # G
    note.Note('E4', quarterLength=1),  # E
    note.Note('D4', quarterLength=2),  # D
]

vocal_part.append(vocal_melody)

# Add all parts to the score
score.insert(0, melody_part)
score.insert(0, harmony_part)
score.insert(0, bass_part)
score.insert(0, vocal_part)

# Save the score as a MIDI file
score.write('midi', fp='extended_pretty_little_song.mid')

print("MIDI file 'extended_pretty_little_song.mid' has been created successfully!")
