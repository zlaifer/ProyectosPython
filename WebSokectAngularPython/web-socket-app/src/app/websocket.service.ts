// src/app/websocket.service.ts
import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject} from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;

  constructor() {
    this.socket$ = webSocket('ws://localhost:8080');
  }

  sendMessage(msg: any) {
    this.socket$.next(msg);
  }

  getMessages() {
    return this.socket$.asObservable();
  }
}
