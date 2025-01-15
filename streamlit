
import streamlit as st
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('expenses.db')

# Function to execute SQL queries and return data as DataFrame
def run_query(query):
    return pd.read_sql_query(query, conn)

# Streamlit App layout
st.title('Expense Tracker Insights')

# Sidebar with query selection
#st.sidebar.title('Select Query')
query_options = [
	'1. What is the total amount spent in each category?',
	'2. What is the total amount spent using each payment mode?',
	'3. What is the total cashback received across all transactions?',
	'4. Which are the top 5 most expensive categories in terms of spending?',
	'5. How much was spent on transportation using different payment modes?',
	'6. Which transactions resulted in cashback?',
	'7. What is the total spending in each month of the year?',
	'8. Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"?',
	'9. Are there any recurring expenses that occur during specific dates of the year (e.g., insurance premiums, property taxes)?',
	'10. How much cashback or rewards were earned in each month?',
	'11. How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?',
	'12. What are the typical costs associated with different types of travel (e.g., flights, accommodation, transportation)?',
	'13. Are there any patterns in grocery spending (e.g., higher spending on weekends, increased spending during specific seasons)?',
	'14. Define High and Low Priority Categories for Month of January.',
	'15. Which category contributes the highest percentage of the total spending?',
	'16. On Which date of every month bills where paid?',
	'17. Total Money spent in purchasing books for every month?',
	'18. Quarterly spending on fuel ?',
	'19. On which 3 days of the week maximum number of movies were seen? (Which is it from Sun-Sat??)',
	'20. On which date, month and day of week was the maximum cashback received?'

]
#query_choice = st.sidebar.selectbox('Choose a query', query_options)
#query_choice = st.radio('Choose a query', query_options)
query_number = st.slider('Select Query Number', 1, len(query_options))
query_choice = query_options[query_number - 1]

# Execute chosen query
if query_choice == '1. What is the total amount spent in each category?':
    query = '''
        SELECT category, SUM("amount paid") AS total_spent FROM expenses GROUP BY category ORDER BY total_spent DESC;
    '''
    df = run_query(query)
    st.write('1. What is the total amount spent in each category?')
    st.write(df)
    st.bar_chart(df.set_index('Category')['total_spent'])

elif query_choice == '2. What is the total amount spent using each payment mode?':
    query = '''
        SELECT "Payment Mode", SUM("amount paid") AS total_spent FROM expenses GROUP BY "Payment Mode" ORDER BY total_spent DESC;
    '''
    df = run_query(query)
    st.write('2. What is the total amount spent using each payment mode?')
    st.write(df)
    st.bar_chart(df.set_index('Payment Mode')['total_spent'])

elif query_choice == '3. What is the total cashback received across all transactions?':
    query = '''
        SELECT SUM(cashback) AS total_cashback FROM expenses;
    '''
    df = run_query(query)
    st.write('3. What is the total cashback received across all transactions?')
    st.write(df)

elif query_choice == '4. Which are the top 5 most expensive categories in terms of spending?':
    query = '''
        SELECT category, SUM("amount paid") AS total_spent FROM expenses GROUP BY category ORDER BY total_spent DESC LIMIT 5;
    '''
    df = run_query(query)
    st.write('4. Which are the top 5 most expensive categories in terms of spending?')
    st.write(df)
    st.bar_chart(df.set_index('Category')['total_spent'])

elif query_choice == '5. How much was spent on transportation using different payment modes?':
    query = '''
        SELECT "Payment Mode", SUM("amount paid") AS total_spent FROM expenses WHERE category = 'Transportation' GROUP BY "Payment Mode" ORDER BY total_spent DESC;
    '''
    df = run_query(query)
    st.write('5. How much was spent on transportation using different payment modes?')
    st.write(df)
    st.bar_chart(df.set_index('Payment Mode')['total_spent'])

elif query_choice == '6. Which transactions resulted in cashback?':
    query = '''
        SELECT * FROM expenses WHERE cashback > 0;
    '''
    df = run_query(query)
    st.write('6. Which transactions resulted in cashback?')
    st.write(df)

elif query_choice == '7. What is the total spending in each month of the year?':
    query = '''
        SELECT strftime('%Y-%m', date) AS month, SUM("amount paid") AS total_spent FROM expenses GROUP BY month ORDER BY month;
    '''
    df = run_query(query)
    st.write('7. What is the total spending in each month of the year?')
    st.write(df)
    st.line_chart(df.set_index('month')['total_spent'])

