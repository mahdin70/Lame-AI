import sys
import time
import threading
from agents.joke_agent import generate_lame_joke
from utils.email_sender import send_email

def send_lame_joke(topic, joke):
    subject = f"AI Agent Testing : Daily Dose of Lame Jokes"
    body = f"{joke}"
    send_email(subject, body)

def show_loader(stop_event):
    spinner = ['|', '/', '-', '\\']
    while not stop_event.is_set():
        for char in spinner:
            sys.stdout.write(f'\rGenerating joke... {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

def generate_with_loader(topic, attempt):
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=show_loader, args=(stop_event,))
    loader_thread.start()
    
    joke = generate_lame_joke(topic, attempt)
    
    stop_event.set()
    loader_thread.join()
    return joke

def main():
    print("Welcome to the Lame Joke Agent!")
    while True:
        topic = input("\nEnter a topic for a lame joke (or 'quit' to exit): ").strip()
        if topic.lower() == "quit":
            print("Exiting...")
            break
        if not topic:
            print("Please enter a valid topic or 'quit'.")
            continue

        attempt = 1
        while True:
            joke = generate_with_loader(topic, attempt)
            print(f"\nGenerated joke:\n{joke}")
            
            action = input("\nType 'send' to send, 'regen' to regenerate, or 'back' to choose a new topic: ").strip().lower()
            
            if action == "send":
                print(f"Sending the joke about '{topic}'...")
                send_lame_joke(topic, joke)
                break
            elif action == "regen":
                attempt += 1
                print("Regenerating a new joke...")
                continue
            elif action == "back":
                print("Returning to topic selection...")
                break
            else:
                print(f"Interpreting '{action}' as a new topic...")
                topic = action 
                attempt = 1  
                continue

if __name__ == "__main__":
    main()