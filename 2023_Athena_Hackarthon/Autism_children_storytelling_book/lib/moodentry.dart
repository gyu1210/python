import 'dart:io';

import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:flutter_tts/flutter_tts_web.dart';

final FlutterTts flutterTts = FlutterTts();

class MoodEntry extends StatefulWidget {
  const MoodEntry({super.key});

  @override
  State<MoodEntry> createState() => _MoodEntryState();
}

class _MoodEntryState extends State<MoodEntry> {
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
    _speak('How are you feeling today?');
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
                          'How are you feeling today?',
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
