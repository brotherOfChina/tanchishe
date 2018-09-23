import sys, random, pygame

from pygame.rect import Rect

red_meat = pygame.Color(255, 0, 0)
white_snake = pygame.Color(255, 255, 255)
black_background = pygame.Color(0, 0, 0)


def game_over():
    pygame.quit()
    sys.exit()


RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'


def mains():
    pygame.init()
    # 定义一个变量，控制游戏速度
    fpsClock = pygame.time.Clock()
    #   创建
    playSurface = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("贪吃蛇")
    #     初始化
    snake_position = [100, 100]
    # 初始化贪吃蛇长度
    snakeBody = [[100, 100], [80, 100], [60, 100]]
    # 方块位置
    block_position = [300, 300]
    # 定义一个标记，判断是否被吃掉,1被吃掉，0没有
    flag = 1
    #     初始化方向
    direction = RIGHT
    change_direction = direction
    # 把事件放到循环当中
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_direction = RIGHT
                elif event.key == pygame.K_UP:
                    change_direction = UP
                elif event.key == pygame.K_LEFT:
                    change_direction = LEFT
                elif event.key == pygame.K_DOWN:
                    change_direction = DOWN
        if change_direction == LEFT and not direction == RIGHT:
            direction = change_direction
        if change_direction == RIGHT and not direction == LEFT:
            direction = change_direction
        if change_direction == UP and not direction == DOWN:
            direction = change_direction
        if change_direction == DOWN and not direction == UP:
            direction = change_direction
        # 根据方向移动舌头的位置，坐标
        if direction == RIGHT:
            snake_position[0] += 20

        if direction == LEFT:
            snake_position[0] -= 20
        if direction == UP:
            snake_position[1] -= 20
        if direction == DOWN:
            snake_position[1] += 20
        # 增加蛇的长度
        snakeBody.insert(0, list(snake_position))


        # 如果贪吃蛇和目标重合，说明吃掉，标记为0
        if snake_position == block_position:
            flag = 0
        else:
            snakeBody.pop()
        if flag == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            block_position = [int(x * 20), int(y * 20)]
            flag = 1
        playSurface.fill(black_background)
        for position in snakeBody:
            pygame.draw.rect(playSurface, white_snake, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, white_snake, Rect(block_position[0], block_position[1], 20, 20))
        pygame.display.flip()
        #    判断是否游戏结束
        if snake_position[0]>620 or snake_position[0]<0:
            game_over()
        elif snake_position[1]>460 or snake_position[1]<0:
            game_over()
        for i in range(len(snakeBody)) :
            if i > 0 and snakeBody[i]==snake_position:
                game_over()
        fpsClock.tick(5)


mains()