elif query_choice == '8. Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"?':
    query = '''
        WITH ranked_spending AS (
            SELECT strftime('%Y-%m', date) AS month,
                   category,
                   SUM("amount paid") AS total_spent,
                   ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM("amount paid") DESC) AS rn
            FROM expenses
            GROUP BY month, category
        )
        SELECT month, category, total_spent
        FROM ranked_spending
        WHERE rn = 1
    '''
    df = run_query(query)
    st.write('8. Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"?')
    st.write(df)
    st.bar_chart(df.set_index('month')['total_spent'])

elif query_choice == '9. Are there any recurring expenses that occur during specific dates of the year (e.g., insurance premiums, property taxes)?':
    query = '''
        SELECT category, strftime('%d', date) AS recurring_date, SUM("amount paid") AS total_spent
        FROM expenses
        GROUP BY category, recurring_date
        HAVING COUNT(DISTINCT strftime('%m', date)) = 12;
    '''
    df = run_query(query)
    st.write('9. Are there any recurring expenses that occur during specific dates of the year (e.g., insurance premiums, property taxes)?')
    st.write(df)

elif query_choice == '10. How much cashback or rewards were earned in each month?':
    query = '''
        SELECT strftime('%m', date) AS month, SUM(cashback) AS total_cashback FROM expenses WHERE cashback > 0 GROUP BY month ORDER BY month;
    '''
    df = run_query(query)
    st.write('10. How much cashback or rewards were earned in each month?')
    st.write(df)
    st.line_chart(df.set_index('month')['total_cashback'])

elif query_choice == '11. How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?':
    query = '''
        SELECT strftime('%Y-%m', date) AS month, SUM("amount paid") AS total_spent FROM expenses GROUP BY month ORDER BY month;
    '''
    df = run_query(query)
    st.write('11. How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?')
    st.write(df)
    st.line_chart(df.set_index('month')['total_spent'])

elif query_choice == '12. What are the typical costs associated with different types of travel (e.g., flights, accommodation, transportation)?':
    query = '''
        SELECT Description, SUM("Amount Paid") AS Total_Amount_Paid FROM expenses WHERE Category = 'Transportation' GROUP BY Description ORDER by "Total_Amount_Paid" DESC;
    '''
    df = run_query(query)
    st.write('12. What are the typical costs associated with different types of travel (e.g., flights, accommodation, transportation)?')
    st.write(df)

elif query_choice == '13. Are there any patterns in grocery spending (e.g., higher spending on weekends, increased spending during specific seasons)?':
    query = '''
        SELECT 
          CASE 
            WHEN strftime('%w', "Date") IN ('0', '6') THEN 'Weekend'   -- 0 = Sunday, 6 = Saturday 
            ELSE 'Weekday' 
          END AS Day_Type, 
          SUM("Amount Paid") AS Total_Spending 
        FROM expenses 
        WHERE "Description" LIKE '%groceries%' 
        GROUP BY 
          CASE 
            WHEN strftime('%w', "Date") IN ('0', '6') THEN 'Weekend' 
            ELSE 'Weekday' 
          END;
    '''
    df = run_query(query)
    st.write('13. Are there any patterns in grocery spending (e.g., higher spending on weekends, increased spending during specific seasons)?')
    st.write(df)


elif query_choice == '14. Define High and Low Priority Categories for Month of January.':
    query = '''
        SELECT 
            date, 
            category, 
            "payment mode", 
            description, 
            "Amount Paid", 
            cashback,
            CASE 
                WHEN category IN ('Bills', 'Food', 'Transportation', 'Pharmacy') THEN 'High Priority'
                WHEN category IN ('Office Supplies', 'Entertainment', 'Skills Improvement') THEN 'Low Priority'
                ELSE 'Unknown Priority'
            END AS priority
        FROM expenses
        WHERE strftime('%Y-%m', date) = '2025-01';
    '''
    df = run_query(query)
    st.write('14. Define High and Low Priority Categories for Month of January.')
    st.write(df)
    #st.bar_chart(df.set_index('weekday')['total_spent'])

elif query_choice == '15. Which category contributes the highest percentage of the total spending?':
    query = '''
        SELECT 
            "Category",
            SUM("Amount Paid") AS Total_Spending,
            (SUM("Amount Paid") / (SELECT SUM("Amount Paid") FROM expenses)) * 100 AS Percentage_Contribution
        FROM expenses
        GROUP BY "Category"
        ORDER BY Percentage_Contribution DESC;
    '''
    df = run_query(query)
    st.write('15. Which category contributes the highest percentage of the total spending?')
    st.write(df)
    st.bar_chart(df.set_index('Category')['Percentage_Contribution'])

