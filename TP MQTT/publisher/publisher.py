import time
import random
import paho.mqtt.client as mqtt

# Callbacks for MQTT events
def on_publish(client, userdata, mid, properties=None):
    print("Temperature data published.")

# MQTT client setup
client = mqtt.Client()
client.on_publish = on_publish
client.username_pw_set("MedChaabouni", "21473913med")
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.connect("61d4b7c5d97d42858b6836273e6b8e39.s2.eu.hivemq.cloud", 8883, 60)

# Simulate temperature sensor
while True:
    # Generate random temperature value between 20 and 30 degrees Celsius
    temperature = round(random.uniform(20, 30), 2)

    # Publish temperature data to the "Temp" topic
    result, mid = client.publish("Temp", payload=str(temperature), qos=1)
    
    if result == mqtt.MQTT_ERR_SUCCESS:
        print(f"Published temperature: {temperature}°C")
    else:
        print(f"Failed to publish temperature data. Error code: {result}")

    # Wait for 5 seconds before publishing the next temperature value
    time.sleep(5)
