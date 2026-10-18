// Admin routes, mounted under /admin by index.ts.
import { Router } from "express";

export const adminRouter = Router();

export function listAudit(req, res) {
  res.send("[]");
}

adminRouter.get("/audit", listAudit);
