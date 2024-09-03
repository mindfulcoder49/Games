from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, midi

def create_harmonically_rich_flute_melody():
    # Initialize the score and set key and time signature
    score = stream.Score()
    score.insert(0, key.KeySignature(2))  # D Major, giving a bright, classical sound
    score.insert(0, meter.TimeSignature('4/4'))
    
    # Set a tempo for the piece
    score.insert(0, tempo.MetronomeMark(number=72))  # Andante tempo for expressive phrasing

    # Define flute instrument
    flute = instrument.Flute()

    # Create part for flute
    flute_part = stream.Part()
    flute_part.insert(0, flute)

    # Define harmonic progressions and motifs inspired by classical theory
    harmony_progressions = [
        ["D5", "F#5", "A5", "B4"],  # I - ii chord outline
        ["G5", "F#5", "E5", "D5"],  # IV - I resolution
        ["A4", "C#5", "E5", "G5"],  # V7 chord leading to tonic
        ["D5", "E5", "F#5", "G5"],  # I - ii progression
        ["B4", "D5", "G5", "F#5"],  # viio7 - I cadence
    ]

    # Motifs with harmonic implications
    motifs = [
        ['D5', 'E5', 'F#5', 'G5', 'A5'],  # Motif 1: Ascending diatonic line
        ['A5', 'F#5', 'D5', 'B4', 'C#5'],  # Motif 2: Descending arpeggio
        ['G5', 'F#5', 'E5', 'D5'],         # Motif 3: Scalar descent
        ['B4', 'D5', 'E5', 'F#5', 'G5'],   # Motif 4: Chromatic embellishment
        ['A5', 'G5', 'F#5', 'E5', 'D5'],   # Motif 5: Descending line with harmonic suspension
    ]

    # Create the flute melody with harmonic consideration
    melody_notes = []

    # Use motifs and harmony progressions to craft a cohesive melody
    for i in range(len(harmony_progressions)):
        # Chord tones and non-chord tones to imply harmony
        progression = harmony_progressions[i]
        motif = motifs[i % len(motifs)]

        # Harmonically strong notes on beats
        for j in range(len(progression)):
            if j == 0 or j == 2:
                # Strong harmonic tones on downbeats
                n = note.Note(progression[j], quarterLength=1.0)
            else:
                # Passing or neighbor tones to create motion
                n = note.Note(motif[j], quarterLength=0.5)
            

            melody_notes.append(n)

        # Add a rest for phrasing
        melody_notes.append(note.Rest(quarterLength=0.5))

    # Final cadence with a more resolved ending
    final_cadence = ['D5', 'C#5', 'B4', 'A4', 'G4', 'F#4', 'E4', 'D4']
    for pitch in final_cadence:
        n = note.Note(pitch, quarterLength=0.5)
        melody_notes.append(n)

    # Add all notes to the flute part
    for n in melody_notes:
        flute_part.append(n)

    # Add the flute part to the score
    score.insert(0, flute_part)

    # Save the score as a MIDI file
    midi_file = midi.translate.streamToMidiFile(score)
    midi_file.open('harmonically_rich_flute_melody.mid', 'wb')
    midi_file.write()
    midi_file.close()

    print("MIDI file 'harmonically_rich_flute_melody.mid' has been created successfully!")

# Run the function to create the flute melody
create_harmonically_rich_flute_melody()
