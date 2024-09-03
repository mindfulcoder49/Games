from music21 import stream, note, chord, instrument, meter, midi

# Define the chord progression in C minor
chord_progression = [
    chord.Chord(['C4', 'Eb4', 'G4']),  # C minor
    chord.Chord(['Ab3', 'C4', 'Eb4']),  # Ab major
    chord.Chord(['Bb3', 'D4', 'F4']),  # Bb major
    chord.Chord(['G3', 'B3', 'D4']),   # G major
    chord.Chord(['Eb3', 'G3', 'Bb3']), # Eb major
    chord.Chord(['F3', 'Ab3', 'C4']),  # F minor
    chord.Chord(['C4', 'Eb4', 'G4'])   # C minor
]

# Define the melody pattern
melody_pattern = [
    ['C4', 'D4', 'E4', 'G4'],  # Measure 1
    ['A4', 'G4', 'F4', 'E4'],  # Measure 2
    ['D4', 'E4', 'F4', 'E4'],  # Measure 3
    ['D4', 'C4', 'G4', 'E4'],  # Measure 4
    ['C5', 'D5', 'E5', 'G5'],  # Measure 5
    ['A5', 'G5', 'F5', 'D5'],  # Measure 6
    ['E5', 'F5', 'D5', 'C5'],  # Measure 7
    ['B4', 'C5', 'G4', 'C4'],  # Measure 8
]

# Define the bassline pattern
bassline_pattern = [
    'C2',  # Measure 1
    'G2',  # Measure 2
    'F2',  # Measure 3
    'C2',  # Measure 4
    'C3',  # Measure 5
    'A2',  # Measure 6
    'D2',  # Measure 7
    'G2'   # Measure 8
]

# Initialize music21 streams for each part
melody_stream = stream.Part()
melody_stream.insert(0, instrument.Piano())  # Choose an instrument for the melody

bassline_stream = stream.Part()
bassline_stream.insert(0, instrument.Violoncello())  # Choose an instrument for the bassline

harmony_stream = stream.Part()
harmony_stream.insert(0, instrument.Viola())  # Choose an instrument for the harmony

# Set time signature
time_signature = meter.TimeSignature('4/4')
melody_stream.append(time_signature)
bassline_stream.append(time_signature)
harmony_stream.append(time_signature)

# Populate the melody stream
for chord_tone in chord_progression:
    for measure in melody_pattern:
        for pitch in measure:
            n = note.Note(pitch)
            n.quarterLength = 1  # Set each note duration
            melody_stream.append(n)

# Populate the bassline stream
for chord_tone in chord_progression:
    for pitch in bassline_pattern:
        n = note.Note(pitch)
        n.quarterLength = 4  # Set each bass note to whole note for each measure
        bassline_stream.append(n)

# Populate the harmony stream with chords
for chord_tone in chord_progression:
    for _ in range(8):  # 8 measures for each chord
        harmony_chord = chord.Chord(chord_tone)
        harmony_chord.quarterLength = 4  # Set chord duration to whole note for each measure
        harmony_stream.append(harmony_chord)

# Combine all streams into one score
score = stream.Score([melody_stream, bassline_stream, harmony_stream])

# Write the score to a MIDI file
midi_file_path = 'classical_piece.mid'
score.write('midi', fp=midi_file_path)

print(f"MIDI file saved to {midi_file_path}")
