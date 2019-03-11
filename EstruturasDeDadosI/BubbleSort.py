def bubble_sort(lst):
    """   Função Bubble Sort  """
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                print(lst[i], lst[i + 1])
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
                
###################################################
                 EXEMPLO DE USO
###################################################
unsorted = [5, 4, 3, 1, 2, 7, 6]
print('Antes: ', unsorted) # Lista desordenada

# Chama função para ordenar a lista
sort_list(unsorted)

print('Depois:', unsorted) # Lista ordenada
