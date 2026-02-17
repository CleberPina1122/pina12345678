import React from 'react';
import { Admin, Resource } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import { PostList, PostEdit, PostCreate } from './components/PostComponents';

const dataProvider = jsonServerProvider('http://localhost:8000'); // URL do backend

const authProvider = {
  login: ({ username, password }: { username: string; password: string }) => {
    return Promise.resolve();
  },
  logout: () => Promise.resolve(),
  checkError: (error: any) => Promise.resolve(),
  checkAuth: () => Promise.resolve(),
  getPermissions: () => Promise.resolve(),
};

const App = () => {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource name="posts" list={PostList} edit={PostEdit} create={PostCreate} />
    </Admin>
  );
};

export default App;