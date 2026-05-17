export function toIsoDate(date = new Date()) {
  return date.toISOString().slice(0, 10);
}

export function addDays(date, days) {
  const next = new Date(date);
  next.setUTCDate(next.getUTCDate() + days);
  return next;
}

export function todayRange(lookbackDays, now = new Date()) {
  return {
    start: toIsoDate(addDays(now, -lookbackDays)),
    end: toIsoDate(now)
  };
}
