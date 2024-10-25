import pygame
import random

pygame.init()

SCREEN_WIDTH = 910
SCREEN_HEIGHT = 750
arrSize = 130
rectSize = 7

# display setup
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

arr = [0] * arrSize
Barr = [0] * arrSize
complete = False


def visualize(window, x=-1, y=-1, z=-1):
    window.fill((0, 0, 0))  # Black screen initially

    for i in range(arrSize):
        rect = pygame.Rect(i * rectSize, SCREEN_HEIGHT - arr[i], rectSize, arr[i])

        if complete:
            color = (100, 180, 100)  # Green for completion
        elif i == x or i == z:
            color = (100, 180, 100)  # Green for active comparisons
        elif i == y:
            color = (165, 105, 189)  # Purple for current element
        else:
            color = (170, 183, 184)  # Gray for unselected

        pygame.draw.rect(window, color, rect)

    pygame.display.update()


def selection_sort():
    for i in range(arrSize - 1):
        min_index = i
        for j in range(i + 1, arrSize):
            if arr[j] < arr[min_index]:
                min_index = j
                visualize(window, i, min_index)
            pygame.time.delay(3)
        arr[i], arr[min_index] = arr[min_index], arr[i]
    visualize(window)
    pygame.time.delay(100)


def bubble_sort():
    for i in range(arrSize - 1):
        for j in range(arrSize - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(window, j, j + 1)
            pygame.time.delay(3)
    visualize(window)
    pygame.time.delay(100)


def merge_sort(arr, l, r):
    if l >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    L = arr[l:mid + 1]
    R = arr[mid + 1:r + 1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        visualize(window, k)
        pygame.time.delay(10)
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        visualize(window, k)
        pygame.time.delay(10)
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        visualize(window, k)
        pygame.time.delay(10)
        k += 1


def load_arr():
    global arr
    arr = Barr[:]


def randomize_and_save_array():
    global Barr
    Barr = [random.randint(10, SCREEN_HEIGHT) for _ in range(arrSize)]


def execute():
    global complete
    randomize_and_save_array()
    load_arr()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    complete = False
                    print("\nEXITING SORTING VISUALIZER.\n")
                elif event.key == pygame.K_0:
                    randomize_and_save_array()
                    complete = False
                    load_arr()
                    print("\nNEW RANDOM LIST GENERATED.\n")
                elif event.key == pygame.K_1:
                    load_arr()
                    print("\nSELECTION SORT STARTED.\n")
                    complete = False
                    selection_sort()
                    complete = True
                    print("\nSELECTION SORT COMPLETE.\n")
                elif event.key == pygame.K_2:
                    load_arr()
                    print("\nBUBBLE SORT STARTED.\n")
                    complete = False
                    bubble_sort()
                    complete = True
                    print("\nBUBBLE SORT COMPLETE.\n")
                elif event.key == pygame.K_3:
                    load_arr()
                    print("\nMERGE SORT STARTED.\n")
                    complete = False
                    merge_sort(arr, 0, arrSize - 1)
                    complete = True
                    print("\nMERGE SORT COMPLETE.\n")

        visualize(window)


if __name__ == "__main__":
    print("__________________________________________________")
    print("\n                    SORTING VISUALIZER            ")
    print("__________________________________________________")

    print("\nPress 0 to generate a new random list.")
    print("Press 1 to Selection Sort.")
    print("Press 2 to Bubble Sort.")
    print("Press 3 to Merge Sort.")
    print("Press Q to Quit.")

    execute()

    pygame.quit()
