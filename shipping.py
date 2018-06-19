def ground_cost(weight):
  cost = 20.00
  if (weight <= 2):
    cost += (weight * 1.50)
  elif (weight <= 6):
    cost += (weight * 3.00)
  elif (weight <= 10):
    cost += (weight * 4.00)
  else:
    cost += (weight * 4.75)
  return cost

print(ground_cost(8.4))

premium_ground_cost = 125.00

def drone_cost(weight):
  return (ground_cost(weight) - 20.00) * 3

print(ground_cost(1.5))
print(drone_cost(1.5))

def cheapest_shipping(weight):
  ground = ground_cost(weight)
  drone  = drone_cost(weight)
  if (ground < drone) and (ground < premium_ground_cost):
    print("It is cheapest to ship by ground.  Cost is $" + str(ground))
  elif (drone < premium_ground_cost):
    print("It is cheapest to ship by drone.  Cost is $" + str(drone))
  else:
    print("It is chepeast to ship by premium ground.  Cost is $" + str(premium_ground_cost))
    
cheapest_shipping(4.8)
cheapest_shipping(41.5)
