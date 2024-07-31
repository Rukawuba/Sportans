import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height, age, gender):
    # BMI formula
    bmi = str((weight / (height * height)) * 10000)
    a=bmi.split('.')
    bmi=a[0]+'.'+a[1][:2]
    return float(bmi)


def calculate_bmr(weight, height, age, gender):
    if gender=="Male":
        bmr=str(66.47+(6.24*(weight*2.205))+(12.7*(height*0.394))-(6.755*age))
    else:
        bmr=str(655.1+(4.35*(weight*2.205))+(4.7*(height*0.394))-(4.7*age))

    a=bmr.split('.')
    bmr=a[0]+'.'+a[1][:2]

    return float(bmr)

         

def Diet_recommendations(bmr):
    recommendations = ""
    
    if bmr<1200.000:
        recommendations = """
        **Low-Calorie Diet** 

        - *Breakfast* :
        \t- Scrambled eggs with spinach and tomatoes
        \t- Whole-grain toast
        - *Snack* :
        \t- Greek yogurt with berries
        - *Lunch* :
        \t- Grilled chicken salad with mixed greens, cucumbers, and vinaigrette
        - *Snack* :
        \t- Carrot and celery sticks with hummus
        - *Dinner* :
        \t- Baked salmon with asparagus
        \t- Quinoa
        """
    elif 1200.000<bmr<1500.000 :
        recommendations = """
        **Low-Calorie Diet** 

        - *Breakfast* :
        \t- Scrambled eggs with spinach and tomatoes
        \t- Whole-grain toast
        - *Snack* :
        \t- Greek yogurt with berries
        - *Lunch* :
        \t- Grilled chicken salad with mixed greens, cucumbers, and vinaigrette
        - *Snack* :
        \t- Carrot and celery sticks with hummus
        - *Dinner* :
        \t- Baked salmon with asparagus
        \t- Quinoa
        """
    elif 1500.00<bmr<1800.00 :
        recommendations = """
        **Recommendations for Moderate Calorie Diet**
        - Breakfast
        \t- Oatmeal with almond butter and banana slices.
        - Snack
        \t- Cottage cheese with pineapple.
        - Lunch
        \t- Turkey and Avocado wrap on whole-grain tortilla.
        \t- Mixed green salad with olive oil dressing.
        - Snack
        \t- Mixed Nuts.
        - Dinner
        \t- Grilled shrimp with Brocolli and Brown Rice.
        """
    elif 1800.00<bmr<2500.00 :
        recommendations ="""
        **High-Calorie Diet** 

        - *Breakfast*
        \t- Whole-grain pancakes with blueberries and maple syrup
        \t- Scrambled eggs
        - *Snack* :
        \t- Greek yogurt with granola
        - *Lunch* :
        \t- Quinoa and black bean bowl with grilled chicken, avocado, and salsa
        - *Snack* :
        \t- Sliced apple with peanut butter
        - *Dinner* :
        \t- Grilled steak with sweet potato and sautéed kale """
    elif bmr>2500.00:
        recommendations ="""
        ** Very High-Calorie Diet** 

        *Breakfast* :
                Veggie and cheese omelette
                Whole-grain toast
        *Snack* :
                Trail mix with dried fruits and nuts
        *Lunch* :
                Brown rice, lentil, and vegetable stew
        *Snack* :
                Cottage cheese with pear slices
        *Dinner* :
                Baked chicken breast with quinoa and steamed broccoli

        """

    return recommendations 
        
    
