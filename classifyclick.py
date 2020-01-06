import sys
from classicle_model import classicle_model

model_name = 'model-bilstm'
seed_text = sys.argv[1]
category = classicle_model(seed_text, model_name)
output = "Your text class: %s" % category
print(output)
