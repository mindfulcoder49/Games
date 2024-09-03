from music21 import stream, note, chord, instrument, meter, midi

# Define the chord progression in C minor
chord_progression = [
    chord.Chord(['C4', 'E4', 'G4']),             # C major (C-E-G)
    chord.Chord(['G3', 'B3', 'D4', 'F4']),       # G dominant 7 (G-B-D-F)
    chord.Chord(['F3', 'A3', 'C4', 'E4']),       # F major 7 (F-A-C-E)
    chord.Chord(['C4', 'E4', 'G4']),             # C major (C-E-G)
    chord.Chord(['E3', 'G#3', 'B3', 'D4']),      # E dominant 7 (E-G#-B-D)
    chord.Chord(['A3', 'C#4', 'E4', 'G4']),      # A minor 7 (A-C#-E-G)
    chord.Chord(['D3', 'F#3', 'A3', 'C4']),      # D minor 7 (D-F#-A-C)
    chord.Chord(['G3', 'B3', 'D4', 'F#4'])       # G major 7 (G-B-D-F#)
]


# add chord progreesion to the end of itself 7 times
chord_progression += chord_progression * 7

# Define the varied melody pattern
melody_pattern = [
    [('C4', 1.5), ('D4', 0.5), ('E4', 1), ('G4', 1)],  # Measure 1 with a dotted quarter note
    [('A4', 0.5), ('G4', 1.5), ('F4', 0.5), ('E4', 1)],  # Measure 2 with a rest
    [('D4', 1), ('E4', 1), ('F4', 0.5), ('E4', 1.5)],  # Measure 3 with varied rhythm
    [('D4', 2), ('C4', 0.5), ('G4', 1.5)],  # Measure 4 with a half note
    [('C5', 1), ('D5', 1), ('E5', 1), ('G5', 1)],  # Measure 5 (all even)
    [('A5', 1.5), ('G5', 0.5), ('F5', 1), ('D5', 1)],  # Measure 6 with a dotted quarter note
    [('E5', 0.5), ('F5', 0.5), ('D5', 2), ('C5', 1)],  # Measure 7 with half note
    [('B4', 1), ('C5', 1), ('G4', 1), ('C4', 1)]  # Measure 8 (all even)
]

# Expanded varied melody pattern
melody_pattern += [
    [('C4', 1.5), ('D4', 0.5), ('E4', 1), ('G4', 1)],  # Measure 1
    [('A4', 0.5), ('G4', 1.5), ('rest', 1), ('E4', 1)],  # Measure 2 with a rest
    [('D4', 1), ('E4', 1), ('F4', 0.5), ('E4', 1.5)],  # Measure 3
    [('D4', 2), ('C4', 0.5), ('G4', 1.5)],  # Measure 4 with a half note
    [('C5', 1), ('D5', 1), ('E5', 1), ('G5', 1)],  # Measure 5
    [('A5', 1.5), ('G5', 0.5), ('F5', 1), ('D5', 1)],  # Measure 6
    [('E5', 0.5), ('F5', 0.5), ('D5', 2), ('C5', 1)],  # Measure 7
    [('B4', 1), ('C5', 1), ('G4', 1), ('C4', 1)],  # Measure 8
    [('C4', 0.5), ('E4', 0.5), ('G4', 1.5), ('rest', 1.5)],  # Measure 9 with triplets and rest
    [('F4', 2), ('E4', 0.5), ('D4', 1.5)],  # Measure 10
    [('G4', 1), ('A4', 0.5), ('Bb4', 0.5), ('A4', 1)],  # Measure 11 with triplets
    [('E4', 1), ('rest', 2), ('G4', 1)],  # Measure 12 with a long rest
    [('C5', 1), ('Bb4', 1), ('A4', 1), ('G4', 1)],  # Measure 13
    [('F4', 0.5), ('G4', 0.5), ('A4', 1), ('Bb4', 2)],  # Measure 14 with a half note
    [('C5', 1.5), ('Bb4', 0.5), ('G4', 1), ('F4', 1)],  # Measure 15
    [('E4', 2), ('D4', 1), ('C4', 1)],  # Measure 16 with a long note
    [('C5', 0.75), ('D5', 0.75), ('E5', 0.75), ('G5', 0.75)],  # Measure 17 with triplet feel
    [('A5', 1.5), ('rest', 1.5), ('D5', 1)],  # Measure 18 with a dotted quarter rest
    [('E5', 1), ('F5', 1), ('E5', 1), ('D5', 1)],  # Measure 19
    [('C5', 0.5), ('B4', 0.5), ('A4', 1), ('G4', 2)],  # Measure 20 with longer notes
    [('F4', 1), ('E4', 0.5), ('rest', 0.5), ('D4', 1)],  # Measure 21 with a short rest
    [('C4', 1), ('Bb3', 1), ('A3', 1), ('G3', 1)],  # Measure 22
    [('F3', 0.5), ('G3', 0.5), ('A3', 1.5), ('Bb3', 0.5)],  # Measure 23
    [('C4', 1), ('D4', 1), ('E4', 2)],  # Measure 24 with a longer note
    [('G4', 1), ('F4', 0.5), ('rest', 1), ('E4', 0.5)],  # Measure 25 with a rest
    [('D4', 1), ('C4', 1), ('B3', 1), ('A3', 1)],  # Measure 26
    [('G3', 2), ('rest', 2)],  # Measure 27 with a longer rest
    [('C4', 0.5), ('D4', 0.5), ('E4', 1.5), ('F4', 1.5)],  # Measure 28
    [('G4', 0.75), ('A4', 0.75), ('Bb4', 0.75), ('C5', 0.75)],  # Measure 29 with triplet feel
    [('D5', 1), ('E5', 1), ('F5', 0.5), ('E5', 0.5), ('D5', 0.5), ('C5', 0.5)],  # Measure 30
    [('Bb4', 1), ('A4', 1), ('G4', 1), ('F4', 1)],  # Measure 31
    [('E4', 0.5), ('D4', 1), ('C4', 2.5)]  # Measure 32 ending with a long note
]

