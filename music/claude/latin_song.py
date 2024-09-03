from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, articulations
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (180 BPM, common for Latin music)
score.insert(0, tempo.MetronomeMark(number=180))

# Define instruments
piano = instrument.Piano()
bass = instrument.ElectricBass()
percussion = instrument.Percussion()
trumpet = instrument.Trumpet()
voice = instrument.Vocalist()

# Define chord progressions for sections (I-V-vi-IV with a Latin twist)
chord_progressions = [
    ['C4', 'E4', 'G4'],  # C major (I)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['A4', 'C5', 'E5'],  # A minor (vi)
    ['F4', 'A4', 'C5'],  # F major (IV)
]

# Define C major scale for melodic lines
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Latin-style motif
latin_motif = ['E4', 'G4', 'A4', 'G4', 'E4', 'C4']

def create_latin_rhythm(length=16):
    rhythm = []
    for _ in range(length):
        if random.random() < 0.7:  # 70% chance of a note, 30% chance of a rest
            note_length = random.choice([0.25, 0.5, 1])
            rhythm.append(note.Note('C4', quarterLength=note_length))
        else:
            rhythm.append(note.Rest(quarterLength=0.25))
    return rhythm

def create_chord_progression(chord_notes, length=16):
    progression = []
    for _ in range(length // 4):
        for notes in chord_notes:
            c = chord.Chord(notes, quarterLength=1)
            progression.append(c)
    return progression

def create_melody(scale, motif, length=16):
    melody = []
    for i in range(length):
        note_name = random.choice(scale) if i % 2 == 0 else motif[i % len(motif)]
        melody_note = note.Note(note_name, quarterLength=0.5)
        melody_note.volume.velocity = random.randint(80, 100)
        melody.append(melody_note)
    return melody

def create_bassline(chord_progression, length=16):
    bassline = []
    for _ in range(length // 4):
        for chord_notes in chord_progression:
            root_note = note.Note(chord_notes[0].replace('4', '2'), quarterLength=1)
            root_note.volume.velocity = 100
            bassline.append(root_note)
    return bassline

def create_percussion_part(length=16):
    percussion_part = stream.Voice()
    for _ in range(length):
        if random.random() < 0.8:  # 80% chance of a hit
            perc_note = note.Note('C2', quarterLength=0.25)
            perc_note.storedInstrument = instrument.Percussion()
            percussion_part.append(perc_note)
        else:
            percussion_part.append(note.Rest(quarterLength=0.25))
    return percussion_part

def create_trumpet_part(scale, motif, length=16):
    trumpet_part = []
    for i in range(length):
        if random.random() < 0.6:  # 60% chance of a note
            note_name = random.choice(scale) if i % 2 == 0 else motif[i % len(motif)]
            trumpet_note = note.Note(note_name, quarterLength=0.5)
            trumpet_note.volume.velocity = random.randint(90, 110)
            trumpet_part.append(trumpet_note)
        else:
            trumpet_part.append(note.Rest(quarterLength=0.5))
    return trumpet_part

# Create parts for different instruments
piano_part = stream.Part()
piano_part.insert(0, piano)

bass_part = stream.Part()
bass_part.insert(0, bass)

percussion_part = stream.Part()
percussion_part.insert(0, percussion)

trumpet_part = stream.Part()
trumpet_part.insert(0, trumpet)

voice_part = stream.Part()
voice_part.insert(0, voice)

# Generate music parts with Latin song structure
sections = ['intro', 'verse', 'chorus', 'verse', 'chorus', 'bridge', 'chorus', 'outro']

for section in sections:
    length = 16  # All sections will have the same length for consistency

    chord_prog = create_chord_progression(chord_progressions, length)
    piano_part.append(chord_prog)
    
    bassline = create_bassline(chord_progressions, length)
    bass_part.append(bassline)
    
    percussion_part.append(create_percussion_part(length))

    trumpet_melody = create_trumpet_part(c_major_scale, latin_motif, length)
    trumpet_part.append(trumpet_melody)

    if section in ['verse', 'chorus', 'bridge']:
        vocal_melody = create_melody(c_major_scale, latin_motif, length)
        voice_part.append(vocal_melody)
    else:
        voice_part.append(note.Rest(quarterLength=length))

# Add all parts to the score
score.insert(0, piano_part)
score.insert(0, bass_part)
score.insert(0, percussion_part)
score.insert(0, trumpet_part)
score.insert(0, voice_part)

# Save the score as a MIDI file
score.write('midi', fp='latin_song.mid')

print("MIDI file 'latin_song.mid' has been created successfully!")