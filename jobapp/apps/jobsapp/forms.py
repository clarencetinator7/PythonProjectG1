from django import forms
from django.utils import timezone
from .models import Job
from datetime import datetime
from ckeditor.widgets import CKEditorWidget

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ["job_title", "description", "type", "skills", "min_salary", "max_salary", "status", "date_posted", "city", "country"]
        
    job_title = forms.CharField(
        label="Job Title",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "Marketing Specialist",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )
    
    description = forms.CharField(
        label="Job Description",
        widget=CKEditorWidget(attrs={
            "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
            "placeholder": "Enter job description...",
            "autocomplete": "off",
            "required": "true",
        }),
    )
    
    type = forms.TypedChoiceField(
        label="Job Type",
        choices=Job.TYPE_CHOICES,
        coerce=lambda x: x,
        empty_value=None,
        widget=forms.Select(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "autocomplete": "off",
            }
        )
    )
    
    skills = forms.CharField(
        label="Skills",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "Strategic Thinking, Adaptability, Data Analysis",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )

    min_salary = forms.IntegerField(
        label="Minimum Salary",
        widget=forms.NumberInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "10000",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )
    
    max_salary = forms.IntegerField(
        label="Maximum Salary",
        widget=forms.NumberInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "20000",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )
    
    status = forms.TypedChoiceField(
        label="Job Status",
        choices=Job.STATUS_CHOICES,
        coerce=lambda x: x,
        empty_value=None,
        widget=forms.Select(
            attrs={
                "class": "block border rounded-md p-2 border-gray-400 outline-none w-full",
                "autocomplete": "off",
            }
        )
    )
    
    date_posted = forms.DateTimeField(
        label="Date Posted",
        widget=forms.DateTimeInput(
            attrs={
                "autocomplete": "off",
                # "required": "true",
            }
        ),
    )
    
    city = forms.CharField(
        label="City",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "Quezon City",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )
    
    country = forms.CharField(
        label="Country",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "block border w-full rounded-md p-2 border-gray-400 outline-none",
                "placeholder": "Philippines",
                "autocomplete": "off",
                "required": "true",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the default value for date_created
        self.fields['date_posted'].initial = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def clean(self):
        cleaned_data = super().clean()
        min_salary = cleaned_data.get("min_salary")
        max_salary = cleaned_data.get("max_salary")
        date_posted = cleaned_data.get("date_posted")
        
        if min_salary > max_salary:
            raise forms.ValidationError("Minimum salary cannot be greater than maximum salary.")
        
        if date_posted > datetime.now(timezone.utc):
            raise forms.ValidationError("Date posted cannot be greater than today.")
        
        return cleaned_data
    
    def save(self, commit=True):
        job = super().save(commit=False)
        job.save()
        return job
    
        