import note_seq
# from magenta.models.music_vae import TrainedModel
# import tensorflow as tf
# tf.disable_v2_behavior() 


def make_music_harder(melody_increase, ornamentation, midi_path):

    input_sequence = note_seq.midi_file_to_note_sequence(midi_path)
    # Adjust the temperature based on both difficulty_increase and ornamentation
    max_difficulty = 5.0  # Define maximum expected value for difficulty_increase
    max_ornamentation = 10  # Define maximum expected value for ornamentation

    # Normalize parameters
    norm_difficulty = min(melody_increase / max_difficulty, 1.0)
    norm_ornamentation = min(ornamentation / max_ornamentation, 1.0)

    # Compute temperature based on both parameters
    temperature = 1.0 + (norm_difficulty * 0.5) + (norm_ornamentation * 0.5)
