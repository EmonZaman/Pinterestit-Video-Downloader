# Pinterestit-Video-Downloader



The Pinterestit Video,image, gif fetcher API is a Flask-based web service that provides an efficient way to fetch video,image, gif link from Pinterestit post. It provides an API endpoint that can be used to retrieve content link.


## Getting Started


#### Prerequisites

- Python 3.8 or higher

#### Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/EmonZaman/Pinterestit-Video-Downloader.git
   ```

2. **Install Dependencies**:
    Navigate to the project directory and install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the Application

Run the application with the following command:

```bash
python main.py
```

The Flask server will start at http://127.0.0.1:5000/.


#### Using the API
##### Endpoint: Get Video Informations

- URL: /api/download
- Method: GET
- URL Params:
    - Required: url=[string] (The Pinterestit Post URL)

#### Testing the Endpoint
##### Via Web Browser

To test the endpoint via a web browser, simply navigate to the following URL (replace <Pinterestit_Post_Url> with the actual Pinterestit Post URL):

```bash
http://127.0.0.1:5000/api/download?url=<Pinterestit_Post_Url>
```

For example:

```bash
http://127.0.0.1:5000/api/download?url=https://www.pinterest.com/pin/16747829859043821/feedback/?invite_code=0884011542c3400daab5816c7feb5f4a&sender_id=607423205900074074
```

##### Via cURL

You can also use cURL in your command line:

```bash
curl "http://127.0.0.1:5000/api/video?url=https://www.pinterest.com/pin/16747829859043821/feedback/?invite_code=0884011542c3400daab5816c7feb5f4a&sender_id=607423205900074074"
```

##### Via Postman

1. Open Postman: Launch the Postman application on your computer.

2. Create a New Request:
    - Click on the `New` button or `+` tab to start a new request. Set the request method to GET by selecting it from the dropdown menu next to the URL input field.

3. Enter the URL:
    - In the `URL` input field, enter: http://127.0.0.1:5000/api/download

4. Add Query Parameters:
    - Below the `URL` input field, locate the section for entering query parameters.
    - In the `Key` field, enter `url`.
    - In the `Value` field, enter the Instragram video URL. For example: http://127.0.0.1:5000/api/video?url=https://www.pinterest.com/pin/16747829859043821/feedback/?invite_code=0884011542c3400daab5816c7feb5f4a&sender_id=607423205900074074

5. Send the Request:
    - Click the `Send` button to execute the request.

6. View the Response:
    - The response will be displayed in the lower section of the Postman interface.
    - If successful, you should see a JSON response with the video title and download links.

Here's an illustration of what your Postman setup might look like:

- Method: GET
- URL: http://127.0.0.1:5000/api/download
- Query Params:
    - Key: `url`
    - Value: http://127.0.0.1:5000/api/download?url=https://www.pinterest.com/pin/16747829859043821/feedback/?invite_code=0884011542c3400daab5816c7feb5f4a&sender_id=607423205900074074

##### Sample Response For Video:

The API responds with a JSON object containing the type and download link of the video:

```bash
[
    {
  "link": "https://v1.pinimg.com/videos/mc/expMp4/2c/20/bd/2c20bd0f3853e131777a63c6c9e52ac6_t1.mp4",
  "success": true,
  "type": "video"
    }

]
```
##### Sample Response For Image:

The API responds with a JSON object containing the type and download link of the image:

```bash
[
   {
  "link": "https://i.pinimg.com/originals/9a/3c/a6/9a3ca6e5ab73279a931024ae8cd7c8a7.jpg",
  "success": true,
  "type": "image"
   }


]
```
##### Sample Response For gif:

The API responds with a JSON object containing the type and download link of the gif:

```bash
[
    {
  "link": "https://i.pinimg.com/originals/e5/94/34/e59434c84ca59869537899717a159cac.gif",
  "success": true,
  "type": "image"
    }


]
```

##### Sample Response For Inavild Post:



```bash
[
    
]
```

If an invalid URL is given, the API responds with:

```bash
[
    {
  "link": "",
  "success": false,
  "type": ""
    }

]
```

If unable to fetch video information, the API responds with:

```bash
[
   {
  "link": "",
  "success": false,
  "type": ""
}

]
```

