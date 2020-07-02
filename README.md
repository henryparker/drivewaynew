# Driveways
Driveways


## Installation from PyPI: 
> pip install driveways-project-cis4930-v6==0.0.8
> runserver



# Resources

[Simplest Git Tutorial](https://rogerdudler.github.io/git-guide/)

[Django API List](https://github.com/wsvincent/awesome-django)

[Django Tutorials](https://github.com/wsvincent/awesome-django#educational)

## API's 



[Django Calendar](https://github.com/llazzaro/django-scheduler)

[Django Map](https://github.com/madisona/django-google-maps)

[Django Forms](https://github.com/django-crispy-forms/django-crispy-forms/)

# DRIVEWAYS

-   Enter destination and be shown available driveways to park nearby
-   User can list their available parking spaces to earn extra income
-   Driveways is meant to offer private parking.

![image-20200617143552790](assets/Design-Prototype/image-20200617143552790.png)\\

## Features / Planning

#TODO: Finish Features

-   Map Functionality: Google API's
    - Object Markers
        - Price/(day,timeframe), location, time, 
-   Search Functionality
    -   address search
    -   distance function
-   **Buyer Portal**
-   **Seller Portal**
        -   Make Listing (Update DB):
            -   Cost, Time, Address
- **Sign in Page**
    -   **Account Details**
        -   Payment
        -   Account Information
    
    

Later features:

## User Testing

> Later: Todo. 






# Grading Overview



As a team, you will complete and deliver a design prototype demonstrating the feasibility and core features of your project. The features demonstrated will encompass a **vertical slice** – i.e., an iteration of your project that has all core features integrated in at least one dimension, though it need not be polished. The prototype should not involve implementations of all aspects of every feature; instead, the design prototype is intended to provide a basis for architecture and practical testing (including usability and user experience). The goal of the design prototype deliverable is to identify exactly how the project will be structured and to provide a foundation for the second phase of the project.

# Specification:

- Interface: UI elements visible and usable. Options intuitve and consistent. Currently selected buttons, menu options, status changes and dialog elements highlighted.
- Navigation: Mechanics functional, controls tested, bugs minimal / not present, good UI. Controls show require significant time for acclimation, predicatble and easy to use.
- User Perception: Application responsive and use intuitive. User testing from non team memebers and report good experience. The prototype help users attain stated goals.
- Reponsiveness: Interactions indicated  (visually / audibly). Changes in app state must be indicated on relevant interface elements. Completion / Failure of tasks indicated.

# Build Quality:

- Robustness: Crashes should not occur regularly. No major glitches.
- Consistency: Predictable except _where explicitly by design_, same input case should yield the result. If app is erratic  compelling.
- Aesthetic Rigor: No cosmetic issues present. All assets present and functional.
- Vertical features:
    - Front End: For each major use case, at least one variant must be implement within the UI. This much connect to _persistent_ state.
    - Persistent State: For each..., must be a demonstration of use of a data store in the application. This must connect to the front-end and back end.
    - Back-End: For each..., at least one variant of data processing step must be implemented. Must connect to persistent state.



## Protoype Submissions and Packaging. 

All projects

1.  Must be buildable from command line using pip and, with permission, apt (must be preapproved)
2.  Must use the Python setup.py script mechanism for all setup other than apt package installation

Mobile App

1.  Must provide course to directly build Android APK from command line Ubuntu
2.  If backend is service, must provide mechanism to build and run service and connect to it from the app  
3.  Kivy: use "buildozer" (we will preinstall this

Web App

1.  Must provide Python-based (not npm-based) mechanism to build and run project; only snippets of JS allowed (no server-side JS or frameworks)
2.  Service must function, at a minimum, in Chrome, Firefox, and Safari

# Submissions:

- Source Code
- Build and run scripts
- Application pack (APK) if target is mobile.
