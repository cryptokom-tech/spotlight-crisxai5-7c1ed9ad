// Copies POST.json to /output for the make.fun program/v1 harness.
import { copyFileSync, mkdirSync } from "node:fs";

mkdirSync("/output", { recursive: true });
copyFileSync("POST.json", "/output/POST.json");
