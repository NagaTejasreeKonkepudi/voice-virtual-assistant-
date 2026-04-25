import os
from dotenv import load_dotenv

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# Load env
load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# Client
client = ElevenLabs(api_key=API_KEY)

# Callbacks
def print_agent_response(response):
    print("Agent:", response)

def print_user_transcript(transcript):
    print("User:", transcript)

# Conversation
conversation = Conversation(
    client,
    AGENT_ID,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_user_transcript=print_user_transcript,
)

# Start
conversation.start_session()

# Stop
input("Press ENTER to stop...\n")

conversation.end_session()