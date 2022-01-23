# # Exercise 2: Virtual Weather-Station

# Create a virtual IoT device that simulates the ambient temperature and
# publishes it via MQTT. The simulation function is already predefined.
# This exercise to give a simple introduction to the communication via MQTT.

# The input sections are marked with 'ToDo'

# #### Steps to complete:
# 1. Set up the missing parameters in the parameter section
# 2. Create an MQTT client using the paho-mqtt package with mqtt.Client()
# 3. Define a callback function that will be executed when the client
#    receives message on a subscribed topic. It should decode your message
#    and store the information for later in our history
# 4. Subscribe to the topic that the device will publish to
# 5. Create a function that publishes the simulated temperature via MQTT as a JSON
# 6. Run the simulation and plot

# ## Import packages
import json
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import time
from urllib.parse import urlparse
# import simulation model
from tutorial.simulation_model import SimulationModel

# ## Parameters
# ToDo: Enter your mqtt broker url and port, e.g mqtt://test.mosquitto.org:1883
MQTT_BROKER_URL = "mqtt://test.mosquitto.org:1883"

# ToDo: Create a topic that your weather station will publish to
topic_weather_station = "fiware_workshop/<name_surname>/weather_station"

# set parameters for the temperature simulation
temperature_max = 10  # maximal ambient temperature
temperature_min = -5  # minimal ambient temperature

t_sim_start = 0  # simulation start time in seconds
t_sim_end = 24 * 60 * 60  # simulation end time in seconds
sim_step = 1  # simulation step in seconds
com_step = 60 * 60  # communication step in seconds

# ## Main script
if __name__ == '__main__':
    # instantiate simulation model
    sim_model = SimulationModel(t_start=t_sim_start,
                                t_end=t_sim_end,
                                dt=sim_step,
                                temp_max=temperature_max,
                                temp_min=temperature_min,
                                temp_start=20)

    # define lists to store historical data
    history_weather_station = []

    # ToDo: create a MQTTv5 client with paho-mqtt
    mqttc = mqtt.Client(protocol=mqtt.MQTTv5)

    # ToDo: Define a callback function that will be executed when the client
    #  receives message on a subscribed topic. It should decode your message
    #  and store the information for later in our history
    #  Note: do not change function's signature!
    def on_message(client, userdata, msg):
        payload = msg.payload.decode('utf-8')
        history_weather_station.append(json.loads(payload))


    # add your callback function to the client
    mqttc.on_message = on_message

    # ToDO: connect to the mqtt broker and subscribe to your topic
    mqtt_url = urlparse(MQTT_BROKER_URL)
    mqttc.connect(host=mqtt_url.hostname,
                  port=mqtt_url.port,
                  keepalive=60,
                  bind_address="",
                  bind_port=0,
                  clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY,
                  properties=None)

    # ToDo: subscribe to the weather station topic
    mqttc.subscribe(topic=topic_weather_station)

    # create a non-blocking thread for mqtt communication
    mqttc.loop_start()

    # ToDo: Create a loop that publishes every second a message to the broker
    #  that holds the simulation time "t_sim" and the corresponding temperature
    #  "temperature" the loop should
    for t_sim in range(sim_model.t_start, sim_model.t_end + com_step, com_step):
        # ToDo: publish the simulated ambient temperature
        mqttc.publish(topic=topic_weather_station,
                      payload=json.dumps({"t_amb": sim_model.t_amb,
                                          "t_sim": sim_model.t_sim}))

        # simulation step for next loop
        sim_model.do_step(t_sim+com_step)
        time.sleep(1)

    # close the mqtt listening thread
    mqttc.loop_stop()
    # disconnect the mqtt device
    mqttc.disconnect()

    # plot results
    fig, ax = plt.subplots()
    t_simulation = [item["t_sim"] for item in history_weather_station]
    temperature = [item["t_amb"] for item in history_weather_station]
    ax.plot(t_simulation, temperature)
    ax.set_xlabel('time in s')
    ax.set_ylabel('ambient temperature in °C')
    plt.show()