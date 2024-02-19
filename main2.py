current_speed = float(input('input the current speed:'))
Speed = float(input('Please input the speed limit: '))
Difference = current_speed - Speed
if current_speed > Speed and Difference <= 5:
    print('Stop accelerating!')
elif Difference >= 5:
    print('Too fast! Brake!')
else:
    print('There is no need to brake.')
    
    