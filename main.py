from faker import Faker
import random
import pandas as pd

fake = Faker()

# Number of rows to generate
num_rows = 100

# Generate patient information
patient_info = []
for i in range(num_rows):
    name = fake.name()
    age = random.randint(18, 90)
    gender = random.choice(['Male', 'Female'])
    medical_history = random.choice(['Malaria', 'HIV/AIDS', 'Chronic Diseases', 'Cancer'])
    allergies = random.choice([
        'Penicillin and related antibiotics',
        'Antibiotics containing sulfonamides (sulfa drugs)',
        'Anticonvulsants',
        'Aspirin, ibuprofen and other nonsteroidal anti-inflammatory drugs (NSAIDs)',
        'Chemotherapy drugs',
        'Peanuts', 'Tree Nuts', 'Fish', 'Crustaceans (Shellfish)',
        'Wheat', 'Soy'])
    prescriptions = random.choice([
        'lisinopril (Zestril)', 'levothyroxine (Synthroid)',
        'atorvastatin (Lipitor)', 'metformin (Glucophage)',
        'simvastatin (Zocor)', 'omeprazole (Prilosec)',
        'amlodipine (Norvasc)', 'metoprolol (Lopressor)'])
    patient_info.append((name, age, gender, medical_history, allergies, prescriptions))

# Generate order information
order_items = [
    'Vitamin D (Drisdol, Calciferol)',
    'Amoxicillin (Amoxil, Biomox, Polymox)',
    'Levothyroxine (Synthroid, Euthyrox, Levoxyl, Unithroid)',
    'Lisinopril (Prinivil, Zestril)', 'Ibuprofen (Advil, Motrin)',
    'Amphetamine/dextroamphetamine (Adderall, Adderall XR)',
    'Amlodipine (Norvasc)']

order_info = []
for i in range(num_rows):
    order_num = fake.uuid4()
    date = fake.date()
    time = fake.time()
    order_item = random.choice(order_items)
    quantity = random.randint(1, 10)
    price = round(random.uniform(5, 50), 2)
    total_amount = round(quantity * price, 2)
    order_info.append((order_num, date, time, order_item, quantity, price, total_amount))

# Generate payment information
payment_info = []
for i in range(num_rows):
    payment_method = random.choice(['Visa', 'Mastercard', 'American Express'])
    credit_card_num = fake.credit_card_number()
    expiration_date = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    security_code = fake.credit_card_security_code()
    billing_address = fake.address()
    payment_info.append((payment_method, credit_card_num, expiration_date, security_code, billing_address))

# Generate shipping information
shipping_info = []
for i in range(num_rows):
    name = fake.name()
    address = fake.address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    shipping_method = random.choice(['Standard', 'Express', 'Overnight'])
    tracking_number = fake.uuid4()
    shipping_info.append((name, address, city, state, zip_code, shipping_method, tracking_number))

# Generate medical product information
medical_product_info = []
for i in range(num_rows):
    product_name = fake.word()
    description = fake.sentence()
    category = fake.word()
    brand = fake.company()
    price = round(random.uniform(5, 50), 2)
    availability = random.choice(['In stock', 'Out of stock'])
    reviews = random.randint(0, 5)
    medical_product_info.append((product_name, description, category, brand, price, availability, reviews))

# Generate customer support information
customer_support_info = []
for i in range(num_rows):
    ticket_num = fake.uuid4()
    date = fake.date()
    time = fake.time()
    customer_name = fake.name()
    issue_description = fake.sentence()
    support_agent_name = fake.name()
    resolution_status = random.choice(['Resolved', 'Pending', 'Closed'])
    customer_support_info.append((ticket_num, date, time, customer_name, issue_description, support_agent_name, resolution_status))

# Create DataFrame
df = pd.DataFrame({
    'Index': range(1, num_rows + 1),  # Adding an index column starting from 1
    'Patient Name': [i[0] for i in patient_info],
    'Patient Age': [i[1] for i in patient_info],
    'Patient Gender': [i[2] for i in patient_info],
    'Medical History': [i[3] for i in patient_info],
    'Allergies': [i[4] for i in patient_info],
    'Prescriptions': [i[5] for i in patient_info],
    'Order Number': [i[0] for i in order_info],
    'Order Date': [i[1] for i in order_info],
    'Order Time': [i[2] for i in order_info],
    'Order Items': [i[3] for i in order_info],
    'Order Quantity': [i[4] for i in order_info],
    'Order Price': [i[5] for i in order_info],
    'Order Total Amount': [i[6] for i in order_info],
    'Shipping Name': [i[0] for i in shipping_info],
    'Shipping Address': [i[1] for i in shipping_info],
    'Shipping City': [i[2] for i in shipping_info],
    'Shipping State': [i[3] for i in shipping_info],
    'Shipping ZIP Code': [i[4] for i in shipping_info],
    'Shipping Method': [i[5] for i in shipping_info],
    'Tracking Number': [i[6] for i in shipping_info],
    'Payment Method': [i[0] for i in payment_info],
    'Credit Card Number': [i[1] for i in payment_info],
    'Expiration Date': [i[2] for i in payment_info],
    'Security Code': [i[3] for i in payment_info],
    'Billing Address': [i[4] for i in payment_info],
    'Product Name': [i[0] for i in medical_product_info],
    'Product Description': [i[1] for i in medical_product_info],
    'Product Category': [i[2] for i in medical_product_info],
    'Product Brand': [i[3] for i in medical_product_info],
    'Product Price': [i[4] for i in medical_product_info],
    'Product Availability': [i[5] for i in medical_product_info],
    'Product Reviews': [i[6] for i in medical_product_info],
    'Support Ticket Number': [i[0] for i in customer_support_info],
    'Support Date': [i[1] for i in customer_support_info],
    'Support Time': [i[2] for i in customer_support_info],
    'Customer Name': [i[3] for i in customer_support_info],
    'Issue Description': [i[4] for i in customer_support_info],
    'Support Agent Name': [i[5] for i in customer_support_info],
    'Resolution Status': [i[6] for i in customer_support_info]
})

# Set 'Index' as the DataFrame index
df.set_index('Index', inplace=True)

# Save DataFrame to parquet file with index
df.to_parquet('business_data.parquet', engine='pyarrow', index=True)

# Connect to PostgreSQL cloud isntance (elephantsql) and load the data
db_link = "postgresql://username:password@host:port/database')"
engine = db.create_engine(db_link)
df.to_sql('business_data', engine, if_exists='replace')


