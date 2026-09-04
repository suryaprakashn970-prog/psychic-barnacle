from speech_output import speak
from agent import calling


def main():

    print("🤖 Jarvis is ready!")

    while True:

        # ⌨️ Get user's query
        query = input("🧑 You: ").strip()

        if not query:
            continue

        # Exit commands
        if query.lower() in ["exit", "quit", "stop", "bye"]:
            speak("Goodbye!")
            break

        # 🧠 Send query to agent
        answer = calling(query)

        # 🤖 Show answer
        print(f"🤖 Jarvis: {answer}")

        # 🔊 Speak answer
        speak(answer)


if __name__ == "__main__":
    main()