def merge_arrays(arr1, arr2):
    hasil = []
    hasil_sementara = arr1 + arr2
    hasil_sementara = list(set(hasil_sementara))  # Remove duplicates
    hasil_sementara.sort()  # Sort the array
    for i in hasil_sementara:
        if i not in hasil:
            hasil.append(i)
    return hasil