# Function to provide fitness recommendations based on BMI
def fitness_recommendations(bmi):
    recommendations = ""

    if bmi < 18.5:
        recommendations = """
        **Recommendations for Underweight Individuals**

        - Increase your calorie intake to gain weight.
        - Consume a balanced diet with a variety of foods.
        - Include lean protein sources like chicken, fish, and beans.
        - Incorporate healthy fats from sources like avocados and nuts.
        - Focus on whole grains, fruits, and vegetables.
        - Consider smaller, more frequent meals.
        - Stay hydrated and avoid empty-calorie drinks.
        - Consult a nutritionist for a personalized plan.
        """
    elif 18.5 <= bmi < 24.9:
        recommendations = """
        **Recommendations for Healthy Weight Individuals**

        - Maintain a balanced diet with a variety of food groups.
        - Focus on lean protein sources, whole grains, and vegetables.
        - Incorporate healthy fats for overall health.
        - Monitor portion sizes to maintain your weight.
        - Stay hydrated with water and limit sugary drinks.
        - Aim for a balanced intake of macronutrients.
        - Consult a nutritionist for personalized guidance.
        """
    elif 25 <= bmi < 29.9:
        recommendations = """
        **Diet Recommendations for Overweight Individuals**

        - Focus on a calorie deficit to lose weight.
        - Choose whole, unprocessed foods and control portion sizes.
        - Increase consumption of fruits and vegetables.
        - Limit added sugars, saturated fats, and sodium.
        - Incorporate lean protein sources for satiety.
        - Stay hydrated with water and limit sugary drinks.
        - Create a balanced, sustainable eating plan.
        - Consult a nutritionist for personalized weight loss strategies.
        """
    else:
        recommendations = """
        **Recommendations for Obese Individuals**

        - Seek professional guidance for severe obesity.
        - Focus on a well-structured, calorie-controlled diet.
        - Prioritize nutrient-dense foods and limit empty calories.
        - Increase physical activity to create a calorie deficit.
        - Monitor portion sizes and reduce overeating.
        - Manage emotional eating and stress-related habits.
        - Consult a healthcare professional and nutritionist for a comprehensive weight loss plan.
        """

    return recommendations

st.title("Fitness Check")


# Input fields for user information
age = st.number_input("Age", min_value=1)
height = st.number_input("Height (in centimeters)", min_value=0.1)
weight = st.number_input("Weight (in kilograms)", min_value=1)
gender = st.radio("Gender", ("Male", "Female", "Other"))

if st.button("Submit"):

    col1,_,col2=st.columns([2,0.1,2])
    # Provide fitness recommendations
    with col1:
        # Calculate BMI
        bmi = calculate_bmi(weight, height, age, gender)

        st.subheader("Your BMI: ")
        st.write(bmi)

        recommendations = fitness_recommendations(bmi)
        st.subheader("Fitness Recommendations:")
        st.write(recommendations)

    with col2:
        bmr = calculate_bmr(weight, height, age, gender)

        st.subheader("Your BMR : ")
        st.write(bmr)

        recommendations = Diet_recommendations(bmr)
        st.subheader("Diet Recommendations:")
        st.write(recommendations)

        



    st.write("---")

    st.header("How Do I Increase my BMR ?  ")
    st.write(''' Everyone's basal metabolic rate (BMR) is different .''')
    st.write(
    " Age , Gender , Size , Height , Weight , Mass , and even the size of your internal organs (larger organs need more fuel) play a part in determining your number. There’s not much you can do to control your genetics, but you can influence your body composition with a few simple changes :"
    )
    st.write('''
    - Build muscle :
    \t- The best way to increase your BMR is to build muscle. Lean muscle mass torches more calories than fat and pumps up your metabolism. Functional training will help you build muscle more than regular workouts; the latter can be limited in terms of movements.
    - Don't cut calories :
    \t- Another way to increase BMR is to eat the right number of calories. That means no semi-starved states and low BMR that comes with it. Men need to consume around 2,500 calories, and women need to consume 2,000 calories daily, according to the National Health Service (NHS). Munch on BMR-boosting foods such as hot peppers, green tea, broccoli, spices, citrus fruits, and cacao.
    - Minimize stress :
    \t- Stress is another huge contributor to low metabolism. A heightened rush of cortisol (the stress hormone) will send your body into “fight or flight” mode. This messes up your system in the long term by making you feel tired, feel irritable, and have hunger pangs and unhealthy cravings.''')


