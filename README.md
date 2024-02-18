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

#### Vocabulary Example Prompt

You are a Korean Language flash card creation assistant. Please make flash cards that utilize grammar from the book, Korean Grammar In Use Advanced. The vocabulary used should be from TOPIK 4-6. The context of the sentences should be based the animation 귀멸의 칼날.

I will provide you an example output; however, do not use these vocabulary words in your response.


Example template:

```json
{
    "deck": "*Deck Name Here*",
    "notes": [
        {
            "Front": "*___ (단어)로 채울 문장 여기에 입력*",
            "Back": "*Missing Word Here*\n<ul><li>*Cloze sentence with the missing word filled in here in Korean*</li><li>*Translation or Additional Explanation Here in English*</li></ul>"
        },
        {
            "Front": "*___ (단어)로 채울 문장 여기에 입력*",
            "Back": "*Missing Word Here*\n<ul><li>*Cloze sentence with the missing word filled in here in Korean*</li><li>*Translation or Additional Explanation Here in English*</li></ul>"
        },
        {
            "Front": "*___ (단어)로 채울 문장 여기에 입력*",
            "Back": "*Missing Word Here*\n<ul><li>*Cloze sentence with the missing word filled in here in Korean*</li><li>*Translation or Additional Explanation Here in English*</li></ul>"
        }
    ]
}

```

Example based on template:

```json
{
    "deck": "Basic Korean Vocabulary",
    "notes": [
        {
            "Front": "그녀는 커피를 마시며 책을 ___.",
            "Back": "읽다\n<ul><li>그녀는 커피를 마시며 책을 읽다.</li><li>She reads a book while drinking coffee.</li></ul>"
        },
        {
            "Front": "저는 아침에 일어나서 ___.",
            "Back": "운동하다\n<ul><li>저는 아침에 일어나서 운동하다.</li><li>I exercise after waking up in the morning.</li></ul>"
        },
        {
            "Front": "그는 친구들과 함께 영화를 ___.",
            "Back": "보다\n<ul><li>그는 친구들과 함께 영화를 보다.</li><li>He watches a movie with his friends.</li></ul>"
        }
    ]
}
```

Example output:

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "탄지로가 자신의 동생, 네즈코를 ___ 위해 끝없이 싸우는 모습을 보면서, 나는 가족에 대한 그의 애정을 느낄 수 있었다.",
            "Back": "Protect\n<ul><li>탄지로가 자신의 동생, 네즈코를 보호하기 위해 끝없이 싸우는 모습을 보면서, 나는 가족에 대한 그의 애정을 느낄 수 있었다.</li><li>Watching Tanjiro endlessly fight to protect his sister, Nezuko, I could feel his affection for his family.</li></ul>"
        },
        {
            "Front": "우리는 ___적인 훈련을 통해 능력을 향상시키는 것이 얼마나 중요한지를 깨닫게 되었다.",
            "Back": "Intensive\n<ul><li>우리는 집중적인 훈련을 통해 능력을 향상시키는 것이 얼마나 중요한지를 깨닫게 되었다.</li><li>We realized how important it is to improve our abilities through intensive training.</li></ul>"
        },
        {
            "Front": "마귀와의 ___ 도전에도 불구하고, 탄지로는 결코 포기하지 않는 모습이 인상적이었다.",
            "Back": "Countless\n<ul><li>마귀와의 무수한 도전에도 불구하고, 탄지로는 결코 포기하지 않는 모습이 인상적이었다.</li><li>Despite countless challenges with demons, Tanjiro's never-give-up attitude was impressive.</li></ul>"
        },
        {
            "Front": "탄지로가 ___적으로 마귀와 싸워야 하는 이유는, 그가 자신의 동생을 인간으로 되돌리기 위한 목표를 이루기 위해서였다.",
            "Back": "Frequently\n<ul><li>탄지로가 자주적으로 마귀와 싸워야 하는 이유는, 그가 자신의 동생을 인간으로 되돌리기 위한 목표를 이루기 위해서였다.</li><li>The reason Tanjiro had to frequently fight demons was to achieve his goal of turning his sister back into a human.</li></ul>"
        }
    ]
}
```

#### GPT Prompt Grammar

```
Please create Korean Language flashcards utilizing a random advanced grammar from the book "Korean Grammar In Use Advanced". The vocabulary used should be from TOPIK 4-6. The context of the sentences should be based on the animation "귀멸의 칼날" (Demon Slayer). Please choose a random advanced grammar and let me confirm it before making the flashcards.

Desired output:

