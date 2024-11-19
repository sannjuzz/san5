from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Quiz data
total_questions = 5
questions = [
    {
        'question': 'What does AI stand for?',
        'options': ['Artificial Inception', 'Automated Intelligence', 'Artificial Intelligence', 'Advanced Interpretation'],
        'answer': 'Artificial Intelligence'
    },
    {
        'question': 'Which programming language is commonly used in AI development?',
        'options': ['Java', 'Python', 'C++', 'Ruby'],
        'answer': 'Python'
    },
    {
        'question': 'What is the name of the AI system developed by OpenAI that plays Dota 2?',
        'options': ['AlphaGo', 'Watson', 'GPT-3', 'OpenAI Five'],
        'answer': 'OpenAI Five'
    },
    {
        'question': 'Which AI technique is inspired by the functioning of the human brain?',
        'options': ['Neural Networks', 'Genetic Algorithms', 'Expert Systems', 'Fuzzy Logic'],
        'answer': 'Neural Networks'
    },
    {
        'question': 'What is the term used to describe AI systems improving themselves over time without human intervention?',
        'options': ['Artificial Evolution', 'Deep Learning', 'Machine Learning', 'Self-Optimization'],
        'answer': 'Machine Learning'
    },
    {
        'question': 'Which AI concept involves computers understanding, interpreting, and generating human-like languages?',
        'options': ['Computer Vision', 'Natural Language Processing', 'Speech Recognition', 'Sentiment Analysis'],
        'answer': 'Natural Language Processing'
    },
    {
        'question': 'What is the famous AI test proposed by Alan Turing?',
        'options': ['Turing Test', 'Turing Challenge', 'Turing Experiment', 'Turing Quest'],
        'answer': 'Turing Test'
    },
    {
        'question': 'What is the name of the AI technique used to train machines to perform tasks by example?',
        'options': ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning', 'Semi-Supervised Learning'],
        'answer': 'Supervised Learning'
    },
    {
        'question': 'Which AI application is used to analyze visual data like images and videos?',
        'options': ['Speech Recognition', 'Natural Language Processing', 'Computer Vision', 'Sentiment Analysis'],
        'answer': 'Computer Vision'
    },
    {
        'question': 'What is the name of the AI technique that mimics the way the human brain learns from experience?',
        'options': ['Reinforcement Learning', 'Genetic Algorithms', 'Neural Networks', 'Expert Systems'],
        'answer': 'Reinforcement Learning'
    },
    {
        'question': 'What is the field of AI that focuses on giving computers the ability to see?',
        'options': ['Natural Language Processing', 'Computer Vision', 'Sentiment Analysis', 'Speech Recognition'],
        'answer': 'Computer Vision'
    },
    {
        'question': 'What is the term used to describe the ability of AI systems to understand, interpret, and generate human-like speech?',
        'options': ['Speech Recognition', 'Natural Language Processing', 'Computer Vision', 'Sentiment Analysis'],
        'answer': 'Speech Recognition'
    },
    {
        'question': 'What is the name of the AI technique used to find patterns in data without explicit programming?',
        'options': ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning', 'Semi-Supervised Learning'],
        'answer': 'Unsupervised Learning'
    },
    {
        'question': 'Which AI technique is used to make decisions by considering long-term rewards?',
        'options': ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning', 'Semi-Supervised Learning'],
        'answer': 'Reinforcement Learning'
    },
    {
        'question': 'What is the name of the AI technique used to generate human-like text based on input?',
        'options': ['Chatbots', 'Recurrent Neural Networks', 'Long Short-Term Memory Networks', 'Transformers'],
        'answer': 'Transformers'
    },
    {
        'question': 'Which AI technique is used to understand and analyze the sentiment behind text?',
        'options': ['Natural Language Processing', 'Computer Vision', 'Speech Recognition', 'Sentiment Analysis'],
        'answer': 'Sentiment Analysis'
    },
    {
        'question': 'What is the name of the AI technique used to predict future events based on historical data?',
        'options': ['Predictive Analytics', 'Time Series Analysis', 'Regression Analysis', 'Machine Learning'],
        'answer': 'Predictive Analytics'
    },
    {
        'question': 'Which AI application is used to understand and generate human-like handwriting?',
        'options': ['Speech Recognition', 'Natural Language Processing', 'Optical Character Recognition', 'Sentiment Analysis'],
        'answer': 'Optical Character Recognition'
    },
    {
        'question': 'What is the term used to describe the process of training an AI model with a large dataset multiple times?',
        'options': ['Repetition Learning', 'Deep Learning', 'Iterative Learning', 'Continual Learning'],
        'answer': 'Deep Learning'
    },
    {
        'question': 'What is the name of the AI technique that mimics the evolutionary process to generate solutions?',
        'options': ['Genetic Algorithms', 'Reinforcement Learning', 'Neural Networks', 'Expert Systems'],
        'answer': 'Genetic Algorithms'
    }
]
chosen_questions = random.sample(questions, 5)
# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Quiz route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global chosen_questions
    if request.method == 'POST':
        # Get answers submitted by user
        answers = []
        for i in range(total_questions):
            answer_key = 'q' + str(i+1)
            user_answer = request.form.get(answer_key)
            answers.append(user_answer)
        
        # Calculate score
            
        score = 0
        for i in range(total_questions):
            print( answers[i]+":"+chosen_questions[i]['answer'])
            if answers[i] == chosen_questions[i]['answer']:

                score += 1
        
        return render_template('result1.html', user_answers = answers,questions=chosen_questions, score=score, total=len(chosen_questions),enumerate=enumerate)
    chosen_questions = random.sample(questions, total_questions)
    return render_template('quiz.html', questions=chosen_questions,len=len,range=range)

if __name__ == '__main__':
    app.run(debug=True)
