from django import forms


class ReturnApplicationFeedbackForm(forms.Form):
    """email = forms.EmailField(widget=forms.EmailInput)
    subject = forms.CharField(widget=forms.TextInput)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self, email):
        send_email_task.delay(
            email,
            self.cleaned_data["subject"],
            self.cleaned_data["message"],
        )"""

