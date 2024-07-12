# yoga-practice-generator

A Python console app where users can search for Yoga poses and create their own stored yoga practices.  
API used: https://yoga-api-nzy4.onrender.com/v1

## Project description

This app was developed to enable users to access the data from the Yoga API in order to create a file storing the poses that they wanted to use for their Yoga practice.  
The app is suitable for anyone who practises Yoga, but in particular for Yoga teachers who are planning Yoga lessons, or for students to create suitable practices for them to work on.  
It is a console app where users are required to register or login to use the app.  
Users can find yoga poses using three different methods and add them to a text file for future use.  
Users can **find poses by category** e.g. standing poses.  
Users can **find poses by searching for the name or part of the name**.  
Users can select the **surprise me option** and choose how many poses they want and the app randomly selects the poses for them.  
Users can go back or quit the program at any time.  
User data is stored in a csv file.

## How to install and run the project

The project was made using Python version 3.12.1 so this is the version that is recommended for running the app.  
This version can be downloaded [here](https://www.python.org/downloads/release/python-3121/).
Clone the git repo to your local machine.  
Open the project folder from your preferred IDE (I used VS Code or Pycharm).  
Install the requests library by typing the following command into your terminal: `pip install requests`.  
Open main.py and run it.

## How to use the project

1. From the main menu, select 1 to login, or 2 to register. 
    You can login with the following credentials: 
    username: ejourzac
    password: 1!!Eee
    
![Welcome](/images/1.Welcome.png) 

2. If you select 2 to register, you will see a screen like this to enter your credentials in.

![Register](/images/2.register.png) 

3. The login screen looks like this.

![Login](/images/3.login.png) 

4. Once you are logged in you will see the main menu.

![Main menu](/images/4.main_menu.png) 

5. Choosing to find poses by category will take you to this screen.

![Poses by category](/images/5.yoga_categories.png) 

6. Then select a category to view the poses and make a selection.

![Select a pose](/images/6.select_pose.png) 

7. Confirm your selection to add the pose to your text file.

![Confirm selection](/images/7.confirm_selection.png) 

8. This will be confirmed on screen.

![File updated](/images/8.file_updated.png) 

9. Alternatively you can search for a particular pose by typing the name or part of the name.

![Search by name](/images/1.Welcome.png) 

10. Or you can select the surprise me option, and choose how many poses you want to add to your file.

![Surprise me](/images/10.surprise_me.png) 

11. Exit back to the main menu to quit the program.

![Exit](/images/11.quit.png) 

12. User data is stored in a csv file.

![CSV](/images/12.csv.png) 

## Future improvements

I would like to develop the app further so that users can choose their preferences for what pose information is saved to the text file for example Sanskrit name or English name.  
I would also like to format the text file so that there is a maximum number of characters on each line.  
I would like the user to be able to access their saved files from inside the app.  
The user should be able to delete saved files or decide to make a new Yoga practice.  
At the moment any poses selected, are added to their existing practice file.

## Credits

Many thanks to Code First Girls for providing instruction, teaching and support to me while working through this project.
* [Instagram](https://www.instagram.com/codefirstgirls/)
* [LinkedIn](https://www.linkedin.com/company/code-first-girls/)

## License

GNU General Public License v3.0
