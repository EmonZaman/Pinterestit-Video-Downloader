import requests
import re
import json

class Pinterest:
    def __init__(self, url):
        self.url = url


    def get_page_content(self):
        """Retrieve the content of the Pinterest page."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            # Handle request-related exceptions
            print(f"Error fetching page content: {e}")
            return None

    def is_a_video(self):
        """Check if the Pinterest pin contains a video."""
        page_content = self.get_page_content()
        return "video-snippet" in page_content if page_content else False
    def get_media_link(self):
        print(f"get_media_link: started url: {self.url}")
        """Retrieve the media link (image or video) from the Pinterest pin."""
        try:
            page_content = self.get_page_content()
            if not page_content:
                # If page content is not retrieved, consider it as an invalid URL or failed request
                print(f"get_media_link: invalid or failed request")
                return {"type": "", "link": "", "success": False}

            if self.is_a_video():
                print(f"get_media_link: valid video")
                match = re.findall(r'<script data-test-id="video-snippet".+?</script>', page_content)
                if match:
                    j = json.loads(match[0].replace('<script data-test-id="video-snippet" type="application/ld+json">', "").replace("</script>", ""))
                    content_url = j.get("contentUrl", "")
                    return {"type": "video", "link": content_url, "success": bool(content_url)}
            else:
                print(f"get_media_link: not a video")
                match = re.findall(r'<script data-test-id="leaf-snippet".+?</script>', page_content)
                if match:
                    j = json.loads(match[0].replace('<script data-test-id="leaf-snippet" type="application/ld+json">', "").replace("</script>", ""))
                    image_link = j.get("image", "")
                    return {"type": "image", "link": image_link, "success": bool(image_link)}
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            print(f"Error decoding JSON: {e}")

        print(f"get_media_link: invalid or failed request")
        return {"type": "", "link": "", "success": False}

