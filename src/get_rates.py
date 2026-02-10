import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://v6.exchangerate-api.com/v6"


def obtener_tasa_ars(base="USD"):

    if not API_KEY:
        raise ValueError("API key no configurada")

    url = f"{BASE_URL}/{API_KEY}/latest/{base}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        datos = response.json()
        if datos.get("result") != "success":
            raise ValueError("Respuesta inválida de la API")

        return datos["conversion_rates"]["ARS"]

    except requests.RequestException as e:
        print(f"Error de conexión con la API: {e}")
        return None


def obtener_tasas(base="USD"):

    if not API_KEY:
        raise ValueError("API key no configurada")

    url = f"{BASE_URL}/{API_KEY}/latest/{base}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        datos = response.json()

        if datos.get("result") != "success":
            raise ValueError("Respuesta inválida de la API")

        return datos["conversion_rates"]  # 👈 devuelve todo el diccionario

    except requests.RequestException as e:
        print(f"Error de conexión con la API: {e}")
        return None
