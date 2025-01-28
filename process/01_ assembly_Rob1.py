import compas_rrc as rrc
import os
from production_data import ProductionData
import json
import sys
import roslibpy
import time

HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, '..', 'data'))
print(DATA)


file_name = DATA + "/"+ "20241206_rob2_GRASP_D08.json"
output_path = os.path.join(file_name + '_output.json')
print(output_path)

PRODUCTION_LOG_CONFIG = dict(
    ENABLED=True,                       # Generate a log of received feedback
    OVERWRITE=True,                     # When True, it will create a new log file every time, otherwise, it will append to existing
    CONSOLE_OUTPUT=True,                # When True, it will print received feedback on the console
)
 
if __name__ == '__main__':

    #open json nd read production data
    if os.path.exists(file_name):
        print('Using production data file: {}'.format(file_name))
        with open(file_name, 'r') as fp:
            production_data = ProductionData.from_data(json.load(fp))
            #print (len(production_data.actions))
    else:
        print('Cannot find production data file: {}'.format(file_name))
        sys.exit(-1)
   
    #Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    #Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

  
    for i in range(len(production_data.actions)):
    #for i in range(1700,1809,1):

        action = production_data.actions[i]
        prefixed_action_class_name = '{}{}'.format("rrc.", action.name)
        instruction_type = eval(prefixed_action_class_name)

        if instruction_type is None:
            raise Exception('Cannot find implementation for instruction: {}'.format(action.name))
        instruction = instruction_type(**action.parameters)
        abb.send(instruction)
        time.sleep(0.01)
        print(instruction)
        # Store production log

    #End of Code
    print('Finished')

    #Close client
    ros.close()
    ros.terminate()
