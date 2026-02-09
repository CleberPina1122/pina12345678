import * as React from "react";
import { List, Datagrid, TextField, BooleanField, Edit, SimpleForm, TextInput, BooleanInput, NumberInput } from "react-admin";

export const ChannelList = () => (
  <List perPage={50}>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="group" />
      <TextField source="url" />
      <BooleanField source="is_active" />
      <TextField source="category_id" />
      <TextField source="playlist_id" />
    </Datagrid>
  </List>
);

export const ChannelEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput source="name" fullWidth />
      <TextInput source="group" fullWidth />
      <TextInput source="logo" fullWidth />
      <TextInput source="url" fullWidth />
      <BooleanInput source="is_active" />
      <NumberInput source="category_id" />
      <BooleanInput source="is_adult" />
    </SimpleForm>
  </Edit>
);
