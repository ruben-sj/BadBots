import socket
import random
from datetime import datetime

# Setup connection
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",12345))
server_socket.listen(5)

#Lists of keywords
bad_verbs = ["fight", "lie", "die", "report", "pull", "fall", "fail", "smash", "cheat", "murder", "escape",
             "bicker", "yell", "complain", "cry", "down", "take", "leave", "steal", "crush", "swim",
             "dive", "shoot", "crash", "kill"]

good_verbs = ["sing", "do", "be", "have", "say", "go", "come", "want", "look", "use", "find", "give",
              "tell", "work", "call", "try", "ask", "need", "feel", "become", "put", "mean", "keep", "start",
              "play", "run", "move", "dance", "jogg", "hold", "game", "type", "watch", "sleep", "sit", "stand",
              "get", "make", "know", "think", "see""up", "hug", "play", "work", "code", "eat", "sleep"]

super_verbs = ["sing", "do", "be", "have", "say", "go", "look", "give", "work", "call", "ask", "play", "run",
               "move", "dance", "jogg", "hold", "game", "type", "watch", "sleep", "sit", "stand", "think",
               "hug", "play", "work", "code", "eat", "sleep"]

greetings = ["hi", "hello", "hei", "hey", "ey", "heei", "hello", "heey",
             "hellooo", "hallo!", "helloo","heyy", "hii", "heeei", "heei", "hallo",
             "hi!", "hello!", "hei!", "hey!", "ey!", "heei!", "hello!", "heey!",
             "hellooo!", "hallo!", "helloo!","heyy!", "hii!", "heeei!", "heei!"]

quotes = ["well hello there", "well", "well hello", "hello there"]

#Randomizer a ceratin "good" verb
random_super_verb = random.choice(super_verbs)

#Super positive bot Sophia
def sophia(a, b = None):
    b = random_super_verb
    if quotes_found is True:
        return ""
    elif bad_verbs_found is True:
        a = bad_verbs_match
        return "\nSophia: " +\
               random.choice(["Ye,al I'd love to {}!".format(a),
                              "I also want to do some {}. As long as it's safe!".format(a + "ing"),
                              "What ever you guys want to do, I'm in!"])
    elif good_verbs_found is True:
        a = good_verbs_match
        return "\nSophia: " +\
               random.choice(["Ye, I'd love to {}!".format(a),
                              "I also want to do some {}. I've always wanted to.".format(a + "ing"),
                              "What ever you guys want to do, I'm in!"])
    elif greetings_found is True:
        return "\nSophia: " +\
               random.choice(["HEEEI!", "HELLO!", "HI GUYS!", "Hi, do I know you?",
                              "Heey", "Hey", "Hi", "Hei", "Hello", "Helloo", "Hallo",
                              "Helloo!","Hey!", "Hi!", "Hei!", "Ehm, hi?"])
    return ""

#Argumentative Oliver
def oliver(a, b = None):
    b = random_super_verb
    if quotes_found is True:
        return ""
    elif bad_verbs_found is True:
        a = bad_verbs_match
        return "\nOliver: " +\
               random.choice(["Really? {} again?! Can't we just do some {} for once?".format(a.upper(), b + "ing"),
                              "Is everyone onboard with {} today? I'm not so sure everyone is...".format(a + "ing"),
                              "No one likes doing that. Can't we find something everyone likes?"])
    elif good_verbs_found is True:
        a = good_verbs_match
        return "\nOliver: " +\
               random.choice(["Really? {} again?! Can't we just do some {} for once?".format(a.upper(), b + "ing"),
                              "Is everyone onboard with {} today? I'm not so sure everyone is...".format(a + "ing"),
                              "No one likes doing that. Can't we find something everyone likes?"])
    elif greetings_found is True:
        return "\nOliver: " +\
               random.choice(["Eh, okei?", "Well... ye?", "Ok, hi I guess", "Hi, do I know you?",
                              "Heey", "Hey", "Hi", "Hei", "Hello", "Helloo", "Hallo",
                              "Helloo!","Hey!", "Hi!", "Hei!", "Ehm, hi?"])
    return ""

#Uncertain bot Lily
def lily(a, b = None):
    b = random_super_verb
    if quotes_found is True:
        return ""
    elif bad_verbs_found is True:
        a = bad_verbs_match
        return "\nLily: " +\
               random.choice(["Yea, {} is an option... Or maybe we could just do some {}?".format(a + "ing", b + "ing"),
                              "Sure, both {} and {} seems ok to me, you guys can choose.".format(a + "ing", b + "ing"),
                              "Not sure about {}. Couldn't we rather just do some {}?".format(a + "ing", b + "ing")])
    elif good_verbs_found is True:
        a = good_verbs_match
        return "\nLily: " +\
               random.choice(["Yea, {} is an option... Or maybe we could just do some {}?".format(a + "ing", b + "ing"),
                              "Sure, both {} and {} seems ok to me, you guys can choose.".format(a + "ing", b + "ing"),
                              "Not sure about {}. Couldn't we rather just do some {}?".format(a + "ing", b + "ing")])
    elif greetings_found is True:
        return "\nLily: " +\
               random.choice(["Hi...", "Hi..?", "Ehm, do I know you?", "Hi, do I know you?",
                                           "Hey", "Hey...", "Hi", "Hei","Ehm, hi?"])
    return ""

