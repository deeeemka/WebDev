import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <section (mouseover)="showSecretMessage()">
      <p>There's a secret message for you, hover to reveal 👀
      {{ message }}</p>
    </section>
  `,
})
export class App {
  message = '';

  showSecretMessage() {
    this.message = "Way to go";
  }
}
