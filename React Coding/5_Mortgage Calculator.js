/**
 5. Mortgage Calculator

Build a calculator that computes the monthly mortgage for a loan.
 */
import React, { useState } from "react";

function App() {
  // Store all user inputs in one state object
  const [formData, setFormData] = useState({
    loanAmount: "",
    interestRate: "",
    loanTerm: "",
  });

  // Store calculated monthly payment
  const [monthlyPayment, setMonthlyPayment] = useState(null);

  // Update input value based on field name
  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Calculate monthly mortgage payment
  const calculateMortgage = (e) => {
    e.preventDefault(); // Stop form from refreshing the page

    // Convert string input values into numbers
    const principal = Number(formData.loanAmount); // Total loan amount
    const annualRate = Number(formData.interestRate); // Annual interest rate in %
    const years = Number(formData.loanTerm); // Loan duration in years

    // Convert annual interest rate into monthly decimal rate
    // Example: 6% yearly = 0.06 / 12 monthly
    const monthlyRate = annualRate / 100 / 12;

    // Convert loan term from years to months
    // Example: 30 years = 360 months
    const totalMonths = years * 12;

    // Mortgage formula:
    // M = P * r * (1 + r)^n / ((1 + r)^n - 1)
    // P = principal
    // r = monthly interest rate
    // n = total number of months
    const payment =
      (principal * monthlyRate * Math.pow(1 + monthlyRate, totalMonths)) /
      (Math.pow(1 + monthlyRate, totalMonths) - 1);

    // Save final monthly payment rounded to 2 decimal places
    setMonthlyPayment(payment.toFixed(2));
  };

  const styles = {
    main: {
      width: "420px",
      margin: "40px auto",
      padding: "20px",
      fontFamily: "Arial",
      border: "1px solid #ddd",
      borderRadius: "8px",
    },
    title: {
      color: "#5C6AC4",
      textAlign: "center",
    },
    form: {
      display: "flex",
      flexDirection: "column",
      gap: "12px",
    },
    input: {
      padding: "10px",
      fontSize: "16px",
    },
    button: {
      padding: "10px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      cursor: "pointer",
      fontSize: "16px",
    },
    result: {
      marginTop: "20px",
      fontSize: "20px",
      fontWeight: "bold",
      textAlign: "center",
    },
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>Mortgage Calculator</h1>

      <form style={styles.form} onSubmit={calculateMortgage}>
        {/* Loan amount entered by user */}
        <input
          style={styles.input}
          type="number"
          name="loanAmount"
          placeholder="Loan Amount"
          value={formData.loanAmount}
          onChange={handleChange}
          required
        />

        {/* Annual interest rate entered by user */}
        <input
          style={styles.input}
          type="number"
          name="interestRate"
          placeholder="Annual Interest Rate (%)"
          value={formData.interestRate}
          onChange={handleChange}
          required
        />

        {/* Loan duration in years */}
        <input
          style={styles.input}
          type="number"
          name="loanTerm"
          placeholder="Loan Term (Years)"
          value={formData.loanTerm}
          onChange={handleChange}
          required
        />

        <button style={styles.button} type="submit">
          Calculate
        </button>
      </form>

      {/* Show monthly payment only after calculation */}
      {monthlyPayment && (
        <div style={styles.result}>
          Monthly Payment: ₹{monthlyPayment}
        </div>
      )}
    </div>
  );
}

export default App;