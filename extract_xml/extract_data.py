import csv
import xml.etree.ElementTree as ET

# Nombre del archivo XML
xml_file = "configplan_cus_customer.xml"

# Analizar el archivo XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Definir un conjunto para almacenar los nombres únicos que contienen jca://
jca_names = set()

# Función para encontrar y almacenar los nombres que contienen jca://
def find_jca_names(element):
    # Recorrer todos los elementos hijos
    for child in element:
        # Si el texto del elemento contiene jca://, agregarlo al conjunto
        if child.text and 'jca://' in child.text:
            jca_names.add(child.text)

        # Llamar recursivamente a la función para los elementos hijos
        find_jca_names(child)

# Llamar a la función para encontrar los nombres jca://
find_jca_names(root)

# Escribir los nombres encontrados en un archivo CSV
csv_file = "EIS.csv"
with open(csv_file, 'w', newline='') as csvfile:
    # Definir el escritor CSV
    csv_writer = csv.writer(csvfile)

    # Escribir el encabezado
    csv_writer.writerow(['EIS'])

    # Escribir cada nombre encontrado
    for name in jca_names:
        csv_writer.writerow([name])

print("Archivo CSV generado exitosamente: ", csv_file)
