# TODO Нeайдите количество книг, которое можно разместить на дискете
let_line = 25
line_page = 50
page_book = 100
memory = 1.44 * 1024 * 1024
book_weight = 4 * let_line * line_page * page_book

print("Количество книг, помещающихся на дискету:", int(memory // book_weight))
