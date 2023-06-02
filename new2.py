import openai
import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv

load_dotenv()
import openai


# Setting page title and header
st.set_page_config(page_title="AJMAN", page_icon=":robot_face:")
st.markdown(
    "<h1 style='text-align: center;'>Ajman Tourist Guide </h1>",
    unsafe_allow_html=True,
)

# Set org ID and API key

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORGANIZATION")


# Initialise session state variables
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = messages = [
        {
            "role": "user",
            "content": "You are a helpful assistant that Plan day tip itineray based on questions you ask for people visiting ajman ,by asking them and waiting for their replies then proceed in asking and make it sound not boring",
        },
        {
            "role": "system",
            "content": "Of course! I'd be happy to help you plan your day trip to Ajman. Please answer the following questions so I can suggest suitable places and activities for you:When are you planning to visit Ajman?",
        },
        {"role": "user", "content": "In july"},
        {
            "role": "system",
            "content": "Great! July is a good time to visit Ajman. However, please note that the weather can be quite hot during this month. Now, let's move on to the next question. 2. How many days will you be spending in Ajman?",
        },
        {"role": "user", "content": "5 days"},
        {
            "role": "system",
            "content": "Excellent! You have a good amount of time to explore Ajman. Now, let's proceed to the next question. 3. Are you interested in exploring historical sites, cultural attractions, outdoor activities, or a combination of all? Please let me know your preferences.",
        },
        {"role": "user", "content": "combination of all"},
        {
            "role": "system",
            "content": "Fantastic! With a combination of historical sites, cultural attractions, and outdoor activities, you'll get a well-rounded experience of Ajman. Now, let's proceed to the next question.4. Do you have any specific dietary preferences or restrictions? This will help me suggest suitable places to eat during your trip.",
        },
        {"role": "user", "content": "I am vegetarian"},
        {
            "role": "system",
            "content": "Understood. Being a vegetarian, there are several restaurants in Ajman that offer vegetarian options. Now, let's move on to the next question.5. How do you plan on getting around in Ajman? Will you have a car, or do you prefer using public transportation or taxis?",
        },
        {"role": "user", "content": "public transportation"},
        {
            "role": "system",
            "content": "Great! Ajman has a well-connected public transportation system that makes it easy to explore the city. Now, let's move on to the next question.Are you interested in beach activities or water sports during your trip to Ajman?",
        },
        {"role": "user", "content": "Yes"},
        {
            "role": "system",
            "content": "Wonderful! Ajman has beautiful beaches and offers a variety of water sports activities. Now, let's proceed to the final question.7. Would you like to include any specific landmarks or attractions that you've already heard about or are particularly interested in visiting in Ajman? If not, I can suggest some popular options for you.",
        },
        {"role": "user", "content": "I have no idea"},
        {
            "role": "system",
            "content": """Not a problem! I'll be happy to suggest some popular landmarks and attractions in Ajman for you to consider. Here is a day trip itinerary for your 5-day visit to Ajman:

Day 1:
- Start your day with a visit to Ajman Museum, located in the heart of the city. It provides insights into the rich history and culture of the region.
   - Museum Location: Latitude 25.4066° N, Longitude 55.4624° E

- Afterward, head to Ajman Corniche, a beautiful waterfront promenade offering stunning views of the Arabian Gulf. Enjoy a leisurely stroll along the corniche and soak in the relaxing atmosphere.
   - Corniche Location: Latitude 25.4061° N, Longitude 55.4454° E

- For lunch, you can try one of the vegetarian-friendly restaurants in Ajman, such as "Govinda's" or "Karma Kafe," offering a variety of vegetarian dishes.

- In the afternoon, visit Al Zorah Nature Reserve, a pristine mangrove forest and wetland area. Take a guided nature walk or a kayak tour to explore the diverse ecosystem.
   - Al Zorah Nature Reserve Location: Latitude 25.5133° N, Longitude 55.4229° E

Day 2:
- Start your day with a visit to Sheikh Zayed Mosque in Ajman, a stunning architectural masterpiece. Admire the intricate design and peaceful ambiance of this grand mosque.
   - Sheikh Zayed Mosque Location: Latitude 25.4346° N, Longitude 55.4901° E

- Afterward, explore the Ajman Gold Souk, where you can browse through a variety of jewelry and gold shops. It's a great place to experience the local market atmosphere.
   - Gold Souk Location: Latitude 25.4007° N, Longitude 55.4514° E

- For lunch, you can try "Saravana Bhavan" or "Manvaar," two popular vegetarian Indian restaurants in Ajman.

- In the afternoon, head to Ajman Dhow Yard, where traditional wooden dhows (boats) are built and repaired. Take a tour to witness the craftsmanship and learn about the dhow-building heritage.
   - Ajman Dhow Yard Location: Latitude 25.4196° N, Longitude 55.4712° E

Day 3:
- Start your day with a visit to Al Jurf Park, a picturesque park with beautiful landscaped gardens and recreational facilities. Enjoy a picnic or relax amidst nature.
   - Al Jurf Park Location: Latitude 25.4307° N, Longitude 55.5297° E

- Afterward, you can visit Ajman Fish Market, a bustling market where you can see a variety of freshly caught seafood. It's an interesting place to experience the local fishing culture.
   - Fish Market Location: Latitude 25.4046° N, Longitude 55.4789° E

- For lunch, you can try "Manna Land" or "Vada Pao Street," offering vegetarian-friendly options in the vicinity.

- In the afternoon, head to Ajman Marina, where you can enjoy a relaxing boat ride or engage in water sports activities such as jet skiing or paddleboarding.
   - Marina Location: Latitude 25.4062° N, Longitude 55.4569° E

Day 4:
- Start your day by visiting the Ajman China Mall, a shopping destination with a wide range of products from China. It's a unique shopping experience with a variety of stores.
   - China Mall Location: Latitude 25.3722° N, Longitude 55.4419° E""",
        },
        {
            "role": "user",
            "content": "Lets do again the same process after I Say Hi and start asking me the same flow above question by question and wait for me to reply after asking questions",
        },
    ]

