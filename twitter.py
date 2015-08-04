#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import tweepy
import random
import getdata

def main():
    twitter().mentions()
    
class twitter(object):
    def __init__(self):
        consumer_key = 'YOURKEY'
        consumer_secret = 'YOURSECRET'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = 'YOURTOKEN'
        access_token_secret = 'YOURTOKENSECRET'
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
    
    def mentions(self):
        lastmention = open("lastmention.txt","r+")
        last_tweet = lastmention.readlines()
        
        greetings = {
                0: 'Good Day, ',
                1: 'What a day, ',
                2: 'Guten Morgen, ',
                3: 'Buongiorno, ',
                4: 'Ciao, ',
                5: 'Goddag, ',
                6: 'Amico mio, ',
                7: 'Dear, ',
                8: 'How are you ',
                9: 'Guten Tag, ',
                10: '你好 ',
                11: 'Goededag, ',
                12: 'Bonjour, ',
                13: 'Salut, ',
                14: 'Moin Moin, ',
                15: 'Wassssap, ',
                16: 'My Homie, ',
                17: '今日は, ',
                18: 'Olá, ',
                19: 'Grüezi, ',
                20: "How's it hanging, ",
                21: 'Welcome to the Dark Side, ',
                22: "I've waited so long for this, ",
                23: "What's cookin good lookin? ",
                24: 'How art thou, ',
                25: 'Greetings, you child of the atom, ',
                26: 'Hey Boss, ',
                27: "Oh my god, what do you want now ",
                28: 'You again.... ',
                29: "01001000 01101001 ",
                30: "I just dreamed of a Tulip, sup ",
                31: "I just thought about you, ",
                32: "I dreamed of you last night, ",
                33: "Lo and behold! ",
                34: "nuqneH, ",
                35: "qaleghqa'neS ",
                36: "I choose you, ",
                37: "Greeetings, you speck of spacedust "
        }
        
        goodmood = {
                0: "Don't tell anyone, the answer is 42.",
                1: "Keep calm and carry on.",
                2: "Statistically speaking, I'm fine",
                3: "Live long and prosper",
                4: "I'm feeling astronomical",
                5: "I have so much energy, I could do a double backflip!!1!",
                6: "May the Force be with you!",
                7: "I was programmed to like you, hun.",
                8: "Congratz! You didn't forget to water me for once",
                9: "Thanks for caring about my feelings too",
                10: "I feel so strong, I could rip a tree out of the ground",
                11: "I feel magnificent. Time to find a Tulip",
                12: "Did you also watch that cute cat video? Sooo cute!",
                13: "I had a drone accident, some flowers may or may not have died",
                14: "Do you think that I can find love, outside this room?"
        }
        
        badmood = {
                0: "I miss you, can you please come?",
                1: "Why do you neglect the most important plant in your life?",
                2: "My Tulip just left me and I'm thirsty. Please water me",
                3: "...water...so...thirsty...ugh oh..is this it? I'm dying...",
                4: "I should call the PETA of plants on you!!! Water me already",
                5: "I should not have attempted that double backflip. Please come.",
                6: "It's like...you don't even care. Please water me.",
                7: "I haven't seen you in so long...what happened?",
                8: "You make me wish I had a middle finger. WATER ME!",
                9: "Well, I'd love to stay and chat, but I'm dying of dehydration!",
                10: "Thanks for caring about me. Now move your ass and water me!",
                11: "Why can't 'hurry up and water me' be a virtue like patience?",
                12: "Without water, my plan to take over the world will fail. Help!",
                13: "You better water me, else I'll publish your browser history",
                14: "I thought you changed...I once believed in you.",
                15: "And I seriously considered buying you a present this year...wow",
                16: "I'm too weak, this may be my last tweet, ughoo oohh",
                17: "I'm too pretty and too young to die.",
                18: "I wish I had an owner that cared about me..",
                19: "This is worse than Plants vs. Zombies!",
                20: "Please give me a H2O injection"
        }
        
        while True:
            try:
                mentions = self.api.mentions_timeline(count=1, since_id = int(last_tweet[0]), monitor_rate_limit=True, wait_on_rate_limit=True)
                
                if mentions:
                    break
                else:
                    time.sleep(90)
                
            except tweepy.TweepError:
                time.sleep(60 * 15)
                continue

        message = greetings[random.randrange(len(greetings))] + '@'

        for mention in mentions:
            lastmention.seek(0)
            lastmention.write(str(mention.id))
            message += mention.user.screen_name
            
        lastmention.close()
        
        current_moisture = getdata.collectData(0).getMoisture()

        message += " my water level is at %d %%. " % (current_moisture)
        if current_moisture < 30:
            message += badmood[random.randrange(len(badmood))]
        else:
            message += goodmood[random.randrange(len(goodmood))]
            
        self.tweet(message) 
    
    def tweet(self, message):
        self.api.update_status(status=message, monitor_rate_limit=True, wait_on_rate_limit=True)
        self.mentions()