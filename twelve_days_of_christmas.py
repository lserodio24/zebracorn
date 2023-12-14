from graphics import *

def display_verse(win, verse_number):
    verse_texts = ["On the first day of Christmas \n my true love sent to me \n A partridge in a pear tree.", "On the second day of Christmas \n My true love gave to me \n Two turtle doves \n And a partridge in a pear tree.", "On the third day of Christmas \n My true love gave to me \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the fourth day of Christmas \n My true love gave to me \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the fifth day of Christmas  \n My true love gave to me   \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the sixth day of Christmas  \n My true love gave to me \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the seventh day of Christmas \n My true love gave to me \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the eighth day of Christmas \n My true love gave to me \n Eight maids a-milking, \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the ninth day of Christmas \n My true love gave to me \n Nine ladies dancing, \n Eight maids a-milking, \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the tenth day of Christmas \n My true love gave to me \n Ten lords a-leaping, \n Nine ladies dancing, \n Eight maids a-milking, \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the eleventh day of Christmas \n My true love gave to me \n Eleven pipers piping, \n Ten lords a-leaping, \n Nine ladies dancing, \n Eight maids a-milking, \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.", "On the twelfth day of Christmas \n My true love gave to me \n Twelve drummers drumming, \n Eleven pipers piping, \n Ten lords a-leaping, \n Nine ladies dancing, \n Eight maids a-milking, \n Seven swans a-swimming, \n Six geese a-laying, \n Five golden rings, \n Four calling birds, \n Three French hens, \n Two turtle doves \n And a partridge in a pear tree.",       ]
    verse_text = Text(Point(win.getWidth() / 2, win.getHeight() / 2), verse_texts[verse_number - 1])
    verse_text.setSize(16)
    verse_text.draw(win)
    if verse_number == 1:
        verse_number_text = Text(Point(win.getWidth() / 2, 20), f"The {verse_number}st day")
    elif verse_number == 2:
        verse_number_text = Text(Point(win.getWidth() / 2, 20), f"The {verse_number}nd day")
    elif verse_number == 3:
        verse_number_text = Text(Point(win.getWidth() / 2, 20), f"The {verse_number}rd day")
    else:
        verse_number_text = Text(Point(win.getWidth() / 2, 20), f"The {verse_number}th day")
    verse_number_text.setSize(16)
    verse_number_text.draw(win)
    return verse_number_text


