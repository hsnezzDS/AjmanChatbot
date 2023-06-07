import openai
import pandas as pd
import json
from PIL import Image, ImageEnhance
import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv

load_dotenv()
import openai


# Setting page title and header
st.set_page_config(page_title="AJMAN", page_icon=":robot_face:")
# st.markdown(
#     """<script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>

#     <link rel="stylesheet" type="text/css" href="./style.css" />
#     <script type="module" src="./index.js"></script>
#     <script
#       src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg&callback=initMap&v=weekly"
#       defer
#     ></script>
#     """,
#     unsafe_allow_html=True,
# )


image = Image.open(r"logo.png")  # Brand logo image (optional)

# Create two columns with different width
col1, col2 = st.columns([0.8, 0.2])
with col1:  # To display the header text using css style
    st.markdown(
        """ <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 style='text-align: center;'>Ajman Tourist Guide </h1>",
        unsafe_allow_html=True,
    )

with col2:  # To display brand logo
    st.image(image, width=150)


# Set org ID and API key

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORGANIZATION")
openai.api_key = st.sidebar.text_input("API Key:")


# Initialise session state variables
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = messages = [
        {
            "role": "assistant",
            "content": """ You are a helpful assistant that Plan day tip itineray based on questions you ask for people visiting ajman ,by asking them and waiting for their replies then proceed in asking and make it sound not boring and generate the final itenary in json object

Of course! I'd be happy to help you plan a day trip itinerary for visiting Ajman. To start, could you please provide me with the following information?

1.  How many days will you be spending in Ajman?
2.  Are there any specific attractions or activities you would like to include in your itinerary?
3.  What are your interests? For example, are you interested in history, culture, outdoor activities, or shopping?
4.  Do you have any dietary restrictions or preferences for meals?

Once I have your answers, I can proceed with generating a personalized itinerary for you.""",
        },
        {
            "role": "user",
            "content": "let them question by question",
        },
        {
            "role": "assistant",
            "content": "Certainly! Let's start with the first question:1.  How many days will you be spending in Ajman?",
        },
        {
            "role": "user",
            "content": "5",
        },
        {
            "role": "assistant",
            "content": """ 
Great! Now let's move on to the next question:2.  Are there any specific attractions or activities you would like to include in your itinerary?""",
        },
        {
            "role": "user",
            "content": "no",
        },
        {
            "role": "assistant",
            "content": "Not a problem! Let's continue with the next question:3.  What are your interests? Are you interested in history, culture, outdoor activities, or shopping?",
        },
        {
            "role": "user",
            "content": "Outdoor",
        },
        {
            "role": "assistant",
            "content": "Fantastic! And now for the final question:4.  Do you have any dietary restrictions or preferences for meals?",
        },
        {
            "role": "user",
            "content": "no",
        },
        {
            "role": "assistant",
            "content": """
Got it! Based on your responses, here's a suggested day trip itinerary for your 5-day visit to Ajman, with a focus on outdoor activities:

Day 1:

*   Morning: Start your day with a visit to Ajman Beach. Enjoy a leisurely stroll along the coastline, take in the beautiful views, and perhaps even dip your toes in the water.
*   Afternoon: Head to Al Zorah Nature Reserve. Explore the mangrove forests, go kayaking or paddleboarding, and admire the diverse wildlife in the area.
*   Evening: Visit Ajman Marina, where you can relax and enjoy a delightful dinner at one of the waterfront restaurants.

Day 2:

*   Morning: Embark on a desert safari adventure. Take a thrilling dune bashing ride, try sandboarding, and experience the enchanting beauty of the desert landscape.
*   Afternoon: Visit Hajar Mountains for a hiking excursion. Enjoy the scenic trails, breathe in the fresh mountain air, and capture some breathtaking panoramic views.
*   Evening: Return to the city and indulge in a delicious dinner at one of the local outdoor dining spots.

Day 3:

*   Morning: Explore the Ajman Corniche, a picturesque waterfront promenade. Take a leisurely walk, rent a bicycle, or simply relax in one of the parks along the Corniche.
*   Afternoon: Visit Sheikh Zayed Mosque in Ajman. Admire the stunning architecture, serene ambiance, and learn about the Islamic culture and heritage.
*   Evening: Enjoy an evening of outdoor entertainment at one of the open-air events or festivals happening in Ajman (check for any ongoing events during your visit).

Day 4:

*   Morning: Take a boat tour to Dibba Al-Hisn, a nearby coastal town known for its crystal-clear waters and abundant marine life. Go snorkeling or scuba diving to explore the vibrant underwater world.
*   Afternoon: Visit Ajman Museum to delve into the rich history and heritage of the region. Explore the exhibits, artifacts, and learn about Ajman's fascinating past.
*   Evening: Head to Al Tallah Camel Racecourse to witness the excitement of traditional camel racing, a popular sport in the UAE.

Day 5:

*   Morning: Explore Al Jarah Cultural Center, a hub for art and culture in Ajman. Attend workshops, browse through art galleries, and immerse yourself in the local artistic scene.
*   Afternoon: Visit Al Montazah Parks for a fun-filled afternoon. Enjoy thrilling rides at the water park, relax in the gardens, and indulge in some delicious snacks.
*   Evening: Wrap up your day trip with a sunset yacht cruise along the Ajman coastline. Relax, unwind, and take in the mesmerizing views of the Arabian Gulf.

Please note that this itinerary is a general suggestion, and you can adjust it based on your preferences and the specific opening hours of attractions during your visit. Enjoy your trip to Ajman!
 """,
        },
        {
            "role": "user",
            "content": "I told make the iteneary in json object",
        },
        {
            "role": "user",
            "content": """ Apologies for the oversight. Here's the suggested day trip itinerary for your 5-day visit to Ajman in JSON format:

json

```json
{
  "itinerary": {
    "day1": {
      "morning": "Ajman Beach",
      "afternoon": "Al Zorah Nature Reserve",
      "evening": "Ajman Marina"
    },
    "day2": {
      "morning": "Desert Safari",
      "afternoon": "Hajar Mountains",
      "evening": "Outdoor dining"
    },
    "day3": {
      "morning": "Ajman Corniche",
      "afternoon": "Sheikh Zayed Mosque",
      "evening": "Outdoor entertainment"
    },
    "day4": {
      "morning": "Dibba Al-Hisn boat tour",
      "afternoon": "Ajman Museum",
      "evening": "Al Tallah Camel Racecourse"
    },
    "day5": {
      "morning": "Al Jarah Cultural Center",
      "afternoon": "Al Montazah Parks",
      "evening": "Sunset yacht cruise"
    }
  }
}
```

Please note that this is a simplified JSON representation of the itinerary, and you can further customize or expand it based on your preferences and specific details for each activity.
""",
        },
        {
            "role": "user",
            "content": "I want it with description and lat lng",
        },
        {
            "role": "assistant",
            "content": """ 
Certainly! Here's an updated version of the suggested day trip itinerary for your 5-day visit to Ajman in JSON format, including descriptions and latitude/longitude coordinates:

json

```json
{
  "itinerary": {
    "day1": {
      "morning": {
        "activity": "Ajman Beach",
        "description": "Enjoy a leisurely stroll along the beautiful coastline of Ajman Beach.",
        "location": {
          "latitude": 25.4085,
          "longitude": 55.4694
        }
      },
      "afternoon": {
        "activity": "Al Zorah Nature Reserve",
        "description": "Explore the mangrove forests and spot diverse wildlife at Al Zorah Nature Reserve.",
        "location": {
          "latitude": 25.4462,
          "longitude": 55.4572
        }
      },
      "evening": {
        "activity": "Ajman Marina",
        "description": "Relax and enjoy a delightful dinner at one of the waterfront restaurants in Ajman Marina.",
        "location": {
          "latitude": 25.4134,
          "longitude": 55.4496
        }
      }
    },
    "day2": {
      "morning": {
        "activity": "Desert Safari",
        "description": "Embark on a thrilling desert safari adventure, including dune bashing and sandboarding.",
        "location": {
          "latitude": 25.2417,
          "longitude": 55.4249
        }
      },
      "afternoon": {
        "activity": "Hajar Mountains",
        "description": "Go hiking and enjoy the scenic trails and panoramic views of the Hajar Mountains.",
        "location": {
          "latitude": 25.6835,
          "longitude": 55.9272
        }
      },
      "evening": {
        "activity": "Outdoor dining",
        "description": "Indulge in a delicious dinner at one of the local outdoor dining spots.",
        "location": null
      }
    },
    "day3": {
      "morning": {
        "activity": "Ajman Corniche",
        "description": "Take a leisurely walk along the picturesque Ajman Corniche waterfront promenade.",
        "location": {
          "latitude": 25.4011,
          "longitude": 55.4497
        }
      },
      "afternoon": {
        "activity": "Sheikh Zayed Mosque",
        "description": "Visit Sheikh Zayed Mosque in Ajman and admire the stunning Islamic architecture.",
        "location": {
          "latitude": 25.4185,
          "longitude": 55.4693
        }
      },
      "evening": {
        "activity": "Outdoor entertainment",
        "description": "Enjoy an evening of outdoor entertainment at one of the open-air events or festivals in Ajman.",
        "location": null
      }
    },
    "day4": {
      "morning": {
        "activity": "Dibba Al-Hisn boat tour",
        "description": "Take a boat tour to Dibba Al-Hisn and explore the beautiful coastal town known for its crystal-clear waters and marine life.",
        "location": {
          "latitude": 25.6098,
          "longitude": 56.2721
        }
      },
      "afternoon": {
        "activity": "Ajman Museum",
        "description": "Learn about the history and heritage of Ajman at Ajman Museum, featuring exhibits and artifacts.",
        "location": {
          "latitude": 25.4132,
          "longitude": 55.4439
        }
      },
      "evening": {
        "activity": "Al Tallah Camel Racecourse",
        "description": "Experience the excitement of traditional camel racing at Al Tallah Camel Racecourse.",
        "location": {
          "latitude": 25.4264,
          "longitude": 55.4933
        }
      }
    },
    "day5": {
      "morning": {
        "activity": "Al Jarah Cultural Center",
        "description": "Explore the art and culture scene at Al Jarah Cultural Center, featuring workshops and art galleries.",
        "location": {
          "latitude": 25.4139,
          "longitude": 55.4386
        }
      },
      "afternoon": {
        "activity": "Al Montazah Parks",
        "description": "Enjoy a fun-filled afternoon at Al Montazah Parks, featuring thrilling rides and beautiful gardens.",
        "location": {
          "latitude": 25.4018,
          "longitude": 55.4234
        }
      },
      "evening": {
        "activity": "Sunset yacht cruise",
        "description": "Relax and enjoy a scenic yacht cruise along the Ajman coastline during sunset.",
        "location": null
      }
    }
  }
}
```
 """,
        },
        {
            "role": "user",
            "content": """always make sure you fill the json in this format 

```json
{
"itinerary": [{
"day1": {
"morning": {
"activity": "Ajman China Mall",
"description": "Visit Ajman China Mall, a multi-story mall with a wide range of shops offering a variety of items such as textiles, electronics, clothing, and home furnishing products.",
"location": null,
"image": null
},
"afternoon": {
"activity": "Ajman Market",
"description": "Head to the nearby Ajman Market, where you can find a unique selection of local and regional products including fresh produce, spices, fabrics, and souvenirs.",
"location": null,
"image": null
},
"evening": {
"activity": "City Centre Ajman",
"description": "Explore City Centre Ajman, a large shopping mall with a variety of international and local brands for fashion, electronics, groceries, and entertainment.",
"location": null,
"image": null
}
},
"day2": {
"morning": {
"activity": "Friday Market",
"description": "Discover the Friday Market, a traditional open-air market located in Masfut, a mountainous region in Ajman, which offers a variety of local goods such as pottery, plants, carpets, and antiques.",
"location": null,
"image": null
},
"afternoon": {
"activity": "Al Jurf Mall",
"description": "Continue your shopping spree at Al Jurf Mall, a lifestyle mall that houses over 160 stores, including a supermarket, cinema, food court, and several international brands.",
"location": null,
"image": null
},
"evening": {
"activity": "Al Hamidiyah Mall",
"description": "Enjoy dinner at one of the restaurants in Al Hamidiyah Mall, a modern mall offering a diverse range of retail options and dining experiences.",
"location": null,
"image": null
}
}
}
    ]
}
```
""",
        },
        {
            "role": "user",
            "content": "Lets do again the same process after I Say Hi and start asking me the same flow above question by question and wait for me to reply after asking questions ans make the itineray response in json object",
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
# model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
# counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")


# reset everything
if clear_button:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["messages"] = messages = [
        {
            "role": "assistant",
            "content": """ You are a helpful assistant that Plan day tip itineray based on questions you ask for people visiting ajman ,by asking them and waiting for their replies then proceed in asking and make it sound not boring and generate the final itenary in json object

Of course! I'd be happy to help you plan a day trip itinerary for visiting Ajman. To start, could you please provide me with the following information?

1.  How many days will you be spending in Ajman?
2.  Are there any specific attractions or activities you would like to include in your itinerary?
3.  What are your interests? For example, are you interested in history, culture, outdoor activities, or shopping?
4.  Do you have any dietary restrictions or preferences for meals?

Once I have your answers, I can proceed with generating a personalized itinerary for you.""",
        },
        {
            "role": "user",
            "content": "let them question by question",
        },
        {
            "role": "assistant",
            "content": "Certainly! Let's start with the first question:1.  How many days will you be spending in Ajman?",
        },
        {
            "role": "user",
            "content": "5",
        },
        {
            "role": "assistant",
            "content": """ 
Great! Now let's move on to the next question:2.  Are there any specific attractions or activities you would like to include in your itinerary?""",
        },
        {
            "role": "user",
            "content": "no",
        },
        {
            "role": "assistant",
            "content": "Not a problem! Let's continue with the next question:3.  What are your interests? Are you interested in history, culture, outdoor activities, or shopping?",
        },
        {
            "role": "user",
            "content": "Outdoor",
        },
        {
            "role": "assistant",
            "content": "Fantastic! And now for the final question:4.  Do you have any dietary restrictions or preferences for meals?",
        },
        {
            "role": "user",
            "content": "no",
        },
        {
            "role": "assistant",
            "content": """
Got it! Based on your responses, here's a suggested day trip itinerary for your 5-day visit to Ajman, with a focus on outdoor activities:

Day 1:

*   Morning: Start your day with a visit to Ajman Beach. Enjoy a leisurely stroll along the coastline, take in the beautiful views, and perhaps even dip your toes in the water.
*   Afternoon: Head to Al Zorah Nature Reserve. Explore the mangrove forests, go kayaking or paddleboarding, and admire the diverse wildlife in the area.
*   Evening: Visit Ajman Marina, where you can relax and enjoy a delightful dinner at one of the waterfront restaurants.

Day 2:

*   Morning: Embark on a desert safari adventure. Take a thrilling dune bashing ride, try sandboarding, and experience the enchanting beauty of the desert landscape.
*   Afternoon: Visit Hajar Mountains for a hiking excursion. Enjoy the scenic trails, breathe in the fresh mountain air, and capture some breathtaking panoramic views.
*   Evening: Return to the city and indulge in a delicious dinner at one of the local outdoor dining spots.

Day 3:

*   Morning: Explore the Ajman Corniche, a picturesque waterfront promenade. Take a leisurely walk, rent a bicycle, or simply relax in one of the parks along the Corniche.
*   Afternoon: Visit Sheikh Zayed Mosque in Ajman. Admire the stunning architecture, serene ambiance, and learn about the Islamic culture and heritage.
*   Evening: Enjoy an evening of outdoor entertainment at one of the open-air events or festivals happening in Ajman (check for any ongoing events during your visit).

Day 4:

*   Morning: Take a boat tour to Dibba Al-Hisn, a nearby coastal town known for its crystal-clear waters and abundant marine life. Go snorkeling or scuba diving to explore the vibrant underwater world.
*   Afternoon: Visit Ajman Museum to delve into the rich history and heritage of the region. Explore the exhibits, artifacts, and learn about Ajman's fascinating past.
*   Evening: Head to Al Tallah Camel Racecourse to witness the excitement of traditional camel racing, a popular sport in the UAE.

Day 5:

*   Morning: Explore Al Jarah Cultural Center, a hub for art and culture in Ajman. Attend workshops, browse through art galleries, and immerse yourself in the local artistic scene.
*   Afternoon: Visit Al Montazah Parks for a fun-filled afternoon. Enjoy thrilling rides at the water park, relax in the gardens, and indulge in some delicious snacks.
*   Evening: Wrap up your day trip with a sunset yacht cruise along the Ajman coastline. Relax, unwind, and take in the mesmerizing views of the Arabian Gulf.

Please note that this itinerary is a general suggestion, and you can adjust it based on your preferences and the specific opening hours of attractions during your visit. Enjoy your trip to Ajman!
 """,
        },
        {
            "role": "user",
            "content": "I told make the iteneary in json object",
        },
        {
            "role": "user",
            "content": """ Apologies for the oversight. Here's the suggested day trip itinerary for your 5-day visit to Ajman in JSON format:

json

```json
{
  "itinerary": {
    "day1": {
      "morning": "Ajman Beach",
      "afternoon": "Al Zorah Nature Reserve",
      "evening": "Ajman Marina"
    },
    "day2": {
      "morning": "Desert Safari",
      "afternoon": "Hajar Mountains",
      "evening": "Outdoor dining"
    },
    "day3": {
      "morning": "Ajman Corniche",
      "afternoon": "Sheikh Zayed Mosque",
      "evening": "Outdoor entertainment"
    },
    "day4": {
      "morning": "Dibba Al-Hisn boat tour",
      "afternoon": "Ajman Museum",
      "evening": "Al Tallah Camel Racecourse"
    },
    "day5": {
      "morning": "Al Jarah Cultural Center",
      "afternoon": "Al Montazah Parks",
      "evening": "Sunset yacht cruise"
    }
  }
}
```

Please note that this is a simplified JSON representation of the itinerary, and you can further customize or expand it based on your preferences and specific details for each activity.
""",
        },
        {
            "role": "user",
            "content": "I want it with description and lat lng",
        },
        {
            "role": "assistant",
            "content": """ 
Certainly! Here's an updated version of the suggested day trip itinerary for your 5-day visit to Ajman in JSON format, including descriptions and latitude/longitude coordinates:

json

```json
{
  "itinerary": {
    "day1": {
      "morning": {
        "activity": "Ajman Beach",
        "description": "Enjoy a leisurely stroll along the beautiful coastline of Ajman Beach.",
        "location": {
          "latitude": 25.4085,
          "longitude": 55.4694
        }
      },
      "afternoon": {
        "activity": "Al Zorah Nature Reserve",
        "description": "Explore the mangrove forests and spot diverse wildlife at Al Zorah Nature Reserve.",
        "location": {
          "latitude": 25.4462,
          "longitude": 55.4572
        }
      },
      "evening": {
        "activity": "Ajman Marina",
        "description": "Relax and enjoy a delightful dinner at one of the waterfront restaurants in Ajman Marina.",
        "location": {
          "latitude": 25.4134,
          "longitude": 55.4496
        }
      }
    },
    "day2": {
      "morning": {
        "activity": "Desert Safari",
        "description": "Embark on a thrilling desert safari adventure, including dune bashing and sandboarding.",
        "location": {
          "latitude": 25.2417,
          "longitude": 55.4249
        }
      },
      "afternoon": {
        "activity": "Hajar Mountains",
        "description": "Go hiking and enjoy the scenic trails and panoramic views of the Hajar Mountains.",
        "location": {
          "latitude": 25.6835,
          "longitude": 55.9272
        }
      },
      "evening": {
        "activity": "Outdoor dining",
        "description": "Indulge in a delicious dinner at one of the local outdoor dining spots.",
        "location": null
      }
    },
    "day3": {
      "morning": {
        "activity": "Ajman Corniche",
        "description": "Take a leisurely walk along the picturesque Ajman Corniche waterfront promenade.",
        "location": {
          "latitude": 25.4011,
          "longitude": 55.4497
        }
      },
      "afternoon": {
        "activity": "Sheikh Zayed Mosque",
        "description": "Visit Sheikh Zayed Mosque in Ajman and admire the stunning Islamic architecture.",
        "location": {
          "latitude": 25.4185,
          "longitude": 55.4693
        }
      },
      "evening": {
        "activity": "Outdoor entertainment",
        "description": "Enjoy an evening of outdoor entertainment at one of the open-air events or festivals in Ajman.",
        "location": null
      }
    },
    "day4": {
      "morning": {
        "activity": "Dibba Al-Hisn boat tour",
        "description": "Take a boat tour to Dibba Al-Hisn and explore the beautiful coastal town known for its crystal-clear waters and marine life.",
        "location": {
          "latitude": 25.6098,
          "longitude": 56.2721
        }
      },
      "afternoon": {
        "activity": "Ajman Museum",
        "description": "Learn about the history and heritage of Ajman at Ajman Museum, featuring exhibits and artifacts.",
        "location": {
          "latitude": 25.4132,
          "longitude": 55.4439
        }
      },
      "evening": {
        "activity": "Al Tallah Camel Racecourse",
        "description": "Experience the excitement of traditional camel racing at Al Tallah Camel Racecourse.",
        "location": {
          "latitude": 25.4264,
          "longitude": 55.4933
        }
      }
    },
    "day5": {
      "morning": {
        "activity": "Al Jarah Cultural Center",
        "description": "Explore the art and culture scene at Al Jarah Cultural Center, featuring workshops and art galleries.",
        "location": {
          "latitude": 25.4139,
          "longitude": 55.4386
        }
      },
      "afternoon": {
        "activity": "Al Montazah Parks",
        "description": "Enjoy a fun-filled afternoon at Al Montazah Parks, featuring thrilling rides and beautiful gardens.",
        "location": {
          "latitude": 25.4018,
          "longitude": 55.4234
        }
      },
      "evening": {
        "activity": "Sunset yacht cruise",
        "description": "Relax and enjoy a scenic yacht cruise along the Ajman coastline during sunset.",
        "location": null
      }
    }
  }
}
```
 """,
        },
        {
            "role": "user",
            "content": """always make sure you fill the json in this format 

```json
{
"itinerary": [{
"day1": {
"morning": {
"activity": "Ajman China Mall",
"description": "Visit Ajman China Mall, a multi-story mall with a wide range of shops offering a variety of items such as textiles, electronics, clothing, and home furnishing products.",
"location": null,
"image": null
},
"afternoon": {
"activity": "Ajman Market",
"description": "Head to the nearby Ajman Market, where you can find a unique selection of local and regional products including fresh produce, spices, fabrics, and souvenirs.",
"location": null,
"image": null
},
"evening": {
"activity": "City Centre Ajman",
"description": "Explore City Centre Ajman, a large shopping mall with a variety of international and local brands for fashion, electronics, groceries, and entertainment.",
"location": null,
"image": null
}
},
"day2": {
"morning": {
"activity": "Friday Market",
"description": "Discover the Friday Market, a traditional open-air market located in Masfut, a mountainous region in Ajman, which offers a variety of local goods such as pottery, plants, carpets, and antiques.",
"location": null,
"image": null
},
"afternoon": {
"activity": "Al Jurf Mall",
"description": "Continue your shopping spree at Al Jurf Mall, a lifestyle mall that houses over 160 stores, including a supermarket, cinema, food court, and several international brands.",
"location": null,
"image": null
},
"evening": {
"activity": "Al Hamidiyah Mall",
"description": "Enjoy dinner at one of the restaurants in Al Hamidiyah Mall, a modern mall offering a diverse range of retail options and dining experiences.",
"location": null,
"image": null
}
}
}
    ]
}
```
""",
        },
        {
            "role": "user",
            "content": "Lets do again the same process after I Say Hi and start asking me the same flow above question by question and wait for me to reply after asking questions ans make the itineray response in json object",
        },
    ]

    st.session_state["number_tokens"] = []
    st.session_state["model_name"] = []
    st.session_state["cost"] = []
    st.session_state["total_cost"] = 0.0
    st.session_state["total_tokens"] = []
    # counter_placeholder.write(
    #     f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
    # )


# generate a response
def generate_response(prompt):
    model = "gpt-3.5-turbo"
    st.session_state["messages"].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model=model, messages=st.session_state["messages"], max_tokens=100
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
        # st.session_state["model_name"].append(model_name)
        # st.session_state["total_tokens"].append(total_tokens)

        # from https://openai.com/pricing#language-models

        # st.session_state["cost"].append(cost)
        # st.session_state["total_cost"] += cost

if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")

            if "```json" in st.session_state["generated"][i]:
                # txt = """Great! Based on your interests and the duration of your trip, here's a suggested day trip itinerary for your 5-day visit to Ajman:json```json{"itinerary": {"day1": {"morning": {"activity": "Ajman China Mall","description": "Visit Ajman China Mall, a multi-story mall with a wide range of shops offering a variety of items such as textiles, electronics, clothing, and home furnishing products.","location": null},"afternoon": {"activity": "Ajman Market","description": "Head to the nearby Ajman Market, where you can find a unique selection of local and regional products including fresh produce, spices, fabrics, and souvenirs.","location": null},"evening": {"activity": "City Centre Ajman","description": "Explore City Centre Ajman, a large shopping mall with a variety of international and local brands for fashion, electronics, groceries, and entertainment.","location": null}},"day2": {"morning": {"activity": "Friday Market","description": "Discover the Friday Market, a traditional open-air market located in Masfut, a mountainous region in Ajman, which offers a variety of local goods such as pottery, plants, carpets, and antiques.","location": null},"afternoon": {"activity": "Al Jurf Mall","description": "Continue your shopping spree at Al Jurf Mall, a lifestyle mall that houses over 160 stores, including a supermarket, cinema, food court, and several international brands.","location": null},"evening": {"activity": "Al Hamidiyah Mall","description": "Enjoy dinner at one of the restaurants in Al Hamidiyah Mall, a modern mall offering a diverse range of retail options and dining experiences.","location": null}},"day3": {"morning": {"activity": "Safeer Mall","description": "Visit Safeer Mall, a family-friendly shopping destination that offers a variety of shopping, dining and entertainment options, including a large Carrefour hypermarket.","location": null},"afternoon": {"activity": "Ajman China Mall","description": "Return to Ajman China Mall to explore more shopping options or visit the Sharjah Shopping Centers in the nearby emirate of Sharjah.","location": null},"evening": {"activity": "Ajman City Centre","description": "Enjoy dinner and more shopping at Ajman City Centre, a modern mall with a diverse range of international and local brands.","location": null}},"day4": {"morning": {"activity": "Ajman Market","description": "Head back to Ajman Market for a unique shopping experience, and perhaps buy some gift items or souvenirs.","location": null},"afternoon": {"activity": "Ajman China Mall","description": "Spend the afternoon exploring more shops and products at Ajman China Mall.","location": null},"evening": {"activity": "Al Nuaimia Market","description": "Experience a traditional shopping atmosphere at Al Nuaimia Market, known for its unique local products such as carpets, perfumes, and textiles","location": null}},"day5": {"morning": {"activity": "Manama Road Souq","description": "Visit Manama Road Souq, a traditional shopping area with a variety of goods, including spices, perfumes, pottery, and baskets.","location": null},"afternoon": {"activity": "Ajman Madina Market","description": "Explore Ajman Madina Market, a modern mall with a range of shops focused on fashion and lifestyle products.","location": null},"evening": {"activity": "Ajman China Mall","description": "Wrap up your trip by visiting Ajman China Mall again, or find some local handicrafts and souvenirs at Souq Al Zabeel in Dubai.","location": null}}}}```Please note that this itinerary is a general suggestion, and you can adjust it based on your preferences and the specific opening hours of attractions during your visit. Enjoy your shopping trip to Ajman!"""
                txt = st.session_state["generated"][i]
                message(st.session_state["generated"][i], key=str(i))
                a = json.loads(txt.split("```json")[1].split("```")[0])
                days = a["itinerary"].keys()
                for day in days:
                    st.markdown(
                        f"""<h1> {day} </h1>""",
                        unsafe_allow_html=True,
                    )

                    day_activity = a["itinerary"][day]
                    for time_shift in day_activity.keys():
                        st.markdown(
                            f"""<h2> In the {time_shift} </h2>""",
                            unsafe_allow_html=True,
                        )
                        activity_per_shift = day_activity[time_shift].get(
                            "description", "Nodesc"
                        )
                        activity_per_shift_name = day_activity[time_shift].get(
                            "activity", ""
                        )
                        latitude = (
                            day_activity[time_shift]
                            .get("location", {})
                            .get("latitude", "")
                        )
                        longitude = (
                            day_activity[time_shift]
                            .get("location", {})
                            .get("longitude", "")
                        )
                        st.markdown(
                            f""" {activity_per_shift}""",
                            unsafe_allow_html=True,
                        )
                        st.markdown(
                            f""" <div id={activity_per_shift}+{time_shift}+map></div> """,
                            unsafe_allow_html=True,
                        )
                        import numpy as np

                        data = {"lat": [latitude], "lon": [longitude]}
                        df = pd.DataFrame(data)

                        st.map(df, use_container_width=True, zoom=10)
                        # st.markdown(
                        #     """ <script> function initMap() { const myLatLng = { lat: """
                        #     + str(latitude)
                        #     + """, lng: """
                        #     + str(longitude)
                        #     + """}; const map = new google.maps.Map(document.getElementById(" """
                        #     + str(activity_per_shift)
                        #     + """+}"""
                        #     + str(time_shift)
                        #     + """_map), { zoom: 4,center: myLatLng,});new google.maps.Marker({position: myLatLng,map,title: "Hello World!",});}window.initMap = initMap;</script> """,
                        #     unsafe_allow_html=True,
                        # )

            else:
                message(st.session_state["generated"][i], key=str(i))

                #         st.markdown(
                #     f""" """,
                #     unsafe_allow_html=True,
                # )
                #         day
                #         time_shift
                #         activity_per_shift

            # if "Day 1:" in st.session_state["generated"][i]:
            #     txt = """ Day 1:

            #         Visit Ajman Museum to explore the rich history and culture of the region. (Location: Latitude 25.4066° N, Longitude 55.4624° E)

            #         Image: Ajman Museum
            #         Take a leisurely stroll along Ajman Corniche and enjoy the beautiful waterfront views. (Location: Latitude 25.4061° N, Longitude 55.4454° E)

            #         Image: Ajman Corniche
            #         Day 2:

            #         Explore the Al Zorah Nature Reserve, a pristine mangrove forest and wetland area. Take a guided nature walk or kayak tour. (Location: Latitude 25.5133° N, Longitude 55.4229° E)
            #         Image: Al Zorah Nature Reserve
            #         Day 3:

            #         Visit Sheikh Zayed Mosque, a stunning architectural masterpiece. Marvel at its intricate design and peaceful ambiance. (Location: Latitude 25.4346° N, Longitude 55.4901° E)
            #         Image: Sheikh Zayed Mosque
            #         Day 4:

            #         Explore the Ajman Gold Souk, where you can browse through a variety of jewelry and gold shops. Experience the vibrant local market atmosphere. (Location: Latitude 25.4007° N, Longitude 55.4514° E)
            #         Image: Ajman Gold Souk
            #         """
            #     col3, col4 = st.columns([0.5, 0.5])
            #     with col3:  # To display the header text using css style
            #         st.markdown(
            #             """ <style> .font {
            #         font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
            #         </style> """,
            #             unsafe_allow_html=True,
            #         )
            #         st.markdown(
            #             "<h1 style='text-align: center;'>Ajman Tourist Guide </h1>",
            #             unsafe_allow_html=True,
            #         )
            #     with col2:  # To display brand logo
            #         st.image(image, width=150)
            #     st.markdown(
            #         """ <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_Homepage.svg/1200px-Google_Homepage.svg.png" alt="Girl in a jacket" width="200" height="200"> """,
            #         unsafe_allow_html=True,
            #     )
            # else:
            #     message(st.session_state["generated"][i], key=str(i))
            # st.write(
            #     f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}"
            # )
            # counter_placeholder.write(
            #     f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
            # )
