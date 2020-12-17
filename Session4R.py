"""
    Synchronization
"""

import time
import threading

# create a Lock Object
lock = threading.Lock()

class MovieTicket:

    def __init__(self, name, time, row, seat_num):
        self.name = name
        self.time = time
        self.row = row
        self.seat_num = seat_num
        self.is_booked = False

    def book_movie_ticket(self):
        if self.is_booked:
            print(".........")
        else:
            self.is_booked = True
            print("~~~~~~~~~~~~~~")
            print("Ticket Details")
            print("{} | {}".format(self.name, self.time))
            print("{} | {}".format(self.row, self.seat_num))
            print("~~~~~~~~~~~~~~")

    def pay(self, email):

        self.email = email

        if self.is_booked:
            print("Sorry {}, Ticket {} | {} is UNAVAILABLE".format(self.email, self.row, self.seat_num))
        else:
            print("{}, Please Pay for Your Movie Ticket {} | {}".format(self.email, self.row, self.seat_num))
            time.sleep(5) # sleep is for transaction taking 5 seconds :)
            print("Thank You {}. We have booked your Ticket {} | {} and sent the email".format(self.email, self.row, self.seat_num))

    def __str__(self):
        return "{} | {} | {} | {}".format(self.name, self.time, self.row, self.seat_num)


class BookMovieTicketTask(threading.Thread):

    def select_seat(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        self.ticket.pay(email=self.email)
        self.ticket.book_movie_ticket()
        lock.release()

def main():

    """
    ticket1 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=1)
    ticket2 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=2)
    ticket3 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=3)
    ticket4 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=4)
    ticket5 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=5)
    ticket6 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=6)
    ticket7 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=7)
    ticket8 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=8)
    ticket9 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=9)
    ticket10 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=10)
    """

    row_a = []
    for i in range(1, 11):
        row_a.append(MovieTicket(name="Avengers", time="20:00", row="A", seat_num=i))


    for ticket in row_a:
        print(ticket)


    task1 = BookMovieTicketTask()
    task2 = BookMovieTicketTask()

    task1.select_seat(ticket=row_a[5], email="john@example.com")
    task2.select_seat(ticket=row_a[5], email="fionna@example.com")

    task1.start()
    task2.start()

if __name__ == '__main__':
    main()