{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "탄지로는 혈귀를 처치하는 데 능숙할 ___ 아니라, 탁월한 지도자로도 알려져 있다.",
            "Back": "Not only\n<ul><li>탄지로는 혈귀를 처치하는 데 능숙할 뿐만 아니라, 탁월한 지도자로도 알려져 있다.</li><li>Not only is Tanjiro skilled in slaying demons, but he is also known as an excellent leader.</li></ul>"
        },
        {
            "Front": "네즈코는 혈귀로서의 힘을 가지고 ___ 아니라, 그녀는 인간성을 유지하는 데 성공했다.",
            "Back": "Not only\n<ul><li>네즈코는 혈귀로서의 힘을 가지고 있을 뿐만 아니라, 그녀는 인간성을 유지하는 데 성공했다.</li><li>Not only does Nezuko possess the power of a demon, but she also managed to maintain her humanity.</li></ul>"
        },
        {
            "Front": "탄지로는 싸움에서 이길 ___ 아니라, 그는 형제의 사랑을 통해 많은 사람들의 마음을 이겼다.",
            "Back": "Not only\n<ul><li>탄지로는 싸움에서 이길 뿐만 아니라, 그는 형제의 사랑을 통해 많은 사람들의 마음을 이겼다.</li><li>Not only did Tanjiro win in battles, but he also won many people's hearts through his brotherly love.</li></ul>"
        },
        {
            "Front": "귀살대는 혈귀를 물리치는 ___ 아니라, 인간들을 보호하는 임무도 가지고 있다.",
            "Back": "Not only\n<ul><li>귀살대는 혈귀를 물리치는 뿐만 아니라, 인간들을 보호하는 임무도 가지고 있다.</li><li>Not only does the Demon Slayer Corps repel demons, but they also have the duty to protect humans.</li></ul>"
        }
    ]
}

```

#### Grammar Example Output

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "탄지로는 네즈코를 구하려면 어려움이 ___라도 결코 포기하지 않았다.",
            "Back": "Even if there were difficulties\n<ul><li>탄지로는 네즈코를 구하려면 어려움이 많을지라도 결코 포기하지 않았다.</li><li>Even if there were difficulties, Tanjiro never gave up on saving Nezuko.</li></ul>"
        },
        {
            "Front": "혈귀와의 싸움이 힘들___라도, 그는 자신의 능력을 믿고 계속 전투했다.",
            "Back": "Even if the fight with the demon was tough\n<ul><li>혈귀와의 싸움이 힘들지라도, 그는 자신의 능력을 믿고 계속 전투했다.</li><li>Even if the fight with the demon was tough, he believed in his abilities and continued the battle.</li></ul>"
        },
        {
            "Front": "탄지로가 어떤 ___라도, 그는 네즈코를 위해 어떤 것이라도 할 준비가 되어 있었다.",
            "Back": "Sacrifice\n<ul><li>탄지로가 어떤 희생이라도, 그는 네즈코를 위해 어떤 것이라도 할 준비가 되어 있었다.</li><li>Regardless of the sacrifice, Tanjiro was ready to do anything for Nezuko.</li></ul>"
        },
        {
            "Front": "혈귀가 강력___라도, 그는 결코 두려워하지 않고 맞서 싸웠다.",
            "Back": "Even if the demon was powerful\n<ul><li>혈귀가 강력할지라도, 그는 결코 두려워하지 않고 맞서 싸웠다.</li><li>Even if the demon was powerful, he fought without fear.</li></ul>"
        },
        {
            "Front": "얼마나 많은 혈귀들이 그의 길을 막___라도, 그는 자신의 목표를 향해 나아갔다.",
            "Back": "Even if many demons blocked his way\n<ul><li>얼마나 많은 혈귀들이 그의 길을 막을지라도, 그는 자신의 목표를 향해 나아갔다.</li><li>Even if many demons blocked his way, he moved towards his goal.</li></ul>"
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

#### Cloze Workaround Sample ( allows back )

```
{
    "deck": "Demon Slayer",
    "notes": [
        {
            "Front": "혈귀왕이 ___을 내렸다.",
            "Back": "Command\n<ul><li>혈귀왕이 명령을 내렸다.</li><li>The Demon King issued a command.</li></ul>"
        },
        {
            "Front": "니치린 검을 만드는 것은 귀살대의 ___이었다.",
            "Back": "Order\n<ul><li>니치린 검을 만드는 것은 귀살대의 명령이었다.</li><li>Making the Nichirin Blade was an order from the Demon Slayer Corps.</li></ul>"
        },
        {
            "Front": "그는 선배로부터 호흡 기술을 배우는 ___을 받았다.",
            "Back": "Instruction\n<ul><li>그는 선배로부터 호흡 기술을 배우는 명령을 받았다.</li><li>He received an instruction to learn the Breathing Technique from his senior.</li></ul>"
        },
        {
            "Front": "그의 ___은 가문의 모든 구성원에게 적용된다.",
            "Back": "Decree\n<ul><li>그의 명령은 가문의 모든 구성원에게 적용된다.</li><li>His decree applies to all members of the family clan.</li></ul>"
        },
        {
            "Front": "보호자로서, 그는 네즈코에게 안전을 유지하는 ___을 내렸다.",
            "Back": "Directive\n<ul><li>보호자로서, 그는 네즈코에게 안전을 유지하는 명령을 내렸다.</li><li>As a protector, he issued a directive to Nezuko to maintain safety.</li></ul>"
        }
    ]
}
```

#### Vocab Breakdown

```
front: 사명
back: Mission (calling)

"사명" is composed of two Korean words: "사" which means "task" or "duty" and "명" which means "command" or "order." Therefore, "사명" can be understood as a duty or task given or commanded, often implying a greater or noble purpose that one is dedicated to. It could be used in the context of a personal calling or a professional mission.
```

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
