import random
from faker import Faker

fake = Faker()

positive_reviews = [
    "This T-shirt is fantastic! The quality is {quality} and it fits {fit}.",
    "I love this T-shirt! The material is {material} and the design is {design}.",
    "Amazing T-shirt! It exceeded my expectations. I will definitely buy more.",
    "Great T-shirt! It's {comfort} and looks {appearance}.",
    "This T-shirt is excellent! The fabric is {fabric_quality} and it fits {fit}.",
    "Highly recommend this T-shirt! The {quality} quality and {design} design make it a great purchase.",
    "The best T-shirt I've ever bought! The {fabric_quality} fabric and {fit} fit are perfect.",
    "Very pleased with this T-shirt. The {material} material and {appearance} look are wonderful.",
    "This T-shirt is my favorite! The {comfort} comfort and {quality} quality are unmatched.",
    "Super happy with this purchase. The T-shirt feels {material} and looks {design}.",
    "The T-shirt is {quality}. It is very {comfort} and fits {fit}.",
    "I am delighted with this T-shirt. The design is {design} and the fabric is {fabric_quality}.",
    "This is an excellent T-shirt! The material is {material} and the fit is {fit}.",
    "I bought this T-shirt and it is {quality}. The appearance is {appearance} and it's {comfort}.",
    "What a fantastic T-shirt! The quality is {quality} and the design is {design}.",
    "This T-shirt is so comfortable and the fabric feels {fabric_quality}.",
    "I'm really impressed with the durability of this T-shirt. It looks {appearance} even after several washes.",
    "This T-shirt has a {design} design and the {material} material is very comfortable.",
    "I can't believe how {quality} this T-shirt is for the price. It fits {fit} and feels {comfort}.",
    "This is the best T-shirt I've ever purchased. The {fabric_quality} fabric and {appearance} look are outstanding.",
    "I'm thrilled with this T-shirt! The {design} design and {comfort} comfort are amazing.",
    "This T-shirt is top-notch. The {material} material is very {comfort} and it fits {fit}.",
    "I love the way this T-shirt looks! The design is {design} and the fabric feels {fabric_quality}.",
    "This T-shirt is a great value. The quality is {quality} and the fit is {fit}.",
    "The color and design of this T-shirt are {appearance}. It's very {comfort} to wear.",
    "I couldn't be happier with this T-shirt. The {fabric_quality} fabric and {fit} fit are perfect.",
    "Fantastic T-shirt! The {material} material is {comfort} and the {design} design is awesome.",
    "This T-shirt exceeded my expectations. The quality is {quality} and it fits {fit} so well.",
    "Best T-shirt I've ever owned. The fabric is {fabric_quality} and the design is {design}.",
    "The fit of this T-shirt is {fit} and the material feels {material}. I highly recommend it.",
    "This T-shirt feels {material} and looks {appearance}. I absolutely love it.",
    "The quality of this T-shirt is {quality}, and the design is {design}.",
    "I was surprised by the {fabric_quality} fabric and the {fit} fit of this T-shirt.",
    "Great value for money. The T-shirt is {quality} and feels {comfort}.",
    "This T-shirt is really {comfort} and the material is {material}.",
    "I am very happy with this purchase. The T-shirt looks {appearance} and fits {fit}.",
    "This T-shirt is exactly what I wanted. The design is {design} and the quality is {quality}.",
    "Love this T-shirt! The {quality} is great and it fits {fit}.",
    "This is the most {comfort} T-shirt I own. The {material} material is just perfect.",
    "I got so many compliments on this T-shirt. The {design} design is eye-catching.",
    "The {fabric_quality} fabric of this T-shirt makes it feel very {comfort}.",
    "I'm very pleased with this T-shirt. The {quality} quality and {appearance} look make it a great buy.",
    "This T-shirt is exceptional! The quality is {quality} and it fits {fit} perfectly.",
    "I adore this T-shirt! The material is {material} and the design is simply {design}.",
    "What a wonderful T-shirt! It feels {comfort} and looks {appearance}.",
    "I'm in love with this T-shirt. The fabric is {fabric_quality} and it fits {fit} just right.",
    "A fantastic purchase. The T-shirt is {quality} and feels {comfort} to wear."
]

