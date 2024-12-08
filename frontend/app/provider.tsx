/* eslint-disable prettier/prettier */
// app/providers.tsx

import { NextUIProvider } from "@nextui-org/system";

// import { NextUIProvider } from "@nextui-org/react";

export function Providers({ children }: { children: React.ReactNode }) {
  return <NextUIProvider>{children}</NextUIProvider>;
}
