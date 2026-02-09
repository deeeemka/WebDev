if (year == 2015) {
  alert( "That's correct!" );
  alert( "You're so smart!" );
}

let year = prompt('In which year was the ECMAScript-2015 specification published?', '');

if (year < 2015) {
  alert( 'Too early...' );
} else if (year > 2015) {
  alert( 'Too late' );
} else {
  alert( 'Exactly!' );
}

let accessAllowed;
let age = prompt('How old are you?', '');

if (age > 18) {
  accessAllowed = true;
} else {
  accessAllowed = false;
}

alert(accessAllowed);

let accessAllowed2 = (age > 18) ? true : false;

let age3 = prompt('age?', 18);

let message = (age3 < 3) ? 'Hi, baby!' :
  (age3 < 18) ? 'Hello!' :
  (age3 < 100) ? 'Greetings!' :
  'What an unusual age!';

alert( message );