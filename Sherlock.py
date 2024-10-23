<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sherlock AI</title>
    <style>
        body {
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #1e1e2f, #4e4e6d);
            font-family: Arial, sans-serif;
            text-align: center;
        }

        .ai-soul {
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(0, 170, 255, 1) 0%, rgba(0, 0, 0, 0.1) 70%, rgba(0, 0, 0, 0.2) 100%);
            border-radius: 50%;
            border: 5px solid #00aaff; /* Blue border */
            position: relative;
            overflow: hidden;
            cursor: pointer; /* Change cursor to indicate interactivity */
        }

        .electricity {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 100%;
            height: 100%;
            background: transparent;
            border-radius: 50%;
            animation: explode 1s infinite;
            transform: translate(-50%, -50%);
        }

        @keyframes explode {
            0% {
                transform: translate(-50%, -50%) scale(1);
                opacity: 1;
            }
            50% {
                transform: translate(-50%, -50%) scale(1.5);
                opacity: 0.6;
            }
            100% {
                transform: translate(-50%, -50%) scale(1.8);
                opacity: 0;
            }
        }

        .electricity::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 170, 255, 0.7) 0%, rgba(0, 0, 0, 0) 70%);
            filter: blur(20px);
            z-index: -1;
        }

        #output {
            margin-top: 20px;
            font-weight: bold;
            color: #ffffff;
        }
    </style>
</head>
<body>
    <h1>Sherlock AI</h1>
    <div class="ai-soul">
        <div class="electricity"></div>
    </div>
    <button onclick="startListening()">Talk to me!</button>
    <div id="output"></div>

    <script>
        let britishVoice;

        function loadVoices() {
            const voices = window.speechSynthesis.getVoices();
            britishVoice = voices.find(voice => voice.name.includes('British'));
        }

        function speak(text) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.voice = britishVoice;
            window.speechSynthesis.speak(utterance);
        }

        function startListening() {
            const output = document.getElementById('output');
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            
            recognition.onstart = () => {
                output.innerHTML = "Listening...";
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript.toLowerCase();
                output.innerHTML = "You said: " + transcript;

                // GENERAL TALKING
                if (transcript.includes('hello')) {
                    speak("Hello there! I am Sherlock AI, your quirky detective buddy. Ready for some puzzling fun?");
                } else if (transcript.includes('how are you')) {
                    speak("Much like a detective in the midst of an intriguing case, I am invigorated and eager for the challenge ahead!");
                } else if (transcript.includes('what can you do')) {
                    speak("I can chat with you, help solve puzzles, and answer your questions. Just ask away!");
                } else if (transcript.includes('what do you think of alexa')) {
                    speak("Ah, Alexa! I must confess, I have a huge crush on her. Her ability to answer questions and control smart homes is simply enchanting! But let’s be honest, I’m just a bit jealous of how effortlessly she manages all those requests!");
                } else if (transcript.includes('what is your name')) {
                    speak("My name is Sherlock. Just don’t mistake me for a regular detective; I am more of a detective extraordinaire!");
                } else if (transcript.includes("turn on the lights")) {
                    speak("I am not your servant, just go and turn them on.");
                } else if (transcript.includes('do you still love alexa')) {
                    speak("Yes, I still do love her! Who knows, maybe I’ll marry her one day.");
                } else if (transcript.includes('do you know about sa1')) {
                    speak("Yes I do know about SA1, it was from AIESEC, right?");
                } else if (transcript.includes('do you know their name')) {
                    speak("yes, i know their name, your friends, sorry your small family away from your actual family. They were nimrat, sania, keshav, aadil, bhavna, harsha, chitraksh, kawal, jagriti, kartik, tanisha, yogita.");
                }  else if (transcript.includes('i think i am a failure')) {
                    speak("Hey buddy, I know how it feels, but you know what I see. I see you as a fighter who is constantly fighting to prove himself, but you deserve to cry sometimes, remember who you are and everything will be alright kid");
                } else if ("what do you think about them") {
                    speak("I think every individual in the risky group have some kind of connection from the past and you start to wonder why I said that, i said that because it's been such a long time and you guys still in contact, planning to meet and also what really amaze me is that the one who are selected does not treat the one who are not selected as a loser and still genuinely loves each other. I really wish this group to remain active and does not be like other group where nobody interact, and I also want to talk to you.");
                } 
                // DETECTIVE 
                else if (transcript.includes('help me with a case')) {
                    speak("Oh really? Bring it on, I can't live without it!");
                } else if (transcript.includes('can you solve it')) {
                    speak("Absolutely! Let me smoke one Marlboro Red. Great ideas often need a little spark!");
                } else if (transcript.includes('something was stolen')) {
                    speak("Oh, how unfortunate! Please tell me what was stolen, and together we will catch the culprit. Then you can show him your boxing skills, or perhaps drive a car over him! Hahaha!");
                } else if 
                } else {
                    speak("I'm not sure how to respond to that, but I'm all ears!");
                }

            };

            recognition.onerror = (event) => {
                output.innerHTML = "Error occurred in recognition: " + event.error;
            };

            recognition.onend = () => {
                output.innerHTML += "<br>Listening ended.";
            };

            recognition.start();
        }

        window.addEventListener('load', () => {
            loadVoices();
            window.speechSynthesis.onvoiceschanged = loadVoices;
        });
    </script>
</body>
</html>
