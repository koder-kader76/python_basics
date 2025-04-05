# Style Guide

# 2. In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.


# iceCreamDensity=10

# while iceCreamDensity>0 :
#     print('Drip...')
#     iceCreamDensity-=1

# print('The ice cream melted.')

# iceCreamDensity - using Camel Case
# iceCreamDensity=10, iceCreamDensity-=1 - no space between operands on either side of '='
# iceCreamDensity>0 - no space between operator
# iceCreamDensity>0 : - colon should follow last character - no space in between

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')