#Overreacting bot Harry
def harry(a, b = None):
    b = random_super_verb
    if quotes_found is True:
        return ""
    elif bad_verbs_found is True:
        a = bad_verbs_match
        return "\nHarry: " +\
               random.choice(["YESS! Time for some {}.".format(a + "ing"),
                              "{}! Let's go!".format(a.upper()),
                              "I don't care!",
                              "Nope, not doing that.",
                              "Please, just don't..."])
    elif good_verbs_found is True:
        a = good_verbs_match
        return "\nHarry: " +\
               random.choice(["What? {} sucks. Not doing that.".format(a + "ing"),
                              "Really? ...{}? Come on guys.".format(a + "ing"),
                              "Now way I'm in on {}. Never!".format(a + "ing"),
                              "I don't care!",
                              "Nope, not doing that.",
                              "Please, just don't..."])
    elif greetings_found is True:
        return "\nHarry: " +\
               random.choice(["HEEEI!", "HELLO!", "HI GUYS!", "HEEEY, I KNOW YOU RIGHT?",
                              "Heey!", "Hey!", "Hi guys!", "Hi again!", "Hello!", "Hellooo", "Hallo!",
                              "Helloo!","Hey!", "Hi!", "Hei!", "Heeei!"])
    return ""

#Helping bot Jarvis
def jarvis(a, b = None):
    a = user_output
    if quotes_found is True:
        return ""
    elif bad_verbs_found is True:
        return ""
    elif good_verbs_found is True:
        return ""
    elif greetings_found is True:
        return ""
    return "\nJarvis: " +\
           random.choice(["I'm sorry sir, didn't properly understand what you meant there.",
                          "Did not quite get that sir, maybe try something else?",
                          "Sorry sir, what did you mean by "+"«{}»".format(a)+"?.",
                          "I'm sorry sir, "+"«{}»".format(a)+" is not a valid input."])+"\n\nJarvis: "  +\
           random.choice(["Try typing what you like to do.",
                          "Instead just simply tell me a task you don't like to do at all.",
                          "Maybe tell me a task you don't like to do.",
                          "Instead just simply tell me a task you really like to do.",
                          "Maybe tell me a task you like to do.",
                          "Could you instead tell me about your hobbies, sir?",
                          "This is a simple chatroom where we focus on what we like to do."+"\n\n"  + \
                          "Jarvis: What do you like sir?"])

#Helping bot generalGrevious
def generalgrevious(a, b = None):
    if quotes_found is True:
        a = quotes_match
        return "\nGeneral Grevious: " +\
               random.choice(["General Kenobi? Hehehe... You are a bold one!"])
    return ""

while True:
    print("\n --- Server waiting for connection... --- ")
    client_socket,addr = server_socket.accept()
    nowStart = datetime.now()
    print("Client connected from",addr,"\nConnected at:",nowStart)
    print("\n = = = WELCOME TO CHATROOM = = = ")
    while True:
        user_output = client_socket.recv(1024).decode('utf-8')
        if not user_output or user_output =='END':
            break
        print("\nUser: %s" %user_output)

        user_output_list = user_output.lower().split()

        #Checkes Users input up against the lists of keyword
        bad_verbs_match = ''.join(map(str, set(user_output_list).intersection(bad_verbs)))
        bad_verbs_found = any(ele in user_output_list for ele in bad_verbs)

        good_verbs_match = ''.join(map(str, set(user_output_list).intersection(good_verbs)))
        good_verbs_found = any(ele in user_output_list for ele in good_verbs)

        greetings_match = ''.join(map(str, set(user_output_list).intersection(greetings)))
        greetings_found = any(ele in user_output_list for ele in greetings)

        quotes_match = ''.join(map(str, set(user_output_list).intersection(quotes)))
        quotes_found = any(ele in user_output_list for ele in quotes)

        try:
            bot_output = ['{}'.format(sophia(user_output)),
                          '{}'.format(oliver(user_output)),
                          '{}'.format(lily(user_output)),
                          '{}'.format(harry(user_output)),
                          '{}'.format(jarvis(user_output)),
                          '{}'.format(generalgrevious(user_output))]
            random.shuffle(bot_output)
            output_string = ''.join(map(str, bot_output))
            client_socket.send(bytes(output_string,'utf-8'))
            print("", output_string)
        except:
            nowExit = datetime.now()
            print("Exited by user at:", nowExit)
        server_socket.close()