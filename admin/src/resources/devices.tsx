import * as React from "react";
import { List, Datagrid, TextField, DateField } from "react-admin";
import { API_URL, authFetch } from "../api";

function Actions({ record }: any) {
  const approve = async () => {
    await authFetch(`${API_URL}/admin/devices/${record.device_id}/approve`, { method: "POST" });
    window.location.reload();
  };
  const block = async () => {
    await authFetch(`${API_URL}/admin/devices/${record.device_id}/block`, { method: "POST" });
    window.location.reload();
  };
  return (
    <div style={{ display: "flex", gap: 8 }}>
      <button onClick={approve}>Aprovar</button>
      <button onClick={block}>Bloquear</button>
    </div>
  );
}

export const DeviceList = () => (
  <List>
    <Datagrid rowClick={false}>
      <TextField source="status" />
      <TextField source="virtual_mac" />
      <TextField source="device_id" />
      <TextField source="device_brand" />
      <TextField source="device_model" />
      <TextField source="android_version" />
      <DateField source="first_seen_at" showTime />
      <DateField source="last_seen_at" showTime />
      {/* @ts-ignore */}
      <Actions />
    </Datagrid>
  </List>
);
