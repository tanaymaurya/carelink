// Liveness probe for the orchestrator.
import { Controller, Get } from "@nestjs/common";

@Controller("health")
export class HealthController {
  @Get("live")
  live() {
    return { ok: true };
  }
}
