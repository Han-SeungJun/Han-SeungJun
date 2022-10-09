import wx
from search import _search2
import keyboard

class mainFrame(wx.Frame):
    def __init__(self, parent, title = "네이버 기사 탭뷰 검색창 0.2ver", size = (500, 500)):
        wx.Frame.__init__(self, parent, title = "네이버 기사 탭뷰 검색창 0.2ver", size = (500, 500))

        self.static_inform_text = wx.StaticText(self, id = 1, label = "검색할 키워드를 입력하세요")
        inform_font = wx.Font(18, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        self.static_inform_text.SetFont(inform_font)

        search_panel = wx.Panel(self)
        self.search_keyword_input = wx.TextCtrl(search_panel, id = 2)
        self.search_result_window = wx.TextCtrl(self, id = 3, size = (500, 300),
                                                value = "이곳에 기사와 링크가 출력됩니다.",
                                                style = wx.TE_MULTILINE | wx.TE_READONLY)

        search_btn = wx.Button(search_panel, label = "검색")
        search_btn.Bind(wx.EVT_BUTTON, self.onClick)
        keyboard.add_hotkey("enter", lambda:self.search_enter())

        search_tab = wx.BoxSizer(wx.HORIZONTAL)
        search_tab.Add(self.search_keyword_input)
        search_tab.Add(search_btn)
        search_panel.SetSizer(search_tab)

        box = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(box)
        box.Add(self.static_inform_text, border = 10, flag = wx.CENTER)
        box.Add(search_panel, flag = wx.ALIGN_CENTER_HORIZONTAL)
        box.Add(self.search_result_window, flag = wx.ALIGN_CENTER_HORIZONTAL)
        
    def onClick(self, event):
        search_text = self.search_keyword_input.GetValue()
        search_result = _search2(search_text)
        f = open('article_text.txt', 'w')
        for x in search_result:
            f.write(x)
            f.write('\n')
        f.close()
        
        f = open('article_text.txt', 'r')
        self.search_result_window.SetValue(f.read())
        f.close()

    def search_enter(self):
        search_text = self.search_keyword_input.GetValue()
        search_result = _search2(search_text)
        f = open('article_text.txt', 'w')
        for x in search_result:
            f.write(x)
            f.write('\n')
        f.close()
        
        f = open('article_text.txt', 'r')
        self.search_result_window.SetValue(f.read())
        f.close()
        
if __name__ == '__main__':
    app = wx.App()
    frame = mainFrame(None)
    frame.Show()
    app.MainLoop()
