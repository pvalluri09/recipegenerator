# recipegenerator

Gourmet Alchemy

Overview
Gourmet Alchemy is a web application built with Streamlit that generates customized recipes based on user input. It leverages the Cohere API for natural language generation to create unique recipes tailored to specific preferences such as ingredients, cuisine type, calorie count, meal type, meal category, and preparation time.

Features
Custom Recipe Generation: Users can input ingredients, cuisine preference, calorie limits, meal type (breakfast, lunch, dinner, dessert), meal category (vegetarian or non-vegetarian), and duration to generate personalized recipes.
Natural Language Processing: Utilizes Cohere's natural language generation model (c4ai-aya-23) to construct coherent recipes based on user specifications.
Interactive Interface: Built using Streamlit, providing a user-friendly interface where users can input their preferences via text inputs and dropdown menus.
Downloadable Recipe: Generated recipes can be downloaded as a text file (recipe.txt) for offline access.
How to Use
Input Details: Fill out the form with details such as ingredients, cuisine preference, calorie limit, meal type, meal category, and duration.
Generate Recipe: Click on the "Generate Recipe" button to initiate the recipe generation process.
View and Download Recipe: The application displays the generated recipe on the screen. Users can also download the recipe by clicking the "Download Recipe" button.

Dependencies
Python 3.x
Streamlit
Cohere Python Client (cohere)
