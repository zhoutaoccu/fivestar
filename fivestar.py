# coding=utf-8
'''
Created on 2014-11-17
@author: Neo

Update on 2017/9/27
@author: Zhoutaoccu
#修正了五角星的边长和外接圆半径之间的关系；
#修正了4小五角星朝向不正对大五角星的错误
'''
import turtle
import math

def draw_polygon(aTurtle, size=50, n=3):
    ''' 绘制正多边形

    args:
        aTurtle: turtle对象实例
        size: int类型，正多边形的边长
        n: int类型，是几边形
    '''
    for i in range(n):
        aTurtle.forward(size)
        aTurtle.left(360.0 / n)


def draw_n_angle(aTurtle, size=50, num=5, color=None):
    ''' 绘制正n角形，默认为黄色

    args:
        aTurtle: turtle对象实例
        size: int类型，正多角形的边长
        n: int类型，是几角形
        color: str， 图形颜色，默认不填色
    '''
    if color:
        aTurtle.begin_fill()
        aTurtle.fillcolor(color)
    for i in range(num):
        aTurtle.forward(size)
        aTurtle.left(360.0 / num)
        aTurtle.forward(size)
        aTurtle.right(2 * 360.0 / num)
    if color:
        aTurtle.end_fill()


def draw_5_angle(aTurtle=None, start_pos=(0, 0), end_pos=(0, 10), radius=100, color=None):
    ''' 根据起始位置、结束位置和外接圆半径画五角星

    args:
        aTurtle: turtle对象实例
        start_pos: int的二元tuple，要画的五角星的外接圆圆心
        end_pos: int的二元tuple，圆心指向的位置坐标点
        radius: 五角星外接圆半径
        color: str， 图形颜色，默认不填色
    '''
    aTurtle = aTurtle or turtle.Turtle()
    # size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)计算公式错误，但不影响显示
    size = radius * math.sin(math.pi / 5) / math.sin(math.pi * 3 / 10)  # 修正
    angle = math.degrees(math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0]))
    print(angle)
    aTurtle.pencolor("yellow")
    aTurtle.penup()
    aTurtle.goto(start_pos)
    aTurtle.setheading(0)
    aTurtle.left(angle)
    aTurtle.fd(radius)
    aTurtle.pendown()
    aTurtle.right(math.degrees(math.pi * 9 / 10))
    draw_n_angle(aTurtle, size, 5, color)


def draw_5_star_flag(times=20.0):
    ''' 绘制五星红旗

    args:
        times: 五星红旗的规格为30*20， times为倍数，默认大小为10倍， 即300*200
    '''
    width, height = 30 * times, 20 * times
    # 初始化屏幕和海龟
    window = turtle.Screen()
    aTurtle = turtle.Turtle()
    aTurtle.hideturtle()
    aTurtle.speed(10)
    # 画红旗
    aTurtle.penup()
    aTurtle.goto(-width / 2, height / 2)
    aTurtle.pendown()
    aTurtle.begin_fill()
    aTurtle.fillcolor('red')
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.end_fill()
    # 画大星星
    draw_5_angle(aTurtle, start_pos=(-10 * times, 5 * times), end_pos=(-10 * times, 8 * times), radius=3 * times,color='yellow')
    # 画四个小星星
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
    for pos in stars_start_pos:
        draw_5_angle(aTurtle, start_pos=(pos[0] * times, pos[1] * times), end_pos=(-10 * times, 5 * times),radius=1 * times, color='yellow')
        # 点击关闭窗口
    window.exitonclick()


if __name__ == '__main__':
    draw_5_star_flag()
