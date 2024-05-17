import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # Ініціалізація мін-купи першими елементами кожного списку
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    result = []
    
    while min_heap:
        # Витягти найменший елемент з купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Додати наступний елемент з того ж списку до купи, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

# Виведення: Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
