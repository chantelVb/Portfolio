// Player one
var pickRandomNumber1 = Math.floor(Math.random()*6)+1;

var randomDiceImage = "dice" + pickRandomNumber1 + ".png";

var imageSource = "https://github.com/chantelVb/Portfolio/blob/main/My-Dice-Game/Images/" + randomDiceImage;

var image1 = document.querySelectorAll("img")[0];

image1.setAttribute("src", imageSource);

// Player 2

var pickRandomNumber2 = Math.floor(Math.random()*6)+1;

var randomDiceImage = "dice" + pickRandomNumber2 + ".png";

var imageSource = "https://github.com/chantelVb/Portfolio/blob/main/My-Dice-Game/Images/" + randomDiceImage;

var image2 = document.querySelectorAll("img")[1];

image2.setAttribute("src", imageSource);

// win or draw message

if (pickRandomNumber1 > pickRandomNumber2){
    document.querySelector("h1").innerHTML = "🏆 You Win Player 1";
}if (pickRandomNumber1 < pickRandomNumber2){
    document.querySelector("h1").innerHTML = "You Win Player 2 🏆";
}else if(pickRandomNumber1===pickRandomNumber2){
    document.querySelector("h1").innerHTML = "Its a Draw 🎲"
}
