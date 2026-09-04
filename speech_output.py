import subprocess

def speak(text):
    text = str(text)

    print("🔊 Speaking:", text)

    command = f'''
    Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speak.Volume = 100
    $speak.Rate = 0
    $speak.Speak("{text.replace('"', '`"')}")
    '''

    subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True
    )