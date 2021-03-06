#!/usr/bin/env python
# File generated by reverse AIRIUM translator (version 0.2.1).
# Any change will be overridden on next run.
# flake8: noqa E501 (line too long)

from airium import Airium
import pandas as pd

linklist = [
    "http://katlas.math.toronto.edu/wiki/Main_Page",
]

def conjure_head(addin=False):
    a = Airium()
    with a.head():
        a.meta(charset='utf-8')
        a.meta(content='width=device-width, initial-scale=1.0', name='viewport')
        a.title(_t='Shane Scott')
        a.link(href='css/foundation.css', rel='stylesheet')
        a.script(src='js/vendor/modernizr.js')
        a.link(href='tenta.ico', rel='shortcut icon')
        if (addin):
            a(addin)
        return a


def wrap_nav_on_body(an_arium = Airium()):
    a = Airium()
    with a.body():
        a('<!-- Navigation Bar! -->')
        with a.div(klass="sticky"):
            with a.nav(klass='top-bar', **{'data-topbar': ''}):
                with a.ul(klass='title-area'):
                    with a.li(klass='name'):
                        with a.h1():
                            a.a(href='index.html', _t='Shane Scott')
                    with a.li(klass='toggle-topbar menu-icon'):
                        with a.a(href='#'):
                            a.span(_t='Menu')
                with a.section(klass='top-bar-section'):
                    a('<!-- Left Nav Section -->')
                    with a.ul(klass='left'):
                        with a.li():
                            a.a(href='cv_shane_scott.pdf', _t='CV')
                    with a.ul(klass='left'):
                        with a.li():
                            a.a(href='researchings.html', _t='Papers')
                    with a.ul(klass='left'):
                        with a.li():
                            a.a(href='posters.html', _t='Posters')
                    with a.ul(klass='left'):
                        with a.li():
                            a.a(href='teachings.html', _t='Teaching')
                    with a.ul(klass='left'):
                        with a.li():
                            a.a(href='mathings.html', _t='Math!')
        a('<!-- End Navigation Bar! -->')
        a('<!-- Body Content -->')
        a(an_arium)
    return a


def conjure_bottom():
    a = Airium()
    a.script(src='../js/vendor/jquery.js')
    a.script(src='../js/foundation.min.js')
    with a.script():
        a('$(document).foundation();')
    return a


