export interface ToastMessage {
    title: string;
    content: string;
    type?: 'success' | 'error' | 'info' | 'warning';
    duration?: number;
}