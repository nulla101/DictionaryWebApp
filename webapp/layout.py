import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self,  view='hHh lpR fFf', classes="bg-blue-200", **kwargs):
        super().__init__(view=view, classes=classes, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True, width=150, overlay=False)

        scroller = jp.QScrollArea(a=drawer, classes="fit bg-blue-100")
        qlist = jp.QList(a=scroller)
        a_classes = "text-lg m-2 pb-5 pl-5 text-center text-italic font-serif hover:text-blue-700"
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary",
                         classes="text-4xl m-2 pt-16 pb-8 text-center text-bold font-serif text-blue-100")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
