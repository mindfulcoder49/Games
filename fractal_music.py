from music21 import stream, note, chord, meter, key, tempo, instrument
import math

# Initialize the score and set key and time signature
score = stream.Score()
score.insert(0, key.Key('C'))
score.insert(0, meter.TimeSignature('4/4'))
score.insert(0, tempo.MetronomeMark(number=120))

# Define instruments
piano = instrument.Piano()
violin = instrument.Violin()
cello = instrument.Violoncello()
flute = instrument.Flute()

# Function to generate a sine wave pattern for melody
def generate_sine_wave_melody(start_pitch='C4', length=16, amplitude=2, frequency=0.2):
    melody = []
    base_pitch = note.Note(start_pitch).pitch.midi  # Convert start pitch to MIDI number
    for i in range(length):
        pitch_variation = int(amplitude * math.sin(frequency * i * 2 * math.pi))  # Sine wave variation
        next_pitch = base_pitch + pitch_variation
        melody.append(note.Note(next_pitch, quarterLength=1))
    return melody

# Function to generate a Fibonacci sequence for rhythm
def generate_fibonacci_rhythm(length=16):
    rhythm = [1, 1]  # Start with two quarter notes
    for _ in range(length - 2):
        rhythm.append(rhythm[-1] + rhythm[-2])  # Fibonacci sequence for rhythm
    # Normalize rhythm to fit within a reasonable time (1-2 quarter lengths)
    rhythm = [r % 2 + 0.5 for r in rhythm]
    return rhythm

# Create parts for the score
melody_part = stream.Part()
melody_part.insert(0, flute)

harmony_part = stream.Part()
harmony_part.insert(0, violin)

bass_part = stream.Part()
bass_part.insert(0, cello)

chords_part = stream.Part()
chords_part.insert(0, piano)

# Generate a sine wave melody
melody_notes = generate_sine_wave_melody(length=32, amplitude=5, frequency=0.1)
melody_part.append(melody_notes)

# Generate a harmony line that complements the melody using Fibonacci rhythm
harmony_notes = []
harmony_rhythm = generate_fibonacci_rhythm(length=32)
base_harmony_pitch = note.Note('A3').pitch.midi  # Base pitch for harmony

for i, duration in enumerate(harmony_rhythm):
    pitch_variation = int(3 * math.sin(0.2 * i * 2 * math.pi))  # Sine variation for harmony
    harmony_note = note.Note(base_harmony_pitch + pitch_variation, quarterLength=duration)
    harmony_notes.append(harmony_note)

harmony_part.append(harmony_notes)

# Create a bass line using a descending scale pattern with Fibonacci rhythmic variation
bass_notes = []
bass_rhythm = generate_fibonacci_rhythm(length=32)
base_bass_pitch = note.Note('C2').pitch.midi

for i, duration in enumerate(bass_rhythm):
    bass_note = note.Note(base_bass_pitch - i % 7, quarterLength=duration)  # Descending pattern
    bass_notes.append(bass_note)

bass_part.append(bass_notes)

# Generate chords that evolve with the melody
chord_sequence = [
    ['C4', 'E4', 'G4'],
    ['F4', 'A4', 'C5'],
    ['G4', 'B4', 'D5'],
    ['E4', 'G4', 'B4'],
    ['A4', 'C5', 'E5'],
    ['D4', 'F4', 'A4'],
    ['G4', 'B4', 'D5']
]

# Create a chord pattern following the Fibonacci rhythm
chord_progression = []
for i, chord_notes in enumerate(chord_sequence):
    current_chord = chord.Chord(chord_notes, quarterLength=2)  # Static quarter length for simplicity
    chord_progression.append(current_chord)
    if i % 2 == 0:  # Add a rest after every second chord for rhythmic variety
        chord_progression.append(note.Rest(quarterLength=1))

chords_part.append(chord_progression)

# Add all parts to the score
score.insert(0, melody_part)
score.insert(0, harmony_part)
score.insert(0, bass_part)
score.insert(0, chords_part)

# Save the score as a MIDI file
score.write('midi', fp='complex_fractal_piece.mid')

print("MIDI file 'complex_fractal_piece.mid' has been created successfully!")
