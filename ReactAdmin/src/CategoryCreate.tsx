import * as React from "react";
import {
  Create,
  SimpleForm,
  TextInput,
  DateInput,
  required,
  NumberField,
  NumberInput,
  SelectInput,
  BooleanField,
} from "react-admin";

export const CategoryCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="name" multiline={true} label="name" fullWidth />
    </SimpleForm>
  </Create>
);
