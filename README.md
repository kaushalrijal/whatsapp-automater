# WhatSpam - WhatsApp Automation Tool

## Overview
WhatSpam is a Python application developed using PyQt6 that allows users to automate sending WhatsApp messages to multiple contacts. It utilizes the PyQt6 library for the graphical user interface, along with pandas, pywhatkit, win32clipboard, and webbrowser to facilitate the automation process.

## Requirements
Make sure you have the following dependencies installed before using WhatSpam:
- PyQt6
- pandas
- pywhatkit
- win32clipboard
- webbrowser

## How to Use WhatsApp Automater

### Prerequisites
Before starting, ensure that you have logged into WhatsApp Web in your default web browser.

### Usage Steps

1. **Create a CSV File:**
   - Create a CSV file with the first element of the first column named "numbers."
   - Insert all your contacts below the first row in the first column.

2. **Import CSV File:**
   - Open WhatSpam.
   - Click on the "Import" button to load your CSV file.

3. **Import Image (Optional):**
   - If you want to send an image along with your messages, import the image using the "Import Image" button.

4. **Subject Field (Optional):**
   - The Subject field is for developer purposes and keeping logs. You can leave it empty if you don't want to fill it.

5. **Type Your Message:**
   - Type your message in the Messages field.

6. **Fill Either Image or Message Fields:**
   - You can fill only one of the two fields: Image and Message. However, both fields cannot be empty.

7. **Send Messages:**
   - Click on the "Send" button to start the automation process.

8. **Error Handling:**
   - If you encounter any errors, feel free to contact the developer via their website: [https://kaushalrijal.com.np](https://kaushalrijal.com.np).

## Note
This application is developed for educational and personal use. Ensure that you comply with WhatsApp's terms of service while using automation tools. The developer is not responsible for any misuse of this application.
