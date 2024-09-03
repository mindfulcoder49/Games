from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, midi

def create_guitar_accompaniment():
    # Initialize the score and set key and time signature
    score = stream.Score()
    score.insert(0, key.KeySignature(2))  # D Major
    score.insert(0, meter.TimeSignature('4/4'))
    
    # Set a tempo for the piece to match the flute
    score.insert(0, tempo.MetronomeMark(number=72))  # Andante tempo

    # Define guitar instrument
    guitar = instrument.Guitar()

    # Create part for guitar
    guitar_part = stream.Part()
    guitar_part.insert(0, guitar)

    # Define harmonic progressions (as chords) to match the flute's harmony
    harmony_progressions = [
        ["D4", "F#4", "A4"],  # D Major (I)
        ["G4", "B4", "D5"],   # G Major (IV)
        ["A3", "C#4", "E4", "G4"],  # A7 (V7)
        ["D4", "F#4", "A4"],  # D Major (I)
        ["B3", "D4", "F#4", "A4"],  # Bm7b5 (viio7)
    ]

    # Define rhythmic pattern for strumming or fingerpicking
    rhythmic_pattern = [0.5, 0.5, 1.0, 1.0]  # A simple rhythm pattern for variety

    # Create the guitar accompaniment
    for harmony_pitches in harmony_progressions:
        harmony = chord.Chord(harmony_pitches, quarterLength=2)  # Create a new Chord object each iteration

        for duration in rhythmic_pattern:
            if duration == 1.0:
                # Full chord strum or arpeggio on stronger beats
                guitar_part.append(chord.Chord(harmony_pitches, quarterLength=duration))
            else:
                # Play broken chords or single notes for variety
                for pitch in harmony_pitches:
                    n = note.Note(pitch, quarterLength=duration)
                    guitar_part.append(n)

    # Final cadence to match the flute's melody
    final_cadence_chords = [
        ["D4", "F#4", "A4"],  # D Major
        ["C#4", "E4", "G#4"], # C# diminished
        ["B3", "D4", "F#4"],  # B Minor
        ["A3", "C#4", "E4"],  # A Major
        ["G3", "B3", "D4"],   # G Major
        ["F#3", "A3", "C#4"], # F# minor
        ["E3", "G3", "B3"],   # E Minor
        ["D3", "F#3", "A3"],  # D Major
    ]

    for final_chord_pitches in final_cadence_chords:
        final_chord = chord.Chord(final_chord_pitches, quarterLength=1)
        guitar_part.append(final_chord)

    # Add the guitar part to the score
    score.insert(0, guitar_part)

    # Save the score as a MIDI file
    midi_file = midi.translate.streamToMidiFile(score)
    midi_file.open('guitar_accompaniment.mid', 'wb')
    midi_file.write()
    midi_file.close()

    print("MIDI file 'guitar_accompaniment.mid' has been created successfully!")

# Run the function to create the guitar accompaniment
create_guitar_accompaniment()
