import zipfile
import os
import xml.etree.ElementTree as ET

ruta_zip = "D:\TAO\XML.zip"  # Ruta al archivo ZIP
ruta_extraccion = "D:\TAO\descomprime"  # Ruta donde se extraerán los archivos

archivo_zip = zipfile.ZipFile(ruta_zip, "r")

try:
    # Obtener la lista de archivos contenidos en el ZIP
    print(archivo_zip.namelist())

    # Extraer todos los archivos
    archivo_zip.extractall(path=ruta_extraccion)

    # Trabajar con el archivo XML extraído
    archivo_xml = os.path.join(ruta_extraccion, "archivo.xml")  # Ruta completa al archivo XML
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    # Ejemplo: Obtener el valor de un elemento específico
    elemento_deseado = root.find("ruta/del/elemento")
    if elemento_deseado is not None:
        print("Valor del elemento deseado:", elemento_deseado.text)
    else:
        print("Elemento no encontrado.")

    # Obtener el nombre del archivo XML
    nombre_archivo_xml = os.path.basename(archivo_xml)
    print("Nombre del archivo XML:", nombre_archivo_xml)

except Exception as e:
    print("Error:", str(e))

archivo_zip.close()