def main():
    verse_number = 0
    win = GraphWin("12 days of Christmas Kareoke!", 600, 400)
    verse_number_text = display_verse(win, verse_number)
    while verse_number <= 12:
        for item in win.items[:]:
            item.undraw()
        verse_number_text.undraw()
        verse_number += 1
        if verse_number % 2 == 0:
            background = Rectangle(Point(0, 400), Point(600, 400))
            win.setBackground("light blue")
            background.draw(win)
            ground = Polygon(Point(0, 400), Point(0, 340), Point(600, 340), Point(600, 400))
            ground.setFill("white")
            ground.draw(win)
            # snowman 1
            man1bottom = Circle(Point((win.getWidth() / 5), 275), 80)
            man1bottom.setFill("white")
            man1bottom.draw(win)
            man1mid = Circle(Point((win.getWidth() / 5), 170), 65)
            man1mid.setFill("white")
            man1mid.draw(win)
            man1top = Circle(Point((win.getWidth() / 5), 80), 50)
            man1top.setFill("white")
            man1top.draw(win)
            bottombutton1 = Circle(Point((win.getWidth() / 5), 210), 4)
            bottombutton1.setFill("black")
            bottombutton1.draw(win)
            midbutton1 = Circle(Point((win.getWidth() / 5), 180), 4)
            midbutton1.setFill("black")
            midbutton1.draw(win)
            topbutton1 = Circle(Point((win.getWidth() / 5), 150), 4)
            topbutton1.setFill("black")
            topbutton1.draw(win)
            lefteye1 = Circle(Point((win.getWidth() / 5) - 20, 80), 7)
            lefteye1.setFill("black")
            lefteye1.draw(win)
            righteye1 = Circle(Point((win.getWidth() / 5) + 20, 80), 7)
            righteye1.setFill("black")
            righteye1.draw(win)
            nose1 = Polygon(Point((win.getWidth() / 5) - 10, 100), Point((win.getWidth() / 5) - 10, 110), Point((win.getWidth() / 5) +20, 105))
            nose1.setFill("orange")
            nose1.draw(win)
            # snowman 2
            man2bottom = Circle(Point((win.getWidth() * 4 / 5), 275), 80)
            man2bottom.setFill("white")
            man2bottom.draw(win)
            man2mid = Circle(Point((win.getWidth() * 4 / 5), 170), 65)
            man2mid.setFill("white")
            man2mid.draw(win)
            man2top = Circle(Point((win.getWidth() * 4 / 5), 80), 50)
            man2top.setFill("white")
            man2top.draw(win)
            bottombutton2 = Circle(Point((win.getWidth() * 4 / 5), 210), 4)
            bottombutton2.setFill("black")
            bottombutton2.draw(win)
            midbutton2 = Circle(Point((win.getWidth() * 4 / 5), 180), 4)
            midbutton2.setFill("black")
            midbutton2.draw(win)
            topbutton2 = Circle(Point((win.getWidth() * 4 / 5), 150), 4)
            topbutton2.setFill("black")
            topbutton2.draw(win)
            lefteye2 = Circle(Point((win.getWidth() * 4 / 5) - 20, 80), 7)
            lefteye2.setFill("black")
            lefteye2.draw(win)
            righteye2 = Circle(Point((win.getWidth() * 4 / 5) + 20, 80), 7)
            righteye2.setFill("black")
            righteye2.draw(win)
            nose2 = Polygon(Point((win.getWidth() * 4 / 5) - 10, 100), Point((win.getWidth() * 4 / 5) - 10, 110), Point((win.getWidth() * 4 / 5) +20, 105))
            nose2.setFill("orange")
            nose2.draw(win)
        elif verse_number % 2 == 1:
            background = Rectangle(Point(0, 400), Point(600, 400))
            win.setBackground("red")
            background.draw(win)
            ground = Polygon(Point(0, 400), Point(0, 340), Point(600, 340), Point(600, 400))
            ground.setFill("white")
            ground.draw(win)
            #tree 1
            trunk1 = Rectangle(Point((win.getWidth() / 5) - 10, 300), Point((win.getWidth() / 5) + 10, 375))
            trunk1.setFill("brown")
            trunk1.draw(win)
            tree1bottom = Polygon(Point((win.getWidth() / 5), 150), Point((win.getWidth() / 5) - 100, 300), Point((win.getWidth() / 5) + 100, 300))
            tree1bottom.setFill("green")
            tree1bottom.draw(win)
            tree1mid = Polygon(Point((win.getWidth() / 5), 100), Point((win.getWidth() / 5) - 75, 225), Point((win.getWidth() / 5) + 75, 225))
            tree1mid.setFill("green")
            tree1mid.draw(win)
            tree1top = Polygon(Point((win.getWidth() / 5), 50), Point((win.getWidth() / 5) - 50, 150), Point((win.getWidth() / 5) + 50, 150))
            tree1top.setFill("green")
            tree1top.draw(win)
            star1 = Polygon(Point((win.getWidth() / 5), 40), Point((win.getWidth() / 5) - 5, 50), Point((win.getWidth() / 5) + 5, 50))
            star1.setFill("yellow")
            star1.draw(win)
            #tree 2
            trunk2 = Rectangle(Point((win.getWidth() * 4 / 5) - 10, 300), Point((win.getWidth() * 4 / 5) + 10, 375))
            trunk2.setFill("brown")
            trunk2.draw(win)
            tree2bottom = Polygon(Point((win.getWidth() * 4 / 5), 150), Point((win.getWidth() * 4 / 5) - 100, 300), Point((win.getWidth() * 4 / 5) + 100, 300))
            tree2bottom.setFill("green")
            tree2bottom.draw(win)
            tree2mid = Polygon(Point((win.getWidth() * 4 / 5), 100), Point((win.getWidth() * 4 / 5) - 75, 225), Point((win.getWidth() * 4 / 5) + 75, 225))
            tree2mid.setFill("green")
            tree2mid.draw(win)
            tree2top = Polygon(Point((win.getWidth() * 4 / 5), 50), Point((win.getWidth() * 4 / 5) - 50, 150), Point((win.getWidth() * 4 / 5) + 50, 150))
            tree2top.setFill("green")
            tree2top.draw(win)
            star2 = Polygon(Point((win.getWidth() * 4 / 5), 40), Point((win.getWidth() * 4 / 5) - 5, 50), Point((win.getWidth() * 4 / 5) + 5, 50))
            star2.setFill("yellow")
            star2.draw(win)
        if verse_number <= 12:
            verse_number_text = display_verse(win, verse_number)
        click_point = win.getMouse()

    win.close()

if __name__ == "__main__":
    main()

