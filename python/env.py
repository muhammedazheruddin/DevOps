import os

stage=os.getenv('STAGE','dev').upper()
output = f"We're Running in {stage}"
if stage.startswith('PROD'):
    output = "Danger!!! - " + output

print(output)