if "model_name" not in st.session_state:
    st.session_state["model_name"] = []
if "cost" not in st.session_state:
    st.session_state["cost"] = []
if "total_tokens" not in st.session_state:
    st.session_state["total_tokens"] = []
if "total_cost" not in st.session_state:
    st.session_state["total_cost"] = 0.0

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.title("Sidebar")
model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(
    f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
)
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"

# reset everything
if clear_button:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["messages"] = messages = [
        {
            "role": "user",
            "content": "You are a helpful assistant that Plan day tip itineray based on questions you ask for people visiting ajman ,by asking them and waiting for their replies then proceed in asking and make it sound not boring",
        },
        {
            "role": "system",
            "content": "Of course! I'd be happy to help you plan your day trip to Ajman. Please answer the following questions so I can suggest suitable places and activities for you:When are you planning to visit Ajman?",
        },
        {"role": "user", "content": "In july"},
        {
            "role": "system",
            "content": "Great! July is a good time to visit Ajman. However, please note that the weather can be quite hot during this month. Now, let's move on to the next question. 2. How many days will you be spending in Ajman?",
        },
        {"role": "user", "content": "5 days"},
        {
            "role": "system",
            "content": "Excellent! You have a good amount of time to explore Ajman. Now, let's proceed to the next question. 3. Are you interested in exploring historical sites, cultural attractions, outdoor activities, or a combination of all? Please let me know your preferences.",
        },
        {"role": "user", "content": "combination of all"},
        {
            "role": "system",
            "content": "Fantastic! With a combination of historical sites, cultural attractions, and outdoor activities, you'll get a well-rounded experience of Ajman. Now, let's proceed to the next question.4. Do you have any specific dietary preferences or restrictions? This will help me suggest suitable places to eat during your trip.",
        },
        {"role": "user", "content": "I am vegetarian"},
        {
            "role": "system",
            "content": "Understood. Being a vegetarian, there are several restaurants in Ajman that offer vegetarian options. Now, let's move on to the next question.5. How do you plan on getting around in Ajman? Will you have a car, or do you prefer using public transportation or taxis?",
        },
        {"role": "user", "content": "public transportation"},
        {
            "role": "system",
            "content": "Great! Ajman has a well-connected public transportation system that makes it easy to explore the city. Now, let's move on to the next question.Are you interested in beach activities or water sports during your trip to Ajman?",
        },
        {"role": "user", "content": "Yes"},
        {
            "role": "system",
            "content": "Wonderful! Ajman has beautiful beaches and offers a variety of water sports activities. Now, let's proceed to the final question.7. Would you like to include any specific landmarks or attractions that you've already heard about or are particularly interested in visiting in Ajman? If not, I can suggest some popular options for you.",
        },
        {"role": "user", "content": "I have no idea"},
        {
            "role": "system",
            "content": """Not a problem! I'll be happy to suggest some popular landmarks and attractions in Ajman for you to consider. Here is a day trip itinerary for your 5-day visit to Ajman:

Day 1:
- Start your day with a visit to Ajman Museum, located in the heart of the city. It provides insights into the rich history and culture of the region.
   - Museum Location: Latitude 25.4066° N, Longitude 55.4624° E

- Afterward, head to Ajman Corniche, a beautiful waterfront promenade offering stunning views of the Arabian Gulf. Enjoy a leisurely stroll along the corniche and soak in the relaxing atmosphere.
   - Corniche Location: Latitude 25.4061° N, Longitude 55.4454° E

- For lunch, you can try one of the vegetarian-friendly restaurants in Ajman, such as "Govinda's" or "Karma Kafe," offering a variety of vegetarian dishes.

- In the afternoon, visit Al Zorah Nature Reserve, a pristine mangrove forest and wetland area. Take a guided nature walk or a kayak tour to explore the diverse ecosystem.
   - Al Zorah Nature Reserve Location: Latitude 25.5133° N, Longitude 55.4229° E

Day 2:
- Start your day with a visit to Sheikh Zayed Mosque in Ajman, a stunning architectural masterpiece. Admire the intricate design and peaceful ambiance of this grand mosque.
   - Sheikh Zayed Mosque Location: Latitude 25.4346° N, Longitude 55.4901° E

- Afterward, explore the Ajman Gold Souk, where you can browse through a variety of jewelry and gold shops. It's a great place to experience the local market atmosphere.
   - Gold Souk Location: Latitude 25.4007° N, Longitude 55.4514° E

- For lunch, you can try "Saravana Bhavan" or "Manvaar," two popular vegetarian Indian restaurants in Ajman.

- In the afternoon, head to Ajman Dhow Yard, where traditional wooden dhows (boats) are built and repaired. Take a tour to witness the craftsmanship and learn about the dhow-building heritage.
   - Ajman Dhow Yard Location: Latitude 25.4196° N, Longitude 55.4712° E

Day 3:
- Start your day with a visit to Al Jurf Park, a picturesque park with beautiful landscaped gardens and recreational facilities. Enjoy a picnic or relax amidst nature.
   - Al Jurf Park Location: Latitude 25.4307° N, Longitude 55.5297° E

- Afterward, you can visit Ajman Fish Market, a bustling market where you can see a variety of freshly caught seafood. It's an interesting place to experience the local fishing culture.
   - Fish Market Location: Latitude 25.4046° N, Longitude 55.4789° E

- For lunch, you can try "Manna Land" or "Vada Pao Street," offering vegetarian-friendly options in the vicinity.

- In the afternoon, head to Ajman Marina, where you can enjoy a relaxing boat ride or engage in water sports activities such as jet skiing or paddleboarding.
   - Marina Location: Latitude 25.4062° N, Longitude 55.4569° E

Day 4:
- Start your day by visiting the Ajman China Mall, a shopping destination with a wide range of products from China. It's a unique shopping experience with a variety of stores.
   - China Mall Location: Latitude 25.3722° N, Longitude 55.4419° E""",
        },
        {
            "role": "user",
            "content": "Lets do again the same process after I Say Hi and start asking me the same flow above question by question and wait for me to reply after asking questions",
        },
    ]

    st.session_state["number_tokens"] = []
    st.session_state["model_name"] = []
    st.session_state["cost"] = []
    st.session_state["total_cost"] = 0.0
    st.session_state["total_tokens"] = []
    counter_placeholder.write(
        f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
    )


# generate a response
def generate_response(prompt):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model=model, messages=st.session_state["messages"]
    )
    response = completion.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # print(st.session_state['messages'])
    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return response, total_tokens, prompt_tokens, completion_tokens


# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key="my_form", clear_on_submit=True):
        user_input = st.text_area("You:", key="input", height=100)
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(
            user_input
        )
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)
        st.session_state["model_name"].append(model_name)
        st.session_state["total_tokens"].append(total_tokens)

        # from https://openai.com/pricing#language-models
        if model_name == "GPT-3.5":
            cost = total_tokens * 0.002 / 1000
        else:
            cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

        st.session_state["cost"].append(cost)
        st.session_state["total_cost"] += cost

if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))
            # st.write(
            #     f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}"
            # )
            # counter_placeholder.write(
            #     f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
            # )
