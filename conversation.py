# conversation.py

class ChatbotConversation:
    def __init__(self):
        self.conversation_history = []
        self.user_name = None   # To store user’s name

    def add_user_message(self, message):
        self.conversation_history.append(("User", message))

    def add_bot_message(self, message):
        self.conversation_history.append(("Bot", message))

    def generate_response(self, user_input):
        # Convert user input to lowercase for easy keyword checks
        lower_input = user_input.lower()

        if "hello" in lower_input:
            reply = "Hello! How can I help you today?"
        elif "my name is" in lower_input:
            reply = self.handle_name_input(user_input)
        else:
            # If we already have the user's name, use it in responses
            if self.user_name:
                reply = f"I'm still learning, {self.user_name}. Could you rephrase or provide more details?"
            else:
                reply = "I'm still learning. Could you rephrase or provide more details?"
        
        self.add_bot_message(reply)
        return reply

    def handle_name_input(self, user_input):
        """
        Looks for the phrase "my name is" and extracts the name.
        Then sets self.user_name, and returns a nice greeting.
        """
        # Example input: "My name is Ziad"
        # Let's split by "my name is"
        # or parse more robustly if needed
        name_part = user_input.lower().split("my name is")
        if len(name_part) > 1:
            # The part after "my name is" might be " Ziad"
            potential_name = name_part[1].strip()
            # Capitalize the first letter (or do more advanced parsing if needed)
            potential_name = potential_name.capitalize()
            self.user_name = potential_name
            return f"Nice to meet you, {self.user_name}!"
        else:
            return "I couldn't catch your name. Please try again."
