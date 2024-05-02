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

export const PostCreate = () => (
  <Create>
    <SimpleForm>
      <NumberInput source="author" validate={[required()]} fullWidth />

      <TextInput source="title" multiline={true} label="title" fullWidth />
      <TextInput source="content" multiline={true} label="content" fullWidth />
      <SelectInput
        source="is_draft"
        choices={[
          { id: "True", name: "True" },
          { id: "False", name: "False" },
        ]}
      />
      <NumberInput source="categories" validate={[required()]} fullWidth />
    </SimpleForm>
  </Create>
);
