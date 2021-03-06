# create a fictional table filled with 200 supermarket products, prices, types, brand
# and store them in a list of dictionaries
# types: fruit, vegetable, meat, bread, dairy, drinks, snacks, drygoods, frozen food, cleaners, papergoods, personalcare, pets, eletronics, books, toys, music, video, games, office, others

store_products  = [
    {'name': 'apple', 'price': '$1.00', 'type': 'fruit'},
    {'name': 'banana', 'price': '$0.50', 'type': 'fruit'},
    {'name': 'orange', 'price': '$0.75', 'type': 'fruit'},
    {'name': 'pear', 'price': '$0.75', 'type': 'fruit'},
    {'name': 'strawberry', 'price': '$1.00', 'type': 'fruit'},
    {'name': 'tomato', 'price': '$0.75', 'type': 'fruit'},
    {'name': 'potato', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'carrot', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'broccoli', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'cucumber', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'onion', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'garlic', 'price': '$0.50', 'type': 'vegetable'},
    {'name': 'beef', 'price': '$2.00', 'type': 'meat'},
    {'name': 'chicken', 'price': '$1.50', 'type': 'meat'},
    {'name': 'pork', 'price': '$1.50', 'type': 'meat'},
    {'name': 'lamb', 'price': '$1.50', 'type': 'meat'},
    {'name': 'turkey', 'price': '$1.50', 'type': 'meat'},
    {'name': 'bread', 'price': '$0.75', 'type': 'bread'},
    {'name': 'cheese', 'price': '$1.00', 'type': 'dairy'},
    {'name': 'milk', 'price': '$1.00', 'type': 'dairy'},
    {'name': 'yogurt', 'price': '$1.00', 'type': 'dairy'},
    {'name': 'eggs', 'price': '$1.00', 'type': 'dairy'},
    {'name': 'juice', 'price': '$1.00', 'type': 'drinks'},
    {'name': 'coffee', 'price': '$1.00', 'type': 'drinks'},
    {'name': 'tea', 'price': '$1.00', 'type': 'drinks'},
    {'name': 'water', 'price': '$1.00', 'type': 'drinks'},
    {'name': 'chocolate', 'price': '$1.00', 'type': 'snacks'},
    {'name': 'nuts', 'price': '$1.00', 'type': 'snacks'},
    {'name': 'soda', 'price': '$1.00', 'type': 'snacks'},
    {'name': 'sausage', 'price': '$1.00', 'type': 'snacks'},
    {'name': 'rice', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'pasta', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'bread', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'cereal', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'soup', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'ice cream', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'ice', 'price': '$0.50', 'type': 'drygoods'},
    {'name': 'frozen', 'price': '$0.50', 'type': 'frozen food'},
    {'name': 'ice cream', 'price': '$0.50', 'type': 'frozen food'},
    {'name': 'ice', 'price': '$0.50', 'type': 'frozen food'},
    {'name': 'cleaning', 'price': '$0.50', 'type': 'cleaners'},
    {'name': 'paper', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'tissue', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'toilet paper', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'shampoo', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'soap', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'toothpaste', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'deodorant', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'toothbrush', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'shaving', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'hair', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'hair gel', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'hair spray', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'hair dye', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'hair care', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'laptop', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'phone', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'tablet', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'camera', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'tv', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'headphones', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'speakers', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'earphones', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'charger', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'headset', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'watch', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'camera', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'laptop', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'phone', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'tablet', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'camera', 'price': '$0.50', 'type': 'electronics'},
    {'name': 'shampoo', 'price': '$0.50', 'type': 'papergoods'},
    {'name': 'soap', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'toothpaste', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'deodorant', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'toothbrush', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'shaving', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'hair', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'hair gel', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'hair spray', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'hair dye', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'hair care', 'price': '$0.50', 'type': 'personal care'},
    {'name': 'cleaning', 'price': '$0.50', 'type': 'cleaners'},
]
