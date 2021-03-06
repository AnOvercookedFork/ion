# Stubs for django.forms.models (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.forms.fields import ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.utils.translation import ugettext_lazy as _

ALL_FIELDS = ... # type: Any

def model_to_dict(instance, fields=None, exclude=None): ...
def fields_for_model(model, fields=None, exclude=None, widgets=None, formfield_callback=None, localized_fields=None, labels=None, help_texts=None, error_messages=None, field_classes=None): ...

class ModelFormOptions:
    model = ... # type: Any
    fields = ... # type: Any
    exclude = ... # type: Any
    widgets = ... # type: Any
    localized_fields = ... # type: Any
    labels = ... # type: Any
    help_texts = ... # type: Any
    error_messages = ... # type: Any
    field_classes = ... # type: Any
    def __init__(self, options=None): ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass):
    def __new__(mcs, name, bases, attrs): ...

class BaseModelForm(BaseForm):
    instance = ... # type: Any
    def __init__(self, data=None, files=None, auto_id='', prefix=None, initial=None, error_class=..., label_suffix=None, empty_permitted=False, instance=None): ...
    def clean(self): ...
    def validate_unique(self): ...
    save_m2m = ... # type: Any
    def save(self, commit=True): ...

class ModelForm(BaseModelForm): ...

def modelform_factory(model, form=..., fields=None, exclude=None, formfield_callback=None, widgets=None, localized_fields=None, labels=None, help_texts=None, error_messages=None, field_classes=None): ...

class BaseModelFormSet(BaseFormSet):
    model = ... # type: Any
    queryset = ... # type: Any
    initial_extra = ... # type: Any
    def __init__(self, data=None, files=None, auto_id='', prefix=None, queryset=None, **kwargs): ...
    def initial_form_count(self): ...
    def get_queryset(self): ...
    def save_new(self, form, commit=True): ...
    def save_existing(self, form, instance, commit=True): ...
    def delete_existing(self, obj, commit=True): ...
    saved_forms = ... # type: Any
    save_m2m = ... # type: Any
    def save(self, commit=True): ...
    def clean(self): ...
    def validate_unique(self): ...
    def get_unique_error_message(self, unique_check): ...
    def get_date_error_message(self, date_check): ...
    def get_form_error(self): ...
    changed_objects = ... # type: Any
    deleted_objects = ... # type: Any
    def save_existing_objects(self, commit=True): ...
    new_objects = ... # type: Any
    def save_new_objects(self, commit=True): ...
    def add_fields(self, form, index): ...

def modelformset_factory(model, form=..., formfield_callback=None, formset=..., extra=1, can_delete=False, can_order=False, max_num=None, fields=None, exclude=None, widgets=None, validate_max=False, localized_fields=None, labels=None, help_texts=None, error_messages=None, min_num=None, validate_min=False, field_classes=None): ...

class BaseInlineFormSet(BaseModelFormSet):
    instance = ... # type: Any
    save_as_new = ... # type: Any
    def __init__(self, data=None, files=None, instance=None, save_as_new=False, prefix=None, queryset=None, **kwargs): ...
    def initial_form_count(self): ...
    @classmethod
    def get_default_prefix(cls): ...
    def save_new(self, form, commit=True): ...
    def add_fields(self, form, index): ...
    def get_unique_error_message(self, unique_check): ...

def inlineformset_factory(parent_model, model, form=..., formset=..., fk_name=None, fields=None, exclude=None, extra=3, can_order=False, can_delete=True, max_num=None, formfield_callback=None, widgets=None, validate_max=False, localized_fields=None, labels=None, help_texts=None, error_messages=None, min_num=None, validate_min=False, field_classes=None): ...

class InlineForeignKeyField(Field):
    widget = ... # type: Any
    default_error_messages = ... # type: Any
    parent_instance = ... # type: Any
    pk_field = ... # type: Any
    to_field = ... # type: Any
    def __init__(self, parent_instance, *args, **kwargs): ...
    def clean(self, value): ...
    def has_changed(self, initial, data): ...

class ModelChoiceIterator:
    field = ... # type: Any
    queryset = ... # type: Any
    def __init__(self, field): ...
    def __iter__(self): ...
    def __len__(self): ...
    def choice(self, obj): ...

class ModelChoiceField(ChoiceField):
    default_error_messages = ... # type: Any
    empty_label = ... # type: Any
    queryset = ... # type: Any
    limit_choices_to = ... # type: Any
    to_field_name = ... # type: Any
    def __init__(self, queryset, empty_label='', required=True, widget=None, label=None, initial=None, help_text='', to_field_name=None, limit_choices_to=None, *args, **kwargs): ...
    def get_limit_choices_to(self): ...
    def __deepcopy__(self, memo): ...
    def label_from_instance(self, obj): ...
    choices = ... # type: Any
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def has_changed(self, initial, data): ...

class ModelMultipleChoiceField(ModelChoiceField):
    widget = ... # type: Any
    hidden_widget = ... # type: Any
    default_error_messages = ... # type: Any
    def __init__(self, queryset, required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs): ...
    def to_python(self, value): ...
    def clean(self, value): ...
    def prepare_value(self, value): ...
    def has_changed(self, initial, data): ...
