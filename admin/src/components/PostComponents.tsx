import React from 'react';
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  TextInput,
  Create,
  SimpleForm,
  Edit,
  LongTextInput,
} from 'react-admin';

export const PostList = (props: any) => (
  <List {...props}>
    <Datagrid>
      <TextField source="id" />
      <TextField source="title" />
      <TextField source="body" />
      <EditButton />
    </Datagrid>
  </List>
);

export const PostEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <LongTextInput source="body" />
    </SimpleForm>
  </Edit>
);

export const PostCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <LongTextInput source="body" />
    </SimpleForm>
  </Create>
);