from music21 import stream, note, chord, meter, key, tempo, instrument, scale
import random

def create_chord_progression(key_obj, num_chords):
    scale_degrees = [1, 4, 5, 6, 2, 3]  # Common chord progressions
    chords = []
    for _ in range(num_chords):
        degree = random.choice(scale_degrees)
        chord_pitches = [key_obj.pitchFromDegree(degree + i) for i in [1, 3, 5]]
        chords.append(chord.Chord(chord_pitches))
    return chords

def create_melody(key_obj, duration, rhythm_pattern):
    melody = []
    scale_obj = scale.MajorScale(key_obj.tonic)
    for _ in range(int(duration / sum(rhythm_pattern))):
        for note_duration in rhythm_pattern:
            if random.random() < 0.1:  # 10% chance of rest
                melody.append(note.Rest(quarterLength=note_duration))
            else:
                scale_degree = random.randint(1, 7)
                pitch = scale_obj.pitchFromDegree(scale_degree)
                melody.append(note.Note(pitch, quarterLength=note_duration))
    return melody

def create_arpeggio(chord_obj, pattern, duration):
    notes = []
    chord_notes = chord_obj.pitches
    for _ in range(int(duration / sum(pattern))):
        for idx, note_duration in enumerate(pattern):
            pitch = chord_notes[idx % len(chord_notes)]
            notes.append(note.Note(pitch, quarterLength=note_duration))
    return notes

def create_composition():
    score = stream.Score()
    
    # Set up the piece
    key_obj = key.Key('C')
    score.append(key_obj)
    score.append(meter.TimeSignature('4/4'))
    score.append(tempo.MetronomeMark(number=60))
    
    # Create parts
    melody_part = stream.Part(instrument.Guitar())
    harmony_part = stream.Part(instrument.Piano())
    bass_part = stream.Part(instrument.Bass())
    
    # Generate content
    total_measures = 64
    for i in range(total_measures // 4):  # Create 4-measure phrases
        chords = create_chord_progression(key_obj, 4)
        
        # Melody
        melody = create_melody(key_obj, 16, [0.5, 0.5, 1, 1])
        melody_part.append(melody)
        
        # Harmony (arpeggios)
        for chord_obj in chords:
            harmony_part.append(create_arpeggio(chord_obj, [0.25, 0.25, 0.25, 0.25], 4))
        
        # Bass
        for chord_obj in chords:
            bass_note = note.Note(chord_obj.root(), quarterLength=4)
            bass_part.append(bass_note)
    
    # Add parts to score
    score.append(melody_part)
    score.append(harmony_part)
    score.append(bass_part)
    
    return score

# Generate and save the composition
composition = create_composition()
composition.write('midi', fp='mozart_beethoven_inspired.mid')
print("MIDI file 'mozart_beethoven_inspired.mid' has been created successfully!")