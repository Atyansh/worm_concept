screen taylor_dance():
    add Movie(size=(1280, 720)) at center
    on "show" action Play("movie", "taylor_dance.webm", loop=True)
    on "hide" action Stop("movie")
    on "replace" action Play("movie", "taylor_dance.webm", loop=True)
    on "replaced" action Stop("movie")

screen neutral_end():
    add "neutral_ending.jpg" zoom 0.6

screen bad_end():
    add "bad_ending.jpg" zoom 0.6

screen good_end():
    add "good_ending.jpg" zoom 0.6
