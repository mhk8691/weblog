import {
  CreateButton,
  Datagrid,
  FilterButton,
  FilterForm,
  ListBase,
  List,
  Pagination,
  TextField,
  TextInput,
  SearchInput,
  EmailField,
  NumberField,
  DateField,
  EditButton,
  ShowButton,
  DeleteButton,
  ImageField,
} from "react-admin";
import { Stack } from "@mui/material";
const CustomerFilters = [
  <SearchInput source="title" alwaysOn placeholder="Title" />,
];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    <FilterForm filters={CustomerFilters} />
    <div>
      <FilterButton filters={CustomerFilters} />
    </div>
  </Stack>
);

export const PostsList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <NumberField source="id" />
      <NumberField source="author" />
      <TextField source="title" />
      {/* <TextField source="image" /> */}
      <TextField source="is_draft" label="Draft" />
      <TextField label="Category" source="categories" />
      <TextField source="content" />
      <EditButton label="edit" />
      <ShowButton label="show" />
      <DeleteButton label="delete" />
    </Datagrid>
  </List>
);
