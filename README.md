# ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS
The "Issue-Resolving Chatbot for Booking and Reserving Hotel Rooms" project is focused on developing a cutting-edge chatbot system designed to enhance the hotel booking and reservation process while effectively addressing customer issues.

![image](https://github.com/czh001118/ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS/assets/64961112/e37b1e3b-5e3e-4ba2-a80c-9a55e5f971b3)

## Chatbot Deployment with Flask and JavaScript
This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/CHONG-Zhi-Hao/ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS.git
$ cd chatbot
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

![image](https://github.com/czh001118/ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS/assets/64961112/440f9fcb-9103-4044-b1a0-b13b14eb2c17)

![image](https://github.com/czh001118/ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS/assets/64961112/67532120-dce0-49ff-8d32-1d681cb73bb6)

## Usability Testing

![image](https://github.com/czh001118/ISSUE-RESOLVING-CHATBOT-FOR-BOOKING-AND-RESERVING-HOTEL-ROOMS/assets/64961112/59d4a32b-e75f-434e-ab2a-2c8d5cc29ff4)
