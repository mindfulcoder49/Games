from music21 import stream, note, chord, meter, key, tempo, instrument, dynamics, articulations
import random

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))

# Set a tempo for the piece (120 BPM, common for pop songs)
score.insert(0, tempo.MetronomeMark(number=120))

# Define instruments
lead_synth = instrument.ElectricPiano()
pad_synth = instrument.Piano()  # Using Piano instead of Synthesizer
bass = instrument.ElectricBass()
drums = instrument.Percussion()  # Using Percussion instead of DrumSet
voice = instrument.Vocalist()

# Define chord progressions for sections (I-V-vi-IV in C major, known as the "pop punk progression")
chord_progressions = [
    ['C4', 'E4', 'G4'],  # C major (I)
    ['G4', 'B4', 'D5'],  # G major (V)
    ['A4', 'C5', 'E5'],  # A minor (vi)
    ['F4', 'A4', 'C5'],  # F major (IV)
]

# Define C major scale for melodic lines
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Catchy hooks and motifs
verse_motif = ['E4', 'G4', 'A4', 'G4']
chorus_hook = ['C5', 'B4', 'A4', 'G4', 'F4', 'G4', 'A4']

def create_chord_progression(chord_notes, length=4):
    progression = []
    for _ in range(length):
        for notes in chord_notes:
            c = chord.Chord(notes, quarterLength=1)
            progression.append(c)
    return progression

def create_melody(scale, motif, length=8):
    melody = []
    for i in range(length):
        note_name = random.choice(scale) if i % 2 == 0 else motif[i % len(motif)]
        melody_note = note.Note(note_name, quarterLength=0.5)
        melody_note.volume.velocity = random.randint(80, 100)
        melody.append(melody_note)
    return melody

def create_bassline(chord_progression, length=4):
    bassline = []
    for _ in range(length):
        for chord_notes in chord_progression:
            root_note = note.Note(chord_notes[0].replace('4', '2'), quarterLength=1)
            root_note.volume.velocity = 100
            bassline.append(root_note)
    return bassline

def create_drum_beat():
    beat = stream.Voice()
    for _ in range(4):
        kick = note.Note('C2', quarterLength=1)
        snare = note.Note('D2', quarterLength=1)
        hi_hat1 = note.Note('F#2', quarterLength=0.5)
        hi_hat2 = note.Note('F#2', quarterLength=0.5)
        hi_hat3 = note.Note('F#2', quarterLength=0.5)
        hi_hat4 = note.Note('F#2', quarterLength=0.5)
        beat.append(kick)
        beat.append(hi_hat1)
        beat.append(hi_hat2)
        beat.append(snare)
        beat.append(hi_hat3)
        beat.append(hi_hat4)
    return beat

def create_vocal_melody(scale, hook, length=8):
    melody = []
    for i in range(length):
        note_name = hook[i % len(hook)]
        vocal_note = note.Note(note_name, quarterLength=1 if i % 2 == 0 else 0.5)
        vocal_note.volume.velocity = random.randint(90, 110)
        melody.append(vocal_note)
        if i % 2 == 1:
            melody.append(note.Rest(quarterLength=0.5))
    return melody

# Create parts for different instruments
lead_synth_part = stream.Part()
lead_synth_part.insert(0, lead_synth)

pad_synth_part = stream.Part()
pad_synth_part.insert(0, pad_synth)

bass_part = stream.Part()
bass_part.insert(0, bass)

drums_part = stream.Part()
drums_part.insert(0, drums)

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
    pad_synth_part.append(chord_prog)
    
    bassline = create_bassline(chord_progressions, length // 4)
    bass_part.append(bassline)
    
    for _ in range(length // 4):
        drums_part.append(create_drum_beat())

    if section in ['verse', 'chorus', 'bridge']:
        melody = create_melody(c_major_scale, verse_motif if section == 'verse' else chorus_hook, length)
        lead_synth_part.append(melody)

        vocal_melody = create_vocal_melody(c_major_scale, chorus_hook if section == 'chorus' else verse_motif, length)
        voice_part.append(vocal_melody)

# Add all parts to the score
score.insert(0, lead_synth_part)
score.insert(0, pad_synth_part)
score.insert(0, bass_part)
score.insert(0, drums_part)
score.insert(0, voice_part)

# Save the score as a MIDI file
score.write('midi', fp='pop_hit_song.mid')

print("MIDI file 'pop_hit_song.mid' has been created successfully!")