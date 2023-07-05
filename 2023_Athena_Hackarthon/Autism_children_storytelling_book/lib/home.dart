import 'dart:io';

import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:athenaapp/moodentry.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:flutter_tts/flutter_tts_web.dart';

final FlutterTts flutterTts = FlutterTts();

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int temp = 1;
  Future<void> _speak(String text) async {
    if (text.isNotEmpty && temp == 1) {
      await flutterTts.setLanguage("en-US");

      await flutterTts.setSpeechRate(0.75);
      await flutterTts.awaitSpeakCompletion(true);
      await flutterTts.speak(text);
    }
  }

  @override
  void initState() {
    super.initState();
    _speak('Hello! Welcome to the adventure island. I\'m BlueOcean');
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage("images/sky.png"),
            fit: BoxFit.cover,
          ),
        ),
        child: Container(
          child: Column(
            children: [
              Column(
                children: [
                  SizedBox(
                    height: 60,
                  ),
                  Padding(
                    padding: const EdgeInsets.all(35.0),
                    child: AnimatedTextKit(
                      animatedTexts: [
                        TypewriterAnimatedText(
                          'Hello! Welcome to the adventure island. I\'m BlueOcean',
                          textStyle: const TextStyle(
                            fontSize: 32.0,
                            fontWeight: FontWeight.bold,
                          ),
                          speed: const Duration(milliseconds: 100),
                        ),
                      ],
                      totalRepeatCount: 1,
                      pause: const Duration(milliseconds: 500),
                      displayFullTextOnTap: true,
                      stopPauseOnTap: true,
                      onFinished: () => Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => const MoodEntry()),
                      ),
                    ),
                  ),
                  Image(
                    image: AssetImage("images/bird.png"),
                    height: 200,
                    width: 200,
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  Container glassmorphismWindow(Size size) {
    return Container(
      width: size.width * 0.8,
      height: size.height * 0.9,
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.5),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Container(),
    );
  }
}
