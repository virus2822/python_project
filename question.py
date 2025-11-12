# Developer: VIRUS
print("=== Personal Question Program ===")
print("Developer: VIRUS\n")

# 5 question types
question_types = ["Basic", "Interests", "Life", "Personality", "SocialLife"]

# Ask user to pick one
question_type = input("What question type do you like? (Basic/Interests/Life/Personality/SocialLife): ").strip().lower()

# === BASIC QUESTIONS ===
if question_type == "basic":
    print("\nLet's start with Basic Questions!\n")
    basic_questions = [
        "What is your full name?",
        "When is your birthday?",
        "Where were you born?",
        "What’s your favorite color?",
        "Do you prefer morning or night?",
        "What’s your favorite food?",
        "Do you have any pets?",
        "What’s your favorite movie?",
        "What’s your favorite season of the year?",
        "Do you like tea or coffee more?",
        "What is your favorite song right now?",
        "What is your favorite book?",
        "Do you enjoy spending time indoors or outdoors?",
        "What is your zodiac sign?",
        "Do you prefer sweet or spicy food?",
        "What language do you speak the most?",
        "What’s your favorite holiday?",
        "What is your favorite time of day?",
        "What is your favorite number?",
        "Do you prefer texting or talking on the phone?"
    ]
    for q in basic_questions:
        input(q + " ")
    print("Thank you for your answers 💖 I hope you like my project!")

# === INTERESTS QUESTIONS ===
elif question_type == "interests":
    print("\nLet's talk about your Interests!\n")
    interests_questions = [
        "What are your hobbies?",
        "Do you like playing video games?",
        "What kind of music do you enjoy?",
        "Do you like reading books?",
        "What’s your favorite sport?",
        "Do you like drawing or painting?",
        "Have you ever tried cooking as a hobby?",
        "What’s your favorite TV show?",
        "Do you enjoy traveling?",
        "What’s your favorite place you’ve visited?",
        "Do you like photography?",
        "Do you prefer watching movies or series?",
        "Do you play any musical instruments?",
        "What’s something new you’d like to learn?",
        "Do you enjoy hiking or nature walks?",
        "Are you more into art or science?",
        "What’s your favorite outdoor activity?",
        "Do you enjoy dancing?",
        "What’s your favorite game to play?",
        "How do you usually spend your weekends?"
    ]
    for q in interests_questions:
        input(q + " ")
    print("Thank you for your answers 💖 I hope you like my project!")

# === LIFE QUESTIONS ===
elif question_type == "life":
    print("\nLet's talk about your Life and Dreams!\n")
    life_questions = [
        "What do you want to achieve in life?",
        "What is your dream job?",
        "Do you like setting goals for yourself?",
        "Where do you see yourself in 10 years?",
        "If you could live anywhere, where would it be?",
        "What motivates you every day?",
        "What’s one thing you really want to learn?",
        "Do you believe in luck or hard work?",
        "What’s something you’ve always dreamed of doing?",
        "Who inspires you the most?",
        "What’s one goal you’ve achieved that makes you proud?",
        "If you could change one thing in your life, what would it be?",
        "What’s your biggest fear about the future?",
        "What’s something you hope never changes about you?",
        "What’s one skill you want to master?",
        "What kind of legacy do you want to leave behind?",
        "What do you value most in life?",
        "What would you do if money wasn’t a problem?",
        "Do you believe dreams have meaning?",
        "What does success mean to you?"
    ]
    for q in life_questions:
        input(q + " ")
    print("Thank you for your answers 💖 I hope you like my project!")

# === PERSONALITY QUESTIONS ===
elif question_type == "personality":
    print("\nLet's learn about your Personality!\n")
    personality_questions = [
        "Are you more introverted or extroverted?",
        "What makes you happy?",
        "What makes you angry?",
        "How do you deal with stress?",
        "What’s your biggest fear?",
        "Do you cry easily?",
        "What motivates you the most?",
        "Are you more logical or emotional?",
        "Do you consider yourself patient?",
        "What makes you laugh the most?",
        "How do you express your emotions?",
        "Do you enjoy being the center of attention?",
        "How do you relax after a long day?",
        "Are you a morning person or a night owl?",
        "Do you like taking risks?",
        "Describe yourself in three words.",
        "What makes you feel confident?",
        "Do you forgive easily?",
        "What usually cheers you up?",
        "Are you more of a planner or spontaneous?"
    ]
    for q in personality_questions:
        input(q + " ")
    print("Thank you for your answers 💖 I hope you like my project!")

# === SOCIAL LIFE QUESTIONS ===
elif question_type == "sociallife":
    print("\nLet's talk about your Social Life!\n")
    social_questions = [
        "Do you enjoy meeting new people?",
        "Who is your best friend?",
        "How do you spend time with friends?",
        "Do you prefer small groups or big gatherings?",
        "Are you close to your family?",
        "Who do you trust the most?",
        "What’s your love language?",
        "How do you show appreciation to others?",
        "Do you like giving or receiving gifts more?",
        "How do you handle arguments?",
        "Do you believe in soulmates?",
        "How do you make new friends?",
        "Do you enjoy helping others?",
        "What’s the most important quality in a friend?",
        "How often do you talk to your family?",
        "What makes you feel loved?",
        "Do you like working in a team or alone?",
        "Have you ever had a long-distance friendship?",
        "Do you like surprises?",
        "Who has influenced you the most in your life?"
    ]
    for q in social_questions:
        input(q + " ")
    print("Thank you for your answers 💖 I hope you like my project!")

# === INVALID TYPE ===
else:
    print("\n❌ Invalid question type! Please choose from:")
    print("Basic / Interests / Life / Personality / SocialLife")
