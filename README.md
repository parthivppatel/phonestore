# Phone Store - Django E-commerce Application

A complete e-commerce web application for selling mobile phones, built with Django framework. This application provides a full customer shopping experience with user authentication, product browsing, cart management, and order processing.

## 🚀 Features

### Customer Features
- **User Authentication**: Registration, login, logout with email verification
- **Product Browsing**: Browse phones by brand (Realme, Oppo, Vivo, Redmi, Nokia, iPhone)
- **Shopping Cart**: Add/remove items, quantity management, cart persistence
- **User Profile**: Manage personal information and shipping addresses
- **Order Management**: Place orders, view order history, track order status
- **Payment Integration**: Credit card payment processing
- **Password Recovery**: Email-based password reset functionality
- **Responsive Design**: Mobile-friendly interface

### Technical Features
- **Django Admin**: Built-in admin interface for data management
- **Session Management**: Secure session handling with timeout
- **Email Integration**: SMTP email service for notifications
- **Static File Management**: Optimized static file serving with WhiteNoise
- **Database**: SQLite database with proper relationships
- **Security**: CSRF protection, password validation, secure authentication

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/parthivppatel/myphone
   cd phonestore
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with the following variables:
   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🏗️ Project Structure

```
phonestore/
├── phone_app/                 # Main Django application
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   └── admin.py              # Admin interface configuration
├── phonestore/               # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── templates/                # HTML templates
│   ├── index.html            # Home page
│   ├── sign_in.html          # Login page
│   ├── sign_up.html          # Registration page
│   ├── cart.html             # Shopping cart
│   ├── profile.html          # User profile
│   ├── order.html            # Order placement
│   └── your_order.html       # Order history
├── static/                   # Static files
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   ├── images/               # Product images
│   └── fonts/                # Custom fonts
├── db.sqlite3               # SQLite database
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## 🗄️ Database Models

### Mobile (Product)
- `id`: Auto-incrementing primary key
- `brand`: Phone brand (CharField)
- `name`: Phone model name (CharField)
- `price`: Product price (IntegerField)
- `network`: Network type (CharField)
- `display`: Display specifications (CharField)
- `ram`: RAM specifications (CharField)
- `os`: Operating system (CharField)
- `description`: Product description (TextField)
- `img`: Image path (CharField)

### Profile (User Profile)
- `user`: One-to-one relationship with User model
- `phone`: Phone number (TextField)
- `pincode`: Postal code (TextField)
- `country`: Country (TextField)
- `flat`: Flat/house number (TextField)
- `area`: Area/locality (TextField)
- `landmark`: Landmark (TextField)
- `state`: State (TextField)
- `city`: City (TextField)

### Cart
- `user`: Foreign key to User model
- `product`: Foreign key to Mobile model
- `is_order`: Boolean flag for order status
- `quantity`: Item quantity (IntegerField)
- `date`: Cart date (DateField)
- `subtotal`: Cart subtotal (IntegerField)

### Orders
- `user`: Foreign key to User model
- `product`: Foreign key to Mobile model
- `date`: Order date (DateField)
- `status`: Order status (TextField)
- `quantity`: Ordered quantity (IntegerField)
- `total`: Order total (IntegerField)
- `cart`: Foreign key to Cart model

### Card (Payment)
- `name`: Cardholder name (TextField)
- `number`: Card number (TextField)
- `expiry`: Expiry date (TextField)
- `cvv`: CVV code (TextField)
- `user`: Foreign key to User model

## 🔗 URL Structure

### Customer URLs
- `/` - Home page with product listings
- `/home` - Home page (alias)
- `/login` - User login
- `/signup` - User registration
- `/register` - Registration form
- `/logout` - User logout
- `/session` - Session timeout
- `/cart` - Shopping cart
- `/cart/<id>` - Add to cart
- `/profile` - User profile management
- `/order` - Order placement
- `/place` - Process order
- `/your` - Order history
- `/delete` - Delete account
- `/email` - Email verification
- `/forgot` - Password recovery
- `/reset` - Password reset
- `/password` - Change password
- `/clear` - Clear cart
- `/next` - Navigation helper

## 🎨 Frontend Technologies

- **HTML5**: Semantic markup
- **CSS3**: Styling and responsive design
- **JavaScript**: Interactive functionality
- **Bootstrap**: UI framework (if used)
- **Font Awesome**: Icons (if used)

## 🔧 Configuration

### Settings Configuration
- **Database**: SQLite3 (development)
- **Static Files**: WhiteNoise for production serving
- **Email**: SMTP with Gmail
- **Session**: 7-day timeout with activity tracking
- **Security**: CSRF protection, password validation

### Environment Variables
- `EMAIL_HOST_USER`: Gmail address for sending emails
- `EMAIL_HOST_PASSWORD`: Gmail app password

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG = False` in settings.py
2. Configure production database (PostgreSQL recommended)
3. Set up proper static file serving
4. Configure production email settings
5. Use environment variables for sensitive data
6. Set up HTTPS

## 📧 Email Configuration

The application uses Gmail SMTP for sending emails. To configure:

1. Enable 2-factor authentication on your Gmail account
2. Generate an app password
3. Add credentials to `.env` file:
   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

## 🔒 Security Features

- **CSRF Protection**: Built-in Django CSRF middleware
- **Password Validation**: Django's password validation system
- **Session Security**: Secure session handling with timeout
- **SQL Injection Protection**: Django ORM protection
- **XSS Protection**: Template auto-escaping

## 🧪 Testing

To run tests:
```bash
python manage.py test
```

## 📝 API Documentation

This application uses traditional Django views (not REST API). All interactions are handled through form submissions and page redirects.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 👥 Authors

- Parthiv Patel

## 🙏 Acknowledgments

- Django framework and community
- Bootstrap for UI components
- Font Awesome for icons

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact: parthivp800@gmail.com

**Note**: This is a development version. For production use, ensure proper security configurations and database optimization. 