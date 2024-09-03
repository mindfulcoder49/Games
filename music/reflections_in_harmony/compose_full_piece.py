from music21 import stream

# Import each section from their respective files
from introduction import create_introduction
from first_theme import create_first_theme
from transition import create_transition
from second_theme import create_second_theme
from development import create_development
from climax import create_climax
from recapitulation import create_recapitulation
from coda import create_coda

def compose_full_piece():
    # Initialize the final score
    full_piece = stream.Score()

    # Add each section in order
    full_piece.append(create_introduction())
    full_piece.append(create_first_theme())
    full_piece.append(create_transition())
    full_piece.append(create_second_theme())
    full_piece.append(create_development())
    full_piece.append(create_climax())
    full_piece.append(create_recapitulation())
    full_piece.append(create_coda())

    # Save the full composition as a MIDI file
    full_piece.write('midi', fp='reflections_in_harmony.mid')
    print("MIDI file 'reflections_in_harmony.mid' has been created successfully!")

if __name__ == "__main__":
    compose_full_piece()
