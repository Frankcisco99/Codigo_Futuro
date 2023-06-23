import obd #pip install obd
import time
# Establecer conexión con el vehículo
connection = obd.OBD()

# Leer datos de diagnóstico específicos para Suzuki Vitara
engine_rpm_cmd = obd.commands.RPM  # RPM del motor
vehicle_speed_cmd = obd.commands.SPEED  # Velocidad del vehículo
throttle_pos_cmd = obd.commands.THROTTLE_POS  # Posición del acelerador

"""
    Para visualizar más comandos visitar el siguiente enlace:
        https://python-obd.readthedocs.io/en/latest/Command%20Tables/
"""

# Obtener y mostrar datos de diagnóstico en tiempo real
while True:
    engine_rpm_response = connection.query(engine_rpm_cmd)
    vehicle_speed_response = connection.query(vehicle_speed_cmd)
    throttle_pos_response = connection.query(throttle_pos_cmd)

    #Verificando que los datos no esten vacios (null)
    if not engine_rpm_response.is_null() and not vehicle_speed_response.is_null() and not throttle_pos_response.is_null():
        #Si los datos recibidos no estan vacios se asignan a las variables y se imprimen en pantalla
        engine_rpm = engine_rpm_response.value.magnitude
        vehicle_speed = vehicle_speed_response.value.magnitude
        throttle_pos = throttle_pos_response.value.magnitude

        print("RPM del motor: {}".format(engine_rpm))
        print("Velocidad del vehículo: {} km/h".format(vehicle_speed))
        print("Posición del acelerador: {}%".format(throttle_pos))

    # Pausar durante un segundo antes de la siguiente lectura
    time.sleep(1)
