# Project Cubed
# Introduction
Project Cubed is a educational project designed with teaching people with little to no multiplayer knowledge on how to build multiplayer systems. For starting small, socket was chosen as the main
method of data communication. Using pygame and other python libraries, developing a multiplayer prototype has been made simpler. The development of the project will progress as more characters and
abilities will be added

# How it works
Upon the client starting the code, it sends a request to the server for authentication. After approval, the player is added to the player list in the server. The server then gives the approval to the client to
send data to the server. Each cycle of the server, the server will then relay that data to the other players client. This repeats several times until the server ends.
