# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"

if color_input == "green":
    print("Go")
elif color_input == "yellow":
    print("Wait...")                
elif color_input == "red":
    print("Stop")   


match color_input:
    case "green":       
        print("Go")
    case "yellow":          
        print("Wait...")
    case "red":     
        print("Stop")   

        

