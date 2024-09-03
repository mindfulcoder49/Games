from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, articulations

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('F'))  # F major key, often associated with warmth and calm
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (60 BPM, slow and calming)
score.insert(0, tempo.MetronomeMark(number=60))

# Define instruments
flute = instrument.Flute()
piano = instrument.Piano()
harp = instrument.Harp()
strings = instrument.StringInstrument()  # Changed to a generic string instrument
soft_percussion = instrument.Percussion()

# Define harmonies (poignant, classic, and soothing)
chord_progressions = [
    ['F4', 'A4', 'C5'],  # F major
    ['Bb4', 'D5', 'F5'],  # Bb major
    ['G4', 'B4', 'D5'],  # G minor
    ['C4', 'E4', 'G4'],  # C major
    ['A4', 'C5', 'E5'],  # A minor
    ['D4', 'F4', 'A4'],  # D minor
]

# Define a melodic line that is smooth and flowing
flute_melody = [
    note.Note('A4', quarterLength=2),
    note.Note('C5', quarterLength=2),
    note.Note('D5', quarterLength=2),
    note.Note('E5', quarterLength=1),
    note.Note('F5', quarterLength=1),
    note.Note('E5', quarterLength=2),
    note.Rest(quarterLength=2),  # Adding a rest for breathing space
    note.Note('D5', quarterLength=2),
    note.Note('C5', quarterLength=2),
    note.Rest(quarterLength=2)
]

# Create a soft piano accompaniment with broken chords (arpeggios)
piano_accompaniment = [
    [note.Note('F3', quarterLength=1), note.Note('A3', quarterLength=1), note.Note('C4', quarterLength=2)],
    [note.Note('Bb3', quarterLength=1), note.Note('D4', quarterLength=1), note.Note('F4', quarterLength=2)],
    [note.Note('G3', quarterLength=1), note.Note('B3', quarterLength=1), note.Note('D4', quarterLength=2)],
    [note.Note('C3', quarterLength=1), note.Note('E3', quarterLength=1), note.Note('G3', quarterLength=2)],
    [note.Note('A3', quarterLength=1), note.Note('C4', quarterLength=1), note.Note('E4', quarterLength=2)],
    [note.Note('D3', quarterLength=1), note.Note('F3', quarterLength=1), note.Note('A3', quarterLength=2)]
]

# Define a harp part with soft glissandos to add a dreamlike texture
harp_glissando = [
    [note.Note('F4', quarterLength=0.5), note.Note('A4', quarterLength=0.5), note.Note('C5', quarterLength=1)],
    [note.Note('Bb4', quarterLength=0.5), note.Note('D5', quarterLength=0.5), note.Note('F5', quarterLength=1)],
    [note.Note('G4', quarterLength=0.5), note.Note('B4', quarterLength=0.5), note.Note('D5', quarterLength=1)],
    [note.Note('C4', quarterLength=0.5), note.Note('E4', quarterLength=0.5), note.Note('G4', quarterLength=1)],
]

# String accompaniment with long, sustained notes to add depth and warmth
strings_accompaniment = [
    note.Note('F3', quarterLength=4),
    note.Note('Bb3', quarterLength=4),
    note.Note('G3', quarterLength=4),
    note.Note('C3', quarterLength=4),
    note.Note('A3', quarterLength=4),
    note.Note('D3', quarterLength=4)
]

# Soft percussion to provide a gentle, steady rhythm (e.g., a soft brush snare)
soft_percussion_part = [
    note.Rest(quarterLength=1),  # Soft intro with no percussion
    note.Note('F2', quarterLength=4),  # Soft snare hit every 4 beats
    note.Rest(quarterLength=4),
    note.Note('F2', quarterLength=4),
    note.Rest(quarterLength=4)
]

# Create parts for different instruments
flute_part = stream.Part()
flute_part.insert(0, flute)
flute_part.append(flute_melody)

piano_part = stream.Part()
piano_part.insert(0, piano)
for chords in piano_accompaniment:
    for n in chords:
        piano_part.append(n)

harp_part = stream.Part()
harp_part.insert(0, harp)
for chords in harp_glissando:
    for n in chords:
        harp_part.append(n)

strings_part = stream.Part()
strings_part.insert(0, strings)
strings_part.append(strings_accompaniment)

percussion_part = stream.Part()
percussion_part.insert(0, soft_percussion)
percussion_part.append(soft_percussion_part)

# Add dynamics and articulations to enhance expressiveness
for n in flute_part.notes:
    n.volume.velocity = 60  # Soft dynamics for flute


        

for c in piano_part.notes:
    c.volume.velocity = 50  # Even softer for the piano background

for n in harp_part.notes:
    n.volume.velocity = 55  # Harp should blend but be heard

for n in strings_part.notes:
    n.volume.velocity = 45  # Strings in the background

for n in percussion_part.notes:
    n.volume.velocity = 40  # Soft percussion for a gentle feel

# Add all parts to the score
score.insert(0, flute_part)
score.insert(0, piano_part)
score.insert(0, harp_part)
score.insert(0, strings_part)
score.insert(0, percussion_part)

# Save the score as a MIDI file
score.write('midi', fp='ethereal_tranquil_song.mid')

print("MIDI file 'ethereal_tranquil_song.mid' has been created successfully!")
