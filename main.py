import pygame
import random


pygame.init()


class DrawingInfo:
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255
    BROWN = 120,69,19
    GREY = 128,128,128
    L_GREY = 160,160,160
    D_GREY = 192,192,192

    BLOCK_COLOURS = [
        GREY, 
        D_GREY,
        L_GREY
    ]

    BACKGROUND_COLOUR = BROWN

    FONT = pygame.font.SysFont("comic-sans", 20, bold=False, italic=True)
    LARGER_FONT = pygame.font.SysFont("Arial", 25, bold=True)

    SIDE_PADDING = 100
    TOP_PADDING = 100

    def __init__(self, width, height, list):
            self.width = width
            self.height = height
            self.set_list(list)
            

            self.window = pygame.display.set_mode((width ,height))
            title       = pygame.display.set_caption("SORTING ALGORITHM VISUALIZER")
            
    def set_list(self, list):
        self.list = list
        self.max = max(list)
        self.min = min(list)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(list))
        self.block_height = round(((self.width - 200) - self.TOP_PADDING) / (self.max - self.min))
        self.start_x = self.SIDE_PADDING // 2
        self.start_y = self.TOP_PADDING // 2
        pass


def draw(draw_info, algorithm_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)

    # Display the sorting algorithm and order
    title = draw_info.LARGER_FONT.render(
        f"{algorithm_name} - {'Ascending' if ascending else 'Descending'}",
        1,
        draw_info.BLUE,
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 25))

    # Display controls for resetting, starting, and toggling order
    control1 = draw_info.LARGER_FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.BLACK,
    )
    draw_info.window.blit(control1, (draw_info.width / 2 - control1.get_width() / 2, 5))

    # Display controls for choosing sorting algorithms
    control2 = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | M - Merge Sort | Q - Quick Sort | S - Selection Sort",
        1,
        draw_info.BLACK,
    )
    draw_info.window.blit(control2, (draw_info.width / 2 - control2.get_width() / 2, 45))

    # Draw the sorting list visualization
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_postion={}, clear_bg=False):
    list = draw_info.list

    if clear_bg:
        clear_rect = (draw_info.SIDE_PADDING//2, draw_info.TOP_PADDING, draw_info.width - draw_info.SIDE_PADDING, draw_info.height - draw_info.TOP_PADDING)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clear_rect)

    for index, value in enumerate(list):

        x = draw_info.start_x + index * draw_info.block_width
        y = draw_info.height - (value - draw_info.min) * draw_info.block_height

        block_colour = draw_info.BLOCK_COLOURS[index % 3]

        if index in color_postion:
            block_colour = color_postion[index] 
        
        pygame.draw.rect(draw_info.window, block_colour, (x , y, draw_info.block_width, draw_info.height ))
    
    if clear_bg:
        pygame.display.update()
    
        


def bubble_sort(draw_info, assending=True):

    list = draw_info.list

    for i in range(len(list) - 1):  
        for j in range(len(list)- 1 - i):   
            num1 = list[j]
            num2 = list[j + 1]
            if assending == False and num1 > num2:
                list[j], list[j + 1] = list[j + 1], list[j]
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, True)
                yield True
            elif assending == True and num1 < num2:
                list[j], list[j + 1] = list[j + 1], list[j]
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, True)
                yield True
              
    return list


def insertion_sort(draw_info, assending=True):
    list = draw_info.list

    for i in range(1, len(list)):

        key = list[i]
        j = i - 1

        while j >=0 and (assending and key < list[j] or not assending and key > list[j]):
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key
        draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, True)
        yield True

    return list

def selection_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(len(lst)):
        min_or_max_index = i
        for j in range(i + 1, len(lst)):
            if (ascending and lst[j] < lst[min_or_max_index]) or (not ascending and lst[j] > lst[min_or_max_index]):
                min_or_max_index = j

        lst[i], lst[min_or_max_index] = lst[min_or_max_index], lst[i]
        draw_list(draw_info, {i: draw_info.RED, min_or_max_index: draw_info.GREEN}, True)
        yield True


def merge_sort(draw_info, ascending=True):
    lst = draw_info.list

    def merge(start, mid, end):
        left = lst[start:mid + 1]
        right = lst[mid + 1:end + 1]

        i = j = 0
        for k in range(start, end + 1):
            if i < len(left) and (j >= len(right) or (ascending and left[i] <= right[j]) or (not ascending and left[i] >= right[j])):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            draw_list(draw_info, {k: draw_info.GREEN}, True)
            yield True

    def merge_sort_recursive(start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        yield from merge_sort_recursive(start, mid)
        yield from merge_sort_recursive(mid + 1, end)
        yield from merge(start, mid, end)

    yield from merge_sort_recursive(0, len(lst) - 1)


def quick_sort(draw_info, ascending=True):
    lst = draw_info.list

    def partition(start, end):
        pivot = lst[end]
        p_index = start

        for i in range(start, end):
            if (ascending and lst[i] <= pivot) or (not ascending and lst[i] >= pivot):
                lst[i], lst[p_index] = lst[p_index], lst[i]
                draw_list(draw_info, {i: draw_info.RED, p_index: draw_info.GREEN}, True)
                p_index += 1

        lst[p_index], lst[end] = lst[end], lst[p_index]
        draw_list(draw_info, {p_index: draw_info.BLUE}, True)
        return p_index

    def quick_sort_recursive(start, end):
        if start >= end:
            return

        p_index = partition(start, end)
        yield from quick_sort_recursive(start, p_index - 1)
        yield from quick_sort_recursive(p_index + 1, end)

    yield from quick_sort_recursive(0, len(lst) - 1)

def generate_starting_list(n, min_val, max_val):

    list = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        list.append(val)
    
    return list


def main():
    running = True
    sorting = False
    ascending = True

    algorithms = {
        'B': bubble_sort,
        'I': insertion_sort,
        'S': selection_sort,
        'M': merge_sort,
        'Q': quick_sort,
    }

    algorithm_name = "Bubble Sort"
    algorithm = bubble_sort
    sort_generator = None

    clock = pygame.time.Clock()

    n = 50
    min_val = 1
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawingInfo(1000, 800, lst)

    while running:
        clock.tick(30)

        if sorting:
            try:
                next(sort_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False

                elif event.key == pygame.K_SPACE and not sorting:
                    sort_generator = algorithm(draw_info, ascending)
                    sorting = True

                elif event.key == pygame.K_a:
                    ascending = True

                elif event.key == pygame.K_d:
                    ascending = False

                elif event.key in [pygame.K_b, pygame.K_i, pygame.K_s, pygame.K_m, pygame.K_q]:
                    if event.key == pygame.K_b:
                        algorithm = bubble_sort
                        algorithm_name = "Bubble Sort"
                    elif event.key == pygame.K_i:
                        algorithm = insertion_sort
                        algorithm_name = "Insertion Sort"
                    elif event.key == pygame.K_s:
                        algorithm = selection_sort
                        algorithm_name = "Selection Sort"
                    elif event.key == pygame.K_m:
                        algorithm = merge_sort
                        algorithm_name = "Merge Sort"
                    elif event.key == pygame.K_q:
                        algorithm = quick_sort
                        algorithm_name = "Quick Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
