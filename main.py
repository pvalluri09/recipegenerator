import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client("CIchyPViQQtN7NQyS0jiOvIE7KjUtKTTVY3DPzOf")

# Title with color
st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🍴 Gourmet Alchemy 🍴</h1>",
    unsafe_allow_html=True,
)

# Subtitle with styling
st.markdown(
    "<p style='text-align: center; color: #4CAF50; font-size: 18px;'>Craft personalized recipes tailored to your preferences!</p>",
    unsafe_allow_html=True,
)

# Recipe generation function
def generate_recipe(ingredients, cuisine, calories, meal, filter, duration):
    prompt = (
        f"You are a world class chef that can prepare any cuisine with restricted ingredients within a given time. "
        f"Generate a delicious recipe with the ingredients: {ingredients}. "
        f"The cuisine should be: {cuisine}. "
        f"The recipe should have {calories} calories. Take into consideration the calories. "
        f"It should be a {meal} meal. "
        f"The meal type option is: {filter}. "
        f"The recipe should take around {duration} to prepare. "
        f"Give me a full step-by-step recipe that sounds like a cookbook recipe and is very professional."
    )

    response = co.generate(
        model='c4ai-aya-23',
        prompt=prompt,
        max_tokens=2000,
        temperature=0.9,
        stop_sequences=[]
    )
    return response.generations[0].text

# Input fields with styling
st.markdown("<h3 style='color: #FF6347;'>Enter Recipe Details:</h3>", unsafe_allow_html=True)

ingredients = st.text_input("🥦 Ingredients (comma-separated):", placeholder="e.g., chicken, garlic, olive oil")
cuisine = st.text_input("🍜 Favourite Cuisine:", placeholder="e.g., Italian, Indian, Mexican")
calories = st.text_input("🔥 Calorie Limit:", placeholder="e.g., 500")
meal = st.selectbox("🍽️ Meal Type:", ["Breakfast", "Lunch", "Dinner", "Dessert"])
filter = st.selectbox("🥗 Meal Option:", ["Non-Vegetarian", "Vegetarian"])
duration = st.selectbox("⏳ Preparation Time:", ["15 mins", "30 mins", "60 mins", "90 mins"])

# Submit button with styling
submit_button = st.button(
    "✨ Generate Recipe ✨",
    help="Click to create your personalized recipe!"
)

# Recipe output section
# Recipe output section
# Recipe output section
if submit_button:
    st.write("Generating a customized meal for you...")
    recipe = generate_recipe(ingredients, cuisine, calories, meal, filter, duration)
    st.markdown(recipe)
#    st.download_button(label="Download Recipe", data=recipe, file_name="recipe.txt", mime="text/plain")
    st.download_button(
        label="📥 Download Recipe",
        data=recipe,
        file_name="recipe.txt",
        mime="text/plain",
        help="Download your recipe as a text file!"
    )
