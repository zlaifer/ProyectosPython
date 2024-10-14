import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from "@angular/common";
import { WebSocketService } from './websocket.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  message: string = '';
  messages: string[] = [];

  constructor(private wsService: WebSocketService) {
    this.wsService.getMessages().subscribe((msg) => {
      this.messages.push(msg);
    });
  }

  sendMessage() {
    this.wsService.sendMessage(this.message);
    this.message = '';
  }
}