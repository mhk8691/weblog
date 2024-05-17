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
const CustomerFilters = [<SearchInput source="id" alwaysOn placeholder="id" />];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    <FilterForm filters={CustomerFilters} />
    <div>
      <FilterButton filters={CustomerFilters} />
    </div>
  </Stack>
);

export const CommentList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <NumberField source="id" />
      <NumberField source="author" />
      <TextField source="content" />
      <NumberField source="post" />
      <EditButton label="edit" />
      <ShowButton label="show" />
      <DeleteButton label="delete" />
    </Datagrid>
  </List>
);
