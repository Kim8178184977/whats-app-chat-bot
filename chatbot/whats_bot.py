def respose(input_message):
    message = input_message.lower()
    if message == 'hi' :
        return 'Hi'
    elif message == 'hello' :
        return 'Hi'
    elif message == 'how are you':
        return 'Great'
    elif message == 'how was the day':
        return 'good how was yours'
    elif 'notes' in message:
        return 'sorry i wont able to take notes'
    else :
        return 'sorry i am not good at Hinglish So, try to ask question in english thanks '
    
