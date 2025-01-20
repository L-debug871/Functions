'''lerato moholo 10 September 2024'''




def get_block(data):
    # Find the block between "BEGIN" and "END"
    start = data.find("BEGIN")
    end = data.find("END")
    if start != -1 and end != -1:
        return data[start:end + len("END")]
    else:
        return None

def location(block):
    # Extract the location information starting from the 4th last character up to 'END'
    start_index = len(block) - 4  # This gives the index of the 4th last character
    end_index = block.find('END')  # Find the position of 'END'
    
    # Extract the substring for location
    extracted_string = block[start_index:end_index].strip()  # Extract from the 4th last character to 'END'
    extracted_string = extracted_string[::-1]  # Reverse the string as per your original logic
    return extracted_string

def temperature(block):
    # Find the start and end of the temperature value
    start_str = block.find('BEGIN') + len('BEGIN') + 1  # Adjust for "BEGIN" and a following space
    end_index = block.find('_')  # Extract until the underscore
    if start_str != -1 and end_index != -1:
        # Extract the substring for temperature
        temp_str = block[start_str:end_index].strip()
        return float(temp_str)  # Convert the temperature to float
    else:
        return None  # Return None if temperature is not found

def x_coordinate(block):
    # Extract the x-coordinate from after ":" up to the comma ","
    start_index = block.find(':') + 1
    end_index = block.find(',')
    
    if start_index != -1 and end_index != -1:
        # Extract the substring for x-coordinate
        return block[start_index:end_index].strip()
    else:
        return None  # Return None if coordinates not found

def y_coordinate(block):
    # Extract the y-coordinate from after the comma "," up to the first space after the start
    start_index = block.find(',') + 1
    end_index = block.find(' ', start_index)
    
    if start_index != -1 and end_index != -1:
        return block[start_index:end_index].strip()
    else:
        return None  # Return None if y-coordinate not found
    
def pressure(block):
    # Extract the pressure value between "_" and ":"
    start_index = block.find('_') + 1
    end_index = block.find(':')
    
    if start_index != -1 and end_index != -1:
        # Extract the substring for pressure
        pressure_str = block[start_index:end_index].strip()
        return float(pressure_str)
    else:
        return None  # Return None if pressure is not found

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    
    if block:
        print('Site information:')
        print('Location:', location(block))
        print('Coordinates:', y_coordinate(block), x_coordinate(block))
        
        temp = temperature(block)
        if temp is not None:
            print(f'Temperature: {temp:.2f} C')
        else:
            print('Temperature not found')
        
        pres = pressure(block)
        if pres is not None:
            print(f'Pressure: {pres:.2f} hPa')
        else:
            print('Pressure not found')
    else:
        print("No valid block found.")

if __name__ == '__main__':
    main()
