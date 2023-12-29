# Linked List class

## Описание

Класс для работы со связанным списком.

Реализован следующий функционал:
* создание пустого связанного списка
* создание списка на основе некоторой коллекции
* добавление элемента в конец, начало или середину списка
* удаление элемента с конца, начало или середины списка
* удаление элементов по значению
* проверка наличия значения в списке
* проверка пустой список или нет
* конвертация в обычный список
* количество значений в списке
* проверка на палиндром
* реверс
* очистка

## Сборка

* linked_list.py: класс связанного списка
* linked_list_test.py: юниттесты

## Примеры использования

#### Создание пустого связанного списка
```
ll = LinkedList()
```
#### Создание связанного списка из коллекции
```
ll = LinkedList([1, 2, 3])
```
#### Добавление элемента в конец списка
```
ll = LinkedList([1, 2, 3])
ll.append(4)
print(ll)  # [1 -> 2 -> 3 -> 4]
```
#### Добавление элемента в начало списка
```
ll = LinkedList([1, 2, 3])
ll.append_left(0)
print(ll)  # [0 -> 1 -> 2 -> 3]
```
#### Добавление элемента в середину списка (по позиции)
```
ll = LinkedList([1, 2, 3])
ll.insert(1, 7)
print(ll)  # [1 -> 7 -> 2 -> 3]
```
#### Удаление элемента с конца списка
```
ll = LinkedList([1, 2, 3, 4])
el = ll.pop()
print(ll)  # [1 -> 2 -> 3]
print(el)  # 4
```
#### Удаление элемента с начала списка
```
ll = LinkedList([1, 2, 3])
el = ll.pop(0)
print(ll)  # [2 -> 3]
print(el)  # 1
```
#### Удаление элемента с середины списка (по позиции)
```
ll = LinkedList([1, 2, 3])
el = ll.pop(1)
print(ll)  # [1 -> 3]
print(el)  # 2
```
#### Удаление элементов по значению
```
ll = LinkedList([1, 2, 2, 3])
ll.delete(2)
print(ll)  # [1 -> 3]
```
#### Проверка наличия значения в списке
```
ll = LinkedList([1, 2, 3])
if 2 in ll:
    print(ll)  # [1 -> 2 -> 3]
```
#### Проверка пустой список или нет
```
ll = LinkedList()
if ll.is_empty():
    print(True)  # True
```
#### Конвертация в обычный список
```
ll = LinkedList([1, 2, 3])
lst = ll.get_list()
print(type(lst), lst)  # <class 'list'> [1, 2, 3]
```
#### Количество значений в списке
```
ll = LinkedList([1, 2, 2, 3])
print(ll.counter())  # defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 1})
```
#### Проверка на палиндром
```
ll = LinkedList(['a', 'b', 'b', 'a'])
print(ll.is_palindrome())  # True
```
#### Реверс
```
ll = LinkedList([1, 2, 3, 4])
ll.reverse()
print(ll)  # [4 -> 3 -> 2 -> 1]
```
#### Очистка
```
ll = LinkedList([1, 2, 3, 4])
ll.clean()
print(ll)  # []
```