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
            "Front": "Noun + (이)라 해도 과언이 아니다",
            "Back": "It is not an exaggeration to say that... (emphasis)\n<ul><li>탄지로가 용감하다고 해도 과언이 아니다.</li><li>It's not an exaggeration to say that Tanjiro is brave.</li></ul>"
        },
        {
            "Front": "Noun + 에 대해 깊이 이해하다",
            "Back": "To deeply understand... (understanding)\n<ul><li>탄지로는 혈귀에 대해 깊이 이해하려고 노력했다.</li><li>Tanjiro made an effort to deeply understand demons.</li></ul>"
        },
        {
            "Front": "Verb stem + (으)ㄹ 필요가 있다",
            "Back": "There is a need to... (necessity)\n<ul><li>우리는 상황을 신속하게 평가할 필요가 있다.</li><li>We need to assess the situation quickly.</li></ul>"
        }
    ]
}


```

#### Vocabulary Example Output

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "혈귀",
            "Back": "Demon\n<ul><li>혈귀는 인간의 피를 마시고 생존한다.</li><li>Demons survive by drinking human blood.</li></ul>"
        },
        {
            "Front": "귀살대",
            "Back": "Demon Slayer Corps\n<ul><li>귀살대는 혈귀를 사냥하는 조직이다.</li><li>The Demon Slayer Corps is an organization that hunts demons.</li></ul>"
        },
        {
            "Front": "니치린 검",
            "Back": "Nichirin Blade\n<ul><li>니치린 검은 혈귀를 무찌르기 위한 특별한 검이다.</li><li>The Nichirin Blade is a special sword for defeating demons.</li></ul>"
        },
        {
            "Front": "통제된 혈귀",
            "Back": "Controlled demon\n<ul><li>통제된 혈귀는 인간에게 해를 끼치지 않는다.</li><li>A controlled demon does not harm humans.</li></ul>"
        },
        {
            "Front": "호흡 기술",
            "Back": "Breathing Technique\n<ul><li>호흡 기술은 혈귀사냥꾼들이 사용하는 강력한 능력이다.</li><li>Breathing Technique is a powerful ability used by demon slayers.</li></ul>"
        },
        {
            "Front": "가문",
            "Back": "Family clan\n<ul><li>그는 오래된 가문에서 왔다.</li><li>He comes from an old family clan.</li></ul>"
        },
        {
            "Front": "보호자",
            "Back": "Protector\n<ul><li>탄지로는 네즈코의 보호자다.</li><li>Tanjiro is Nezuko's protector.</li></ul>"
        },
        {
            "Front": "인간과 혈귀의 혼혈",
            "Back": "Human-demon hybrid\n<ul><li>인간과 혈귀의 혼혈은 매우 드문 현상이다.</li><li>A human-demon hybrid is a very rare phenomenon.</li></ul>"
        },
        {
            "Front": "불멸",
            "Back": "Immortality\n<ul><li>혈귀는 불멸에 가까운 생명력을 가지고 있다.</li><li>Demons have a life force close to immortality.</li></ul>"
        },
        {
            "Front": "일식",
            "Back": "Solar eclipse\n<ul><li>일식 동안 혈귀들은 더 강해진다.</li><li>During a solar eclipse, demons become stronger.</li></ul>"
        }
    ]
}
```