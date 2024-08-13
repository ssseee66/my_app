import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

void main() async {
  await setupDesktop();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flet Flutter Demo',
      home: FletApp(
        pageUrl: "http://localhost:8550",
        assetsDir: 'G:\\flutter_project\\pluginsmy_app\\assets',
      ),
    );
  }
}
