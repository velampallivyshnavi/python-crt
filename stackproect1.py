class browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
        print(f"visited {page}")
    def undo(self):
        if len(self.history)>1:
           self.history.pop()
           print(f"back to{self.history[-1]}")
        else:
            print("no pages to comback")
browser=browser()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("facebook.com")
browser.undo()
browser.undo()
browser.undo()