from flask import Flask, request, render_template_string
from conversation import ChatbotConversation
import openai
import os

openai.api_key = os.getenv("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")  # If you stored it as an env variable

app = Flask(__name__)
chatbot = ChatbotConversation()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Chatbot</title>
</head>
<body>
    <h1>AI Chatbot</h1>
    <form method="POST">
        <input type="text" name="user_input" placeholder="Type your message..." />
        <input type="submit" value="Send" />
    </form>
    <hr/>
    <div>
        {% for role, msg in conversation %}
            <p><b>{{ role }}:</b> {{ msg }}</p>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            # Add user message to conversation
            chatbot.add_user_message(user_input)
            # Generate bot response
            response = chatbot.generate_response(user_input)

    return render_template_string(HTML_TEMPLATE, conversation=chatbot.conversation_history)

if __name__ == "__main__":
    app.run(debug=True)


    
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
