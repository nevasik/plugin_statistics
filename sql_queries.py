TOTAL_TURNOVER_AND_MARGIN = """
SELECT cl.name,
       SUM(c.amount_in) AS pay_in, SUM(c.amount_out) AS pay_out,
       (SUM(c.amount_in + c.amount_out) * 0.05) AS general_marga
FROM public.claim c
JOIN general.client cl
    ON c.client_id = cl.id
WHERE c.status_id = 5
GROUP BY cl.name;
"""

TURNOVER_AND_MARGIN_BY_PERIOD = """
SELECT cl.name,
       SUM(c.amount_in) AS pay_in, SUM(c.amount_out) AS pay_out,
       (SUM(c.amount_in + c.amount_out) * 0.05) AS general_marga
FROM public.claim c
JOIN general.client cl
    ON c.client_id = cl.id
WHERE DATE(c.create_time) BETWEEN %s AND %s AND c.status_id = 5
GROUP BY cl.name;
"""

CLAIM_STATUS_BY_EXTERNAL_ID = """
SELECT s.name
FROM public.claim c
JOIN public.status s
    ON s.id = c.status_id
WHERE c.external_id = %s;
"""

TOTAL_TURNOVER_AND_MARGIN_GENERAL = """
SELECT SUM(c.amount_in + c.amount_out) AS abarot,
       (SUM(c.amount_in + c.amount_out) * 0.05) AS marga
FROM public.claim c
WHERE c.status_id = 5;
"""
