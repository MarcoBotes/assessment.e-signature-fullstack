import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ToastMessage } from '../models/toast.models';

@Injectable({
  providedIn: 'root'
})
export class ToastService {
  private toastSubject = new Subject<ToastMessage>();
  toast$ = this.toastSubject.asObservable();

  show(message: ToastMessage) {
    this.toastSubject.next(message);
  }
}
