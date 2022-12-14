from tkinter import *
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import credentials as cr


class Select:
    def __init__(self, root):
        self.window = root
        self.window.title("Library Management System")
        self.window.geometry("1070x720")
        self.window.config(bg="white")

        # Left Frame
        self.frame_1 = Frame(self.window, bg="yellow")
        self.frame_1.place(x=0, y=0, width=650, relheight=1)

        label1 = Label(self.frame_1, text="SQL", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(
            x=100,
            y=200)
        label2 = Label(self.frame_1, text="Library", font=("times new roman", 40, "bold"), bg="yellow",
                       fg="RoyalBlue1").place(x=180, y=200)
        label3 = Label(self.frame_1, text="Интерфейс библиотеки", font=("times new roman", 13, "bold"), bg="yellow",
                       fg="brown4").place(x=100, y=250)

        # Right Frame
        self.frame_2 = Frame(self.window, bg="gray95")
        self.frame_2.place(x=650, y=0, relwidth=1, relheight=1)

        # A frame inside the right frame
        self.frame_3 = Frame(self.frame_2, bg=cs.color_2)
        self.frame_3.place(x=0, y=300, relwidth=1, relheight=1)


        self.all_book = Button(self.frame_2, text='Показать книги', font=(cs.font_1, 16), bd=2, command=self.ShowBooks,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=20, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать Читальные залы', font=(cs.font_1, 16), bd=2, command=self.ShowRooms,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=70, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать библиотекарей', font=(cs.font_1, 16), bd=2,
                       command=self.ShowLibrarians,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=120, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать карточки бронирования', font=(cs.font_1, 16), bd=2,
                               command=self.ShowIssueCards,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=170, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать место хранения книг', font=(cs.font_1, 16), bd=2,
                       command=self.ShowBookPlaces,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=220, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать читателей', font=(cs.font_1, 16), bd=2,
                       command=self.ShowReaders,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=270, width=400, height=40)

        self.all_book = Button(self.frame_2, text='Показать карточки выдачи книг', font=(cs.font_1, 16), bd=2,
                               command=self.ShowBookingCards,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=320, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать администраторов', font=(cs.font_1, 16), bd=2,
                               command=self.ShowAdmins,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=370, width=400, height=40)
        self.all_book = Button(self.frame_2, text='Показать работников читального зала', font=(cs.font_1, 16), bd=2,
                               command=self.ShowLibrarianRooms,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=420, width=400, height=45)

        self.clear = Button(self.frame_2, text='Очистить экран', font=(cs.font_1, 16), bd=2, command=self.ClearScreen,
                            cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=210, y=670, width=200, height=40)
        self.exit = Button(self.frame_2, text='Выйти', font=(cs.font_1, 16), bd=2, command=self.Exit, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=670, width=200, height=40)
    def OnSelectedforShowBooks(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteBook,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateBookDetails, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)
    def OnSelectedforShowBookPlace(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteBookPlace,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateBookPlace, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)
    def OnSelectedforShowAdministrators(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteAdmin,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateAdmin, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)
    def OnSelectedforShowIssueCard(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteIssueCard,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateIssueCard, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)
    def OnSelectedforShowBookingCard(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteBookingCard,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateBookingCard, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)

    def OnSelectedforShowReaders(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteReader,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateReader, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)

    def OnSelectedforShowLibrarianRoom(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteLibrarianRoom,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateLibrarianRoom, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)

    def OnSelectedforShowLibrarians(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteLibrarian,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateLibrarian, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)

    def OnSelectedforShowRooms(self, a):
        self.dlt_record = Button(self.frame_2, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteRoom,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=500, width=100)
        self.update_record = Button(self.frame_2, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateRoom, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=500, width=100)

    def DeleteBook(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateBookDetails(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        author = Label(self.frame_1, text="author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.insert(0, row[1])
        self.author_entry.place(x=220, y=130, width=300)

        publication_year = Label(self.frame_1, text="publication_year", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.publication_year_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publication_year_entry.insert(0, row[2])
        self.publication_year_entry.place(x=220, y=200, width=300)

        publisher = Label(self.frame_1, text="publisher", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
        self.publisher_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publisher_entry.insert(0, row[3])
        self.publisher_entry.place(x=220, y=270, width=300)

        name = Label(self.frame_1, text="name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
        self.name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.name_entry.insert(0, row[4])
        self.name_entry.place(x=220, y=340, width=300)

        isbn = Label(self.frame_1, text="isbn", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
        self.isbn_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.isbn_entry.insert(0, row[5])
        self.isbn_entry.place(x=220, y=410, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateBook, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateBook(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update books set author=%s,publication_year=%s,publisher=%s,name=%s,isbn=%s where id=%s",
                         (
                             self.author_entry.get(),
                             self.publication_year_entry.get(),
                             self.publisher_entry.get(),
                             self.name_entry.get(),
                             self.isbn_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteRoom(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateRoom(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        Id = Label(self.frame_1, text="ID", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        name = Label(self.frame_1, text="Room Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                         y=100)
        self.name_room_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.name_room_entry.insert(0, row[1])
        self.name_room_entry.place(x=220, y=130, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateRoom, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateRoom(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update rooms set name=%s where id=%s",
                         (
                             self.name_room_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteLibrarian(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateLibrarian(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        login = Label(self.frame_1, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.login_lib_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.login_lib_entry.insert(0, row[1])
        self.login_lib_entry.place(x=220, y=130, width=300)

        password = Label(self.frame_1, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.password_lib_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.password_lib_entry.insert(0, row[2])
        self.password_lib_entry.place(x=220, y=200, width=300)


        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateLibrarian, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateLibrarian(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update librarians set login=%s,password=%s where id=%s",
                         (
                             self.login_lib_entry.get(),
                             self.password_lib_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteBookingCard(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateBookingCard(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        time = Label(self.frame_1, text="time", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                   y=100)
        self.time_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.time_book_entry.insert(0, row[1])
        self.time_book_entry.place(x=220, y=130, width=300)

        period_book = Label(self.frame_1, text="period", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=170)
        self.period_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.period_book_entry.insert(0, row[2])
        self.period_book_entry.place(x=220, y=200, width=300)

        readers_id_issue = Label(self.frame_1, text="readers_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=240)
        self.readers_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.readers_id_book_entry.insert(0, row[3])
        self.readers_id_book_entry.place(x=220, y=270, width=300)

        librarians_id_issue = Label(self.frame_1, text="librarians_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=270)
        self.librarians_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.librarians_id_book_entry.insert(0, row[3])
        self.librarians_id_book_entry.place(x=220, y=300, width=300)

        books_id_issue = Label(self.frame_1, text="books_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                                 y=310)
        self.books_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_book_entry.insert(0, row[4])
        self.books_id_book_entry.place(x=220, y=340, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateBookingCard, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateBookingCard(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update booking_cards set time=%s,period=%s,readers_id=%s,librarians_id=%s,books_id=%s where id=%s",
                         (
                             self.time_issue_entry.get(),
                             self.period_issue_entry.get(),
                             self.readers_id_issue_entry.get(),
                             self.librarians_id_book_entry.get(),
                             self.books_id_issue_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteIssueCard(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateIssueCard(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        time = Label(self.frame_1, text="time", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.time_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.time_issue_entry.insert(0, row[1])
        self.time_issue_entry.place(x=220, y=130, width=300)

        period_issue = Label(self.frame_1, text="period", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.period_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.period_issue_entry.insert(0, row[2])
        self.period_issue_entry.place(x=220, y=200, width=300)

        readers_id_issue = Label(self.frame_1, text="readers_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
        self.readers_id_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.readers_id_issue_entry.insert(0, row[3])
        self.readers_id_issue_entry.place(x=220, y=270, width=300)

        books_id_issue = Label(self.frame_1, text="books_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
        self.books_id_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_issue_entry.insert(0, row[4])
        self.books_id_issue_entry.place(x=220, y=340, width=300)


        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateIssueCard, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateIssueCard(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update issue_cards set time=%s,period=%s,readers_id=%s,books_id=%s where id=%s",
                         (
                             self.time_issue_entry.get(),
                             self.period_issue_entry.get(),
                             self.readers_id_issue_entry.get(),
                             self.books_id_issue_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteAdmin(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Administrator', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from administrators where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from administrators where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateAdmin(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        id = Label(self.frame_1, text="Admin ID", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        booking_cards_id = Label(self.frame_1, text="Booking_cards_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.booking_cards_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.booking_cards_id_entry.insert(0, row[1])
        self.booking_cards_id_entry.place(x=220, y=130, width=300)

        login = Label(self.frame_1, text="Login", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.login_adm_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.login_adm_entry.insert(0, row[2])
        self.login_adm_entry.place(x=220, y=200, width=300)

        password = Label(self.frame_1, text="Password", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=220)
        self.password_adm_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.password_adm_entry.insert(0, row[2])
        self.password_adm_entry.place(x=220, y=250, width=300)


        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateAdmin, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateAdmin(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update administrators set booking_cards_id=%s,login=%s,password=%s where id=%s",
                         (
                             self.booking_cards_id_entry.get(),
                             self.login_adm_entry.get(),
                             self.password_adm_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteBookPlace(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books_place where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from book_places where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateBookPlace(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        quantity = Label(self.frame_1, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.quantity_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.quantity_entry.insert(0, row[0])
        self.quantity_entry.place(x=220, y=130, width=300)

        shell_number = Label(self.frame_1, text="Shell Number", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.shell_number_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.shell_number_entry.insert(0, row[1])
        self.shell_number_entry.place(x=220, y=200, width=300)

        books_id = Label(self.frame_1, text="Books ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
        self.books_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_entry.insert(0, row[2])
        self.books_id_entry.place(x=220, y=270, width=300)

        rooms_id = Label(self.frame_1, text="Rooms ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
        self.rooms_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.rooms_id_entry.insert(0, row[3])
        self.rooms_id_entry.place(x=220, y=340, width=300)


        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateBookPlace, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateBookPlace(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update book_places set quantity=%s,shell_number=%s,books_id=%s,rooms_id=%s where rooms_id=%s",
                         (
                             self.quantity_entry.get(),
                             self.shell_number_entry.get(),
                             self.books_id_entry.get(),
                             self.rooms_id_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteReader(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete readers', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from readers where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from readers where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The readers record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateReader(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        Reader_id = Label(self.frame_1, text="Reader Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        name = Label(self.frame_1, text="Reader Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=130)
        self.reader_name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.reader_name_entry.insert(0, row[1])
        self.reader_name_entry.place(x=220, y=150, width=300)

        Password = Label(self.frame_1, text="Reader Password", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                          y=180)
        self.reader_password_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.reader_password_entry.insert(0, row[2])
        self.reader_password_entry.place(x=220, y=200, width=300)

        passport = Label(self.frame_1, text="Passport", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=230)
        self.Passport_reader_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.Passport_reader_entry.insert(0, row[3])
        self.Passport_reader_entry.place(x=220, y=250, width=300)

        address = Label(self.frame_1, text="address", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                                  y=280)
        self.Address_reader_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.Address_reader_entry.insert(0, row[4])
        self.Address_reader_entry.place(x=220, y=300, width=300)

        phone = Label(self.frame_1, text="phone", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                                  y=320)
        self.phone_reader_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.phone_reader_entry.insert(0, row[5])
        self.phone_reader_entry.place(x=220, y=350, width=300)


        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateReader, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateReader(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update readers set name=%s,password=%s,passport=%s,address=%s,phone=%s where id=%s",
                         (
                             self.reader_name_entry.get(),
                             self.reader_password_entry.get(),
                             self.Passport_reader_entry.get(),
                             self.Address_reader_entry.get(),
                             self.phone_reader_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteLibrarianRoom(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete librarian_room', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from librarian_rooms where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from librarian_rooms where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateLibrarianRoom(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        rooms_id = Label(self.frame_1, text="rooms_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,                                                                                                  y=100)
        self.rooms_id_lib_room_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.rooms_id_lib_room_entry.insert(0, row[1])
        self.rooms_id_lib_room_entry.place(x=220, y=130, width=300)

        librarians_id = Label(self.frame_1, text="librarians_id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=160)
        self.librarians_id_lib_room_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.librarians_id_lib_room_entry.insert(0, row[1])
        self.librarians_id_lib_room_entry.place(x=220, y=200, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateLibarianRooms, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateLibarianRooms(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update librarian_rooms set rooms_id=%s,librarians_id=%s where rooms_id=%s",
                         (
                             self.rooms_id_lib_room_entry.get(),
                             self.librarians_id_lib_room_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def ShowBooks(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.books, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('author', text='Author', anchor=W)
        self.tree.heading('publication_year', text='Publication year', anchor=W)
        self.tree.heading('publisher', text='Publisher', anchor=W)
        self.tree.heading('name', text='Book Name', anchor=W)
        self.tree.heading('isbn', text='ISBN', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from books")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def ShowRooms(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.rooms, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('name', text='Room Name', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowRooms)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from rooms")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1]))

    def ShowLibrarians(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.librarians, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('login', text='Login', anchor=W)
        self.tree.heading('password', text='Password', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowLibrarians)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from librarians")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", (rows.index(list)),
                             values=(list[0], list[1], list[2]))

    def ShowBookPlaces(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.book_places, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('quantity', text='Quantity', anchor=W)
        self.tree.heading('shell_number', text='Shell Number', anchor=W)
        self.tree.heading('books_id', text='Book ID', anchor=W)
        self.tree.heading('rooms_id', text='Room ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBookPlace)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from book_places")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3]))

    def LibrarianRooms(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.librarian_rooms, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('rooms_id', text='Room ID', anchor=W)
        self.tree.heading('librarians_id', text='Librarian ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowLibrarianRoom)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from librarian_rooms")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1]))

    def ShowReaders(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.readers, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('name', text='Reader Name', anchor=W)
        self.tree.heading('password', text='Password', anchor=W)
        self.tree.heading('passport', text='Passport', anchor=W)
        self.tree.heading('address', text='Address', anchor=W)
        self.tree.heading('phone', text='Phone', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowReaders)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from readers")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def ShowIssueCards(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.issue_cards, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('time', text='Time', anchor=W)
        self.tree.heading('period', text='Period', anchor=W)
        self.tree.heading('readers_id', text='Reader ID', anchor=W)
        self.tree.heading('books_id', text='Book ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowIssueCard)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from issue_cards")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4]))

    def ShowBookingCards(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.booking_cards, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('time', text='Time', anchor=W)
        self.tree.heading('period', text='Period', anchor=W)
        self.tree.heading('readers_id', text='Reader ID', anchor=W)
        self.tree.heading('librarians_id', text='Librarians ID', anchor=W)
        self.tree.heading('books_id', text='Book ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBookingCard)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from booking_cards")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def ShowLibrarianRooms(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.librarian_rooms, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('rooms_id', text='rooms_id', anchor=W)
        self.tree.heading('librarians_id', text='librarians_id', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowLibrarianRoom)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from librarian_rooms")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1]))

    def ShowAdmins(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.administrators, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('id', text='id', anchor=W)
        self.tree.heading('booking_cards_id', text='booking_cards_id', anchor=W)
        self.tree.heading('login', text='login', anchor=W)
        self.tree.heading('password', text='password', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowAdministrators)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from administrators")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3]))


    # Removes all widgets from the frame 1 and frame 3
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

        for widget in self.frame_3.winfo_children():
            widget.destroy()

    '''Exit window'''

    def Exit(self):
        self.window.destroy()


# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Select(root)
    root.mainloop()