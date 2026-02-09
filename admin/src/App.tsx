import * as React from "react";
import { Admin, Resource } from "react-admin";
import simpleRestProvider from "ra-data-simple-rest";
import { API_URL, authProvider, authFetch } from "./api";

import { UserList } from "./resources/users";
import { ChannelList, ChannelEdit } from "./resources/channels";
import { DeviceList } from "./resources/devices";

const dataProvider = simpleRestProvider(API_URL, authFetch);

export default function App() {
  return (
    <Admin title="Carbi Play Admin" dataProvider={dataProvider} authProvider={authProvider as any} requireAuth>
      <Resource name="admin/users" options={{ label: "Usuários" }} list={UserList} />
      <Resource name="admin/channels" options={{ label: "Canais" }} list={ChannelList} edit={ChannelEdit} />
      <Resource name="admin/devices" options={{ label: "Dispositivos" }} list={DeviceList} />
    </Admin>
  );
}