# Continue expanding the varied melody pattern from Measure 32
melody_pattern += [
    [('D4', 1), ('F4', 1), ('E4', 0.5), ('D4', 0.5), ('C4', 1)],  # Measure 33
    [('B3', 1.5), ('rest', 0.5), ('A3', 1), ('G3', 1)],  # Measure 34 with a rest
    [('F3', 0.5), ('G3', 0.5), ('A3', 1), ('Bb3', 2)],  # Measure 35 with a half note
    [('C4', 1), ('rest', 1), ('D4', 1), ('E4', 1)],  # Measure 36 with a rest
    [('F4', 0.5), ('G4', 0.5), ('A4', 1.5), ('G4', 0.5)],  # Measure 37 with dotted rhythms
    [('F4', 1), ('E4', 1), ('D4', 1), ('C4', 1)],  # Measure 38
    [('G4', 0.75), ('A4', 0.75), ('Bb4', 0.75), ('C5', 0.75)],  # Measure 39 with triplet feel
    [('D5', 1), ('E5', 1), ('F5', 0.5), ('E5', 0.5), ('D5', 0.5), ('C5', 0.5)],  # Measure 40
    [('Bb4', 2), ('rest', 2)],  # Measure 41 with a longer rest
    [('A4', 0.5), ('G4', 0.5), ('F4', 1), ('E4', 1.5)],  # Measure 42 with a dotted rhythm
    [('D4', 1), ('C4', 1), ('B3', 1), ('A3', 1)],  # Measure 43
    [('G3', 2), ('F3', 1), ('E3', 1)],  # Measure 44
    [('D3', 1), ('C3', 1), ('B2', 1), ('A2', 1)],  # Measure 45
    [('G2', 0.5), ('A2', 0.5), ('B2', 1), ('C3', 1.5)],  # Measure 46
    [('D3', 1), ('rest', 1), ('E3', 1), ('F3', 1)],  # Measure 47 with a rest
    [('G3', 0.75), ('A3', 0.75), ('Bb3', 0.75), ('C4', 0.75)],  # Measure 48 with triplet feel
    [('D4', 1.5), ('rest', 0.5), ('E4', 1), ('F4', 1)],  # Measure 49 with a rest
    [('G4', 1), ('A4', 0.5), ('G4', 1), ('F4', 1)],  # Measure 50 with a dotted rhythm
    [('E4', 0.5), ('D4', 0.5), ('C4', 2), ('rest', 1)],  # Measure 51 with a rest
    [('Bb3', 1), ('A3', 1), ('G3', 1), ('F3', 1)],  # Measure 52
    [('E3', 0.5), ('D3', 0.5), ('C3', 2), ('rest', 1)],  # Measure 53 with a rest
    [('B2', 1), ('C3', 1), ('D3', 1), ('E3', 1)],  # Measure 54
    [('F3', 1), ('G3', 1), ('A3', 1), ('Bb3', 1)],  # Measure 55
    [('C4', 0.5), ('D4', 0.5), ('E4', 1), ('F4', 1.5)],  # Measure 56 with a dotted rhythm
    [('G4', 1), ('F4', 1), ('E4', 0.5), ('D4', 1.5)],  # Measure 57 with a varied rhythm
    [('C4', 1), ('B3', 1), ('A3', 1), ('G3', 1)],  # Measure 58
    [('F3', 2), ('E3', 0.5), ('rest', 1.5)],  # Measure 59 with a longer rest
    [('D3', 1), ('C3', 1), ('B2', 1), ('A2', 1)],  # Measure 60
    [('G2', 1), ('rest', 2), ('F2', 1)],  # Measure 61 with a rest
    [('E2', 0.5), ('D2', 0.5), ('C2', 1), ('rest', 2)],  # Measure 62 with a rest
    [('C4', 4)]  # Measure 63 ending with a whole note
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

# Populate the melody stream with varied note durations
for measure in melody_pattern:
    for pitch, duration in measure:
        if pitch == 'rest':
            n = note.Rest()
        else:
            n = note.Note(pitch)
        n.quarterLength = duration
        melody_stream.append(n)

# Populate the bassline stream
for _ in range(8):  # 8 measures for the bassline
    for pitch in bassline_pattern:
        n = note.Note(pitch)
        n.quarterLength = 4  # Set each bass note to whole note for each measure
        bassline_stream.append(n)

# Populate the harmony stream with chords
for chord_tone in chord_progression:
    for _ in range(1):  # 8 measures for each chord
        harmony_chord = chord.Chord(chord_tone)
        harmony_chord.quarterLength = 4  # Set chord duration to whole note for each measure
        harmony_stream.append(harmony_chord)

# Combine all streams into one score
score = stream.Score([melody_stream, bassline_stream, harmony_stream])

# Write the score to a MIDI file
midi_file_path = 'classical_piece_varied_melody.mid'
score.write('midi', fp=midi_file_path)

print(f"MIDI file saved to {midi_file_path}")
