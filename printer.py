
import win32api
import win32ui

dc = win32ui.CreateDC()
dc.CreatePrinterDC()
dc.StartDoc('My Python Document')
dc.StartPage()
dc.TextOut(100,100, 'Python Prints!')
dc.EndPage()
dc.EndDoc()
