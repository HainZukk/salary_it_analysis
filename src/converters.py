def convertir_a_usd(monto,moneda_origen,tasas):
    
    try: 
        tasa = tasas.get(moneda_origen)
        if tasa is None:
            raise ValueError(f"La moneda de {moneda_origen} no esta disponible en las tasas")
        return monto / tasa
    except TypeError:
        print("Error: El monto debe ser un numero y 'tasas' un diccionario")
    except ZeroDivisionError:
        print(f"Error: La tasa para {moneda_origen} es cero. No se puede dividir.")
    except ValueError as e:
        print(f"Error de validacion {e}")
    except ValueError as e:
        print(f"Error inesperado {e}")
    
    return None



       