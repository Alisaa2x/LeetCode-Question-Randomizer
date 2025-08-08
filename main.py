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