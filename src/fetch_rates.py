from converters import convertir_a_usd
from get_rates import obtener_tasas

tasas_disponibles = obtener_tasas("USD")

if tasas_disponibles:
    try:
        monto = float(input("Ingrese el monto: "))
        moneda = input("Ingrese el tipo de moneda (EJ: ARS,VND,EUR): ").strip().upper()

        resultado = convertir_a_usd(monto, moneda, tasas_disponibles)

        if resultado is not None:
            print("\n--- Resultado ---")
            print(f"{monto} {moneda} equivalen a {resultado:.2f} USD")
        else:
            print("Moneda no válida.")

    except ValueError:
        print("Error: Ingrese un número válido.")
