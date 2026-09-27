class HistoryNode:
    def __init__(self, url = ''):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.hist = HistoryNode(homepage)
        

    def visit(self, url: str) -> None:
        tmp = self.hist
        self.hist.next = HistoryNode(url)
        self.hist = self.hist.next
        self.hist.prev = tmp
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.hist.prev: break
            self.hist = self.hist.prev
        return self.hist.url
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.hist.next: break
            self.hist = self.hist.next
        return self.hist.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)