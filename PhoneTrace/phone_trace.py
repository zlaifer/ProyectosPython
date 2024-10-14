import phonenumbers
from phonenumbers import geocoder, carrier

# Número de teléfono a analizar
phone_number = "+528117485364"
# phone_number = "+573137893058"

# Parsear el número de teléfono
parsed_number = phonenumbers.parse(phone_number, None)

# Obtener la ubicación geográfica
location = geocoder.description_for_number(parsed_number, "es")

# Obtener el proveedor de servicios
service_provider = carrier.name_for_number(parsed_number, "es")

# Imprimir los resultados
print(f"Número de teléfono: {phone_number}")
print(f"Ubicación geográfica: {location}")
print(f"Proveedor de servicios: {service_provider}")
