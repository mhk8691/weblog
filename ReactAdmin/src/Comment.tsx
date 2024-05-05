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

// const CustomerFilters = [
//   <SearchInput source="username" alwaysOn placeholder="username" />,
//   <TextInput
//     label="email"
//     source="email"
//     defaultValue="@gmail.com"
//     placeholder="email"
//   />,
//   <TextInput label="phone" source="phone" placeholder="phone" />,
// ];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    {/* <FilterForm filters={CustomerFilters} /> */}
    <div>{/* <FilterButton filters={CustomerFilters} /> */}</div>
  </Stack>
);

export const CommentList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <NumberField source="id" />
      <NumberField source="author" />
      <TextField source="content" />
      <NumberField label="post" />
      <EditButton label="edit" />
      <ShowButton label="show" />
      <DeleteButton label="delete" />
    </Datagrid>
  </List>
);
