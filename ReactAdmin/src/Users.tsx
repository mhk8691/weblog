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
  ListProps,
} from "react-admin";
import { Stack } from "@mui/material";

const CustomerFilters = [
  <SearchInput source="username" alwaysOn placeholder="username" />,
];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    <FilterForm filters={CustomerFilters} />
    <div>
      <FilterButton filters={CustomerFilters} />
    </div>
  </Stack>
);

export const UsersList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <NumberField source="id" />
      <TextField source="username" />
      <EmailField source="email" />
      <TextField source="password" />
      <EditButton label="edit" />
      <ShowButton label="show" />
      <DeleteButton label="delete" />
    </Datagrid>
  </List>
);
