import pandas as pd

# Initializing inventory dataframe
inventory = pd.DataFrame(columns=['Product', 'Quantity', 'Reorder_Level', 'Price'])

# Function to add new product
def add_product(product, quantity, reorder_level, price):
    global inventory
    new_product = pd.DataFrame([[product, quantity, reorder_level, price]], columns=['Product', 'Quantity', 'Reorder_Level', 'Price'])
    inventory = pd.concat([inventory, new_product], ignore_index=True)
    print(f'Added {product} to inventory.')

# Function to view Inventory
def view_inventory():
    print("\nCurrent Inventory:")
    print(inventory)

# Function to check for reorder alerts
def check_reorder_alerts():
    reorder_products = inventory[inventory['Quantity'] < inventory['Reorder_Level']]
    if len(reorder_products) > 0:
        print("\nReorder Alert! The following products need to be reordered:")
        print(reorder_products[['Product', 'Quantity', 'Reorder_Level']])
    else:
        print("\nNo products require reordering at the moment.")

# Function to update stock
def update_stock(product, quantity):
    global inventory
    inventory.loc[inventory['Product'] == product, 'Quantity'] += quantity
    print(f'Updated {product} stock by {quantity}.')

def main():
    # Add products
    add_product('Widget A', 50, 20, 5.99)
    add_product('Widget B', 10, 15, 3.49)
    add_product('Gadget C', 5, 10, 7.99)

    # View inventory
    view_inventory()

    # Check for reorder alerts
    check_reorder_alerts()

    # Update stock for a product
    update_stock('Gadget C', 20)

    # View updated inventory
    view_inventory()

    # Re-check reorder alerts
    check_reorder_alerts()

if __name__ == "__main__":
    main()
