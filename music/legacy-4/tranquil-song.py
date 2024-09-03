from music21 import stream, note, chord, midi, meter, key

def create_beautiful_song():
    # Create a stream for the song
    song = stream.Score()
    
    # Define the key and time signature
    song.append(key.KeySignature(0))  # C Major
    song.append(meter.TimeSignature('4/4'))

    # Create parts for Piano and Strings
    piano_part = stream.Part()
    strings_part = stream.Part()

    # Define the chord progression
    chord_progression = [("C", "major"), ("G", "major"), ("A", "minor"), ("F", "major")]

    # Duration of each chord (in whole notes)
    duration = 2

    # Construct the chords and melodies
    for root, quality in chord_progression:
        # Construct the chord for Piano
        c = chord.Chord([root + "4", root + "3", root + "5"], quarterLength=duration*4)
        piano_part.append(c)

        # Construct the melody for Strings (simple arpeggiation of the chord)
        for n in [root + "5", root + "3", root + "4", root + "5"]:
            strings_part.append(note.Note(n, quarterLength=duration))

    # Append parts to the song
    song.insert(0, piano_part)
    song.insert(0, strings_part)

    # Write to MIDI file
    midi_file = midi.translate.streamToMidiFile(song)
    midi_file.open('tranquil_beautiful_song.mid', 'wb')
    midi_file.write()
    midi_file.close()

    print("MIDI file 'tranquil_beautiful_song.mid' has been created.")

# Run the function to create the song
create_beautiful_song()
