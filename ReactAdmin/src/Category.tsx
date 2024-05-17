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
  <SearchInput source="name" alwaysOn placeholder="name" />,
];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    <FilterForm filters={CustomerFilters} />
    <div>
      <FilterButton filters={CustomerFilters} />
    </div>
  </Stack>
);

export const CategoryList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <NumberField source="id" />
      <TextField label="name" source="name" />
      <EditButton label="edit" />
      <ShowButton label="show" />
      <DeleteButton label="delete" />
    </Datagrid>
  </List>
);
