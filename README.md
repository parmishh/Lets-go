# Travel Itinerary

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)     
**Video-Demo:**




https://github.com/user-attachments/assets/f0daa8bc-1836-46a3-8f2d-492dcf432c60





## Problem statement
Need to develop a web application that generates personalized travel itineraries based on user preferences such as Location, budget, interests, and trip duration. Functionally, an ideal solution should offer a user-friendly interface for inputting preferences and deliver detailed, dynamic itineraries tailored to individual users.

## Solution
Simple website where user can enter his/her preferences like Start/End location, Trip duration, Maximum Budget and Theme/Interests. We use Google Palm API to generate a travel itinerary personalized according to user preferences. Aditionally we have weather, Map info and User can Download the entire itinerary options. I have kept the iterface simple and user friendly, the interface is made using Html and CSS.
## Features

- Allows User to choose preferences like: Start/End location, Trip duration, Maximum Budget and Theme/Interests.
- Weather information for the locations for the entire duration of the trip
- Download option, to download entire itinerary
- Map information for the trip.(Currently hard coded due to unavaliable API keys)


## Working
The entered details/preferences are provided to Google's Palm model using API, which then generates Travel itinerary according to the preferences. I used Visual Crossing Weather API for providing weather conditions during the travel duration. And google iframe tag to embeed google map on the website, apart from that the download feature is implemented using html2pdf.js.

## How to Setup this Project

1. Clone the repository:

   ```shell
   https://github.com/parmishh/Lets-go
   cd Lets-go
2. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```
3. Write API keys: In a `.env` file.
```shell
WEATHER_API_KEY='Your Visual Crossing Weather API Key'
PALM_API_KEY='Your Google Palm API Key'
```
and save it in the root directory of the project.

Run the following command to start the application:
```shell
python wsgi.py
```



## Outputs
<table align="center">
<tr>
    <td align="center">&nbsp;<img src="https://private-user-images.githubusercontent.com/91942072/362272043-5bf6148c-9d91-4961-8c33-f645a377f419.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ4NDcwNzcsIm5iZiI6MTcyNDg0Njc3NywicGF0aCI6Ii85MTk0MjA3Mi8zNjIyNzIwNDMtNWJmNjE0OGMtOWQ5MS00OTYxLThjMzMtZjY0NWEzNzdmNDE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI4VDEyMDYxN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNmNWE1YjY0OWFkMDVhYzA1NDFmMTNjZmQ2MTgyZTdiNjQzNWNlNDlkNzVmMzA1NzVkYTYwOTc0Zjg0ZTZiZGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.fcxe17WK8l2iATEU2vmMk8xrwdxVTzICmjAOt4Oqhoo" alt="parmishh" /></td>
 <td align="center">&nbsp;<img src="https://private-user-images.githubusercontent.com/91942072/362272049-309072f6-f7c3-4be9-a2b9-771613712ea6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ4NDcwNzcsIm5iZiI6MTcyNDg0Njc3NywicGF0aCI6Ii85MTk0MjA3Mi8zNjIyNzIwNDktMzA5MDcyZjYtZjdjMy00YmU5LWEyYjktNzcxNjEzNzEyZWE2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI4VDEyMDYxN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQxMmFmYTQ0M2I0Mzk0MWE3NjczNDEwYjI3Njk0ZmY4ODE5MzljN2UyNWRlZGNlZGRmZjNlOWZkOTExMmI1YzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.jsrsjzabX2CBKRHpyOvOthIjw3s3ohz4eE2TO2I18gA"  alt="parmishh" /></td>
</tr>
</table>
<table align="center">
<tr>
    <td align="center">&nbsp;<img  src="https://private-user-images.githubusercontent.com/91942072/362272046-88ba2860-8cab-477e-b37c-b4fc54d2f289.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ4NDcwNzcsIm5iZiI6MTcyNDg0Njc3NywicGF0aCI6Ii85MTk0MjA3Mi8zNjIyNzIwNDYtODhiYTI4NjAtOGNhYi00NzdlLWIzN2MtYjRmYzU0ZDJmMjg5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI4VDEyMDYxN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQzODAwMWNiYjg1Yjk3ZWRhZWEwN2IyYjA5YmQxNDEzYTY3YTdiNjUwZTUwNGQxYzNiNTQxZmZiN2E0MzU3MDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Tf4qplp8_KEDssBbzMz34STyFryVhEm-n6wai-Yh-RI" alt="parmishh" /></td>
 <td align="center">&nbsp;<img  src="https://private-user-images.githubusercontent.com/91942072/362272027-b0bde594-0c1f-474b-b7a6-f559899efa00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ4NDcwNzcsIm5iZiI6MTcyNDg0Njc3NywicGF0aCI6Ii85MTk0MjA3Mi8zNjIyNzIwMjctYjBiZGU1OTQtMGMxZi00NzRiLWI3YTYtZjU1OTg5OWVmYTAwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI4VDEyMDYxN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM4MDFiYzFmNTlmYjEwYTA1ZjcxMzI0YjE3MGM2NTFhYTFkNGE1MGRkODg3MTE0YzE3MmM2YmE3YzkxNjBlODUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.vKQb0M3-4yRSud1V_M_TjDAeWKJOPqaclLYvBuPpHho"  alt="parmishh" /></td>
</tr>
</table>

