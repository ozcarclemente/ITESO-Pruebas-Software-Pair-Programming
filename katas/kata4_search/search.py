import json
import os

def _load_cities() -> list:
    """Función auxiliar para cargar los datos del JSON."""
    path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["cities"]
    

def search(search_text: str) -> list:
    """
    Busca ciudades basándose en el texto de entrada.
    """
    cities = _load_cities()

    # Requerimiento 5: Asterisco retorna todo
    if search_text == "*":
        return cities

    # Requerimiento 1: Menos de 2 caracteres retorna lista vacía
    if len(search_text) < 2:
        return []

    # Requerimientos 2, 3 y 4: Búsqueda case-insensitive por prefijo/substring
    search_lower = search_text.lower()
    return [city for city in cities if search_lower in city.lower()]

