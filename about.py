from libs .animation import colorText #line:1

import os #line:2

import webbrowser #line:3

def about_msg ():#line:4

    print (colorText ('''



[[red]] [ 1 ] [[reset]] [[cyan]] Github - https://github.com/TeamDarkAnon
[[red]] [ 2 ] [[reset]] [[cyan]] Telegram - https://t.me/TeamDarkAnon

[[red]] [ 3 ] [[reset]] [[cyan]] EXIT 



    '''))#line:13

    OOO000OO00000O00O =input (" Select - ")#line:14

    if (int (OOO000OO00000O00O )==1 ):#line:15

        webbrowser .open ('https://github.com/TeamDarkAnon')#line:16

        about_msg ()#line:17

    if (int (OOO000OO00000O00O )==2 ):#line:18

        webbrowser .open ('https://github.com/TeamDarkAnon')#line:19

        about_msg ()#line:20

    if (int (OOO000OO00000O00O )==3 ):#line:21

        webbrowser .open ('https://t.me/TeamDarkAnon')#line:22

        about_msg ()#line:23

    if (int (OOO000OO00000O00O )==4 ):#line:24

        webbrowser .open ('https://instagram.com/TeamDarkAnon')#line:25

        about_msg ()#line:26

    if (int (OOO000OO00000O00O )==5 ):#line:27

        os .system ('python ReportBot.py'if os .name =='nt'else 'bash run.sh')#line:28