neutral_reviews = [
    "This T-shirt is okay. The quality is {quality} and it fits {fit}.",
    "The T-shirt is decent. The material is {material} and the design is {design}.",
    "An average T-shirt. It met my expectations, nothing more.",
    "It's a good T-shirt. It feels {comfort} and looks {appearance}.",
    "The T-shirt is satisfactory. The fabric is {fabric_quality} and it fits {fit}.",
    "A reasonable purchase. The {quality} quality and {design} design are acceptable.",
    "This T-shirt is fine. The {fabric_quality} fabric and {fit} fit are okay.",
    "A decent T-shirt. The {material} material and {appearance} look are fine.",
    "This T-shirt is alright. The {comfort} comfort and {quality} quality are okay.",
    "Satisfied with this purchase. The T-shirt feels {material} and looks {design}.",
    "The T-shirt is {quality}. It is {comfort} and fits {fit}.",
    "Content with this T-shirt. The design is {design} and the fabric is {fabric_quality}.",
    "An acceptable T-shirt. The material is {material} and the fit is {fit}.",
    "I bought this T-shirt and it is {quality}. The appearance is {appearance} and it's {comfort}.",
    "A good T-shirt! The quality is {quality} and the design is {design}.",
    "This T-shirt is reasonably comfortable and the fabric feels {fabric_quality}.",
    "Impressed with the durability of this T-shirt. It looks {appearance} after several washes.",
    "This T-shirt has a {design} design and the {material} material is okay.",
    "This T-shirt is good for the price. It fits {fit} and feels {comfort}.",
    "This is a good T-shirt for everyday use. The {fabric_quality} fabric and {appearance} look are satisfactory.",
    "This T-shirt is decent. The {design} design and {comfort} comfort are acceptable.",
    "A good T-shirt. The {material} material is {comfort} and it fits {fit}.",
    "I like the way this T-shirt looks. The design is {design} and the fabric feels {fabric_quality}.",
    "This T-shirt is a fair value. The quality is {quality} and the fit is {fit}.",
    "The color and design of this T-shirt are {appearance}. It's {comfort} to wear.",
    "I'm okay with this T-shirt. The {fabric_quality} fabric and {fit} fit are acceptable.",
    "An average T-shirt. The {material} material is {comfort} and the {design} design is okay.",
    "This T-shirt met my expectations. The quality is {quality} and it fits {fit}.",
    "A decent T-shirt. The fabric is {fabric_quality} and the design is {design}.",
    "The fit of this T-shirt is {fit} and the material feels {material}. A fair purchase.",
    "This T-shirt feels {material} and looks {appearance}. I'm satisfied.",
    "The quality of this T-shirt is {quality}, and the design is {design}.",
    "The {fabric_quality} fabric and the {fit} fit of this T-shirt are okay.",
    "Good value for money. The T-shirt is {quality} and feels {comfort}.",
    "This T-shirt is {comfort} and the material is {material}.",
    "I am okay with this purchase. The T-shirt looks {appearance} and fits {fit}.",
    "This T-shirt is just what I needed. The design is {design} and the quality is {quality}.",
    "A decent T-shirt! The {quality} is good and it fits {fit}.",
    "This is a comfortable T-shirt. The {material} material is okay.",
    "I got compliments on this T-shirt. The {design} design is nice.",
    "The {fabric_quality} fabric of this T-shirt is {comfort}.",
    "I'm satisfied with this T-shirt. The {quality} quality and {appearance} look are acceptable.",
    "This T-shirt is good! The quality is {quality} and it fits {fit}.",
    "This T-shirt is alright. The material is {material} and the design is {design}.",
    "An acceptable T-shirt. It feels {comfort} and looks {appearance}.",
    "I'm okay with this T-shirt. The fabric is {fabric_quality} and it fits {fit}.",
    "A good purchase. The T-shirt is {quality} and feels {comfort} to wear."
]

