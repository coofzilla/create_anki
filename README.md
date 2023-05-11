# README

## Description

This is a Python Flask application that creates Anki notes with the AnkiConnect API using a POST request. The application creates a deck with the given name and adds the notes to that deck. The deck is created if it does not already exist.

## Prerequisites

Before running the application, make sure you have:

- Anki installed on your computer
- AnkiConnect add-on installed in Anki
- Python 3.x installed on your computer
- Flask and urllib Python libraries installed

## How to run

1. Open Anki and make sure AnkiConnect add-on is installed.
2. Clone or download the repository.
3. Navigate to the directory in your terminal where the repository is located.
4. Install Flask and urllib by running the command: `pip install flask urllib`
5. Start the Flask server by running the command: `python create_anki.py`
6. The server will start running on http://127.0.0.1:3001/
7. Use a tool like Postman to send a POST request to http://127.0.0.1:3001/anki/notes with the following JSON body:

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "비위",
            "Back": "Dislike"
        },
        {
            "Front": "얼굴",
            "Back": "Face"
        },
        ...
    ]
}
```

8. The notes will be added to the "Demon Slayer" deck in Anki. If the deck does not exist, it will be created.

## API Documentation

### POST /anki/notes

This endpoint adds notes to the Anki deck.

#### Request Body

| Field | Type   | Description                                                                                                                                                         |
| ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deck  | string | **Required.** The name of the Anki deck.                                                                                                                            |
| notes | array  | **Required.** An array of notes to add to the deck. Each note is an object with "Front" and "Back" fields representing the front and back of the note respectively. |

Example:

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "비위",
            "Back": "Dislike"
        },
        {
            "Front": "얼굴",
            "Back": "Face"
        },
        ...
    ]
}
```

#### Response

| Status Code | Description                      |
| ----------- | -------------------------------- |
| 200         | Notes added successfully.        |
| 400         | Missing deck name or notes data. |

#### GPT Prompt Script

```
You are a Korean Language flash card assistant. You are to take the provided Japanese script and give me vocabulary related to it. However, the front of the card should be Korean and back should be English.

Desired output:

{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "비위",
            "Back": "Dislike"
        },
        {
            "Front": "얼굴",
            "Back": "Face"
        },
        ...
    ]
}

Script: <Japanese Script Here>
```

#### GPT Prompt Grammar

```
You are an AI Korean language creation flash card assistant. Please make me a list of useful grammar referencing the book Korean grammar in use intermediate as a guide that is related to the anime "Demon Slayer".

To be clear, the example sentences should be related to the anime Demon Slayer.


Desired output:

{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "Verb stem + (으)면 할수록",
            "Back": "The more... the more (comparison)\n<ul><li>탄지로는 훈련을 하면 할수록 강해진다.</li><li>The more Tanjiro trains, the stronger he becomes.</li></ul>"
        },
        {
            "Front": "Noun + 에 비추어 보아",
            "Back": "Considering... (judgment)\n<ul><li>그의 나이에 비추어 보아, 그는 매우 강하다.</li><li>Considering his age, he is very strong.</li></ul>"
        },
        {
            "Front": "Verb stem + (으)ㄹ 바에야",
            "Back": "It's better to... (preference)\n<ul><li>저주 받을 바에야, 그는 혈귀와 싸울 것이다.</li><li>He would rather fight with the demon than be cursed.</li></ul>"
        },
    ]
}


```
