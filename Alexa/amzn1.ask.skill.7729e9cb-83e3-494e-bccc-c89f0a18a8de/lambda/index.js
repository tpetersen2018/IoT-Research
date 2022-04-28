/* *
 * This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK (v2).
 * Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
 * session persistence, api calls, and more.
 * */
const Alexa = require('ask-sdk-core');




// This is the intial welcome message
//const welcomeMessage = "Welcome to the Cipher Game skill, " +
  //  "To get started, say 'Game Rules' or 'Start Game'.";
/*
// This is the message that is repeated if the response to the initial welcome message is not heard
const repeatWelcomeMessage = "You are currently using the Cipher Game skill. This skill is designed " +
    "to teach students about decryption and encryption via a cipher game. Say something like, Start Game if you're ready to play" +
    "or Game Rules, if you need more information.";

// this is the message that is repeated if Alexa does not hear/understand the reponse to the welcome message
const promptToStartMessage = "Say something like, Start Game or Game Rules, to get started.";

// this is the help message during the setup at the beginning of the game
const helpMessage = "This skill has the ability to provide beginner lessons on encryption and decryption. " +
    "To begin, say, Start Game, and we will begin playing the cipher game. " +
    "During the game you will be able to select the letters needed to decode your given message." +
    "You will select the letter you believe corresponds to the encrypted letter and I will let you know if it is correct or not. " +
    "If you are stuck at any point you can either ask for a hint by stating, Alexa give me a hint, or by hitting the hint button." +
    "You will be given 3 hints throughout the game. " +
    "If you are still confused, a more_options button will be available to provide more help. ";
*/
// these are messages when a request was invalid
//const noGameMessage = "Sorry, I didn't hear the request. Would you like to start the game?";
//const noGameRepeatMessage = "Would you like me to Start Game or hear the Game Rules?";

// these are messages when a guess is made for a game, but no game is in progress
const noGameMessage = "Sorry, no game is currently in-progress. If you would like to begin the game " +
    "cipher game, just say, 'Start Game.'";
const noGameReminderMessage = "Are you interested in playing the cipher game? If so, " +
    "just say, 'Start Game' and I will give you the encrypted message.";

// this is the message after the level is taught
const repromptLevelMessage = "Would you like to play again? If so, " +
    "please say something like, Play Game Again.";

// This is the goodbye message when the user has asked to quit the game
const goodbyeMessage = "Ok, see you next time!";

// Tis is the unhandled message when the skill is invoked, but unclear of 
const unhandledMessage = "I'm sorry, I didn't understand your request. Would you like me to " +
   "Start the game? If so, please say something like, Start Game, to get started.";













const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest';
    },
    handle(handlerInput) {
        //const speakOutput = 'Welcome, you can say Hello or Help. Which would you like to try?';
        // This is the intial welcome message
        const welcomeMessage = "Welcome to the Cipher Game skill, to get started, say 'Game Rules' or 'Start Game'.";
        // This is the message that is repeated if the response to the initial welcome message is not heard
        const repeatWelcomeMessage = "You are currently using the Cipher Game skill. This skill is designed to teach students about decryption and encryption via a cipher game. "+
        "Say something like, Start Game if you're ready to play or Game Rules, if you need more information.";

        return handlerInput.responseBuilder
            .speak(welcomeMessage)
            .reprompt(repeatWelcomeMessage)
            .getResponse();
    }
};

const StartGameIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'StartGameIntentHandler';
    },
    handle(handlerInput) {
        const StartGameMessage = "This is the cipher game. I will provide you, the  user "+
        "with encrypted phrases. It is your duty to decrypt the message and uncover its secret meaning. "+
        "Please start the game by selecting an available level. There are 3 available levels. To select a level, say " +
        "'Start Beginner'.";
       // const session  = this.event.session.attributes;

        return handlerInput.responseBuilder
            .speak(StartGameMessage)
            .reprompt(StartGameMessage)
            .getResponse();
    }
};

const GameRulesIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'GameRulesIntentHandler';
    },
    handle(handlerInput) {
        const GameRulesMessage = "Players will guess the letters of an encrypted phrase " +
	"in order to uncover a secret message. Students will use the decryption " +
	"algorithm for Ceasar ciphers in order to uncover the message and build upon their cryptographic skills. "+
	"There are hints available for each level of the game that will help you if you are struggling to decipher the message."+
	"Would you like to review the rules or begin? Just say, " +
	    "'GameRules', or 'StartGame' to continue.";

	const repromptGameRulesMessage = "Would you like to review the rules or begin? Just say, " +
	    "'GameRules', or 'StartGame' to continue.";

        return handlerInput.responseBuilder
            .speak(GameRulesMessage)
            .reprompt(repromptGameRulesMessage)
            .getResponse();
    }
};

const BeginnerIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'BeginnerIntentHandler';
    },
    handle(handlerInput) {
        const encryptedphrase = "khoor";
      
        var beginnerphrase = "Your encrypted message is ";
        var spelling;
    
        for(var i = 0; i < encryptedphrase.length; i++){
           spelling = encryptedphrase[i] + "  ,";
           beginnerphrase += spelling;
        }
        beginnerphrase += " . Please decipher this message by giving me each letter of the decrypted message. Just say 'I have a letter' to begin guessing the phrase." +
        " If you'd like a hint, just say 'Hint Please'.";
        
        const endphrase = beginnerphrase;
    

        return handlerInput.responseBuilder
            .speak(endphrase)
            .reprompt(beginnerphrase)
            .getResponse();
    }
};

const GetLetterIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'GetLetterIntentHandler';
    },
    handle(handlerInput) {
        const slots = handlerInput.requestEnvelope.request.intent.slots;
        const myletter = slots['spokenletter'].value;
        const getletter = "Your letter is ${myletter}" +
        ". If you'd like to guess again then just say 'I have a letter'.";
        
        
        

        return handlerInput.responseBuilder
            .speak(getletter)
            .reprompt(getletter)
            .withSimpleCard('I have a letter', getletter)
            .getResponse();
    }
};
// this.attributes['EncryptedPassphrase'] = encryptedphrase;
        //this.attributes['GuessCorrect'] = 0;
        //this.attributes['DecryptedPassPhrase'] = "";

const CheckLetterIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'CheckLetterIntentHandler';
    },
    handle(handlerInput) {
        const getletter = "Please state your letter";

        return handlerInput.responseBuilder
            .speak(getletter)
            .reprompt(getletter)
            .withSimpleCard(getletter)
            .getResponse();
    }
};


const LevelTwoIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LevelTwoIntentHandler';
    },
    handle(handlerInput) {
        const GameRulesMessage = "This level is in development. Please use level one for testing.";



        return handlerInput.responseBuilder
            .speak(GameRulesMessage)
           // .reprompt(repromptGameRulesMessage)
            .getResponse();
    }
};
const LevelThreeIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LevelThreeIntentHandler';
    },
    handle(handlerInput) {
         const GameRulesMessage = "This level is in development. Please use level one for testing.";

        return handlerInput.responseBuilder
            .speak(GameRulesMessage)
           // .reprompt(repromptGameRulesMessage)
            .getResponse();
    }
};
const HintOneIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HintOneIntentHandler';
    },
    handle(handlerInput) {
        const speakOutput = "Remember, a Ceaser ciphers shifts a letter three spaces to the right in order to find its encrypted counterpart." +
        "To go back to your level, just say 'Return to Beginner'.";

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};
const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Hello World!';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const HelpIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'You can say hello to me! How can I help?';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && (Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.CancelIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.StopIntent');
    },
    handle(handlerInput) {
        const speakOutput = 'Goodbye!';

        return handlerInput.responseBuilder
            .speak(goodbyeMessage)
            .getResponse();
    }
};
/* *
 * FallbackIntent triggers when a customer says something that doesn’t map to any intents in your skill
 * It must also be defined in the language model (if the locale supports it)
 * This handler can be safely added but will be ingnored in locales that do not support it yet 
 * */
const FallbackIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.FallbackIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Sorry, I don\'t know about that. Please try again.';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};
/* *
 * SessionEndedRequest notifies that a session was ended. This handler will be triggered when a currently open 
 * session is closed for one of the following reasons: 1) The user says "exit" or "quit". 2) The user does not 
 * respond or says something that does not match an intent defined in your voice model. 3) An error occurs 
 * */
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        console.log(`~~~~ Session ended: ${JSON.stringify(handlerInput.requestEnvelope)}`);
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse(); // notice we send an empty response
    }
};
/* *
 * The intent reflector is used for interaction model testing and debugging.
 * It will simply repeat the intent the user said. You can create custom handlers for your intents 
 * by defining them above, then also adding them to the request handler chain below 
 * */
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speakOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};
/**
 * Generic error handling to capture any syntax or routing errors. If you receive an error
 * stating the request handler chain is not found, you have not implemented a handler for
 * the intent being invoked or included it in the skill builder below 
 * */
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        const speakOutput = 'Sorry, I had trouble doing what you asked. Please try again.';
        console.log(`~~~~ Error handled: ${JSON.stringify(error)}`);

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

/**
 * This handler acts as the entry point for your skill, routing all request and response
 * payloads to the handlers above. Make sure any new handlers or interceptors you've
 * defined are included below. The order matters - they're processed top to bottom 
 * */
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        StartGameIntentHandler,
        GameRulesIntentHandler,
        BeginnerIntentHandler,
        CheckLetterIntentHandler,
        GetLetterIntentHandler,
        LevelTwoIntentHandler,
        LevelThreeIntentHandler,
        HintOneIntentHandler,
        HelloWorldIntentHandler,
        HelpIntentHandler,
        CancelAndStopIntentHandler,
        FallbackIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler)
    .addErrorHandlers(
        ErrorHandler)
    .withCustomUserAgent('sample/hello-world/v1.2')
    .lambda();