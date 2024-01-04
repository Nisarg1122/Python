
Empty_Tuple = ()

Sisters = ('Edda', 'Kaylie', 'Priyanka')

Brothers = ('Ricon', 'Edard', 'Karth')

Siblings = Brothers + Sisters

Num_Siblings = len(Siblings)

Family_Members = ('Father', 'Mother') + Siblings

Father, Mother, *Other_Family_Members = Family_Members

Fruits = ('Apple', 'Banana', 'Mango')

Vegetables = ('Beens', 'Spinach', 'Carrot')

Animal_Products = ('Milk', 'Meat', 'Eggs')

Food_Stuff_TP = Fruits + Vegetables + Animal_Products

Food_Stuff_IT = list(Food_Stuff_TP)

Middle_Index = len(Food_Stuff_IT) // 2

Middle_Item = Food_Stuff_IT[Middle_Index] if len(Food_Stuff_IT) % 2 != 0 else Food_Stuff_IT[Middle_Index-1:Middle_Index+1]

First_Three_Items = Food_Stuff_IT[:3]

Last_Three_Items = Food_Stuff_IT[-3:]

del Food_Stuff_TP

Nordic_Countries = ('India', 'Estonia', 'USA', 'Iceland', 'Germany')

Estonia_Nordic = 'Estonia' in Nordic_Countries

Iceland_Nordic = 'Iceland' in Nordic_Countries

