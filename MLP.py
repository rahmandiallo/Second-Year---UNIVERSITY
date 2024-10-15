import random




def parameters(num_of_inputs, hidden_units, output_units, num_of_epochs, activation_function,learning_rate):

def input(training_data):

    # get user to type in 
    training_data = input("Enter the training data")

def Structure():
    global num_of_inputs
    num_of_inputs = int(input("What are the number of inputs"))
    global hidden_units
    hidden_units = int(input("How many hidden units"))
    global output
    output = int(input("What are the outputs"))


def Initalise():
    # l is the layer, h is the hidden unit , i is the input, o is the output
    # Nested for - loop 
    # The outer loop is the layer
    layer = 2
    for l in range(1,layer+1):
        # Checks if it is in layer 1 or layer 2
        if l == 1:
            # Produces random weights between input and hidden units
            for h in range(1,hidden_units+1):
                for i in range(1,num_of_inputs + 1):
                    random_weight = round(random.random(),2)
                    print(f"Input : {i} , hidden_unit : {h} , random_weight = {random_weight}")
        # As this is in layer 2 , produces random weights between hidden units and output            
        for h in range(1,hidden_units + 1):
            for o in range(1,output+1):
                random_weight = round(random.random(),2)
                print(f"Hidden Unit : {h} , Output : {o} , random_weight = {random_weight}")
                


    





    