class Genie:
    def __init__(self):
        self.tome = pd.read_csv("tome.csv")
        self.tome_of_exlinks = pd.read_csv("tome_of_links.csv")

    def conjure_sqbutton(self, row, col_size):
        a = Airium()
        # row = self.tome.loc[row_ii]
        with a.div(klass='small-'+str(col_size)+' small columns'):
            with a.div(klass='content'):
                with a.a(href=row['link']):
                    a.img(src=row['icon'], style='width:100%')
                with a.p():
                    with a.center():
                        with a.a(klass='medium button', href=row['link'],
                                 style='width:100%'):
                            a(row['title'])
        return a

    def conjure_contents(self):
        gridshape = 2
        vis_tome = self.tome[self.tome['type']!='poster_n']
        #
        a = Airium()
        # with a.div(klass='small-11 small-centered columns'):
        with a.p():
            ii=0
            rowcnt = vis_tome.shape[0]
            while (ii < rowcnt):
                with a.div(klass='row'):
                    for foo in range(gridshape):
                        row = vis_tome.iloc[ii]
                        a(self.conjure_sqbutton(row, 12//gridshape))
                        ii = ii + 1
                        if (ii == rowcnt):
                            break
                    # a.div(klass='small-1 column')
                    # a(self.conjure_sqbutton(ii))
                    # ii = ii + 1
        return a

    def conjure_index_page(self):
        a = Airium()
        a('<!DOCTYPE html>')
        head = conjure_head()
        a(head)
        bod_con = self.conjure_contents()
        bod = wrap_nav_on_body(bod_con)
        a(bod)
        bot = conjure_bottom()
        a(bot)
        return a

    def conjure_paperrow(self, row_ii, col_size):
        a = Airium()
        row = self.tome.loc[row_ii]
        with a.div(klass='small-'+str(col_size)+' small columns'):
            with a.div(klass='content'):
                with a.a(href=row['link']):
                    a.img(src=row['icon'], style='width:100%')
                with a.p():
                    with a.center():
                        with a.a(klass='medium button', href=row['link'],
                                 style='width:100%'):
                            a(row['title'])
        return a

    def conjure_paper_contents(self):
        a = Airium()
        # with a.div(klass='small-11 small-centered columns'):
        tome_of_papers = self.tome[self.tome['type']=='paper']
        with a.p():
            for ii, row in tome_of_papers.iterrows():
                with a.div(klass='row align-middle'):
                    with a.div(klass='small-2 small columns'):
                        with a.div(klass='content'):
                            with a.a(href=row['link']):
                                a.img(src=row['icon'], style='width:100%')
                    with a.div(klass='small-10 small columns'):
                        with a.div(klass='content'):
                            with a.a(href=row['link']):
                                a(row['reference'])
        return a

    def conjure_papers_page(self):
        paper_air = Airium()
        paper_air('<!DOCTYPE html>')
        head = conjure_head()
        paper_air(head)
        bod_con = self.conjure_paper_contents()
        bod = wrap_nav_on_body(bod_con)
        paper_air(bod)
        bot = conjure_bottom()
        paper_air(bot)
        return paper_air

    def conjure_posters_contents(self):
        a = Airium()
        # with a.div(klass='small-11 small-centered columns'):
        tome_of_papers = self.tome[(self.tome['type']=='poster')|(self.tome['type']=='poster_n')]
        with a.p():
            for ii, row in tome_of_papers.iterrows():
                with a.div(klass='row align-middle'):
                    with a.div(klass='small-12 small columns'):
                        with a.a(href=row['link']):
                            a.img(src=row['link'], style='width:100%')
        return a

    def conjure_posters_page(self):
        paper_air = Airium()
        paper_air('<!DOCTYPE html>')
        head = conjure_head()
        paper_air(head)
        bod_con = self.conjure_posters_contents()
        bod = wrap_nav_on_body(bod_con)
        paper_air(bod)
        bot = conjure_bottom()
        paper_air(bot)
        return paper_air

    def conjure_js_randomlink_code(self):
        aa = "\n<!--\nfunction Randomlink()\n{\n\turl = new Array;\n"
        for foo, rr in self.tome_of_exlinks.iterrows():
            aa += "\turl["+str(foo)+"]=\""+rr["link"]+"\";\n"
        aa += "\tChooselink = Math.round(Math.random() * (url.length + 1));\n\twindow.open(url[Chooselink], \'_blank\');\n}\n//-->"
        airo = Airium()
        with airo.script(language="Javascript"):
            airo(aa)
        return airo

    def conjure_mathing_contents(self):
        gridwidth = 3
        ds = self.tome_of_exlinks
        #
        a = Airium()
        # with a.div(klass='small-11 small-centered columns'):
        with a.p():
            with a.div(klass='row'):
                with a.center():
                    with a.div(klass='small-12 columns'):
                        with a.a(klass='small button', href="#", onclick=" Randomlink (); return(false)"):
                            a("RANDOM")

            ii=0
            rowcnt = ds.shape[0]
            while (ii < rowcnt):
                with a.div(klass='row'):
                    for foo in range(gridwidth):
                        row = ds.iloc[ii]
                        with a.div(klass='small-' + str(12//gridwidth) + ' columns'):
                            with a.center():
                                with a.a(klass='small button',  href=row['link'], style='width:100%'):
                                    a(row['title'])
                        ii = ii + 1
                        if (ii == rowcnt):
                            break
                    # a.div(klass='small-1 column')
                    # a(self.conjure_sqbutton(ii))
                    # ii = ii + 1
        return a

    def conjure_math_page(self):
        math_air = Airium()
        math_air('<!DOCTYPE html>')
        with math_air.html(klass="no-js", lang="en"):
            randolink_js = self.conjure_js_randomlink_code()
            head = conjure_head(randolink_js)
            math_air(head)
            bod_con = self.conjure_mathing_contents()
            bod = wrap_nav_on_body(bod_con)
            math_air(bod)
            bot = conjure_bottom()
            math_air(bot)
        return math_air

if __name__ == "__main__":
    genie = Genie()
    aa = genie.conjure_index_page()
    with open("../index.html", "w") as f:
        f.write(str(aa))
    bb = genie.conjure_papers_page()
    with open("../researchings.html", "w") as f:
        f.write(str(bb))
    bb = genie.conjure_posters_page()
    with open("../posters.html", "w") as f:
        f.write(str(bb))
    mathpage = genie.conjure_math_page()
    with open("../mathings.html", "w") as f:
        f.write(str(mathpage))

