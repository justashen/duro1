/* eslint-disable import/order */
"use client";
import { Button } from "@nextui-org/button";
import { Card, CardBody } from "@nextui-org/card";
import { Input } from "@nextui-org/input";
import { Link } from "@nextui-org/link";
import { Tab, Tabs } from "@nextui-org/tabs";
import React, { useState } from "react";
import axios from "../api/axios";

export default function App() {
  const [selected, setSelected] = useState<React.Key>("login");

  const handleLoginSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const data = Object.fromEntries(formData.entries());
    const response = await axios.post(`/api/auth/login/`, data);

      console.log("Sign in Response:", response.data);
    try {
    } catch (error) {
      console.error("Login Error:", error);
      // Handle login error, e.g., show error message
    }
  };

  const handleSignUpSubmit = async (
    event: React.FormEvent<HTMLFormElement>
  ) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const data = Object.fromEntries(formData.entries());

    try {
      const response = await axios.post(`/api/auth/register/`, data);

      console.log("Sign Up Response:", response.data);
      // Handle successful registration, e.g., redirect to login, show message, etc.
    } catch (error) {
      console.error("Sign Up Error:", error);
      // Handle sign-up error, e.g., show error message
    }
  };

  return (
    <div className="flex flex-col w-full">
      <Card className="max-w-full w-[340px] h-max">
        <CardBody className="overflow-hidden">
          <Tabs
            fullWidth
            aria-label="Tabs Form"
            // @ts-ignore
            selectedKey={selected}
            size="md"
            onSelectionChange={setSelected}
          >
            <Tab key="login" title="Login">
              <form
                className="flex flex-col gap-4"
                onSubmit={handleLoginSubmit}
              >
                <Input
                  isRequired
                  label="Username"
                  name="username"
                  placeholder="Enter your username"
                  type="text"
                />
                <Input
                  isRequired
                  label="Password"
                  name="password"
                  placeholder="Enter your password"
                  type="password"
                  autoComplete="true"
                />
                <p className="text-center text-small">
                  Need to create an account?{" "}
                  <Link size="sm" onPress={() => setSelected("sign-up")}>
                    Sign up
                  </Link>
                </p>
                <div className="flex gap-2 justify-end">
                  <Button fullWidth color="primary" type="submit">
                    Login
                  </Button>
                </div>
              </form>
            </Tab>
            <Tab key="sign-up" title="Sign up">
              <form
                className="flex flex-col gap-4 h-[450px]"
                onSubmit={handleSignUpSubmit}
              >
                <Input
                  isRequired
                  label="Name"
                  name="name"
                  placeholder="Enter your name"
                  type="text"
                />
                <Input
                  isRequired
                  label="Last Name"
                  name="lastName"
                  placeholder="Enter your last name"
                  type="text"
                />
                <Input
                  isRequired
                  label="Username"
                  name="username"
                  placeholder="Enter your first name"
                  type="text"
                />
                <Input
                  isRequired
                  label="Email"
                  name="email"
                  placeholder="Enter your email"
                  type="email"
                />
                <Input
                  isRequired
                  label="Password"
                  name="password"
                  placeholder="Enter your password"
                  type="password"
                  autoComplete="true"
                />
                <p className="text-center text-small">
                  Already have an account?{" "}
                  <Link size="sm" onPress={() => setSelected("login")}>
                    Login
                  </Link>
                </p>
                <div className="flex gap-2 justify-end">
                  <Button fullWidth color="primary" type="submit">
                    Sign up
                  </Button>
                </div>
              </form>
            </Tab>
          </Tabs>
        </CardBody>
      </Card>
    </div>
  );
}
