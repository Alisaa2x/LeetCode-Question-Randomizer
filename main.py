import json
import random
import os

questions_file = 'questions.json'

# Load questions from a JSON file
def load_questions(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return json.load(f)
    
# Save questions back to the JSON file
def save_questions(filename, questions):
    with open(filename, 'w') as f:
        json.dump(questions, f, indent=4)

# Get a random question that doesn't have the same topic as last time
def get_random_question(questions, last_topic):
    filtered = [question for question in questions if question['topic'] != last_topic]
    if not filtered:
        return None
    return random.choice(filtered)

def main():
    questions = load_questions(questions_file)
    if not questions:
        print("No questions found. Add more questions to your list.")
        return
    
    last_topic = None

    while questions:
        question = get_random_question(questions, last_topic)
        if not question:
            print("No more questions with a different topic available.")
            break

        print(f"\n🎯 Your question is: {question['title']}")
        print(f"🧠 Topic: {question['topic']} | 📈 Difficulty: {question['difficulty']}")
        print(f"🔗 Link: {question['link']}")

        response = input("✅ Did you complete it? (y/n): ").strip().lower()
        if response == 'y':
            questions.remove(question)
            save_questions(questions_file, questions)
            last_topic = question['topic']
        else:
            print("Okay, we'll keep it for later.")
            last_topic = None

        cont = input("➡️  Get another question? (y/n): ").strip().lower()
        if cont != 'y':
            break

    print("✅ Done for now. Happy coding!")

if __name__ == "__main__":
    main()