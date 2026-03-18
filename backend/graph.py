from query_engine import generate_sql
from db import run_query
from memory import user_state, save_user


def pmgt_graph(user_input):

    text = user_input.lower().strip()

    # -------------------
    # Greeting
    # -------------------

    if text in ["hi", "hello", "hii", "hey"]:
        return "Hello! 👋 Before we begin, what may I call you?"

    # -------------------
    # Name capture
    # -------------------

    if user_state["name"] is None:
        user_state["name"] = user_input
        return f"Nice to meet you, {user_input}! Please share your phone number with country code (e.g., +91XXXXXXXXXX)."

    # -------------------
    # Phone capture
    # -------------------

    if user_state["phone"] is None:
        user_state["phone"] = user_input
        return "Thank you 👍 Now please provide your email address so we can stay in touch."

    # -------------------
    # Email capture
    # -------------------

    if user_state["email"] is None:

        user_state["email"] = user_input

        save_user(
            user_state["name"],
            user_state["phone"],
            user_state["email"]
        )

        return f"You're all set, {user_state['name']}! How can I assist you today?"

    # -------------------
    # Basic conversational responses
    # -------------------

    if "my name" in text:
        return f"Your name is {user_state['name']} 😊"

    if "are you here" in text or "u here" in text or "you here" in text:
        return "Yes, I'm here. How can I assist you?"

    if "alive" in text or "u alive" in text:
        return "Yes, I'm here and ready to help with project information."

    # -------------------
    # Current country
    # -------------------

    if "which country" in text or "what country" in text:
        return "We are currently operating in India."

    # -------------------
    # Cities currently operating
    # -------------------

    if "which cities" in text or "cities are you in" in text:

        sql = "SELECT DISTINCT city FROM project_sites"

        result = run_query(sql)

        if result:
            cities = [row[0] for row in result]
            return ", ".join(cities)

        return "I couldn't retrieve the city information."

    # -------------------
    # Future city / state plans
    # -------------------

    if "plans" in text or "future" in text:

        words = text.split()

        possible_location = words[-1].capitalize()

        return f"We have not yet started operations in {possible_location}, but we may expand there in the future."

    # -------------------
    # Bye
    # -------------------

    if "bye" in text:
        return "Thank you for interacting with the PMGT Assistant. We will reach out via email if needed. Have a great day! 👋"

    # -------------------
    # SQL generation
    # -------------------

    sql = generate_sql(user_input)

    if sql is None:
        return "I couldn't understand the request. Please rephrase."

    result = run_query(sql)

    if result is None:
        return "I couldn't process the request safely."

    if len(result) == 0:
        return "No matching data found."

    # -------------------
    # Format output
    # -------------------

    if len(result[0]) == 1:
        return str(result[0][0])

    formatted = []

    for row in result:
        formatted.append(", ".join(str(x) for x in row))

    return "\n".join(formatted)
