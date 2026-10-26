# Setup and deployment

## Local setup
1. Install Python 3.11+.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Copy `.env.example` to `.env`; set `DJANGO_SECRET_KEY`.
5. For local-only development, omit `DATABASE_URL` to use SQLite. For Supabase integration, set `DATABASE_URL` to the database URI from Supabase and retain TLS verification.
6. Run `python manage.py check`.
7. Run `python manage.py makemigrations accounts core`.
8. Run `python manage.py migrate`.
9. Run `python manage.py createsuperuser`.
10. Run `python manage.py runserver`.

## Supabase
Use the connection URI and endpoint appropriate to your deployment's network topology. Use a direct connection where IPv6/network access supports it, otherwise choose the appropriate Supabase pooler. Do not embed credentials in source control. Use a database role with only the permissions needed by the application, and test TLS connectivity before deploying.

## Production checklist
- Set DEBUG=False, a strong secret key, and exact allowed hosts.
- Configure HTTPS, secure cookies, trusted proxy settings as appropriate, and CSRF trusted origins.
- Use private object storage for supplier documents; do not expose a public media directory.
- Configure backups and periodically test restore procedures.
- Run migrations in a controlled deployment step.
- Review Django deployment checks and logging before go-live.
