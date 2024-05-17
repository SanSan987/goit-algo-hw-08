import heapq

def min_cost_to_connect_cables(cables):
    # Перетворення списку кабелів у мін-кучу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки у купі більше одного кабеля
    while len(cables) > 1:
        # Витягти два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на їх з'єднання
        cost = first + second
        total_cost += cost
        
        # Додати новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6, 9, 8]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))

#  Виведення: "Мінімальні витрати на з'єднання кабелів: 78"