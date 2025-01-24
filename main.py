import streamlit as st
import cohere

co = cohere.Client("CIchyPViQQtN7NQyS0jiOvIE7KjUtKTTVY3DPzOf")

st.title("Gourmet Alchemy")


def generate_recipe(ingredients, cuisine, calories, meal, filter, duration):
    prompt = (
        f"You are a world class chef that can prepare any cuisime with restructed ingredients within a given time so generate a delicious recipe with the ingredients: {ingredients}. "
        f"The cuisine should be: {cuisine}. "
        f"The recipe should have {calories} calories.Take into the considerations of the calories "
        f"It should be a {meal} meal. "
        f"The meal type option is: {filter}. "
        f"The recipe should take around {duration} to prepare. give me a full step by step recipe for the above it should sound like a cookbook recipe and should be very professional"
    )

    response = co.generate(
        model='c4ai-aya-23',
        prompt=prompt,
        max_tokens=2000,
        temperature=0.9,
        stop_sequences=[]
    )
    print(response.generations[0].text)
    return response.generations[0].text


ingredients = st.text_input("Enter the ingredients for a delicious recipe")
cuisine = st.text_input("Enter your favourite cuisine!")
calories = st.text_input("Enter the number of calories")
meal = st.selectbox("Enter the meal type", ["Breakfast", "Lunch", "Dinner", "Dessert"])
filter = st.selectbox("Enter the type of meal", ["Non-Vegetarian", "Vegetarian"])
duration = st.selectbox("Select the duration for the recipe", ["15 mins", "30 mins", "60 mins", "90 mins"])
submit_button = st.button("Generate Recipe")

if submit_button:
    st.write("Generating a customized meal for you...")
    recipe = generate_recipe(ingredients, cuisine, calories, meal, filter, duration)
    st.markdown(recipe)
    st.download_button(label="Download Recipe", data=recipe, file_name="recipe.txt", mime="text/plain")
