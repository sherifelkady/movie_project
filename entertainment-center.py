import media
from fresh_tomatoes import open_movies_page

# Creat Movies objects

# alpha 2018 Movie
alpha = media.Movie(
    "Alpha 2018",
    "http://www.impawards.com/2018/posters/alpha_ver4.jpg",
    "https://www.youtube.com/watch?v=uIxnTi4GmCo"
    )

# Troy Movie
troy = media.Movie(
    "Troy",
    "https://images-na.ssl-images-amazon.com/images/I/51URq2GUSaL.jpg",
    "https://www.youtube.com/watch?v=znTLzRJimeY"
    )

# Twilight Movie
twilight = media.Movie(
    "Twilight",
    "http://www.impawards.com/2008/posters/twilight.jpg",
    "https://www.youtube.com/watch?v=uxjNDE2fMjI"
    )

# Upgrade Movie
upgrade = media.Movie(
    "Upgrade",
    "https://www.cimaflix.net/uploads/cover/pwMWXna9vP5cS0U.jpg",
    "https://www.youtube.com/watch?v=1hTLGlgZ4Z8"
    )

# Jungle Book Movie
jungle_book = media.Movie(
    "The Jungle Book",
    "http://www.impawards.com/2016/posters/jungle_book.jpg",
    "https://www.youtube.com/watch?v=HcgJRQWxKnw"
    )

# War Craft
war_craft = media.Movie(
    "War Craft",
    "https://pbs.twimg.com/media/CeUzhTwWEAApXE5.jpg",
    "https://www.youtube.com/watch?v=2Rxoz13Bthc"
    )

# Movies List
movies = [alpha, troy, twilight, upgrade, jungle_book, war_craft]

# Open Movies Function Calll From Fresh_tomatoes
open_movies_page(movies)
