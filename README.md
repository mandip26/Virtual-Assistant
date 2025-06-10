# Bug - Voice Assistant

Bug is a personal voice assistant that connects to your devices and helps you perform various tasks through voice commands.

## Features

- Voice command recognition
- Web search capabilities
- WhatsApp integration for messages and calls
- Contact management
- System command execution
- Application launching

## Requirements

- Python 3.11+
- Android device (optional, for mobile integration)

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r Requirements.txt
   ```
3. Set up the virtual environment (optional):
   ```bash
   python -m venv envbug
   source envbug/Scripts/activate  # On Windows: envbug\Scripts\activate
   ```

## Usage

Run the assistant with:

```bash
python run.py
```

The assistant will start listening for the wake word "bug" and will execute commands based on your voice input.

### Available Commands

- Web searches
- Contact management
- WhatsApp messaging and calling
- System application launching
- And more...

## Project Structure

- `Backend/`: Core functionality and command processing
- `Frontend/`: Web interface using Eel
- `run.py`: Main entry point for the application
- `main.py`: Frontend initialization
- `device.bat`: Scripts for connecting to Android devices

## Database

The application uses SQLite for storing:
- Contacts
- Web commands
- System commands
