# LeetCode-Question-Randomizer
## Introduction
A Python CLI tool that randomly select coding problems from a curated list, organized by topic and difficulty, while avoiding repetition of topics in consecutive picks. 
Perfect for anyone preparing for technical interviews or practicing daily problem-solving on platforms like LeetCode.

Curated list of questions provided is from Leetcode Top Interview 150: https://leetcode.com/studyplan/top-interview-150/

## Features
- Randomly selects a question from a JSON list
- Avoids repeating the same topic back-to-back
- Lets you mark problems as completed (they’re removed from the list)
- Saves your progress automatically
- Lightweight and easy to customize

## Getting Started
1. Clone the Repository
```python
https://github.com/Alisaa2x/LeetCode-Question-Randomizer.git
```
2. Run the Program <br>
Make sure you have Python 3 installed.
```python
python main.py
```
You’ll be prompted with a random question, its topic, difficulty, and link to LeetCode.

Example: <br>
Initially running the program:
<img width="1026" height="114" alt="Screenshot 2025-10-06 090840" src="https://github.com/user-attachments/assets/3df0c681-d861-467a-9452-044ccee94197" />

Completing the problem prompted, asks if you would like another question to be selected. When you mark a question as completed (y), it will be removed from questions.json so you don’t get repeats:
<img width="1030" height="154" alt="Screenshot 2025-10-06 090932" src="https://github.com/user-attachments/assets/b3d5dead-c7b9-42e2-8567-3c55d59b02f4" />

Ending after completing the question provided:
<img width="1008" height="168" alt="Screenshot 2025-10-06 091014" src="https://github.com/user-attachments/assets/379ba0a9-9699-47b7-9755-3163d725e7c5" />

Not completing the quetion provided:
<img width="702" height="165" alt="Screenshot 2025-10-06 090958" src="https://github.com/user-attachments/assets/545279e0-6ab8-4613-9982-64d04d1d55dd" />

## Project Structure
```python
.
├── main.py           # Main script for running the question picker
├── questions.json    # List of LeetCode problems with topic & difficulty
└── README.md         # Project documentation
```

## Customize It
You can easily expand or modify the question list by editing questions.json.

Each question follows this format:
```json
{
  "title": "Merge Sorted Array",
  "link": "https://leetcode.com/problems/merge-sorted-array/",
  "topic": "array",
  "difficulty": "easy"
}
```

Feel free to:
- Add new problems or remove ones you’ve finished
- Add new topics (like “graphs”, “dynamic programming”, etc.)
- Adjust difficulty tags
