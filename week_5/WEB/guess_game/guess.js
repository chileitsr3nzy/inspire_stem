const randomNumber =Math.floor(math.random()*100) +1;
console.log(randomNumber)
let attempt = 0;

function checkGuess(){
    const guess = parseInt(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess)|| guess < 1 || guess > 100){
        setmessage("please enter a valid number between 1 and 100")
        return;

    }
    if(guess === randomNumber){
        setmessage("congratulations!Guessed correctly")
        document.getElementById("guessfield").disabled = true;
    
    }else if (guess< randomNumber){
        setmessage("too low try again")
    }else{
        setmessage("too high ,try again")
    }
}
function setmessage(message){
    document.getElementById("message").textContent= message
}

