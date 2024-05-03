import ast
import openai
from mido import MidiFile, MidiTrack, Message
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def request_midi_data(style):
    """Request MIDI data from OpenAI API based on the specified musical style."""
    print("Requesting MIDI data...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that converts melody descriptions into textual MIDI representations. You are knowledgeable in different musical styles and can translate descriptive notes into MIDI format accordingly."
            },
            {
                "role": "user",
                "content": f"""Take a deep breath and let's immerse ourselves into the world of music composition. Imagine we are in the presence of a grand piano, ready to weave a melody that resonates with the elegance and intricacy of {style}. First, contemplate the unique characteristics that define the {style} style of music. Reflect on the emotions it conveys, the pace it follows, and the type of notes and scales that are predominantly used. Think step by step, and with each note, envision how it contributes to building a melody that truly embodies the essence of {style}. With this mindful approach, kindly provide me a sequence of notes where each note is represented as a tuple. The first element should be the pitch (integer MIDI value), and the second the duration (float where 0.125 is an eighth note, 0.25 is a quarter note, 0.5 is a half note, 1 is a whole note, and 2 is a double whole note). An example to guide you would be pitch_duration_data = [(60, 0.25), (62, 0.25), (64, 0.5), ...]. Let the music flow!"""
            }
        ],
        max_tokens=1000
    )
    print("Data received.")
    return response['choices'][0]['message']['content']

def parse_generated_text(generated_text):
    """Parse the generated text into a usable data structure."""
    print("Parsing received data...")
    try:
        start_index = generated_text.find('[')
        end_index = generated_text.find(']') + 1
        if start_index != -1 and end_index != -1:
            data_str = generated_text[start_index:end_index]
            pitch_duration_data = ast.literal_eval(data_str)
            if isinstance(pitch_duration_data, list):
                print("Parsing successful.")
                return pitch_duration_data
    except Exception as e:
        print(f"Error in parsing: {e}")
    return None

def create_midi(pitch_duration_data, filename='melody.mid'):
    """Create a MIDI file based on the parsed data."""
    print("Creating MIDI file...")
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    for pitch, duration in pitch_duration_data:
        time = int(duration * 480)  # Convert float duration to MIDI ticks (assuming 480 ticks per beat)
        track.append(Message('note_on', note=pitch, velocity=64, time=0))
        track.append(Message('note_off', note=pitch, velocity=64, time=time))
    mid.save(filename)
    print(f"MIDI file created: {filename}")

def main():
    """Main function to orchestrate the generation and parsing of MIDI data."""
    specified_style = 'EDM, House , Avicii style, melody with chords for 16 bars, 124 bpm'
    print(f"Starting process for {specified_style} melody...")
    generated_text = request_midi_data(specified_style)
    print(generated_text)
    pitch_duration_data = parse_generated_text(generated_text)
    if pitch_duration_data:
        create_midi(pitch_duration_data)
    print("Process completed.")

if __name__ == "__main__":
    main()
