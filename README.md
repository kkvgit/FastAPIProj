Title: 
    FastAPIProject

Description: 
    This is a sample project to perform an addition on input lists of integers with FastAPI

System Requirements:
    Must have installed python 3.12 or latest version
    Must have packages FastAPI, Uvicorn if not preinstalled via pip install fastapi uvicorn

To run the server:
    open the project in any python editor let say in VS code latest
    open the terminal and navigate to app path and execute the following command
    python -m uvicorn main:app --reload
    make sure "Application startup complete" in terminal screen

To validate:
    Open browser, and type http://127.0.0.1:8000/
    you should seen "welcome"

    to validate test cases, use the swagger UI with the below one
    Open browser, and type http://127.0.0.1:8000/docs

    #1 click on POST button
    #2 click Try it out
    #3 on request body replace the json string with {"batchID":"id0101", "payload": [[1, 2], [3,4]]}
    #4 click Execute button
    #5 Make sure we get success response(200) 

    repeat these steps for other test cases by altering the json.

Finally stop the terminal

Note: 
   Read requirements.txt file for packages dependencies
