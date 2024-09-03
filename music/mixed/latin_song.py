from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, articulations
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (96 BPM, typical for a Latin song)
score.insert(0, tempo.MetronomeMark(number=96))

# Define instruments
acoustic_guitar = instrument.AcousticGuitar()
maracas = instrument.Maracas()
congas = instrument.CongaDrum()
trumpet = instrument.Trumpet()
voice = instrument.Vocalist()

# Define chord progressions for sections (ii-V-I in C major, common in Latin music)
chord_progressions = [
    ['D4', 'F4', 'A4'],  # D minor (ii)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['C4', 'E4', 'G4'],  # C major (I)
    ['A4', 'C5', 'E5'],  # A minor (vi)
]

# Define C major scale for melodic lines
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Catchy hooks and motifs
verse_motif = ['E4', 'G4', 'A4', 'F4']
chorus_hook = ['G4', 'F4', 'E4', 'D4', 'C4']

def create_chord_progression(chord_notes, length=4):
    progression = []
    for _ in range(length):
        for notes in chord_notes:
            c = chord.Chord(notes, quarterLength=1)
            c.volume.velocity = random.randint(60, 100)
            progression.append(c)
    return progression

def create_melody(scale, motif, length=8):
    melody = []
    for i in range(length):
        note_name = random.choice(scale) if i % 2 == 0 else motif[i % len(motif)]
        melody_note = note.Note(note_name, quarterLength=0.5)
        melody_note.volume.velocity = random.randint(80, 100)
        if random.random() > 0.7:
            melody_note.articulations.append(articulations.Accent())  # Add accents
        if random.random() > 0.5:
             # Add grace notes for Latin flavor
            grace_note = note.Note(random.choice(scale), quarterLength=0.25)
            melody.append(grace_note)
        melody.append(melody_note)
    return melody

def create_bassline(chord_progression, length=4):
    bassline = []
    for _ in range(length):
        for chord_notes in chord_progression:
            root_note = note.Note(chord_notes[0].replace('4', '2'), quarterLength=1)
            root_note.volume.velocity = 100
            if random.random() > 0.5:
                root_note.articulations.append(articulations.Accent())  # Add accents
            bassline.append(root_note)
    return bassline

def create_drum_beat(length=4):
    beat = stream.Voice()
    for _ in range(length):
        conga = note.Note('C2', quarterLength=1)
        maraca = note.Note('F#2', quarterLength=0.5)
        conga.volume.velocity = 90
        maraca.volume.velocity = 70
        beat.append(conga)
        beat.append(maraca)
    return beat

def create_vocal_melody(scale, hook, length=8):
    melody = []
    for i in range(length):
        note_name = hook[i % len(hook)]
        vocal_note = note.Note(note_name, quarterLength=1 if i % 2 == 0 else 0.5)
        vocal_note.volume.velocity = random.randint(90, 110)
        if random.random() > 0.3:
            # Add trills for Latin flavor
            trill_note = note.Note(random.choice(scale), quarterLength=0.25)
            melody.append(trill_note)
        melody.append(vocal_note)
        if i % 2 == 1:
            melody.append(note.Rest(quarterLength=0.5))
    return melody

# Create parts for different instruments
guitar_part = stream.Part()
guitar_part.insert(0, acoustic_guitar)

percussion_part = stream.Part()
percussion_part.insert(0, maracas)

conga_part = stream.Part()
conga_part.insert(0, congas)

trumpet_part = stream.Part()
trumpet_part.insert(0, trumpet)

voice_part = stream.Part()
voice_part.insert(0, voice)

# Generate music parts with pop song structure
sections = ['intro', 'verse', 'chorus', 'verse', 'chorus', 'bridge', 'chorus', 'outro']

for section in sections:
    if section in ['intro', 'outro']:
        length = 4
    elif section == 'bridge':
        length = 8
    else:
        length = 16

    chord_prog = create_chord_progression(chord_progressions, length // 4)
    guitar_part.append(chord_prog)
    
    bassline = create_bassline(chord_progressions, length // 4)
    conga_part.append(bassline)
    
    drum_beat = create_drum_beat(length // 4)
    percussion_part.append(drum_beat)

    if section in ['verse', 'chorus', 'bridge']:
        melody = create_melody(c_major_scale, verse_motif if section == 'verse' else chorus_hook, length)
        trumpet_part.append(melody)

        vocal_melody = create_vocal_melody(c_major_scale, chorus_hook if section == 'chorus' else verse_motif, length)
        voice_part.append(vocal_melody)

# Add all parts to the score
score.insert(0, guitar_part)
score.insert(0, percussion_part)
score.insert(0, conga_part)
score.insert(0, trumpet_part)
score.insert(0, voice_part)

# Save the score as a MIDI file
score.write('midi', fp='latin_song.mid')

print("MIDI file 'latin_song.mid' has been created successfully!")
