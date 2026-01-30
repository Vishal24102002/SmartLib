import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:smartlib/home_pages/user%20home.dart';
import 'package:smartlib/pages/Book_detail.dart';
import 'package:smartlib/pages/login.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.tealAccent),
      ),
      initialRoute: '/login',
      routes: {
        '/home': (context) => Student_home(title: "Smart Lib"),
        '/login': (context) => LoginPage(),
        '/books_details': (context) => BookDetail(),
        // '':(context) => (),
      },
    );
  }
}
