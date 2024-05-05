import {
  Admin,
  Resource,
  EditGuesser,
  ShowGuesser,
  LayoutProps,
  ListGuesser,
} from "react-admin";
import { Layout } from "react-admin";

import { MyAppBar } from "./MyAppBar";
import { JSX } from "react/jsx-runtime";
import Dashboard from "./Dashboard";
import { dataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import { UsersList } from "./Users";
import { UserCreate } from "./UserCreate";
import { PostCreate } from "./PostCreate";
import { PostsList } from "./Post";
import { CategoryList } from "./Category";
import { CategoryCreate } from "./CategoryCreate";
import { CommentList } from "./Comment";
import { CommentCreate } from "./CommentCreate";

const MyLayout = (props: JSX.IntrinsicAttributes & LayoutProps) => (
  <Layout {...props} appBar={MyAppBar} />
);

export const App = () => (
  <Admin
    dataProvider={dataProvider}
    // authProvider={authProvider}
    layout={MyLayout}
    darkTheme={{ palette: { mode: "dark" } }}
    dashboard={Dashboard}

    // darkTheme={darkTheme}
  >
    <Resource
      name="user"
      list={UsersList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={UserCreate}
    />
    <Resource
      name="post"
      list={PostsList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={PostCreate}
    />

    <Resource
      name="category"
      list={CategoryList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={CategoryCreate}
    />
    <Resource
      name="comment"
      list={CommentList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={CommentCreate}
    />
  </Admin>
);
