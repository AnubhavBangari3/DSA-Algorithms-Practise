import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const validationSchema = Yup.object({
  name: Yup.string()
    .min(3, "Name must be at least 3 characters")
    .required("Name is required"),

  email: Yup.string()
    .email("Enter a valid email")
    .required("Email is required"),

  password: Yup.string()
    .min(6, "Password must be at least 6 characters")
    .required("Password is required")
});

function App() {
  const initialValues = {
    name: "",
    email: "",
    password: ""
  };

  const handleSubmit = (values, { resetForm }) => {
    console.log("Form submitted:", values);

    resetForm();
  };

  return (
    <div>
      <h1>Registration Form</h1>

      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            <div>
              <label>Name</label>

              <Field
                type="text"
                name="name"
                placeholder="Enter your name"
              />

              <ErrorMessage name="name" component="p" />
            </div>

            <div>
              <label>Email</label>

              <Field
                type="email"
                name="email"
                placeholder="Enter your email"
              />

              <ErrorMessage name="email" component="p" />
            </div>

            <div>
              <label>Password</label>

              <Field
                type="password"
                name="password"
                placeholder="Enter your password"
              />

              <ErrorMessage name="password" component="p" />
            </div>

            <button type="submit" disabled={isSubmitting}>
              Submit
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default App;