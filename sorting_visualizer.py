import turtle
import random

class SortingVisualizer:
    def __init__(self, bars):
        self.bars = bars
        self.bar_colors = ["red" for i in range(len(bars))]
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(-250, 250)
        self.turtle.pendown()

    def quicksort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quicksort(low, pivot_index - 1)
            self.quicksort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.bars[high]
        i = low - 1
        for j in range(low, high):
            if self.bars[j] <= pivot:
                i += 1
                self.bars[i], self.bars[j] = self.bars[j], self.bars[i]
                self.bar_colors[i], self.bar_colors[j] = self.bar_colors[j], self.bar_colors[i]
                self.draw_bars()
        self.bars[i + 1], self.bars[high] = self.bars[high], self.bars[i + 1]
        self.bar_colors[i + 1], self.bar_colors[high] = self.bar_colors[high], self.bar_colors[i + 1]
        self.draw_bars()
        return i + 1

    def draw_bars(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(-250, 250)
        self.turtle.pendown()
        for i in range(len(self.bars)):
            self.turtle.fillcolor(self.bar_colors[i])
            self.turtle.begin_fill()
            self.turtle.left(90)
            self.turtle.forward(self.bars[i])
            self.turtle.right(90)
            self.turtle.forward(5)
            self.turtle.right(90)
            self.turtle.forward(self.bars[i])
            self.turtle.left(90)
            self.turtle.end_fill()
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()
        self.screen.update()

def main():
    bars = [random.randint(20, 100) for i in range(50)]
    visualizer = SortingVisualizer(bars)
    visualizer.quicksort(0, len(bars) - 1)
    turtle.done()

if __name__ == "__main__":
    main()

