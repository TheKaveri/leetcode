# This problem can be solved by representing each
# webpage as a doubly linked list with that stores
# a url, and references to the previous page as well
# as the forward or 'next' page.

# Keep in mind to property assign and/or update any 
# references like 'previous','next', 'current' etc.
# while adding a new webpage.

class Webpage:

    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = self.current = Webpage(homepage)

    def visit(self, url: str) -> None:
        new_page = Webpage(url)
        self.current.next = new_page
        new_page.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        count = 0

        while count < steps:
            if self.current is self.homepage:
                return self.current.url
            self.current = self.current.prev
            count += 1
        
        return self.current.url

    def forward(self, steps: int) -> str:
        count = 0

        while count < steps:
            if self.current.next is None:
                return self.current.url
            self.current = self.current.next
            count += 1

        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Here's a recursive approach to impelement back and forward:

    def back_recursive(self, steps: int) -> str:
        if steps == 0:
            return self.current.url
        elif self.current is self.homepage:
            return self.current.url
        else:
            self.current = self.current.prev
            return self.back_recursive(steps - 1)

    def forward_recursive(self, steps: int) -> str:
        if steps == 0:
            return self.current.url
        elif self.current.next is None:
            return self.current.url
        else:
            self.current = self.current.next
            return self.forward_recursive(steps - 1)