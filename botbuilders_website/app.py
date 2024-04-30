from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']  # Make sure this key matches what's sent by the frontend
    response = get_bot_response(user_input)  # The keyword-based response function
    return jsonify({'answer': response})  # Sending back a JSON object with an 'answer' key

def get_bot_response(user_input):
    keywords = user_input.lower()
    
    if 'course' in keywords:
        return 'We offer various courses in Computer Science, Business, and Engineering. Which department are you interested in?'
    elif 'computer science' in keywords:
        return 'The Computer Science department offers courses like Programming, Data Structures, and Algorithms.'
    elif 'business' in keywords:
        return 'The Business department offers courses like Marketing, Finance, and Management.'
    elif 'engineering' in keywords:
        return 'The Engineering department offers courses like Mechanical Engineering, Electrical Engineering, and more.'
    else:
        return "Sorry, I couldn't find information related to your query. Please try again or ask another question."

if __name__ == '__main__':
    app.run(debug=True)
