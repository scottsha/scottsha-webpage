sq_icon, link, description
sq_icons/yellow_sq.svg

from airium import Airium

a = Airium()

a('<!DOCTYPE html>')
with a.html(klass='no-js', lang='en'):
    with a.head():
        a.meta(charset='utf-8')
        a.meta(content='width=device-width, initial-scale=1.0', name='viewport')
        a.title(_t='Shane Scott')
        a.link(href='css/foundation.css', rel='stylesheet')
        a.script(src='js/vendor/modernizr.js')
        a.link(href='tenta.ico', rel='shortcut icon')
    with a.body():
        a('<!-- Navigation Bar! -->')
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
                        a.a(href='researchings.html', _t='Research')
                with a.ul(klass='left'):
                    with a.li():
                        a.a(href='teachings.html', _t='Teaching')
                with a.ul(klass='left'):
                    with a.li():
                        a.a(href='mathings.html', _t='Math!')
        a('<!-- Navigation Bar! -->')
        with a.p():
            with a.div(klass='row'):
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='yellow_gui.html'):
                            a.img(src='sq_icons/yellow_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                a.a(klass='medium button', href='yellow_gui.html', style='width:100%', _t='The Yellow Pince-nez')
                a.div(klass='small-2 columns')
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='teach/3012spring18/math3012.html'):
                            a.img(src='sq_icons/icosahedral_group_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='teach/3012spring18/math3012.html', style='width:100%'):
                                    a('Lectures in Combinatorics')
            a('<!--ROW thesis-->')
            with a.div(klass='row'):
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='thesisdefense.svg'):
                            a.img(src='sq_icons/thesis_definse_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='pres_n_post/thesisdefense.svg', style='width:100%'):
                                    a('Defense: Models for Surface and Free Group Symmetries')
                a.div(klass='small-2 columns')
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='thesis.pdf'):
                            a.img(src='sq_icons/thesis_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='thesis.pdf', style='width:100%'):
                                    a('Combinatorial Models for Surface and Free Group Symmetries')
            a('<!--ROW -->')
            a('<!--ROW -->')
            with a.div(klass='row'):
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='llnltp.pdf'):
                            a.img(src='sq_icons/vein_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='pres_n_post/llnltp.pdf', style='width:100%'):
                                    a('Poster: Tubular Parametrization for Vascular Geometry')
                a.div(klass='small-2 columns')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='llnltp.pdf'):
                            a.img(src='sq_icons/tube_sq.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='pres_n_post/llnl_nsf.pdf', style='width:100%'):
                                    a('Paper: Tubular Parametrization for Vascular Geometry')
            a('<!--ROW END-->')
            a('<!--ROW -->')
            with a.div(klass='row'):
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='modulispace.svg'):
                            a.img(src='sq_icons/moduli_space.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                a.a(klass='medium button', href='pres_n_post/modulispace.svg', style='width:100%', _t='Lecture: Moduli Space')
                a.div(klass='small-2 columns')
                a('<!-- -->')
                with a.div(klass='small-5 columns'):
                    with a.div(klass='content'):
                        with a.a(href='inkscape_and_sozi_sozi/inkscape_and_sozi.svg'):
                            a.img(src='sq_icons/sozi_icon.svg', style='width:100%')
                        with a.p():
                            with a.center():
                                with a.a(klass='medium button', href='inkscape_and_sozi_sozi/inkscape_and_sozi.svg', style='width:100%'):
                                    a('Lecture: Sozi for Topology Students')
            a('<!--ROW End-->')
        a('<!--End of all rows-->')
    a.script(src='js/vendor/jquery.js')
    a.script(src='js/foundation.min.js')
    with a.script():
        a('$(document).foundation();')