negative_reviews = [
    "I am disappointed with this T-shirt. The quality is {quality} and it doesn't fit {fit}.",
    "This T-shirt is terrible. The fabric is {fabric_quality} and it {issue} after the first wash.",
    "I don't like this T-shirt at all. The color {color_quality} and it feels {comfort}.",
    "This T-shirt is not worth the money. It looks {appearance} in the picture but is {quality}.",
    "I regret buying this T-shirt. It's too {fit} and the material feels {comfort}.",
    "Not satisfied with this T-shirt. The {quality} quality and {fit} fit are disappointing.",
    "Avoid this T-shirt. The {fabric_quality} fabric and {appearance} look are not good.",
    "This T-shirt is a waste of money. The {material} material and {comfort} comfort are subpar.",
    "Terrible T-shirt. The {color_quality} color and {issue} issue are unacceptable.",
    "This T-shirt didn't meet my expectations. The {quality} quality and {fit} fit are poor.",
    "The T-shirt is {quality}. It is very {comfort} and fits {fit}.",
    "I am unhappy with this T-shirt. The design is {design} and the fabric is {fabric_quality}.",
    "This is a poor T-shirt! The material is {material} and the fit is {fit}.",
    "I bought this T-shirt and it is {quality}. The appearance is {appearance} and it's {comfort}.",
    "What a terrible T-shirt! The quality is {quality} and the design is {design}.",
    "This T-shirt is very uncomfortable. The fabric feels {comfort} and the fit is {fit}.",
    "The color of this T-shirt {color_quality} and the material is {material}.",
    "I am really disappointed with the quality of this T-shirt. It looks {appearance} after just one wash.",
    "This T-shirt is poorly made. The fabric is {fabric_quality} and it {issue}.",
    "I regret purchasing this T-shirt. The {quality} quality and {fit} fit are not good.",
    "The material of this T-shirt is {material} and it feels {comfort} on the skin.",
    "This T-shirt is overpriced for the quality it offers. The fit is {fit} and the material is {material}.",
    "I didn't like this T-shirt at all. The design is {design} and the quality is {quality}.",
    "The fabric of this T-shirt is {fabric_quality} and it doesn't fit {fit}.",
    "I'm not happy with this purchase. The T-shirt looks {appearance} and feels {comfort}.",
    "The T-shirt {issue} after the first wash. The quality is {quality} and the fit is {fit}.",
    "Very poor quality T-shirt. The material is {material} and the design is {design}.",
    "I wouldn't recommend this T-shirt. The color {color_quality} and the fabric is {fabric_quality}.",
    "This T-shirt doesn't meet the advertised standards. The quality is {quality} and the fit is {fit}.",
    "I'm dissatisfied with this T-shirt. The material is {material} and the appearance is {appearance}.",
    "This T-shirt is cheaply made. The {fabric_quality} fabric is not durable.",
    "I am very unhappy with this T-shirt. The {design} design is not appealing.",
    "The T-shirt arrived in poor condition. The quality is {quality} and the fit is {fit}.",
    "I don't recommend this T-shirt. The material is {material} and it's very {comfort}.",
    "This T-shirt is a huge disappointment. The color {color_quality} and the fit is {fit}.",
    "The quality of this T-shirt is {quality} and it doesn't feel {comfort} at all.",
    "I'm regretting my purchase. The fabric is {fabric_quality} and the design is {design}.",
    "This T-shirt looks {appearance} and feels {material}. Not worth the money.",
    "The fabric quality is {fabric_quality} and it doesn't fit {fit}.",
    "The design is {design} and the color quality is {color_quality}. Very disappointing.",
    "This T-shirt is very {comfort} and the quality is {quality}.",
    "I'm not happy with this T-shirt. It looks {appearance} and the fit is {fit}.",
    "The material feels {material} and the T-shirt {issue} after one wash.",
    "I don't recommend this T-shirt. The {design} design and {quality} quality are poor.",
    "This T-shirt is not worth the price. The quality is {quality} and the fit is {fit}.",
    "I'm very disappointed with this T-shirt. The material is {material} and it feels {comfort}.",
    "The color {color_quality} and the fabric {fabric_quality}. A bad purchase.",
    "I wouldn't buy this T-shirt again. The {design} design is {quality}.",
    "The T-shirt looks {appearance} but the material feels {material}."
]

positive_qualities = ["top-notch", "excellent", "superb", "remarkable", "fantastic", "outstanding", "great", "wonderful", "amazing", "high-quality"]
neutral_qualities = ["decent", "satisfactory", "acceptable", "average", "okay", "good", "fair", "adequate", "reasonable", "fine"]
negative_qualities = ["poor", "mediocre", "substandard", "inferior", "shoddy", "terrible", "disappointing", "bad", "low-quality", "unacceptable"]

positive_fits = ["perfectly", "well", "just right", "comfortably", "nicely", "ideally"]
neutral_fits = ["okay", "alright", "fairly well", "adequately", "decently", "reasonably"]
negative_fits = ["poorly", "awkwardly", "too tight", "too loose", "badly", "improperly"]

positive_materials = ["soft", "comfortable", "smooth", "luxurious", "premium", "high-quality", "delicate", "plush", "silky", "fine"]
neutral_materials = ["decent", "okay", "good", "average", "fine", "satisfactory", "adequate", "acceptable", "fair", "reasonable"]
negative_materials = ["rough", "itchy", "cheap", "flimsy", "low-grade", "uncomfortable", "scratchy", "stiff", "crude", "coarse"]