elif query_choice == '16. On Which date of every month bills where paid?':
    query = '''
        SELECT strftime('%m', Date) AS Month, MIN(Date) AS Payment_Date
        FROM expenses
        WHERE Category = 'Bills'
        GROUP BY strftime('%Y-%m', Date)
        ORDER BY strftime('%Y-%m', Date);
    '''
    df = run_query(query)
    st.write('16. On Which date of every month bills where paid?')
    st.write(df)
    st.bar_chart(df.set_index('Month')['Payment_Date'])

elif query_choice == '17. Total Money spent in purchasing books for every month?':
    query = '''
        SELECT 
            strftime('%m', Date) AS month,
            SUM(CASE WHEN Description LIKE '%books%' THEN "Amount Paid" ELSE 0 END) AS total_amount_spent_on_books
        FROM expenses
        GROUP BY month
        ORDER BY month;
    '''
    df = run_query(query)
    st.write('17. Total Money spent in purchasing books for every month?')
    st.write(df)
    #st.bar_chart(df.set_index('weekday')['total_amount_spent'])

elif query_choice == '18. Quarterly spending on fuel ?':
    query = '''
        SELECT 
            strftime('%Y', Date) AS Year,
            CASE 
                WHEN strftime('%m', Date) BETWEEN '01' AND '03' THEN 'Q4_2024'
                WHEN strftime('%m', Date) BETWEEN '04' AND '06' THEN 'Q1_2025'
                WHEN strftime('%m', Date) BETWEEN '07' AND '09' THEN 'Q2_2025'
                WHEN strftime('%m', Date) BETWEEN '10' AND '12' THEN 'Q3_2025'
                ELSE 'Other Quarter'
            END AS Quarter,
            SUM("Amount Paid") AS Total_Spending
        FROM expenses
        GROUP BY Year, Quarter
        ORDER BY Year, Quarter
    '''
    df = run_query(query)
    st.write('18. Quarterly spending on fuel ?')
    st.write(df)
    st.bar_chart(df.set_index('Quarter')['Total_Spending'])

elif query_choice == '19. On which 3 days of the week maximum number of movies were seen? (Which is it from Sun-Sat??)':
    query = '''
        SELECT 
          CASE strftime('%w', Date)
            WHEN '0' THEN 'Sunday'
            WHEN '1' THEN 'Monday'
            WHEN '2' THEN 'Tuesday'
            WHEN '3' THEN 'Wednesday'
            WHEN '4' THEN 'Thursday'
            WHEN '5' THEN 'Friday'
            WHEN '6' THEN 'Saturday'
          END AS DayOfWeek,
          COUNT(*) AS MovieCount
        FROM expenses
        WHERE Description LIKE '%movie%'
        GROUP BY DayOfWeek
        ORDER BY MovieCount DESC
        LIMIT 3;
    '''
    df = run_query(query)
    st.write('19. On which 3 days of the week maximum number of movies were seen? (Which is it from Sun-Sat??)')
    st.write(df)
    st.bar_chart(df.set_index('DayOfWeek')['MovieCount'])

elif query_choice == '20. On which date, month and day of week was the maximum cashback received?':
    query = '''
        SELECT 
            Date, 
            MAX(Cashback) AS MaxCashback,
            strftime('%m', Date) AS MonthNumber,
            CASE strftime('%m', Date)
                WHEN '01' THEN 'January'
                WHEN '02' THEN 'February'
                WHEN '03' THEN 'March'
                WHEN '04' THEN 'April'
                WHEN '05' THEN 'May'
                WHEN '06' THEN 'June'
                WHEN '07' THEN 'July'
                WHEN '08' THEN 'August'
                WHEN '09' THEN 'September'
                WHEN '10' THEN 'October'
                WHEN '11' THEN 'November'
                WHEN '12' THEN 'December'
            END AS MonthName,
            CASE strftime('%w', Date)
                WHEN '0' THEN 'Sunday'
                WHEN '1' THEN 'Monday'
                WHEN '2' THEN 'Tuesday'
                WHEN '3' THEN 'Wednesday'
                WHEN '4' THEN 'Thursday'
                WHEN '5' THEN 'Friday'
                WHEN '6' THEN 'Saturday'
            END AS DayOfWeek
        FROM expenses
        GROUP BY Date
        ORDER BY MaxCashback DESC
        LIMIT 1;
    '''
    df = run_query(query)
    st.write('20. On which date, month and day of week was the maximum cashback received?')
    st.write(df)


 #Close the database connection
conn.close()

