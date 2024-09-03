from music21 import stream, note, chord, tempo, metadata, key, meter, midi

# Create a Stream for the piece
piece = stream.Score()

# Add metadata
piece.metadata = metadata.Metadata()
piece.metadata.title = 'Tranquil Piece'
piece.metadata.composer = 'AI Composer'

# Create Piano and Strings Parts
piano_part = stream.Part()
strings_part = stream.Part()

# Set the tempo
piano_part.append(tempo.MetronomeMark(number=60))  # 60 BPM for a slow tempo
strings_part.append(tempo.MetronomeMark(number=60))

# Define the key and time signature
piece.append(key.KeySignature(0))  # C Major
piece.append(meter.TimeSignature('4/4'))

# Define chord progression
chord_progression = [
    chord.Chord(['C4', 'E4', 'G4']),  # C Major
    chord.Chord(['F4', 'A4', 'C5']),  # F Major
    chord.Chord(['G4', 'B4', 'D5']),  # G Major
    chord.Chord(['C4', 'E4', 'G4'])   # C Major
]

# Define a measure length in quarter notes
measure_length = 4  # 4 beats per measure

# Add piano part
for _ in range(4):  # 4 measures
    measure = stream.Measure()
    for chord in chord_progression:
        measure.append(chord)
    piano_part.append(measure)

# Add strings part (same chord progression but with longer note durations)
for _ in range(4):  # 4 measures
    measure = stream.Measure()
    for chord in chord_progression:
        # Strings will hold each chord for a whole note
        for pitch in chord.pitches:
            measure.append(note.Note(pitch, duration=note.Duration(4.0)))
    strings_part.append(measure)

# Add parts to the piece
piece.append(piano_part)
piece.append(strings_part)

# Write the piece to a MIDI file
mf = midi.translate.music21ObjectToMidiFile(piece)
mf.open('tranquil_piece.mid', 'wb')
mf.write()
mf.close()

print("MIDI file 'tranquil_piece.mid' has been created.")
