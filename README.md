
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/link858/MuggleShuffle">
  </a>

<h1 align="center">MUGGLE SHUFFLE</h1>

  <p align="center">
    A WoW Shuffle Script!
    <br />
    <a href="https://github.com/link858/MuggleShuffle/issues"><strong>Report Bug »</strong></a>
    <br />
    <br />
    <a href="https://github.com/link858/MuggleShuffle/issues"><strong>Request Feature »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/link858/MuggleShuffle)

**A neat script I wrote to help shuffle through prospecting and creating gems and maintaining a low price on the AH**
I am very new to scripting / coding in general 

**PROSPECT MODE**
* It will prospect and count the results, once there is no more saronite it goes to **Green Craft Mode**

**GREEN CRAFT MODE**
* Craft the green disenchantables till you have crafted the total amount you counted for
* Checks if inventory gets full and will enter the mailbox and send disenchantables to character specified and continue crafting
* Checks for crystallized and eternal earth and if your out it will break and continue to **Blue Craft Mode**

**BLUE CRAFT MODE**
* Does the exact same thing as **GREEN CRAFT MODE** except now it cuts all the raw blue gems it counted
* After its completed its loops it enters **Auction Mode**

**AUCTION MODE**
* Posts items specified in the TSM addon
* Constantly refreshes and checks for Undercuts
* If a specified amount of cancelled undercuts is reached in one time it will enter the MailBox Sub_Mode
* **MAILBOX MODE** Will walk to the mailbox and retrieve cancelled auctions then walk back to AH and enter Auction Mode

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python](https://python.org)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

**It requires the [Trade Skill Master(TSM)](https://www.tradeskillmaster.com/install) addon and their Desktop client so its fully functional**
***YOU MUST set up groups like normal so Auction Mode will work***

***You MUST use the TSM UI for the MailBox and Auction House***

### Prerequisites
**PYTHON**
First and foremost you obviously need Python.

Im not sure if you have to install these yourself but it uses pyautogui and PIL
* pyautogui
  ```sh
  pip install pyautogui
  ```
* Pill or Pillow
  ```sh
  pip install pillow
  ```

  
  

### Installation

1. Download the zip from github

2. Extract the files into a folder

3. Locate the MuggleMacros folder and copy it to your WoW Addons Folder

**I MADE AN ADDON FOR WORLD OF WARCRAFT TO AUTOMATICALLY CREATE THE MACROS FOR YOU**

Just put the folder ***"MuggleMacros"*** into your WoW Addons folder
Enable the Addon and INGAME type /mugglesetup to create the macros and the new chat window, /muggledel removes the macros but you need to close the chat yourself
Do not resize the new black chat window or cover it, its how the script can see things to count.(if the count is off, make sure the new chat tab is the last tab you clicked so the macro can refresh the chat)

1. **You must put the macros on your bar manually, there are ****2 pictures bar_setup 1 and 2****, you must make yours the same as shown.**
2. **You must have click to move enabled and INTERACT WITH TARGET set to 'F'**
3. **YOU MUST BE IN IRONFORGE TO USE ANY OF THE PATHING AND START THE BOT IN THE SPOT SHOWN IN** ***Starting_Spot.png***
4. **YOU MUST HAVE SOME SARONITE IN YOUR INVENTORY WHEN YOU START**

Sometime I will add the ability to change the keybinds

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

**Starting the script**

Open the command prompt in the scripts folder and use
* py MuggleShuffle.py
  ```sh
  py MuggleShuffle.py
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Create variables for all the keybinds used
- [ ] Create GUI to make configuration easier(Plus I want to see how you make one)
- [ ] Create a new mode **BUY MODE** 
- [ ] Learng and figure out how to do Pathfinding

See the [open issues](https://github.com/link858/MuggleShuffle/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please if you have anything to contribute or suggest feel free, especially if it involves any kind of pathfinding ^_^
I tried and researched about it and gave it a shot but I failed
there is a way to create a WoW addon that has 2 colored squares that you change the rgb values of with the coords and facing of the character
then you use pixel matching to read the colors and translate them as coords.
somehow then you can calculate or come up with a way to better do pathing this way.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
**DISCORD**
Wreckin#2365 - wreckinisterrible@gmail.com

Project Link: [https://github.com/link858/MuggleShuffle](https://github.com/link858/MuggleShuffle)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* Shoi


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/link858/MuggleShuffle/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/link858/MuggleShuffle/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/link858/MuggleShuffle/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/link858/MuggleShuffle/issues
[product-screenshot]: images/screenshot.png
[Python.org]: https://img.shields.io/badge/python-v3.7-blue
[Python-url]: https://python.org 
