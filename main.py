import pygame
import random


pygame.init()


class DrawingInfo:
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255
    GREY = 128,128,128
    L_GREY = 160,160,160
    D_GREY = 192,192,192

    BLOCK_COLOURS = [
        GREY, 
        D_GREY,
        L_GREY
    ]

    BACKGROUND_COLOUR = WHITE

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
        self.block_height = round((self.width - self.TOP_PADDING) / (self.max - self.min))
        self.start_x = self.SIDE_PADDING // 2
        self.start_y = self.TOP_PADDING // 2
        pass


def draw(draw_info, bubble , assending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)

    title = draw_info.LARGER_FONT.render(f"{"Bubble Sort" if bubble else "Insertion Sort"} - {"Assending" if assending else "Dessending"}", 1, draw_info.BLUE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 25))

    control1 = draw_info.LARGER_FONT.render("R - Reset | SPACE - Start sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(control1, (draw_info.width / 2 - control1.get_width() / 2, 5))


    control2 = draw_info.FONT.render("I - Insertion sort | B - Bubble sort", 1, draw_info.BLACK)
    draw_info.window.blit(control2, (draw_info.width / 2 - control2.get_width() / 2, 45))

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

def generate_starting_list(n, min_val, max_val):

    list = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        list.append(val)
    
    return list


def main():
    running = True
    sorting = False
    assending = False

    bubble = False

    sort_algorithm = [bubble_sort, insertion_sort]
    sort_algorithm_names = ["bubble sort", "insertion sort"]
    algo_name = ""
    sort_generator = None

    if bubble is True:
        algo_name = sort_algorithm_names[0]
    else:
        algo_name = sort_algorithm_names[1]


    clock = pygame.time.Clock()

    n = 50
    min_val = 1
    max_val = 100


    list = generate_starting_list(n, min_val, max_val)
    draw_info = DrawingInfo(800,800,list)


    while(running):

        clock.tick(30)

        if (sorting):
            try:
                next(sort_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info,bubble, assending)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()

        # if event.type != pygame.KEYDOWN:
        #     continue

        if keys[pygame.K_r]:
            sorting = False
            list = generate_starting_list(n, min_val, max_val)
            draw_info.list = list
            draw(draw_info,bubble, assending)
        elif keys[pygame.K_SPACE] and sorting == False:
            sorting = True
            if (bubble == True):
                sort_generator = sort_algorithm[0](draw_info, assending)
            if (bubble == False):
                sort_generator = sort_algorithm[1](draw_info, assending)
        elif keys[pygame.K_a]:
            assending = True
        elif keys[pygame.K_d]:
            assending = False
        elif keys[pygame.K_i]:
            bubble = False

        elif keys[pygame.K_b]:
            bubble = True

       


            
    pygame.quit()
            

if __name__ == "__main__":
    main()