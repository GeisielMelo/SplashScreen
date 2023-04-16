
# Circular Splash Screen

This Circular Splash Screen is designed to check the existence of certain files and create them if they don't exist to ensure proper system functionality. During the verification process, a circular animation will spin on the screen to indicate that the system is being checked and to keep users informed of the verification progress. If the files exist, the animation will disappear quickly, indicating that the system is ready to use.

## Screenshot
Here's a screenshot of the application in action:

![App Screenshot](https://github.com/GeisielMelo/SplashScreen/blob/main/Screenshot.png?raw=true)




# Instalation

You will need to install PySide6.
```
pip install PySide6
```

Once you have installed PySide6, you can use the following steps to use this Splash Screen in your own project:
```
  1º Create a new folder.
  2º Copy "splash_screen.ui", "ui_splash_screen.py", "widgets folder".
  3ª Paste all archives into your new folder.
  4º Open "Class Code.txt", copy all and paste into your main folder project.
  5º On "class MainWindow(QMainWindow)", update "self.ui = YOUR_MAIN_WINDOW()"
```

## Running the program
Once you have installed PySide6 and followed the installation steps, you can run the Splash Screen by adding the following code to your main program:
```python
if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec())
```

# Folders
> **Circular Bar Progress**: Clean application with no changes.

> **Complete Project Example**: A simple implementation example.



## Author
- This project was created by [@GeisielMelo](https://github.com/GeisielMelo).


- Special thanks to [Wanderson](https://www.youtube.com/@WandersonItsMe), whose YouTube channel inspired this project.


## License

[MIT](https://choosealicense.com/licenses/mit/)

> This interface is free for any use.

> **Warning**: This project was created using PySide6 and Python 3.11.2, using previous versions can cause compatibility problems.
