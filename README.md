Description:

The MIDI Generator is an innovative tool designed to transform descriptive musical prompts into MIDI representations, providing users with a seamless pathway to translate creative ideas into tangible musical compositions. Leveraging the power of OpenAI's language models and MIDI manipulation libraries, this application offers a dynamic platform for crafting melodies across diverse musical genres with ease and precision.

Features:

Dynamic Prompt Interpretation: The MIDI Generator employs advanced natural language processing techniques to interpret user prompts, enabling seamless communication of musical concepts and preferences.
Style Customization: Users can specify the desired musical style, allowing for the generation of MIDI data tailored to a wide range of genres, from classical symphonies to contemporary EDM tracks.
Flexible MIDI Output: The generated MIDI data is meticulously structured to accommodate various musical nuances, including pitch, duration, and tempo, providing users with a versatile framework for musical exploration.
Error Handling: The application incorporates robust error handling mechanisms to ensure smooth execution, mitigating potential parsing errors and streamlining the generation process.
User-Friendly Interface: With clear instructions and intuitive interaction patterns, the MIDI Generator offers a user-friendly experience, empowering both novice and experienced musicians to engage in creative expression effortlessly.
How to Run:

Installation:
Ensure that Python 3.x is installed on your system.
Clone the repository from GitHub.
Install the required dependencies by running pip install -r requirements.txt.
Set up an OpenAI API key by registering at OpenAI.
Configuration:
Create a .env file in the project directory.
Add your OpenAI API key to the .env file: OPENAI_API_KEY=your_api_key_here.
Execution:
Open a terminal or command prompt.
Navigate to the project directory.
Run the main.py script using python main.py.
Input:
Upon execution, the program will prompt you to specify the musical style in a descriptive manner. Follow the instructions provided to articulate your desired musical characteristics effectively.
Output:
The program will generate MIDI data based on your input, incorporating the specified musical style and nuances.
The MIDI file will be saved in the project directory with the default name melody.mid.
Note:

For optimal results, provide clear and concise descriptions of the desired musical style, including elements such as emotions, tempo, and preferred instruments.
Experiment with different prompts and styles to explore the full potential of the MIDI Generator and unleash your creative prowess in music composition.
Author:

[Eugene Solovei]

Acknowledgements:

This project utilizes the OpenAI API for natural language processing.
MIDI manipulation is performed using the mido library.
Environment variables are managed using the dotenv library.
Disclaimer:

The MIDI Generator is provided as-is without any warranty. Users are encouraged to use the tool responsibly and adhere to relevant copyright and intellectual property regulations when generating musical compositions.

