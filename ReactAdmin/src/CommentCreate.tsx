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

export const CommentCreate = () => (
  <Create>
    <SimpleForm>
      <NumberInput source="author" multiline={true} label="author" fullWidth />
      <TextInput source="comment" multiline={true} label="comment" fullWidth />
      <NumberInput source="post" multiline={true} label="post" fullWidth />
    </SimpleForm>
  </Create>
);
