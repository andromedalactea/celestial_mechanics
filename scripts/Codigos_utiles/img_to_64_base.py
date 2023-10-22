import base64
from PIL import Image

def image_to_base64(image_path):
    """
    Convierte una imagen en un archivo a una cadena Base64.

    Parámetros:
    image_path (str): Ruta al archivo de imagen que se convertirá.

    Retorna:
    str: Cadena Base64 que representa la imagen.
    """
    
    with open(image_path, "rb") as image_file:
        # Lee el archivo y lo convierte en bytes
        image_data = image_file.read()
        
        # Codifica los bytes en Base64
        base64_str = base64.b64encode(image_data).decode("utf-8")
        
    return base64_str

# Uso de la función
base64_output = image_to_base64("/home/andromeda/celestial_mechanics/scripts/Codigos_utiles/velocidades.png")
print(base64_output)