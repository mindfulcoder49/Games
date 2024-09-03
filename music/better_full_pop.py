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

    # First Repetition: Simple chordal structure
    for root, quality in chord_progression1:
        # Create the chord for the Piano
        c = chord.Chord([root + "4", root + "3", root + "5"], quarterLength=duration)
        piano_part.append(c)
        
        # Simple arpeggiated melody for the Strings
        for n in [root + "5", root + "3", root + "4", root + "5"]:
            strings_part.append(note.Note(n, quarterLength=1))

        # Flute melody: simple sustained notes
        flute_part.append(note.Note(root + "5", quarterLength=2))
        flute_part.append(note.Note(root + "4", quarterLength=2))

        # Drum part: Simple pop beat
        drum_part.append(note.Rest(quarterLength=1))
        drum_part.append(note.Note('C2', quarterLength=1))  # Snare placeholder
        drum_part.append(note.Rest(quarterLength=1))
        drum_part.append(note.Note('C2', quarterLength=1))  # Snare placeholder

    # Second Repetition: Introduce counter-melody and variations
    for root, quality in chord_progression2:
        # Chords with added 7ths for more harmonic complexity
        c = chord.Chord([root + "4", root + "3", root + "5", root + "6"], quarterLength=duration)
        piano_part.append(c)

        # Strings now have a counter-melody
        strings_part.append(note.Note(root + "5", quarterLength=1))
        strings_part.append(note.Note(root + "3", quarterLength=1.5))
        strings_part.append(note.Note(root + "4", quarterLength=0.5))
        strings_part.append(note.Note(root + "5", quarterLength=1))

        # Flute introduces more rhythmic variation
        flute_part.append(note.Note(root + "5", quarterLength=1.5))
        flute_part.append(note.Rest(quarterLength=0.5))
        flute_part.append(note.Note(root + "4", quarterLength=2))

        # Drum part with added hi-hat rhythm
        drum_part.append(note.Rest(quarterLength=0.5))
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Snare placeholder
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Hi-hat placeholder
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Snare placeholder
        drum_part.append(note.Rest(quarterLength=2))

    # Third Repetition: More rhythmic complexity and harmony
    for root, quality in chord_progression1:
        # Chords with added 9ths for even more harmonic interest
        c = chord.Chord([root + "4", root + "3", root + "5", root + "7"], quarterLength=duration)
        piano_part.append(c)

        # Strings play more complex motifs
        strings_part.append(note.Note(root + "5", quarterLength=1))
        strings_part.append(note.Note(root + "3", quarterLength=0.5))
        strings_part.append(note.Note(root + "4", quarterLength=0.5))
        strings_part.append(note.Rest(quarterLength=1))
        strings_part.append(note.Note(root + "5", quarterLength=1))

        # Flute harmonizes with itself (two notes at once)
        flute_part.append(chord.Chord([root + "5", root + "6"], quarterLength=2))
        flute_part.append(note.Rest(quarterLength=2))

        # Drum part introduces toms and more complex fills
        drum_part.append(note.Note('C2', quarterLength=1))  # Tom placeholder
        drum_part.append(note.Rest(quarterLength=0.5))
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Snare placeholder
        drum_part.append(note.Note('C2', quarterLength=1))  # Hi-hat placeholder

    # Fourth Repetition: Modulation and dynamic swells
    for root, quality in chord_progression2:
        # Modulate up by a whole step using pitch interval
        modulated_root = note.Note(root + "4")
        modulated_root.transpose('M2', inPlace=True)  # Transpose by a Major 2nd
        c = chord.Chord([modulated_root.nameWithOctave, 
                         modulated_root.transpose('P8').nameWithOctave, 
                         modulated_root.transpose('m3').nameWithOctave, 
                         modulated_root.transpose('P5').nameWithOctave], 
                        quarterLength=duration)
        piano_part.append(c)

        # Strings now have dynamic swells
        note1 = note.Note(modulated_root.nameWithOctave, quarterLength=2)
        note1.volume = .8 # Forte
        strings_part.append(note1)
        strings_part.append(note.Rest(quarterLength=2))
        note2 = note.Note(modulated_root.transpose('m3').nameWithOctave, quarterLength=2)
        note2.volume =  .4 # Piano
        strings_part.append(note2)

        # Flute plays a more expressive line with trills
        flute_note = note.Note(modulated_root.nameWithOctave, quarterLength=1.5)
        flute_part.append(flute_note)
        trill_note = note.Note(modulated_root.transpose('M2').nameWithOctave, quarterLength=0.5)
        #trill_note.articulations.append(note.Trill())
        flute_part.append(trill_note)
        flute_part.append(note.Rest(quarterLength=2))

        # Drum part with a full drum kit groove
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Kick placeholder
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Snare placeholder
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Hi-hat placeholder
        drum_part.append(note.Note('C2', quarterLength=0.5))  # Snare placeholder
        drum_part.append(note.Note('C2', quarterLength=1))  # Kick placeholder

    # Add all parts to the score
    score.insert(0, piano_part)
    score.insert(0, strings_part)
    score.insert(0, flute_part)
    score.insert(0, drum_part)

    # Save the score as a MIDI file
    midi_file = midi.translate.streamToMidiFile(score)
    midi_file.open('full_length_beautiful_pop_song_expanded.mid', 'wb')
    midi_file.write()
    midi_file.close()

    print("MIDI file 'full_length_beautiful_pop_song_expanded.mid' has been created successfully!")

# Run the function to create the song
create_full_length_pop_song()
