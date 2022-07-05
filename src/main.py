
if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    print('width: ' + str(screen_width) + ', height: ' + str(screen_height))