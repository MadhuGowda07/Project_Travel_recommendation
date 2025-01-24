# %%
import matplotlib.pyplot as plt
import seaborn as sns


# %%
merged_data=pd.read_csv('merged_data.csv')

top_destinations = merged_data['Destination'].value_counts().head(10)
sns.barplot(x=top_destinations.index, y=top_destinations.values, color='pink')
plt.xlim(-1,10)
plt.title('Popular Destinations')
plt.ylabel('Number of Flights')
plt.xticks(rotation=90)
plt.show()


# %%
Age_Group_Seates_Booked=merged_data.groupby('Age_Group')['Seats_Booked'].sum()
print(Age_Group_Seates_Booked)
Age_Group_Seates_Booked.plot(kind='bar',color='indigo')
plt.title('Age Distribution of Customers')
plt.xticks(rotation=0)
plt.ylabel('Seats Booked')
plt.show()



# %%

Month=merged_data['Booking_Date'].apply(lambda x: x.split('-')[1])
Month.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Monthly Booking Trends')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
plt.show()

# %%
day_of_week=merged_data['Booking_Date'].apply(lambda x: x.split('-')[0])
day_of_week.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Booking Trends of Date')
plt.xlabel('Day')
plt.ylabel('Number of Bookings')
plt.xlim(-1,31)
plt.xticks(rotation=0)
plt.show()

# %%
popular_rotes=merged_data['Route_ID'].value_counts().head(10)
popular_rotes.plot(kind='bar',color='y')
plt.title('Top 10 Most Popular Routes')
plt.xlabel('Destination')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=0)
plt.show()

# %%
year_booking=merged_data['Booking_Date'].apply(lambda x: x.split('-')[2])
year_booking.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Booking Trend of Year')
plt.xlabel('Year')
plt.ylabel('Number of Bookings')
plt.xlim(-1,4)
plt.xticks(rotation=0)
plt.show()

# %%



