import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf", classes="bg-blue-200")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True, width=150, overlay=False)

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

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary",
                         classes="text-4xl m-2 pt-16 pb-8 text-center text-bold font-serif text-blue-100")
        #jp.QIcon(a=toolbar, name="d.png", right=True, size="lg", color="white-600")

        container = jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-blue-200 h-screen text-center")
        jp.Div(a=div, text="Welcome to the homepage!",
               classes="text-4xl m-2 pt-16 pb-8 text-center text-bold font-serif")
        jp.Div(a=div, text="Welcome to the Instant Dictionary, your gateway to a world of knowledge at your fingertips."
                           " This revolutionary web app allows you to instantly access the definition of any English "
                           "word, right as you type it. No more tediously flipping through pages or searching through "
                           "online dictionaries. With our intuitive interface, you can effortlessly expand your "
                           "vocabulary and enhance your understanding of language.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
