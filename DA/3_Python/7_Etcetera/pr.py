import pyttsx3;
import cowsay;

engine = pyttsx3.init();
this = input("enter: ");
cowsay.cow(this);
engine.say(this);
engine.runAndWait();