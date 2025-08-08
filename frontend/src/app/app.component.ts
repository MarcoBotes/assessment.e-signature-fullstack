import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Subscription, timer } from 'rxjs';

import { HttpClient, HttpClientModule } from '@angular/common/http';

import { ToastMessage } from './models/toast.models';
import { ToastService } from './services/toast.service';

@Component({
  selector: 'app-root',
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit, OnDestroy {
  // Went a little overboard and added a toast
  toast?: ToastMessage;
  subscriptions: Record<string, Subscription> = {};

  constructor(private http: HttpClient, private toastService: ToastService) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const file = input.files[0];
      console.debug('Selected file:', file.name, file.size, file.type);

      const formData = new FormData();
      formData.append('file', file);

      this.http.post('http://127.0.0.1:5000/upload', formData)
        .subscribe({
          next: (response) => this.showSuccessToast(response),
          error: (response) => this.showFailureToast(response.error),
        });
    }

    // Clear input so (change) event can be triggered if you re-upload the same file
    if (input) {
      input.value = '';
    }
  }

  showSuccessToast(response: any) {
    console.debug({
      callback: "showSuccessToast",
      response,
    })
    this.toastService.show({
      title: "Success",
      content: response.message,
      type: 'success',
    });
  }

  showFailureToast(response: any) {
    console.debug({
      callback: "showFailureToast",
      response,
    })
    this.toastService.show({
      title: "Failure",
      content: response.error,
      type: 'error',
    });
  }

  ngOnInit() {
    this.subscriptions['toast'] = this.toastService.toast$.subscribe(toast => {
      console.debug({
        newToast: toast,
      });
      this.toast = toast;
      timer(toast.duration || 3000).subscribe(() => this.toast = undefined);
    });
  }

  ngOnDestroy() {
    Object.values(this.subscriptions).forEach(sub => sub.unsubscribe());
    this.subscriptions = {};
  }
 
}