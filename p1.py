import re

my_str = """A video blog or video log, sometimes shortened to vlog[1] (/vlɒɡ/), is a form of blog for which the medium is video,[2] and is a form of web television. Vlog entries often combine embedded video (or a video link) with supporting text, images, and other metadata. Entries can be recorded in one take or cut into multiple parts. Vlog category is popular on the video-sharing platform YouTube."

In recent years Vlogging has evolved into a giant community on social media where people can release any information that they want. Vlogs are a unique way for people to help people in so many aspects of their lives. Written Blogs can't provide a visual design in the ways Vlogs can deliver deeper context through imagery.[3]

Video logs (vlogs) also often take advantage of web syndication to allow for the distribution of video over the Internet using either the RSS or Atom syndication formats, for automatic aggregation and playback on mobile devices and personal computers see video podcast
"""
patt = re.compile(r"^video")

matches = patt.finditer(my_str)
for match in matches:
    print(match)