positive_designs = ["stylish", "modern", "elegant", "trendy", "chic", "attractive", "cool", "fashionable", "classy", "sleek"]
neutral_designs = ["simple", "plain", "average", "unremarkable", "ordinary", "basic", "standard", "common", "decent", "fair"]
negative_designs = ["plain", "unattractive", "dated", "outdated", "ugly", "boring", "tacky", "dull", "old-fashioned", "bland"]

positive_comforts = ["comfortable", "cozy", "pleasant", "snug", "soft", "relaxing", "easygoing", "soothing", "welcoming", "comfy"]
neutral_comforts = ["okay", "decent", "average", "fine", "adequate", "acceptable", "fair", "reasonable", "satisfactory", "alright"]
negative_comforts = ["uncomfortable", "scratchy", "irritating", "annoying", "rough", "stiff", "unpleasant", "itchy", "harsh", "unbearable"]

positive_appearances = ["great", "fantastic", "awesome", "vibrant", "attractive", "beautiful", "appealing", "gorgeous", "eye-catching", "striking"]
neutral_appearances = ["decent", "okay", "good", "fine", "average", "satisfactory", "adequate", "acceptable", "reasonable", "fair"]
negative_appearances = ["okay", "bad", "dull", "unattractive", "disappointing", "ugly", "plain", "uninspiring", "drab", "unappealing"]

positive_fabric_qualities = ["high-quality", "durable", "premium", "long-lasting", "robust", "solid", "first-class", "excellent", "superior", "resilient"]
neutral_fabric_qualities = ["decent", "okay", "good", "fine", "average", "satisfactory", "adequate", "acceptable", "reasonable", "fair"]
negative_fabric_qualities = ["cheap", "flimsy", "low-grade", "fragile", "weak", "inferior", "delicate", "poor", "second-rate", "shoddy"]

positive_color_qualities = ["stayed vibrant", "was perfect", "was bright", "was consistent", "held up well", "was sharp", "did not fade", "remained true", "was lively", "looked great"]
neutral_color_qualities = ["was okay", "was decent", "was good", "was fine", "was average", "was satisfactory", "was acceptable", "was reasonable", "was fair", "was adequate"]
negative_color_qualities = ["faded quickly", "looked dull", "was inconsistent", "was washed out", "did not hold up", "was patchy", "lost its color", "bled", "was muddy", "was uneven"]

issues = ["shrunk", "stretched", "faded", "tore", "pilled", "frayed", "lost shape", "discolored", "ripped", "deformed"]

reviews = []


number_of_reviews = random.randint(1000, 1200)

for _ in range(number_of_reviews):
    random_val = random.random()
    if random_val < 0.75:
        template = random.choice(positive_reviews)
        review = template.format(
            quality=random.choice(positive_qualities),
            fit=random.choice(positive_fits),
            material=random.choice(positive_materials),
            design=random.choice(positive_designs),
            comfort=random.choice(positive_comforts),
            appearance=random.choice(positive_appearances),
            fabric_quality=random.choice(positive_fabric_qualities),
            color_quality=random.choice(positive_color_qualities),
            issue=random.choice(issues)  
        )
    elif random_val < 0.9:
        template = random.choice(negative_reviews)
        review = template.format(
            quality=random.choice(negative_qualities),
            fit=random.choice(negative_fits),
            material=random.choice(negative_materials),
            design=random.choice(negative_designs),
            comfort=random.choice(negative_comforts),
            appearance=random.choice(negative_appearances),
            fabric_quality=random.choice(negative_fabric_qualities),
            color_quality=random.choice(negative_color_qualities),
            issue=random.choice(issues)
        )
    else:
        template = random.choice(neutral_reviews)
        review = template.format(
            quality=random.choice(neutral_qualities),
            fit=random.choice(neutral_fits),
            material=random.choice(neutral_materials),
            design=random.choice(neutral_designs),
            comfort=random.choice(neutral_comforts),
            appearance=random.choice(neutral_appearances),
            fabric_quality=random.choice(neutral_fabric_qualities),
            color_quality=random.choice(neutral_color_qualities),
            issue=random.choice(issues) 
        )

        
    reviews.append(review)

with open('filling_reviews/tshirt_review_1.txt', 'w') as f:
    for review in reviews:
        f.write(review + "\n\n")
