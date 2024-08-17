// const express = require('express')
import express from "express"; // method-2
import dotenv from "dotenv";
import connectDB from "./config/database.js";
import userRoute from "./routes/userRoute.js";

dotenv.config({});

const app = express();

const PORT = process.env.PORT || 5000;
// middleware

app.use(express.json());
//routes
app.use("/api/v1/user", userRoute);

app.listen(PORT, () => {
  connectDB();
  console.log(`Server listen at prot ${PORT}`);
});
