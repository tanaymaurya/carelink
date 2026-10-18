// Portal back-office server.
import express from "express";
import { adminRouter } from "./admin";

const app = express();

app.get("/status", (req, res) => res.send("ok"));
app.use("/admin", adminRouter);

app.listen(3001);
