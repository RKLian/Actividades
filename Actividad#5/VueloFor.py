Vuelo = {
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}

print("Valor del diccionario:")
for Key, Value in Vuelo.items():
    print(f"{Key}: {Value}")

print("\nTipo de maleta:")
for Maleta in Vuelo['Tipo_Maleta']:
    print(Maleta)
