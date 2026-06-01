def farenheit_conversion():
  celcius=int(input("Enter your celcius="))
  farenheit=((celcius*9/5)+32)
  print("farenheit=",farenheit)
  return farenheit
farenheit_conversion()
def celcius_conversion():
  farenheit=int(input("Enter your temperature in farenheit="))
  celcius=((farenheit-32)*5/9)
  print("celcius=",celcius)
  return celcius
celcius_conversion()
    