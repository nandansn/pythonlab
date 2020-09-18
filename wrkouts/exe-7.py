f_person = input("name:")

quote = '''{0} once said:, \n "A person who never made a
mistake never tried anything new."'''

print(quote.format(f_person))

f_person = "\t" + f_person + "\t"

print(f_person)

print(f_person.lstrip())

print(f_person.rstrip())

print(f_person.strip())