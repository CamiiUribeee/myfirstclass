def max_subarray_sum(arr):
    max_actual = arr[0]  # Mejor suma hasta el momento
    max_global = arr[0]  # Mejor suma encontrada

    for i in range(1, len(arr)):
        # Decidimos si sumamos el elemento o empezamos desde él
        max_actual = max(arr[i], max_actual + arr[i])
        max_global = max(max_global, max_actual)

    return max_global

# Ejemplo
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))  # Salida: 6
