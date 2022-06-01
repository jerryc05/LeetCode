class BrowserHistory:
    def __init__(self, homepage: str):
        self.l = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        if len(self.l) <= self.i:
            self.l.append(url)
        else:
            self.l[self.i] = url
            self.l = self.l[: self.i + 1]

    def back(self, steps: int) -> str:
        self.i -= steps
        if self.i < 0:
            self.i = 0
        return self.l[self.i]

    def forward(self, steps: int) -> str:
        self.i += steps
        if self.i >= len(self.l):
            self.i = len(self.l) - 1
        return self.l[self.i]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
assert browserHistory.back(1) == "facebook.com"
assert browserHistory.back(1) == "google.com"
assert browserHistory.forward(1) == "facebook.com"
browserHistory.visit("linkedin.com")
assert browserHistory.forward(2) == "linkedin.com"
assert browserHistory.back(2) == "google.com"
assert browserHistory.back(7) == "leetcode.com"
print('ok')
