tipping_point = int(input())
infected = int(input())
infection_rate = int(input())

iterations = 0
newly_infected = infected

while infected <= tipping_point:
    iterations += 1
    newly_infected = newly_infected * infection_rate
    infected += newly_infected

print(iterations)
