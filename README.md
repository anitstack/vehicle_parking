# Automatic Ticket Parking
### *Easy to park, exist & search vehicle tasks in Python*
*Updated 29/08/2021*


#### How to use application 

step-1:
- activate the virtual environment using command "source venv/bin/activate"
- install requirements file by using command "pip3 install -r requirements.txt"

step-2:
- put input.txt file in same directory where app.py existing or you can pass absolute path for file

step-3:
- run the application, use command - "python3 app.py input.txt"


#### run unit test for application

command-1: "python3 -m unittest unittests/test_parking.py"

command-2: "python3 -m unittest unittests/test_vehicle.py"

command-3: "python3 -m unittest unittests/test_parking.py"

### Logging
 - log file is storing in same directory of project with name - vehicle_parking.log
# Attributes
- green - for success output
- yellow - for warning output
- red - for error or exception
- status_update - for display normal data
- begin_status_update - starting for each command
- end_status_update - ending for each command
- queue_full_log

# recommanded termial for view log

#### Drawback
- for successfully run application, each command in the file should be in suggested format