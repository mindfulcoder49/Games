from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, midi

def create_full_length_pop_song():
    # Initialize the score and set key and time signature
    score = stream.Score()
    score.insert(0, key.KeySignature(0))  # C Major
    score.insert(0, meter.TimeSignature('4/4'))
    
    # Set a tempo for the piece
    score.insert(0, tempo.MetronomeMark(number=90))  # 90 BPM for a typical pop tempo

    # Define instruments
    piano = instrument.Piano()
    strings = instrument.StringInstrument()
    flute = instrument.Flute()
    drums = instrument.Woodblock()  # Placeholder for a simple drum beat

    # Define chord progressions
    chord_progression1 = [("C", "major"), ("G", "major"), ("A", "minor"), ("F", "major")]
    chord_progression2 = [("A", "minor"), ("F", "major"), ("C", "major"), ("G", "major")]

    # Combine all chord progressions for a longer song structure
    full_chord_progression = chord_progression1 * 2 + chord_progression2 * 2

    # Create parts for different instruments
    piano_part = stream.Part()
    strings_part = stream.Part()
    flute_part = stream.Part()
    drum_part = stream.Part()

    piano_part.insert(0, piano)
    strings_part.insert(0, strings)
    flute_part.insert(0, flute)
    drum_part.insert(0, drums)

    # Duration of each chord
    duration = 4  # Each chord lasts one full measure

    # Build the song
    for root, quality in full_chord_progression:
        # Create the chord for the Piano
        c = chord.Chord([root + "4", root + "3", root + "5"], quarterLength=duration)
        piano_part.append(c)
        
        # Create a simple arpeggiated melody for the Strings
        for n in [root + "5", root + "3", root + "4", root + "5"]:
            strings_part.append(note.Note(n, quarterLength=1))

        # Flute melody: simple sustained notes or short motifs
        flute_part.append(note.Note(root + "5", quarterLength=2))
        flute_part.append(note.Note(root + "4", quarterLength=2))

        # Drum part: Simple pop beat
        drum_part.append(note.Rest(quarterLength=1))
        drum_part.append(note.Note('C2', quarterLength=1))  # Snare placeholder
        drum_part.append(note.Rest(quarterLength=1))
        drum_part.append(note.Note('C2', quarterLength=1))  # Snare placeholder

    # Add all parts to the score
    score.insert(0, piano_part)
    score.insert(0, strings_part)
    score.insert(0, flute_part)
    score.insert(0, drum_part)

    # Adjust dynamics to enhance expressiveness
    for part in [piano_part, strings_part, flute_part, drum_part]:
        for n in part.notes:
            n.volume.velocity = 60  # Moderate dynamics for a balanced pop sound

    # Save the score as a MIDI file
    midi_file = midi.translate.streamToMidiFile(score)
    midi_file.open('full_length_beautiful_pop_song.mid', 'wb')
    midi_file.write()
    midi_file.close()

    print("MIDI file 'full_length_beautiful_pop_song.mid' has been created successfully!")

# Run the function to create the song
create_full_length_pop_song()
