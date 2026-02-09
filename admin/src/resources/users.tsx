import * as React from "react";
import { List, Datagrid, TextField, BooleanField, DateField } from "react-admin";

export const UserList = () => (
  <List>
    <Datagrid rowClick={false}>
      <TextField source="id" />
      <TextField source="email" />
      <BooleanField source="is_admin" />
      <DateField source="created_at" showTime />
    </Datagrid>
  </List>
);
